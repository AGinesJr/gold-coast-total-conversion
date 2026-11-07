#!/usr/bin/env python3
"""Build and validate a deterministic, metadata-only REDmod ZIP scaffold."""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import re
import sys
import zipfile

ROOT_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")
MANIFEST_NAME = "info.json"

def read_manifest(source: pathlib.Path) -> dict:
    path = source / MANIFEST_NAME
    if not path.is_file():
        raise ValueError(f"missing {MANIFEST_NAME} at package root")
    data = json.loads(path.read_text(encoding="utf-8"))
    for field in ("name", "version", "author", "description"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"manifest field {field!r} must be a non-empty string")
    if not ROOT_NAME_RE.fullmatch(data["name"]):
        raise ValueError("manifest name must be a safe folder identifier")
    if not re.fullmatch(r"\d+\.\d+\.\d+", data["version"]):
        raise ValueError("manifest version must use MAJOR.MINOR.PATCH")
    return data

def collect_files(source: pathlib.Path) -> list[pathlib.Path]:
    if source.is_symlink() or not source.is_dir():
        raise ValueError("source must be a real directory (not a symlink)")
    files = []
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlinks are not allowed: {path.relative_to(source)}")
        if path.is_file():
            rel = path.relative_to(source)
            if rel.is_absolute() or ".." in rel.parts:
                raise ValueError(f"unsafe path: {rel}")
            files.append(path)
    if not files:
        raise ValueError("source package contains no files")
    return files

def build(source: pathlib.Path, output: pathlib.Path) -> tuple[str, int]:
    source = source.resolve()
    manifest = read_manifest(source)
    files = collect_files(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    root = manifest["name"]
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            rel = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(f"{root}/{rel}", date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes())
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(f"{digest}  {output.name}\n", encoding="ascii")
    validate(output)
    return digest, len(files)

def validate(package: pathlib.Path) -> dict:
    with zipfile.ZipFile(package, "r") as zf:
        bad = zf.testzip()
        if bad:
            raise ValueError(f"ZIP CRC failed for {bad}")
        names = zf.namelist()
        if not names or any(name.startswith("/") or ".." in pathlib.PurePosixPath(name).parts for name in names):
            raise ValueError("ZIP contains empty or unsafe paths")
        roots = {pathlib.PurePosixPath(name).parts[0] for name in names}
        if len(roots) != 1:
            raise ValueError(f"package must have exactly one top-level mod folder; found {sorted(roots)}")
        root = next(iter(roots))
        manifest_path = f"{root}/{MANIFEST_NAME}"
        if manifest_path not in names:
            raise ValueError(f"package missing {manifest_path}")
        manifest = json.loads(zf.read(manifest_path).decode("utf-8"))
        if manifest.get("name") != root:
            raise ValueError("manifest name does not match ZIP top-level folder")
        return {"root": root, "files": len(names), "version": manifest.get("version")}

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("--source", type=pathlib.Path, required=True)
    b.add_argument("--output", type=pathlib.Path, required=True)
    v = sub.add_parser("validate")
    v.add_argument("--package", type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            digest, count = build(args.source, args.output)
            print(f"PACKAGE BUILD PASSED | files={count} | sha256={digest} | output={args.output}")
        else:
            result = validate(args.package)
            print(f"PACKAGE VALIDATION PASSED | root={result['root']} | files={result['files']} | version={result['version']}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"PACKAGE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
