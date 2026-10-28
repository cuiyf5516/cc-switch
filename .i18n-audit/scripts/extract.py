from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
LOCALE_DIR = ROOT / "src/i18n/locales"
REFERENCE = "zh"
TARGET = "ko"
SUPPORTING = "en"


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def flatten(value: Any, path: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from flatten(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from flatten(child, path + (f"[{index}]",))
    else:
        yield path, value


def parse_json_keep_duplicates(path: Path) -> tuple[Any, list[dict[str, Any]]]:
    duplicates: list[dict[str, Any]] = []

    def hook(pairs: list[tuple[str, Any]]) -> OrderedDict[str, Any]:
        result: OrderedDict[str, Any] = OrderedDict()
        for key, value in pairs:
            if key in result:
                duplicates.append({"key": key, "value": value, "previous": result[key]})
            result[key] = value
        return result

    with path.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=hook), duplicates


def rust_block(text: str, marker: str, code: str) -> str | None:
    marker_at = text.find(marker)
    if marker_at < 0:
        return None
    match = re.search(rf'"{re.escape(code)}"\s*=>\s*Self\s*\{{', text[marker_at:])
    if not match:
        return None
    brace_at = marker_at + match.end() - 1
    depth = 0
    in_string = False
    escaped = False
    for index in range(brace_at, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[brace_at + 1:index]
    return None


def rust_string_literals(block: str) -> dict[str, str]:
    values: dict[str, str] = {}
    pattern = re.compile(r'^\s*(\w+):\s*"((?:\\.|[^"\\])*)",?\s*$', re.MULTILINE)
    for field, raw in pattern.findall(block):
        value = raw.replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\\\", "\\")
        values[field] = value
    return values


def rust_return_block(text: str, marker: str, pattern: str) -> str | None:
    marker_at = text.find(marker)
    if marker_at < 0:
        return None
    match = re.search(pattern, text[marker_at:])
    if not match:
        return None
    brace_at = marker_at + match.end() - 1
    depth = 0
    in_string = False
    escaped = False
    for index in range(brace_at, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[brace_at + 1:index]
    return None


def rust_assignments(block: str) -> dict[str, str]:
    values: dict[str, str] = {}
    pattern = re.compile(r'^\s*texts\.(\w+)\s*=\s*"((?:\\.|[^"\\])*)";\s*$', re.MULTILINE)
    for field, raw in pattern.findall(block):
        value = raw.replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\\\", "\\")
        values[field] = value
    return values


def panel_blocks(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    marker = "pub fn from_language"
    result: dict[str, dict[str, str]] = {}
    english_block = rust_return_block(text, marker, r'"en"\s*\|\s*"tr"\s*=>\s*Self\s*\{')
    if english_block:
        english = rust_string_literals(english_block)
        english.setdefault("lightweight_mode", "Lightweight mode")
        result["en"] = english
        turkish = dict(english)
        turkish["lightweight_mode"] = "Hafif mod"
        result["tr"] = turkish
    chinese_block = rust_return_block(text, marker, r'_\s*=>\s*Self\s*\{')
    if chinese_block:
        result["zh"] = rust_string_literals(chinese_block)
    for code, pattern in (
        ("ja", r'"ja"\s*=>\s*Self\s*\{'),
        ("zh-TW", r'"zh-TW"\s*=>\s*Self\s*\{'),
        ("ko", r'"ko"\s*=>\s*Self\s*\{'),
    ):
        block = rust_return_block(text, marker, pattern)
        if block:
            result[code] = rust_string_literals(block)
    return result


def tray_blocks(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    marker = "pub fn from_language"
    base = rust_return_block(text, marker, r'"en"\s*=>\s*Self\s*\{')
    chinese = rust_return_block(text, marker, r'_\s*=>\s*Self\s*\{')
    korean = rust_return_block(text, marker, r'"ko"\s*=>\s*\{')
    japanese = rust_return_block(text, marker, r'"ja"\s*=>\s*Self\s*\{')
    traditional = rust_return_block(text, marker, r'"zh-TW"\s*=>\s*Self\s*\{')
    result: dict[str, dict[str, str]] = {}
    if base:
        english = rust_string_literals(base)
        result["en"] = english
        turkish = dict(english)
        turkish.update(rust_assignments(rust_return_block(text, marker, r'"tr"\s*=>\s*\{') or ""))
        result["tr"] = turkish
    if chinese:
        result["zh"] = rust_string_literals(chinese)
    if japanese:
        result["ja"] = rust_string_literals(japanese)
    if traditional:
        result["zh-TW"] = rust_string_literals(traditional)
    if korean and "en" in result:
        korean_values = dict(result["en"])
        korean_values.update(rust_assignments(korean))
        result["ko"] = korean_values
    return result


def all_rust_blocks(path: Path, marker: str) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, dict[str, str]] = {}
    for code in ("zh", "zh-TW", "en", "ja", "tr", "ko", "_"):
        block = rust_block(text, marker, code)
        if block is None:
            continue
        normalized = "zh" if code == "_" else code
        result[normalized] = rust_string_literals(block)
    return result


def embedded_error_messages(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, dict[str, str]] = {}
    for function in ("invalid_json_format_error", "invalid_toml_format_error"):
        start = text.find(f"fn {function}")
        if start < 0:
            continue
        end = text.find("\nfn ", start + 4)
        section = text[start : end if end >= 0 else len(text)]
        values: dict[str, str] = {}
        replacements = {re.escape("{" + name + "}"): "{{" + name + "}}" for name in ("error",)}
        for quoted_code, fallback_code, raw in re.findall(r'(?:"([a-zA-Z_-]+)"|(_))\s*=>\s*format!\(\s*"((?:\\.|[^"\\])*)"', section):
            code = quoted_code or fallback_code
            value = raw.replace('\\"', '"')
            for escaped, replacement in replacements.items():
                value = re.sub(escaped, replacement, value)
            values["zh" if code == "_" else code] = value
        result[function] = values
    return result


PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\{\s*[^{}]+\s*\}\}"),
    re.compile(r"\{\s*[A-Za-z_][A-Za-z0-9_.-]*\s*\}"),
    re.compile(r"%[-+0-9.#]*[a-zA-Z]"),
]
HTML_TAG = re.compile(r"</?[A-Za-z][^>]*>")


def technical_tokens(value: str) -> dict[str, Any]:
    placeholders: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        for found in pattern.findall(value):
            if found not in placeholders:
                placeholders.append(found)
    return {
        "placeholders": sorted(placeholders),
        "html_tags": sorted(set(HTML_TAG.findall(value))),
        "newline_count": value.count("\n"),
        "leading_space": value[:1].isspace() if value else False,
        "trailing_space": value[-1:].isspace() if value else False,
    }


def main() -> int:
    if not LOCALE_DIR.exists():
        print(f"Locale directory not found: {LOCALE_DIR}", file=sys.stderr)
        return 2

    locale_files = sorted(LOCALE_DIR.glob("*.json"))
    locale_values: dict[str, dict[str, str]] = {}
    locale_meta: list[dict[str, Any]] = []
    duplicate_keys: list[dict[str, Any]] = []
    parse_issues: list[dict[str, Any]] = []
    non_string_leaves: list[dict[str, Any]] = []

    for path in locale_files:
        language = path.stem
        try:
            tree, duplicates = parse_json_keep_duplicates(path)
        except Exception as exc:  # noqa: BLE001 - surfaced in the audit manifest
            parse_issues.append({"file": path.relative_to(ROOT).as_posix(), "error": str(exc)})
            continue
        values: dict[str, str] = {}
        for parts, leaf in flatten(tree):
            key = ".".join(parts)
            if isinstance(leaf, str):
                values[key] = leaf
            else:
                non_string_leaves.append({
                    "file": path.relative_to(ROOT).as_posix(), "key": key, "type": type(leaf).__name__, "value": leaf,
                })
        locale_values[language] = values
        for index, duplicate in enumerate(duplicates, 1):
            duplicate_keys.append({
                "file": path.relative_to(ROOT).as_posix(),
                "ordinal": index,
                "key": duplicate["key"],
                "value": duplicate["value"],
                "previous": duplicate["previous"],
            })
        locale_meta.append({
            "language": language,
            "file": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "string_count": len(values),
            "fingerprint": sha256("\n".join(f"{key}\0{value}" for key, value in sorted(values.items()))),
        })

    if not all(lang in locale_values for lang in (REFERENCE, TARGET, SUPPORTING)):
        print("Required zh/ko/en locale files were not all parsed", file=sys.stderr)
        return 2

    all_keys = sorted(set().union(*(set(values) for values in locale_values.values())))
    records: list[dict[str, Any]] = []
    for key in all_keys:
        content = {lang: locale_values[lang].get(key) for lang in sorted(locale_values)}
        present = {lang: value is not None for lang, value in content.items()}
        fingerprints = {
            lang: sha256(value) if value is not None else None for lang, value in content.items()
        }
        technical = {
            lang: technical_tokens(value) if value is not None else None for lang, value in content.items()
        }
        combined = sha256("\n".join(f"{lang}\0{value or ''}" for lang, value in sorted(content.items())))
        records.append({
            "id": f"json:src/i18n/locales#{key}",
            "source_kind": "json-locale",
            "source_file": "src/i18n/locales/{language}.json",
            "namespace": key.split(".", 1)[0],
            "key": key,
            "values": content,
            "present": present,
            "fingerprints": fingerprints,
            "combined_fingerprint": combined,
            "technical": technical,
            "review_batch": None,
            "review_status": "未审核",
        })

    native_sources = [
        ("tray", ROOT / "src-tauri/src/tray.rs", "pub fn from_language"),
        ("panel", ROOT / "src-tauri/src/tray_panel.rs", "pub fn from_language"),
    ]
    for namespace, path, marker in native_sources:
        blocks = tray_blocks(path) if namespace == "tray" else panel_blocks(path)
        if TARGET not in blocks:
            parse_issues.append({"file": path.relative_to(ROOT).as_posix(), "error": f"Korean block not found near {marker}"})
            continue
        fields = sorted(set().union(*(block.keys() for block in blocks.values())))
        for field in fields:
            content = {lang: block.get(field) for lang, block in blocks.items()}
            if not any(isinstance(value, str) for value in content.values()):
                continue
            fingerprints = {lang: sha256(value) if isinstance(value, str) else None for lang, value in content.items()}
            technical = {lang: technical_tokens(value) if isinstance(value, str) else None for lang, value in content.items()}
            combined = sha256("\n".join(f"{lang}\0{value or ''}" for lang, value in sorted(content.items())))
            records.append({
                "id": f"rust:{path.relative_to(ROOT).as_posix()}#{field}",
                "source_kind": f"native-{namespace}",
                "source_file": path.relative_to(ROOT).as_posix(),
                "namespace": namespace,
                "key": field,
                "values": content,
                "present": {lang: isinstance(value, str) for lang, value in content.items()},
                "fingerprints": fingerprints,
                "combined_fingerprint": combined,
                "technical": technical,
                "review_batch": None,
                "review_status": "未审核",
            })

    error_path = ROOT / "src-tauri/src/commands/config.rs"
    for key, blocks in embedded_error_messages(error_path).items():
        content = {lang: block.get(lang) for lang, block in {"messages": blocks}.items()} if False else blocks
        if not content:
            continue
        fingerprints = {lang: sha256(value) if isinstance(value, str) else None for lang, value in content.items()}
        technical = {lang: technical_tokens(value) if isinstance(value, str) else None for lang, value in content.items()}
        combined = sha256("\n".join(f"{lang}\0{value or ''}" for lang, value in sorted(content.items())))
        records.append({
            "id": f"rust:{error_path.relative_to(ROOT).as_posix()}#{key}",
            "source_kind": "native-inline-error",
            "source_file": error_path.relative_to(ROOT).as_posix(),
            "namespace": "nativeErrors",
            "key": key,
            "values": content,
            "present": {lang: isinstance(value, str) for lang, value in content.items()},
            "fingerprints": fingerprints,
            "combined_fingerprint": combined,
            "technical": technical,
            "review_batch": None,
            "review_status": "未审核",
        })

    anomalies: list[dict[str, Any]] = []
    for record in records:
        key = record["key"]
        if not record["present"].get(TARGET):
            anomalies.append({"type": "missing_korean", "id": record["id"], "key": key})
        elif not record["values"][TARGET].strip() and (record["values"].get(REFERENCE) or "").strip():
            anomalies.append({"type": "empty_korean_but_reference_nonempty", "id": record["id"], "key": key})
        if not record["present"].get(REFERENCE):
            anomalies.append({"type": "missing_chinese", "id": record["id"], "key": key})
        if not record["present"].get(SUPPORTING):
            anomalies.append({"type": "missing_english", "id": record["id"], "key": key})
        source_ph = (record["technical"].get(REFERENCE) or {}).get("placeholders", [])
        target_ph = (record["technical"].get(TARGET) or {}).get("placeholders", [])
        english_ph = (record["technical"].get(SUPPORTING) or {}).get("placeholders", [])
        expected_ph = source_ph or english_ph
        if record["present"].get(TARGET) and sorted(target_ph) != sorted(expected_ph):
            anomalies.append({
                "type": "placeholder_mismatch", "id": record["id"], "key": key,
                "expected": expected_ph, "korean": target_ph,
            })

    manifest = {
        "schema_version": 1,
        "generated_by": ".i18n-audit/scripts/extract.py",
        "project_root": ROOT.as_posix(),
        "reference_language": REFERENCE,
        "target_language": TARGET,
        "supporting_language": SUPPORTING,
        "locale_files": locale_meta,
        "duplicate_keys": duplicate_keys,
        "parse_issues": parse_issues,
        "non_string_leaves": non_string_leaves,
        "resource_count": len(records),
        "records": records,
        "anomalies": anomalies,
    }
    atomic_json(OUT / "manifest/resources.json", manifest)
    print(json.dumps({
        "resource_count": len(records),
        "locale_files": len(locale_meta),
        "duplicate_keys": len(duplicate_keys),
        "parse_issues": len(parse_issues),
        "anomalies": len(anomalies),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
