from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
HUMAN = OUT / "reviews" / "human-review"
HUMAN.mkdir(parents=True, exist_ok=True)

COLUMNS = [
    "issue_id", "issue_type", "priority", "source_file", "location_or_key",
    "original_text", "current_korean", "ai_status", "ai_reason", "ai_suggestion",
    "review_decision", "final_text", "fix_scope", "reviewer_note",
]
PLAN_COLUMNS = [
    "issue_id", "issue_type", "priority", "source_file", "location_or_key",
    "approved_text", "fix_scope", "reviewer_note",
]

translations = json.loads((OUT / "manifest/resources.json").read_text(encoding="utf-8"))["records"]
hardcoded = json.loads((OUT / "manifest/hardcoded_candidates.json").read_text(encoding="utf-8"))["candidates"]

rows = []
for record in translations:
    if record["review_status"] not in {"必改", "建议改", "待核实"}:
        continue
    review = record.get("review", {})
    rows.append({
        "issue_id": record["id"],
        "issue_type": "translation",
        "priority": record["review_status"],
        "source_file": "src/i18n/locales/ko.json" if record["source_kind"] == "json-locale" else record["source_file"],
        "location_or_key": record["key"] if record["source_kind"] == "json-locale" else f"{record['namespace']}.{record['key']}",
        "original_text": record["values"].get("zh") or "",
        "current_korean": record["values"].get("ko") or "",
        "ai_status": record["review_status"],
        "ai_reason": review.get("reason") or "",
        "ai_suggestion": review.get("suggestion") or "",
        "review_decision": "",
        "final_text": "",
        "fix_scope": "translation-only",
        "reviewer_note": "",
    })

for candidate in hardcoded:
    if candidate["status"] not in {"确认遗漏", "待核实"}:
        continue
    review = candidate.get("review", {})
    source_file = candidate["source_file"]
    if source_file == "deplink.html":
        fix_scope = "deplink-page"
    elif candidate["source_kind"] == "dynamic_i18n_key":
        fix_scope = "dynamic-key"
    elif source_file.startswith("src-tauri/"):
        fix_scope = "backend-error"
    else:
        fix_scope = "frontend-i18n"
    suggestion = review.get("suggested_action") or ""
    if review.get("suggested_ko"):
        suggestion = f"{suggestion} 推荐韩文：{review['suggested_ko']}".strip()
    rows.append({
        "issue_id": candidate["id"],
        "issue_type": "missing_i18n",
        "priority": review.get("severity") or candidate["status"],
        "source_file": source_file,
        "location_or_key": f"{candidate['function']}@{candidate['line']}",
        "original_text": candidate["expression"],
        "current_korean": "",
        "ai_status": candidate["status"],
        "ai_reason": review.get("reason") or "",
        "ai_suggestion": suggestion,
        "review_decision": "",
        "final_text": "",
        "fix_scope": fix_scope,
        "reviewer_note": "",
    })

rows.sort(key=lambda row: (row["issue_type"], row["source_file"], row["location_or_key"], row["issue_id"]))

review_path = HUMAN / "review_decisions.csv"
with review_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

plan_path = HUMAN / "repair_plan.csv"
with plan_path.open("w", encoding="utf-8-sig", newline="") as handle:
    csv.DictWriter(handle, fieldnames=PLAN_COLUMNS).writeheader()

print(f"review_rows={len(rows)}")
print(f"translation_issues={sum(row['issue_type'] == 'translation' for row in rows)}")
print(f"missing_i18n_issues={sum(row['issue_type'] == 'missing_i18n' for row in rows)}")
print(review_path.relative_to(ROOT))
print(plan_path.relative_to(ROOT))
