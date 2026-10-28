from __future__ import annotations

import json
import math
import re
import shutil
from collections import Counter, defaultdict
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


def safe(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-")


def assert_within(path: Path, parent: Path) -> None:
    resolved = path.resolve()
    root = parent.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"refusing to touch path outside {root}: {resolved}") from exc


def replace_directory_atomically(staged: Path, target: Path, backup: Path) -> None:
    assert_within(staged, OUT)
    assert_within(target, OUT)
    assert_within(backup, OUT)
    if backup.exists():
        shutil.rmtree(backup)
    if target.exists():
        target.rename(backup)
    staged.rename(target)
    if backup.exists():
        shutil.rmtree(backup)


def main() -> int:
    manifest_path = OUT / "manifest/hardcoded_candidates.json"
    manifest = load(manifest_path)
    batches_payload = load(OUT / "manifest/hardcoded_batches.json")
    candidates = manifest["candidates"]
    candidate_by_id = {item["id"]: item for item in candidates}
    scope_excluded = {
        item["path"]
        for item in CONFIG.get("scope_exclusions", [])
        if isinstance(item, dict) and item.get("path")
    }
    excluded_ids = {
        item["id"] for item in candidates if item.get("source_file") in scope_excluded
    }
    # The freshly scanned manifest no longer contains excluded files. Recover their historical
    # IDs from review records so they can be removed explicitly instead of becoming silent orphans.
    review_dir = OUT / "reviews/hardcoded"
    review_records: dict[str, dict[str, Any]] = {}
    duplicate_ids: list[str] = []
    for path in sorted(review_dir.glob("*.json")):
        payload = load(path)
        for record in payload.get("records", []):
            rid = record.get("id")
            if not rid:
                continue
            if record.get("source_file") in scope_excluded:
                excluded_ids.add(rid)
            if rid in review_records:
                duplicate_ids.append(rid)
            review_records[rid] = record
    if duplicate_ids:
        raise RuntimeError(f"duplicate hardcoded review IDs: {len(duplicate_ids)}")

    unknown = sorted(set(review_records) - set(candidate_by_id) - excluded_ids)
    if unknown:
        raise RuntimeError(f"refusing to prune non-excluded orphan reviews: {len(unknown)}")

    current_ids = set(candidate_by_id)
    retained: dict[str, dict[str, Any]] = {}
    dropped_excluded = 0
    for rid, record in review_records.items():
        if rid in excluded_ids:
            dropped_excluded += 1
            continue
        if rid not in current_ids:
            continue
        record["review_batch"] = candidate_by_id[rid]["review_batch"]
        retained[rid] = record

    missing_reviews = sorted(current_ids - set(retained))
    if missing_reviews:
        raise RuntimeError(f"scope cleanup would leave {len(missing_reviews)} candidates unreviewed")

    batch_by_id = {item["batch_id"]: item for item in batches_payload["batches"]}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rid, record in retained.items():
        batch_id = candidate_by_id[rid]["review_batch"]
        if batch_id not in batch_by_id:
            raise RuntimeError(f"missing batch assignment for {rid}: {batch_id}")
        grouped[batch_id].append(record)

    batch_dir = OUT / "batches/hardcoded"
    staged_batches = OUT / "batches/.hardcoded-scope-staged"
    if staged_batches.exists():
        shutil.rmtree(staged_batches)
    staged_batches.mkdir(parents=True)
    for batch in batches_payload["batches"]:
        atomic_json(staged_batches / f"{safe(batch['batch_id'])}.json", batch)

    staged_reviews = OUT / "reviews/.hardcoded-scope-staged"
    if staged_reviews.exists():
        shutil.rmtree(staged_reviews)
    staged_reviews.mkdir(parents=True)
    for batch in batches_payload["batches"]:
        batch_id = batch["batch_id"]
        records = sorted(grouped.get(batch_id, []), key=lambda item: item["id"])
        if len(records) != batch["record_count"]:
            raise RuntimeError(
                f"review count mismatch for {batch_id}: {len(records)} != {batch['record_count']}"
            )
        reviewed_at = max((item.get("reviewed_at", "") for item in records), default="")
        payload = {
            "schema_version": 1,
            "batch_id": batch_id,
            "kind": "hardcoded",
            "group": batch["group"],
            "reviewed_at": reviewed_at,
            "review_count": len(records),
            "records": records,
        }
        atomic_json(staged_reviews / f"{safe(batch_id)}.json", payload)

    for candidate in candidates:
        record = retained[candidate["id"]]
        candidate["status"] = record["status"]
        candidate["review"] = record
        candidate["review_batch"] = record["review_batch"]

    replace_directory_atomically(
        staged_reviews,
        review_dir,
        OUT / "reviews/.hardcoded-scope-backup",
    )
    replace_directory_atomically(
        staged_batches,
        batch_dir,
        OUT / "batches/.hardcoded-scope-backup",
    )
    atomic_json(manifest_path, manifest)

    quality_path = OUT / "reviews/quality/second_round.json"
    quality = load(quality_path)
    hard_quality = quality["hardcoded"]
    quality_keys = (
        "confirmed_recheck_ids",
        "pending_recheck_ids",
        "dynamic_key_recheck_ids",
        "no_i18n_sample_ids",
    )
    for key in quality_keys:
        filtered = [rid for rid in hard_quality.get(key, []) if rid in current_ids]
        hard_quality[key] = filtered
        count_key = key.removesuffix("_ids") + "_count"
        hard_quality[count_key] = len(filtered)
    no_i18n_count = sum(1 for item in candidates if item["status"] == "无需国际化")
    hard_quality["required_no_i18n_sample_count"] = math.ceil(no_i18n_count * 0.15)
    quality["scope_exclusions"] = [
        {"path": item["path"], "reason": item.get("reason", "")}
        for item in CONFIG.get("scope_exclusions", [])
    ]
    atomic_json(quality_path, quality)

    counts = Counter(item["status"] for item in candidates)
    print(json.dumps({
        "scope_excluded_files": sorted(scope_excluded),
        "dropped_excluded_review_records": dropped_excluded,
        "remaining_candidates": len(candidates),
        "remaining_reviews": len(retained),
        "status_counts": dict(counts),
        "remaining_batches": len(batches_payload["batches"]),
        "no_i18n_sample_reviewed": len(hard_quality["no_i18n_sample_ids"]),
        "no_i18n_sample_required": hard_quality["required_no_i18n_sample_count"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
