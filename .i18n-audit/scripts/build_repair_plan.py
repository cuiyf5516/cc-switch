from __future__ import annotations
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HUMAN = ROOT / ".i18n-audit/reviews/human-review"
TRANSLATION_SOURCE = HUMAN / "translation_review_decisions.csv"
MISSING_SOURCE = HUMAN / "missing_i18n_review_decisions.csv"
OUTPUT = HUMAN / "repair_plan.csv"

TRANSLATION_DECISIONS = {"", "采纳", "修改后采纳", "保留原译", "暂不处理"}
MISSING_DECISIONS = {"", "确认修复", "误报", "无需国际化", "暂不处理"}
APPROVED = {"采纳", "修改后采纳", "确认修复"}
PLAN_COLUMNS = [
    "问题ID", "问题类型", "优先级", "文件", "位置或键",
    "批准韩文或修复要求", "修复范围", "审核备注",
]


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    for path in (TRANSLATION_SOURCE, MISSING_SOURCE):
        if not path.exists():
            print(f"Missing {path}", file=sys.stderr)
            return 2
    translation_rows = load(TRANSLATION_SOURCE)
    missing_rows = load(MISSING_SOURCE)
    errors: list[str] = []
    approved_rows: list[dict[str, str]] = []

    for line, row in enumerate(translation_rows, 2):
        decision = (row.get("人工决定") or "").strip()
        if decision not in TRANSLATION_DECISIONS:
            errors.append(f"翻译文件第 {line} 行：非法人工决定 {decision!r}")
            continue
        if decision not in APPROVED:
            continue
        approved_text = (row.get("最终韩文") or "").strip()
        if not approved_text:
            approved_text = (row.get("建议韩文") or "").strip()
        if not approved_text:
            errors.append(f"翻译文件第 {line} 行：采纳项缺少最终韩文或建议韩文")
            continue
        approved_rows.append({
            "问题ID": row.get("问题ID", ""),
            "问题类型": "translation",
            "优先级": row.get("状态", ""),
            "文件": row.get("文件", ""),
            "位置或键": row.get("资源键", ""),
            "批准韩文或修复要求": approved_text,
            "修复范围": "translation-only",
            "审核备注": (row.get("备注") or "").strip(),
        })

    for line, row in enumerate(missing_rows, 2):
        decision = (row.get("人工决定") or "").strip()
        if decision not in MISSING_DECISIONS:
            errors.append(f"国际化遗漏文件第 {line} 行：非法人工决定 {decision!r}")
            continue
        if decision not in APPROVED:
            continue
        approved_rows.append({
            "问题ID": row.get("问题ID", ""),
            "问题类型": "missing_i18n",
            "优先级": row.get("状态", ""),
            "文件": row.get("文件", ""),
            "位置或键": row.get("位置", ""),
            "批准韩文或修复要求": (row.get("最终韩文/修复要求") or "").strip(),
            "修复范围": (row.get("修复范围") or "").strip(),
            "审核备注": (row.get("备注") or "").strip(),
        })

    if errors:
        print("修复计划校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PLAN_COLUMNS)
        writer.writeheader()
        writer.writerows(approved_rows)

    print(f"translation_candidates={len(translation_rows)}")
    print(f"missing_i18n_candidates={len(missing_rows)}")
    print(f"approved_for_repair={len(approved_rows)}")
    print(f"output={OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
