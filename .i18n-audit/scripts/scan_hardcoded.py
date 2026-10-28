from __future__ import annotations

import hashlib
import html.parser
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
CONFIG = json.loads((OUT / "config.json").read_text(encoding="utf-8"))


def sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def is_test_path(rel: str) -> bool:
    lower = rel.lower()
    name = Path(rel).name.lower()
    return (
        "/tests/" in f"/{lower}/"
        or "/__tests__/" in lower
        or ".test." in name
        or ".spec." in name
        or name.endswith("_tests.rs")
        or name == "agy_smoke_tests.rs"
        or name == "tests.rs"
    )


def enumerate_sources() -> tuple[list[str], list[dict[str, Any]]]:
    included: list[str] = []
    excluded: list[dict[str, Any]] = []
    scope_exclusions = {
        item["path"]: item["reason"]
        for item in CONFIG.get("scope_exclusions", [])
        if isinstance(item, dict) and item.get("path")
    }
    for base in (ROOT / "src", ROOT / "src-tauri/src"):
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            ext = path.suffix.lower()
            if ext not in {".ts", ".tsx", ".js", ".jsx", ".html", ".rs"}:
                continue
            if is_test_path(rel):
                excluded.append({"path": rel, "reason": "test file", "category": "test/non-production"})
            elif rel in scope_exclusions:
                excluded.append({"path": rel, "reason": scope_exclusions[rel], "category": "scope-exclusion"})
            else:
                included.append(rel)
    for rel, reason in scope_exclusions.items():
        path = ROOT / rel
        if path.is_file() and rel not in included and not any(item["path"] == rel for item in excluded):
            excluded.append({"path": rel, "reason": reason, "category": "scope-exclusion"})
    return sorted(set(included)), sorted(excluded, key=lambda item: item["path"])


def rust_strings(text: str) -> list[tuple[str, int, str]]:
    result: list[tuple[str, int, str]] = []
    i = 0
    n = len(text)
    line_comment = False
    block_depth = 0
    while i < n:
        if line_comment:
            if text[i] == "\n":
                line_comment = False
            i += 1
            continue
        if block_depth:
            if text.startswith("/*", i):
                block_depth += 1
                i += 2
            elif text.startswith("*/", i):
                block_depth -= 1
                i += 2
            else:
                i += 1
            continue
        if text.startswith("//", i):
            line_comment = True
            i += 2
            continue
        if text.startswith("/*", i):
            block_depth = 1
            i += 2
            continue
        raw = re.match(r'r(#*)(")', text[i:])
        if raw:
            hashes, quote = raw.group(1), raw.group(2)
            start = i
            content_start = i + len(raw.group(0))
            end_marker = quote + hashes
            end = text.find(end_marker, content_start)
            if end < 0:
                break
            result.append((text[content_start:end], start, "raw"))
            i = end + len(end_marker)
            continue
        if text[i] == '"':
            start = i
            i += 1
            chars: list[str] = []
            while i < n:
                char = text[i]
                if char == "\\" and i + 1 < n:
                    esc = text[i + 1]
                    mapping = {"n": "\n", "r": "\r", "t": "\t", '"': '"', "\\": "\\"}
                    chars.append(mapping.get(esc, esc))
                    i += 2
                elif char == '"':
                    i += 1
                    break
                else:
                    chars.append(char)
                    i += 1
            result.append(("".join(chars), start, "normal"))
            continue
        if text[i] == "'":
            i += 1
            while i < n:
                if text[i] == "\\":
                    i += 2
                elif text[i] == "'":
                    i += 1
                    break
                else:
                    i += 1
            continue
        i += 1
    return result


def strip_cfg_test_modules(text: str) -> str:
    pattern = re.compile(r"#\[cfg\(test\)\]\s*mod\s+[A-Za-z0-9_]+\s*\{")
    while True:
        match = pattern.search(text)
        if not match:
            return text
        brace = text.find("{", match.start())
        depth = 0
        in_string = False
        escaped = False
        end = len(text)
        for i in range(brace, len(text)):
            char = text[i]
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
                    end = i + 1
                    break
        text = text[:match.start()] + "\n" * text[match.start():end].count("\n") + text[end:]


