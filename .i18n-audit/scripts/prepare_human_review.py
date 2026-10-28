from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
HUMAN = OUT / "reviews" / "human-review"
HUMAN.mkdir(parents=True, exist_ok=True)

TRANSLATION_COLUMNS = [
    "问题ID", "状态", "文件", "资源键", "中文原文", "当前韩文",
    "问题说明", "建议韩文", "人工决定", "最终韩文", "备注",
]
MISSING_COLUMNS = [
    "问题ID", "状态", "严重程度", "文件", "位置", "功能上下文", "原文或表达式",
    "问题说明", "建议处理方式", "建议韩文", "人工决定", "最终韩文/修复要求",
    "修复范围", "备注",
]
PLAN_COLUMNS = [
    "问题ID", "问题类型", "优先级", "文件", "位置或键",
    "批准韩文或修复要求", "修复范围", "审核备注",
]

translations = json.loads((OUT / "manifest/resources.json").read_text(encoding="utf-8"))["records"]
hardcoded = json.loads((OUT / "manifest/hardcoded_candidates.json").read_text(encoding="utf-8"))["candidates"]

translation_rows = []
for record in translations:
    if record["review_status"] not in {"必改", "建议改", "待核实"}:
        continue
    review = record.get("review", {})
    translation_rows.append({
        "问题ID": record["id"],
        "状态": record["review_status"],
        "文件": "src/i18n/locales/ko.json" if record["source_kind"] == "json-locale" else record["source_file"],
        "资源键": record["key"] if record["source_kind"] == "json-locale" else f"{record['namespace']}.{record['key']}",
        "中文原文": record["values"].get("zh") or "",
        "当前韩文": record["values"].get("ko") or "",
        "问题说明": review.get("reason") or "",
        "建议韩文": review.get("suggestion") or "",
        "人工决定": "",
        "最终韩文": "",
        "备注": "",
    })

missing_rows = []
for candidate in hardcoded:
    if candidate["status"] not in {"确认遗漏", "待核实"}:
        continue
    review = candidate.get("review", {})
    source_file = candidate["source_file"]
    if candidate["source_kind"] == "dynamic_i18n_key":
        fix_scope = "dynamic-key"
    elif source_file.startswith("src-tauri/"):
        fix_scope = "backend-error"
    else:
        fix_scope = "frontend-i18n"
    function = candidate.get("function") or "<module>"
    attribute = candidate.get("ui_attribute")
    context = function + (f" / {attribute}" if attribute else "")
    missing_rows.append({
        "问题ID": candidate["id"],
        "状态": candidate["status"],
        "严重程度": review.get("severity") or "",
        "文件": source_file,
        "位置": f"第 {candidate['line']} 行，第 {candidate['column']} 列",
        "功能上下文": context,
        "原文或表达式": candidate["expression"],
        "问题说明": review.get("reason") or "",
        "建议处理方式": review.get("suggested_action") or "",
        "建议韩文": review.get("suggested_ko") or "",
        "人工决定": "",
        "最终韩文/修复要求": "",
        "修复范围": fix_scope,
        "备注": "",
    })

translation_rows.sort(key=lambda row: (row["状态"], row["资源键"], row["问题ID"]))
missing_rows.sort(key=lambda row: (row["文件"], row["位置"], row["问题ID"]))

translation_path = HUMAN / "translation_review_decisions.csv"
with translation_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=TRANSLATION_COLUMNS)
    writer.writeheader()
    writer.writerows(translation_rows)

missing_path = HUMAN / "missing_i18n_review_decisions.csv"
with missing_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=MISSING_COLUMNS)
    writer.writeheader()
    writer.writerows(missing_rows)

plan_path = HUMAN / "repair_plan.csv"
with plan_path.open("w", encoding="utf-8-sig", newline="") as handle:
    csv.DictWriter(handle, fieldnames=PLAN_COLUMNS).writeheader()

print(f"translation_rows={len(translation_rows)}")
print(f"missing_i18n_rows={len(missing_rows)}")
print(translation_path.relative_to(ROOT))
print(missing_path.relative_to(ROOT))
print(plan_path.relative_to(ROOT))
