#!/usr/bin/env python3
"""
build_index.py — Build a machine-readable catalog for World Food Wiki (foods/ only)
"""

from __future__ import annotations
import re
import json
import argparse
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional, Set

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

FRONTMATTER_PATTERN = re.compile(r'^\s*---\s*\n(.*?)\n---\s*\n?', re.DOTALL | re.MULTILINE)
HEADING_PATTERN = re.compile(r'^(#+)\s+(.*)$', re.MULTILINE)

def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='ignore')

def extract_frontmatter(md_text: str):
    m = FRONTMATTER_PATTERN.match(md_text)
    if m:
        return m.group(1), md_text[m.end():]
    return None, md_text

def minimal_yaml_parse(fm_text: str) -> Dict[str, Any]:
    data = {}
    current_key = None
    for raw_line in fm_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith('- ') and current_key is not None:
            val = line.split('- ', 1)[1].strip()
            data.setdefault(current_key, [])
            if val.startswith(("'", '"')) and val.endswith(("'", '"')):
                val = val[1:-1]
            data[current_key].append(val)
            continue
        if ':' in line and not line.lstrip().startswith('- '):
            key, val = line.split(':', 1)
            key, val = key.strip(), val.strip()
            current_key = key
            if val == '':
                data[key] = []
            elif val.startswith('[') and val.endswith(']'):
                items = [x.strip().strip('\'"') for x in val[1:-1].split(',') if x.strip()]
                data[key] = items
            else:
                data[key] = val.strip('\'"')
    return data

def parse_frontmatter_text(fm_text: Optional[str]) -> Dict[str, Any]:
    if fm_text is None:
        return {}
    if HAVE_YAML:
        try:
            obj = yaml.safe_load(fm_text) or {}
            return obj if isinstance(obj, dict) else {}
        except Exception:
            return minimal_yaml_parse(fm_text)
    return minimal_yaml_parse(fm_text)

def normalize_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()]
    if isinstance(x, str):
        return [s.strip() for s in [x] if s.strip()]
    return [str(x).strip()]

def extract_headings(md_text: str) -> List[Dict[str, Any]]:
    heads = []
    for m in HEADING_PATTERN.finditer(md_text):
        level = len(m.group(1))
        text = m.group(2).strip()
        anchor = re.sub(r'[^a-zA-Z0-9\-_ ]', '', text).strip().lower().replace(' ', '-')
        heads.append({"level": level, "text": text, "anchor": anchor})
    return heads

def load_tags(tags_path: Path) -> Dict[str, Set[str]]:
    if not tags_path.exists():
        return {}
    content = read_text(tags_path)
    obj = yaml.safe_load(content) if HAVE_YAML else minimal_yaml_parse(content)
    result = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            result[str(k)] = set(normalize_list(v))
    return result

def validate_against_tags(fm: Dict[str, Any], tags: Dict[str, Set[str]]) -> List[str]:
    warnings = []
    mapping = {"regions": "regions", "periods": "periods", "techniques": "techniques", "categories": "categories"}
    for fm_key, tag_key in mapping.items():
        if tag_key in tags and fm_key in fm:
            values = set(normalize_list(fm.get(fm_key)))
            unknown = [v for v in values if v not in tags[tag_key]]
            if unknown:
                warnings.append(f"[{fm.get('title','(untitled)')}] Unknown {fm_key}: {unknown}")
    return warnings

def collect_item(md_path: Path, repo_root: Path, tags: Dict[str, Set[str]]):
    rel = md_path.relative_to(repo_root).as_posix()
    text = read_text(md_path)
    fm_text, body = extract_frontmatter(text)
    fm = parse_frontmatter_text(fm_text)
    item = {
        "title": fm.get("title") or md_path.stem,
        "regions": normalize_list(fm.get("regions")),
        "periods": normalize_list(fm.get("periods")),
        "techniques": normalize_list(fm.get("techniques")),
        "ingredients": normalize_list(fm.get("ingredients")),
        "path": rel,
        "word_count": len(re.findall(r'\w+', body)),
        "headings": extract_headings(body),
    }
    warns = validate_against_tags(fm, tags)
    return item, warns

def scan_foods(repo_root: Path) -> List[Path]:
    base = (repo_root / "foods").resolve()
    if not base.exists():
        return []
    return [f for f in base.glob("**/*.md") if f.name.lower() != "readme.md"]

def aggregate_count(items: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    ctr = {}
    for it in items:
        for val in it.get(key, []) or []:
            ctr[val] = ctr.get(val, 0) + 1
    return dict(sorted(ctr.items(), key=lambda kv: (-kv[1], kv[0])))

def build_catalog(repo_root: Path, tags_path: Optional[Path]):
    tags = load_tags(tags_path) if tags_path else {}
    files = scan_foods(repo_root)
    items, warnings = [], []
    for f in files:
        item, warns = collect_item(f, repo_root, tags)
        items.append(item)
        warnings.extend(warns)
    meta = {
        "items_count": len(items),
        "by_region": aggregate_count(items, "regions"),
        "by_period": aggregate_count(items, "periods"),
        "by_technique": aggregate_count(items, "techniques"),
    }
    return {"meta": meta, "items": items}, warnings

def main():
    parser = argparse.ArgumentParser(description="Build catalog.json from foods/")
    parser.add_argument("--root", type=str, default="../", help="Repository root")
    parser.add_argument("--tags", type=str, default="data/tags.yml", help="Path to tags.yml")
    parser.add_argument("--out", type=str, default="../data/catalog.json", help="Output JSON path")
    parser.add_argument("--fail-on-unknown-tags", action="store_true", help="Fail if unknown tags are found")
    parser.add_argument("--print-summary", action="store_true", help="Print summary to stdout")
    args = parser.parse_args()

    repo_root, tags_path = Path(args.root).resolve(), Path(args.tags).resolve()
    catalog, warnings = build_catalog(repo_root, tags_path)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.print_summary:
        print(json.dumps(catalog["meta"], ensure_ascii=False, indent=2))

    if args.fail_on_unknown_tags and warnings:
        for w in warnings:
            print("WARNING:", w)
        raise SystemExit(2)

if __name__ == "__main__":
    main()