def natural_rust_candidate(value: str) -> bool:
    text = value.strip()
    if not text:
        return False
    if re.search(r"[\u3400-\u9fff\uac00-\ud7af]", text):
        return True
    if not re.search(r"[A-Za-z]", text) or len(text) < 3:
        return False
    if re.match(r"^(?:https?://|/|[A-Za-z]:\\|[a-z][a-z0-9+.-]*:)", text):
        return False
    return bool(re.search(r"\s", text) and re.search(r"[.!?:…]$|^[A-Z]", text))


def nearest_function(text: str, offset: int) -> str:
    prefix = text[:offset]
    matches = list(re.finditer(r"\b(?:pub\s+)?(?:async\s+)?fn\s+([A-Za-z_][A-Za-z0-9_]*)", prefix))
    return matches[-1].group(1) if matches else "<module>"



def split_rust_args(fragment: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    depth = 0
    string = False
    escaped = False
    i = 0
    while i < len(fragment):
        char = fragment[i]
        if string:
            current.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                string = False
        else:
            if char == '"':
                string = True
                current.append(char)
            elif char in "([{":
                depth += 1
                current.append(char)
            elif char in ")]}":
                depth -= 1
                current.append(char)
            elif char == "," and depth == 0:
                args.append("".join(current).strip())
                current = []
            else:
                current.append(char)
        i += 1
    if current:
        args.append("".join(current).strip())
    return args


def rust_literal(argument: str) -> str | None:
    match = re.fullmatch(r'"((?:\\.|[^"\\])*)"', argument.strip(), re.DOTALL)
    if not match:
        return None
    return match.group(1).replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\\\", "\\")


def extract_backend_localized_candidates(rel: str) -> list[dict[str, Any]]:
    path = ROOT / rel
    text = strip_cfg_test_modules(path.read_text(encoding="utf-8"))
    candidates: list[dict[str, Any]] = []
    for match in re.finditer(r"(?:AppError::)?localized\s*\(", text):
        open_at = text.find("(", match.start())
        depth = 0
        string = False
        escaped = False
        close_at = None
        for i in range(open_at, len(text)):
            char = text[i]
            if string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    string = False
                continue
            if char == '"':
                string = True
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    close_at = i
                    break
        if close_at is None:
            continue
        args = split_rust_args(text[open_at + 1:close_at])
        if len(args) < 3:
            continue
        key = rust_literal(args[0])
        if not key:
            continue
        zh = rust_literal(args[1])
        en = rust_literal(args[2])
        line = text.count("\n", 0, match.start()) + 1
        function = nearest_function(text, match.start())
        digest = sha(f"{key}\0{zh or ''}\0{en or ''}")[:16]
        candidates.append({
            "id": f"backend-localized:{rel}:{function}:{digest}:001",
            "source_file": rel, "line": line,
            "column": match.start() - text.rfind("\n", 0, match.start()),
            "expression": key,
            "raw_expression": text[match.start():close_at + 1][:1000],
            "content_fingerprint": sha(f"{key}\0{zh or ''}\0{en or ''}"),
            "source_kind": "backend_localized_error",
            "ui_attribute": None, "function": function, "property_chain": [],
            "parent_kind": "AppError::localized", "status": "未审核",
            "translation_payload": {"zh": zh, "en": en, "ko": None},
        })
    return candidates

def scan_rust(rel: str, source_files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    path = ROOT / rel
    text = strip_cfg_test_modules(path.read_text(encoding="utf-8"))
    candidates: list[dict[str, Any]] = []
    for value, offset, flavor in rust_strings(text):
        line = text.count("\n", 0, offset) + 1
        lines = text.splitlines()
        context = "\n".join(lines[max(0, line - 5):min(len(lines), line)])
        if re.search(r"log::(?:trace|debug|info|warn|error)!|println!|eprintln!|dbg!|assert(?:!|_eq!|_ne!)", context):
            continue
        returned_error = bool(re.search(r"return\s+Err|Err\(|map_err|bail!|anyhow!|ensure!|write!\(|write_str\(", context))
        if not returned_error:
            continue
        if not (natural_rust_candidate(value) or (len(value.strip()) >= 3 and re.search(r"[A-Za-z\u3400-\u9fff\uac00-\ud7af]", value))):
            continue
        if re.search(r"^(?:SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|pragma|#[!])", value, re.IGNORECASE):
            continue
        trimmed = value.strip()
        digest = sha(value)[:16]
        function = nearest_function(text, offset)
        candidates.append({
            "id": f"hardcoded:{rel}:{function}:{line}:{digest}",
            "source_file": rel,
            "line": line,
            "column": max(1, offset - text.rfind("\n", 0, offset)),
            "expression": trimmed,
            "raw_expression": value,
            "content_fingerprint": sha(value),
            "source_kind": "rust_string",
            "ui_attribute": None,
            "function": function,
            "property_chain": [],
            "parent_kind": context[:500],
            "status": "未审核",
        })
    source_files.append({
        "path": rel, "language": "rust", "status": "scanned", "bytes": path.stat().st_size,
        "candidate_count": len(candidates), "parse_errors": [],
    })
    return candidates


class VisibleHTMLParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.candidates: list[tuple[str, int, str, str | None]] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style"}:
            self.skip_depth += 1
        line = self.getpos()[0]
        for name, value in attrs:
            if value and name.lower() in {"placeholder", "title", "aria-label", "aria-description", "alt", "content"}:
                self.candidates.append((value, line, "html_attribute", name))

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and data.strip():
            self.candidates.append((data, self.getpos()[0], "html_text", None))


def scan_html(rel: str, source_files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    parser = VisibleHTMLParser()
    parser.feed(text)
    candidates: list[dict[str, Any]] = []
    for value, line, kind, attr in parser.candidates:
        trimmed = value.strip()
        if not re.search(r"[\u3400-\u9fff\uac00-\ud7afA-Za-z]", trimmed):
            continue
        if len(trimmed) < 2:
            continue
        digest = sha(value)[:16]
        candidates.append({
            "id": f"hardcoded:{rel}:html:{line}:{digest}",
            "source_file": rel, "line": line, "column": 1,
            "expression": trimmed, "raw_expression": value,
            "content_fingerprint": sha(value), "source_kind": kind,
            "ui_attribute": attr, "function": "<html>", "property_chain": [],
            "parent_kind": f"<{kind}>", "status": "未审核",
        })
    source_files.append({
        "path": rel, "language": "html", "status": "scanned", "bytes": path.stat().st_size,
        "candidate_count": len(candidates), "parse_errors": [],
    })
    return candidates


def main() -> int:
    included, excluded = enumerate_sources()
    ts_files = [rel for rel in included if Path(rel).suffix.lower() in {".ts", ".tsx", ".js", ".jsx"}]
    ts_input = OUT / "manifest/ts_source_files.json"
    ts_output = OUT / "manifest/ts_scan_raw.json"
    atomic_json(ts_input, ts_files)
    result = subprocess.run(
        ["node", str(OUT / "scripts/scan_ts.mjs"), str(ts_input), str(ts_output)],
        cwd=ROOT, text=True, capture_output=True,
    )
    if result.returncode != 0:
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return result.returncode
    ts_payload = json.loads(ts_output.read_text(encoding="utf-8"))
    source_files = list(ts_payload["sourceFiles"])
    candidates = list(ts_payload["candidates"])
    for rel in included:
        suffix = Path(rel).suffix.lower()
        if suffix == ".rs":
            if rel in {"src-tauri/src/tray.rs", "src-tauri/src/tray_panel.rs", "src-tauri/src/commands/config.rs"}:
                source_files.append({"path": rel, "language": "rust", "status": "scanned", "bytes": (ROOT / rel).stat().st_size, "candidate_count": 0, "parse_errors": [], "note": "handled as an existing translated resource by extract.py"})
                continue
            candidates.extend(scan_rust(rel, source_files))
            if rel != "src-tauri/src/error.rs":
                candidates.extend(extract_backend_localized_candidates(rel))
        elif suffix == ".html":
            candidates.extend(scan_html(rel, source_files))

    # Stable de-duplication only for exact same location/content; identical text at different UI sites remains separate.
    deduped: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        deduped[candidate["id"]] = candidate
    candidates = sorted(deduped.values(), key=lambda item: (item["source_file"], item["line"], item["column"], item["expression"]))

    # Stable identity excludes line numbers. Re-number only duplicate content in the same structural scope.
    occurrences: dict[tuple[str, str, str], int] = {}
    for candidate in candidates:
        scope_key = (candidate["source_file"], candidate["function"], candidate["content_fingerprint"])
        occurrences[scope_key] = occurrences.get(scope_key, 0) + 1
        candidate["id"] = (
            f"hardcoded:{candidate['source_file']}:{candidate['function']}:"
            f"{candidate['content_fingerprint'][:16]}:{occurrences[scope_key]:03d}"
        )

    dynamic_occurrences: dict[tuple[str, str, str], int] = {}
    for index, ref in enumerate(ts_payload["dynamicTranslationRefs"], 1):
        digest = sha(ref["expression"])[:16]
        scope_key = (ref["source_file"], ref["function"], digest)
        dynamic_occurrences[scope_key] = dynamic_occurrences.get(scope_key, 0) + 1
        candidates.append({
            "id": f"dynamic-i18n:{ref['source_file']}:{ref['function']}:{digest}:{dynamic_occurrences[scope_key]:03d}",
            "source_file": ref["source_file"], "line": ref["line"], "column": ref["column"],
            "expression": ref["expression"], "raw_expression": ref["expression"],
            "content_fingerprint": sha(ref["expression"]), "source_kind": "dynamic_i18n_key",
            "ui_attribute": None, "function": ref["function"], "property_chain": [],
            "parent_kind": "translation-call", "status": "未审核",
            "dynamic_reason": ref["reason"],
        })

    resources = json.loads((OUT / "manifest/resources.json").read_text(encoding="utf-8"))
    resource_keys = {record["key"] for record in resources["records"] if record["source_kind"] == "json-locale"}
    missing_keys = []
    for ref in ts_payload["translationRefs"]:
        if ref["key"] not in resource_keys:
            missing_keys.append({**ref, "problem": "static translation key is absent from locale resources"})

    manifest = {
        "schema_version": 1,
        "generated_by": ".i18n-audit/scripts/scan_hardcoded.py",
        "scope": CONFIG["production_scope"],
        "scope_exclusions": CONFIG.get("scope_exclusions", []),
        "source_file_count": len(included) + len(excluded),
        "included_source_file_count": len(included),
        "excluded_source_file_count": len(excluded),
        "scanned_source_file_count": sum(1 for item in source_files if item.get("status") == "scanned"),
        "failed_source_file_count": sum(1 for item in source_files if item.get("status") == "failed"),
        "excluded_files": excluded,
        "source_files": sorted(source_files, key=lambda item: item["path"]),
        "candidate_count": len(candidates),
        "candidates": candidates,
        "translation_refs": ts_payload["translationRefs"],
        "dynamic_translation_refs": ts_payload["dynamicTranslationRefs"],
        "missing_translation_keys": missing_keys,
        "scan_command": "node .i18n-audit/scripts/scan_ts.mjs + Python Rust/HTML scanner",
    }
    atomic_json(OUT / "manifest/source_files.json", {
        "schema_version": 1, "included": included, "excluded": excluded, "source_files": manifest["source_files"],
    })
    atomic_json(OUT / "manifest/hardcoded_candidates.json", manifest)
    print(json.dumps({
        "source_files": len(included), "excluded": len(excluded), "scanned": manifest["scanned_source_file_count"],
        "failed": manifest["failed_source_file_count"], "candidates": len(candidates),
        "translation_refs": len(ts_payload["translationRefs"]),
        "dynamic_translation_refs": len(ts_payload["dynamicTranslationRefs"]),
        "missing_translation_keys": len(missing_keys),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
