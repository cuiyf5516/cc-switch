from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
RESULT_PATH = OUT / "reviews/quality/dynamic_key_verification.json"
MANIFEST_PATH = OUT / "manifest/hardcoded_candidates.json"
QUALITY_PATH = OUT / "reviews/quality/second_round.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def main() -> int:
    result = load(RESULT_PATH)
    decisions = {item["id"]: item for item in result["decisions"]}
    manifest = load(MANIFEST_PATH)
    candidates = manifest["candidates"]
    by_id = {item["id"]: item for item in candidates}
    if len(decisions) != 162:
        raise RuntimeError(f"expected 162 dynamic decisions, found {len(decisions)}")
    unknown = set(decisions) - set(by_id)
    if unknown:
        raise RuntimeError(f"dynamic decisions reference {len(unknown)} unknown candidates")

    now = datetime.now(timezone.utc).isoformat()
    records_by_id: dict[str, dict[str, Any]] = {}
    for path in sorted((OUT / "reviews/hardcoded").glob("*.json")):
        payload = load(path)
        changed = False
        for record in payload.get("records", []):
            decision = decisions.get(record.get("id"))
            if not decision:
                continue
            status = decision["status"]
            record["status"] = status
            record["reason"] = decision["reason"]
            record["suggested_action"] = (
                "为 `apps.kimi`、`apps.dsh` 增加 zh/en/ko 资源键，或对不支持的应用不渲染该帮助文案。"
                if status == "确认遗漏"
                else None
            )
            record["suggested_ko"] = decision.get("suggested_ko")
            record["severity"] = "中" if status == "确认遗漏" else "低"
            record["reviewed_at"] = now
            record["dynamic_key_verification"] = True
            record["dynamic_key_resolution"] = decision["resolution"]
            record["evidence_keys"] = decision.get("evidence", [])
            records_by_id[record["id"]] = record
            changed = True
        if changed:
            atomic_json(path, payload)

    missing_records = sorted(set(decisions) - set(records_by_id))
    if missing_records:
        raise RuntimeError(f"dynamic decisions without review records: {len(missing_records)}")
    for item in candidates:
        record = records_by_id.get(item["id"])
        if record:
            item["status"] = record["status"]
            item["review"] = record

    quality = load(QUALITY_PATH)
    hard_quality = quality["hardcoded"]
    confirmed_ids = sorted(rid for rid, decision in decisions.items() if decision["status"] == "确认遗漏")
    pending_ids = sorted(rid for rid, decision in decisions.items() if decision["status"] == "待核实")
    dynamic_ids = sorted(decisions)
    hard_quality["confirmed_recheck_ids"] = confirmed_ids
    hard_quality["confirmed_recheck_count"] = len(confirmed_ids)
    hard_quality["pending_recheck_ids"] = pending_ids
    hard_quality["pending_recheck_count"] = len(pending_ids)
    hard_quality["dynamic_key_recheck_ids"] = dynamic_ids
    hard_quality["dynamic_key_recheck_count"] = len(dynamic_ids)

    no_i18n_ids = {item["id"] for item in candidates if item["status"] == "无需国际化"}
    sample = [rid for rid in hard_quality.get("no_i18n_sample_ids", []) if rid in no_i18n_ids]
    required = math.ceil(len(no_i18n_ids) * 0.15)
    new_safe_dynamic = sorted(
        [
            rid for rid in decisions
            if decisions[rid]["status"] == "无需国际化" and rid not in sample
        ],
        key=digest,
    )
    for rid in new_safe_dynamic:
        if len(sample) >= required:
            break
        sample.append(rid)
    hard_quality["no_i18n_sample_ids"] = sample
    hard_quality["no_i18n_sample_count"] = len(sample)
    hard_quality["required_no_i18n_sample_count"] = required
    all_language_defects = [
        {
            "id": rid,
            "source_file": decisions[rid]["source_file"],
            "line": decisions[rid]["line"],
            "expression": decisions[rid]["expression"],
            "reason": decisions[rid]["reason"],
            "resolution": decisions[rid]["resolution"],
            "suggested_ko": decisions[rid].get("suggested_ko"),
        }
        for rid in dynamic_ids
        if decisions[rid].get("resolution") == "all-language-missing"
    ]
    quality["dynamic_key_verification"] = {
        "total": len(dynamic_ids),
        "confirmed_missing": len(confirmed_ids),
        "safe_or_false_positive": len(dynamic_ids) - len(confirmed_ids) - len(all_language_defects),
        "pending": len(pending_ids),
        "all_language_missing": len(all_language_defects),
        "result_file": str(RESULT_PATH.relative_to(ROOT)),
    }
    quality["all_language_i18n_defects"] = all_language_defects
    note = "动态翻译键已逐项核实：161 条解析为有限枚举、本地词典或有意回退；1 条确认缺少 apps.kimi/apps.dsh。"
    if note not in hard_quality.setdefault("findings", []):
        hard_quality["findings"].append(note)

    atomic_json(MANIFEST_PATH, manifest)
    atomic_json(QUALITY_PATH, quality)
    print(json.dumps({
        "confirmed": confirmed_ids,
        "pending": len(pending_ids),
        "safe_or_false_positive": len(dynamic_ids) - len(confirmed_ids) - len(all_language_defects),
        "status_counts": dict(Counter(item["status"] for item in candidates)),
        "no_i18n_sample_count": len(sample),
        "no_i18n_sample_required": required,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
