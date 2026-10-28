from __future__ import annotations
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HUMAN = ROOT / ".i18n-audit/reviews/human-review"
SOURCE = HUMAN / "review_decisions.csv"
OUTPUT = HUMAN / "repair_plan.csv"

TRANSLATION_DECISIONS = {"", "采纳", "修改后采纳", "保留原译", "暂不处理"}
MISSING_DECISIONS = {"", "确认修复", "误报", "无需国际化", "暂不处理"}
APPROVED = {"采纳", "修改后采纳", "确认修复"}
PLAN_COLUMNS = [
    "issue_id", "issue_type", "priority", "source_file", "location_or_key",
    "approved_text", "fix_scope", "reviewer_note",
]


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing {SOURCE}", file=sys.stderr)
        return 2
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    errors: list[str] = []
    approved_rows: list[dict[str, str]] = []
    counts = {"translation": 0, "missing_i18n": 0}
    for line, row in enumerate(rows, 2):
        issue_type = row.get("issue_type", "")
        decision = (row.get("review_decision") or "").strip()
        counts[issue_type] = counts.get(issue_type, 0) + 1
        allowed = TRANSLATION_DECISIONS if issue_type == "translation" else MISSING_DECISIONS
        if decision not in allowed:
            errors.append(f"line {line}: invalid decision {decision!r} for {issue_type}")
            continue
        if decision not in APPROVED:
            continue
        approved_text = (row.get("final_text") or "").strip()
        if issue_type == "translation" and not approved_text:
            approved_text = (row.get("ai_suggestion") or "").strip()
        if issue_type == "translation" and not approved_text:
            errors.append(f"line {line}: approved translation requires final_text or ai_suggestion")
            continue
        approved_rows.append({
            "issue_id": row.get("issue_id", ""),
            "issue_type": issue_type,
            "priority": row.get("priority", ""),
            "source_file": row.get("source_file", ""),
            "location_or_key": row.get("location_or_key", ""),
            "approved_text": approved_text,
            "fix_scope": (row.get("fix_scope") or "").strip(),
            "reviewer_note": (row.get("reviewer_note") or "").strip(),
        })
    if errors:
        print("Repair plan validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PLAN_COLUMNS)
        writer.writeheader()
        writer.writerows(approved_rows)
    print(f"candidates={len(rows)}")
    print(f"translation_candidates={counts.get('translation', 0)}")
    print(f"missing_i18n_candidates={counts.get('missing_i18n', 0)}")
    print(f"approved_for_repair={len(approved_rows)}")
    print(f"output={OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
