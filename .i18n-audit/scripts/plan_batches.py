from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
CONFIG = json.loads((OUT / "config.json").read_text(encoding="utf-8"))


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def safe(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-")


def load_reviews() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in sorted((OUT / "reviews/translations").glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for record in payload.get("records", []):
            if isinstance(record, dict) and record.get("id"):
                result[record["id"]] = record
    return result


def main() -> int:
    manifest_path = OUT / "manifest/resources.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = manifest["records"]
    existing = load_reviews()
    restored = 0
    stale = 0
    for record in records:
        review = existing.get(record["id"])
        if not review:
            continue
        if review.get("combined_fingerprint") == record["combined_fingerprint"] and review.get("status") in CONFIG["translation_statuses"]:
            record["review_status"] = review["status"]
            record["review"] = review
            restored += 1
        else:
            stale += 1
    atomic_json(manifest_path, manifest)

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[(record["source_kind"], record["namespace"])].append(record)

    size = int(CONFIG.get("translation_batch_size", 40))
    batches: list[dict[str, Any]] = []
    assignments: dict[str, str] = {}
    for (source_kind, namespace), items in sorted(grouped.items()):
        items.sort(key=lambda item: item["key"])
        for chunk_index, start in enumerate(range(0, len(items), size), 1):
            chunk = items[start:start + size]
            batch_id = f"translation:{safe(source_kind)}:{safe(namespace)}:{chunk_index:03d}"
            batch = {
                "batch_id": batch_id,
                "kind": "translation",
                "source_kind": source_kind,
                "namespace": namespace,
                "ordinal": chunk_index,
                "record_count": len(chunk),
                "record_ids": [item["id"] for item in chunk],
                "keys": [item["key"] for item in chunk],
            }
            batches.append(batch)
            for item in chunk:
                item["review_batch"] = batch_id
                assignments[item["id"]] = batch_id
            atomic_json(OUT / "batches/translations" / f"{safe(batch_id)}.json", batch)

    atomic_json(manifest_path, manifest)
    payload = {
        "schema_version": 1,
        "generated_by": ".i18n-audit/scripts/plan_batches.py",
        "batch_size": size,
        "batch_count": len(batches),
        "record_count": len(records),
        "restored_valid_reviews": restored,
        "stale_reviews": stale,
        "batches": batches,
    }
    atomic_json(OUT / "manifest/translation_batches.json", payload)
    print(json.dumps({
        "record_count": len(records), "batch_count": len(batches),
        "restored_valid_reviews": restored, "stale_reviews": stale,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
