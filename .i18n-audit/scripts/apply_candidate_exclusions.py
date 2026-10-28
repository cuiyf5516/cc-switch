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


def matches(rule: dict[str, Any], candidate: dict[str, Any]) -> bool:
    kind = rule.get("source_kind")
    prefix = rule.get("source_file_prefix")
    if kind and candidate.get("source_kind") != kind:
        return False
    if prefix and not candidate.get("source_file", "").startswith(prefix):
        return False
    statuses = rule.get("apply_to_statuses")
    if statuses and candidate.get("status") not in statuses:
        return False
    return bool(kind or prefix)


def main() -> int:
    rules = [
        item
        for item in CONFIG.get("candidate_scope_exclusions", [])
        if isinstance(item, dict) and (item.get("source_kind") or item.get("source_file_prefix"))
    ]
    manifest_path = OUT / "manifest/hardcoded_candidates.json"
    manifest = load(manifest_path)
    candidates = manifest["candidates"]
    by_id = {item["id"]: item for item in candidates}
    quality_path = OUT / "reviews/quality/second_round.json"
    quality = load(quality_path)
    previous_exclusions = {
        item.get("id"): set(item.get("matched_ids", []))
        for item in quality.get("candidate_scope_exclusions", [])
        if isinstance(item, dict) and item.get("id")
    }
    rule_members: dict[str, set[str]] = {}
    for rule in rules:
        label = rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix")
        current = {item["id"] for item in candidates if matches(rule, item)}
        historical = previous_exclusions.get(label, set()) & set(by_id)
        rule_members[label] = current | historical
    target_ids = set().union(*rule_members.values()) if rule_members else set()
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
            rule = next(
                rule for rule in rules
                if rid in rule_members[rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix")]
            )
            record["status"] = rule.get("status", "无需国际化")
            record["reason"] = rule.get("reason") or "该候选类别按产品决定不纳入国际化遗漏项。"
            record["suggested_action"] = None
            record["suggested_ko"] = None
            record["severity"] = rule.get("severity", "低")
            record["reviewed_at"] = now
            record["excluded_from_missing"] = True
            record["exclusion_rule_id"] = rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix")
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
        {
            "id": rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix"),
            "source_kind": rule.get("source_kind"),
            "source_file_prefix": rule.get("source_file_prefix"),
            "count": len(rule_members[rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix")]),
            "reason": rule.get("reason", ""),
            "matched_ids": sorted(rule_members[rule.get("id") or rule.get("source_kind") or rule.get("source_file_prefix")]),
        }
        for rule in rules
    ]
    quality["candidate_scope_exclusion_unique_count"] = len(target_ids)
    note = "按产品决定，后端错误及单语/双语前端硬编码文案不纳入韩语国际化遗漏项。"
    if note not in hard_quality.setdefault("findings", []):
        hard_quality["findings"].append(note)

    resources = load(OUT / "manifest/resources.json")
    resource_keys = {
        record["key"]
        for record in resources["records"]
        if record.get("source_kind") == "json-locale"
    }
    false_positive_rules = CONFIG.get("false_positive_translation_refs", [])
    missing_refs: list[dict[str, Any]] = []
    false_positive_refs: list[dict[str, Any]] = []
    for ref in manifest.get("translation_refs", []):
        if ref.get("key") in resource_keys:
            continue
        rule = next(
            (
                item for item in false_positive_rules
                if item.get("source_file") == ref.get("source_file") and item.get("key") == ref.get("key")
            ),
            None,
        )
        if rule:
            false_positive_refs.append({**ref, "false_positive": True, "reason": rule.get("reason", "")})
        else:
            missing_refs.append(ref)
    manifest["missing_translation_keys"] = missing_refs
    manifest["false_positive_translation_refs"] = false_positive_refs
    quality["false_positive_translation_ref_count"] = len(false_positive_refs)

    atomic_json(quality_path, quality)
    atomic_json(manifest_path, manifest)

    print(json.dumps({
        "updated_reviews": updated_reviews,
        "candidate_scope_exclusions": {key: len(value) for key, value in rule_members.items()},
        "unique_excluded_candidates": len(target_ids),
        "status_counts": dict(Counter(item["status"] for item in candidates)),
        "no_i18n_sample_count": len(sample),
        "no_i18n_sample_required": required,
        "false_positive_translation_ref_count": len(false_positive_refs),
        "remaining_missing_translation_keys": len(missing_refs),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
