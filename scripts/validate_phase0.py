#!/usr/bin/env python3
"""Validate Gold Coast Phase 0 task contracts and metadata-only asset records."""
from __future__ import annotations
import argparse, json, pathlib, sys
import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load_yaml(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)

def validate_json_schema(instance, schema_path: pathlib.Path, label: str):
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        details = "; ".join(f"{label}: {'/'.join(map(str,e.path)) or '<root>'}: {e.message}" for e in errors)
        raise ValueError(details)

def validate_task(path: pathlib.Path):
    task = load_yaml(path)
    validate_json_schema(task, ROOT / "schemas/agent-task.schema.json", str(path))
    if not task.get("allowed_paths") or not task.get("forbidden_actions"):
        raise ValueError(f"{path}: allow/deny lists must be non-empty")
    if "push_to_main" not in task["forbidden_actions"]:
        raise ValueError(f"{path}: push_to_main must be forbidden")
    return task["task_id"]

def validate_asset_record(path: pathlib.Path):
    record = load_yaml(path)
    validate_json_schema(record, ROOT / "schemas/asset-catalog-record.schema.json", str(path))
    if record["source"] == "base_game_reference" and record["license_status"] != "base_game_no_redistribution":
        raise ValueError(f"{path}: base-game references must prohibit redistribution")
    return record["asset_id"]

def validate_toolchain(path: pathlib.Path):
    lock = load_yaml(path)
    required = {"schema_version","last_reviewed","lock_status","game","tools","automation","policy"}
    missing = required - set(lock or {})
    if missing:
        raise ValueError(f"{path}: missing top-level keys: {sorted(missing)}")
    for name, entry in lock["tools"].items():
        if entry.get("status") not in {"verified","verified_loaded","installed","detected","active","candidate","unknown","blocked","experimental","planned"}:
            raise ValueError(f"{path}: {name} has invalid status {entry.get('status')!r}")
        if entry.get("status") == "verified" and not entry.get("evidence"):
            raise ValueError(f"{path}: verified tool {name} must include evidence")
    if lock["game"].get("executable_version") == "unknown" and lock["lock_status"] == "locked":
        raise ValueError(f"{path}: cannot lock unknown game executable version")
    return len(lock["tools"])

def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",default=str(ROOT))
    args=parser.parse_args(argv)
    root=pathlib.Path(args.root)
    failures=[]; counts={"tasks":0,"asset_records":0,"tools":0}
    for path in sorted((root/"agent/tasks").glob("*.yaml")):
        try: validate_task(path); counts["tasks"]+=1
        except Exception as exc: failures.append(str(exc))
    for path in sorted((root/"catalogs/samples").glob("*.yaml")):
        try: validate_asset_record(path); counts["asset_records"]+=1
        except Exception as exc: failures.append(str(exc))
    try: counts["tools"]=validate_toolchain(root/"config/toolchain.lock.yaml")
    except Exception as exc: failures.append(str(exc))
    if failures:
        print("PHASE0 VALIDATION FAILED")
        for error in failures: print(f"- {error}")
        return 1
    print("PHASE0 VALIDATION PASSED")
    print(f"Task contracts: {counts['tasks']} | asset sample records: {counts['asset_records']} | tool entries: {counts['tools']}")
    print("Evidence note: this validates repository metadata only; it is not a game/runtime test.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
