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
CONFIG = json.loads((OUT / "config.json").read_text(encoding="utf-8"))


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
    rules = {
        item["source_kind"]: item
        for item in CONFIG.get("candidate_scope_exclusions", [])
        if isinstance(item, dict) and item.get("source_kind")
    }
    manifest_path = OUT / "manifest/hardcoded_candidates.json"
    manifest = load(manifest_path)
    candidates = manifest["candidates"]
    by_id = {item["id"]: item for item in candidates}
    target_ids = {
        item["id"]
        for item in candidates
        if item.get("source_kind") in rules
    }
    if not target_ids:
        raise RuntimeError("no candidates matched candidate_scope_exclusions")

    now = datetime.now(timezone.utc).isoformat()
    updated_reviews = 0
    found_ids: set[str] = set()
    for path in sorted((OUT / "reviews/hardcoded").glob("*.json")):
        payload = load(path)
        changed = False
        for record in payload.get("records", []):
            rid = record.get("id")
            candidate = by_id.get(rid)
            if not candidate or rid not in target_ids:
                continue
            rule = rules[candidate["source_kind"]]
            record["status"] = rule.get("status", "无需国际化")
            record["reason"] = rule.get("reason") or "该候选类别按产品决定不纳入国际化遗漏项。"
            record["suggested_action"] = None
            record["suggested_ko"] = None
            record["severity"] = rule.get("severity", "低")
            record["reviewed_at"] = now
            record["excluded_from_missing"] = True
            record["exclusion_source_kind"] = candidate["source_kind"]
            candidate["status"] = record["status"]
            candidate["review"] = record
            found_ids.add(rid)
            updated_reviews += 1
            changed = True
        if changed:
            atomic_json(path, payload)

    missing = sorted(target_ids - found_ids)
    if missing:
        raise RuntimeError(f"excluded candidates without review records: {len(missing)}")

    quality_path = OUT / "reviews/quality/second_round.json"
    quality = load(quality_path)
    hard_quality = quality["hardcoded"]
    for key in ("confirmed_recheck_ids", "pending_recheck_ids", "dynamic_key_recheck_ids"):
        filtered = [rid for rid in hard_quality.get(key, []) if rid not in target_ids]
        hard_quality[key] = filtered
        hard_quality[key.removesuffix("_ids") + "_count"] = len(filtered)

    no_i18n_ids = {item["id"] for item in candidates if item["status"] == "无需国际化"}
    sample = [rid for rid in hard_quality.get("no_i18n_sample_ids", []) if rid in no_i18n_ids]
    required = math.ceil(len(no_i18n_ids) * 0.15)
    candidates_for_sample = sorted(target_ids - set(sample), key=digest)
    for rid in candidates_for_sample:
        if len(sample) >= required:
            break
        sample.append(rid)
    hard_quality["no_i18n_sample_ids"] = sample
    hard_quality["no_i18n_sample_count"] = len(sample)
    hard_quality["required_no_i18n_sample_count"] = required
    quality["candidate_scope_exclusions"] = [
        {"source_kind": kind, "count": sum(1 for item in candidates if item["source_kind"] == kind), "reason": rule.get("reason", "")}
        for kind, rule in sorted(rules.items())
    ]
    note = "按产品决定，仅实现中英双语的后端错误归类为无需国际化，不作为韩语遗漏项。"
    if note not in hard_quality.setdefault("findings", []):
        hard_quality["findings"].append(note)
    atomic_json(quality_path, quality)
    atomic_json(manifest_path, manifest)

    print(json.dumps({
        "updated_reviews": updated_reviews,
        "candidate_scope_exclusions": {kind: sum(1 for item in candidates if item["source_kind"] == kind) for kind in rules},
        "status_counts": dict(Counter(item["status"] for item in candidates)),
        "no_i18n_sample_count": len(sample),
        "no_i18n_sample_required": required,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
