#!/usr/bin/env python3
"""Build a searchable metadata-only index from Gold Coast YAML asset records.

This tool indexes catalog metadata, never game asset bytes. It does not extract,
copy, package, or redistribute Cyberpunk resources.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from datetime import datetime, timezone

import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "asset-catalog-record.schema.json"


def read_record(path: pathlib.Path) -> dict:
    with path.open("r", encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: list(e.path))
    if errors:
        message = "; ".join(f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in errors)
        raise ValueError(f"{path}: {message}")
    if value["source"] == "base_game_reference" and value["license_status"] != "base_game_no_redistribution":
        raise ValueError(f"{path}: base-game references must be marked no-redistribution")
    return value


def build_index(catalog_dir: pathlib.Path) -> dict:
    records = []
    seen = set()
    for path in sorted(catalog_dir.rglob("*.y*ml")):
        record = read_record(path)
        asset_id = record["asset_id"]
        if asset_id in seen:
            raise ValueError(f"duplicate asset_id: {asset_id}")
        seen.add(asset_id)
        # Store catalog metadata and its repo-relative record location only.
        records.append({
            "asset_id": asset_id,
            "kind": record["kind"],
            "game_version": record["game_version"],
            "source": record["source"],
            "source_uri": record["source_uri"],
            "provenance": record["provenance"],
            "license_status": record["license_status"],
            "license_reference": record.get("license_reference", ""),
            "reuse_decision": record["reuse_decision"],
            "verification": record["verification"],
            "notes": record.get("notes", ""),
            "record_path": path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.name,
        })
    return {
        "index_schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalog_root": catalog_dir.relative_to(ROOT).as_posix() if catalog_dir.is_relative_to(ROOT) else str(catalog_dir),
        "record_count": len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=pathlib.Path, default=ROOT / "catalogs")
    parser.add_argument("--out", type=pathlib.Path, default=ROOT / "catalogs" / "asset-index.json")
    args = parser.parse_args()
    try:
        index = build_index(args.catalog)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Indexed {index['record_count']} metadata records -> {args.out}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"asset index failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
