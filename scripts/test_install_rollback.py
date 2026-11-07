#!/usr/bin/env python3
"""Safe filesystem simulation of REDmod install/uninstall (never targets a real game)."""
from __future__ import annotations
import argparse, hashlib, json, pathlib, shutil, zipfile

RECEIPT = ".goldcoast-install-receipt.json"

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def install(package: pathlib.Path, sandbox: pathlib.Path) -> pathlib.Path:
    sandbox = sandbox.resolve()
    if sandbox == pathlib.Path(sandbox.anchor) or sandbox.exists() and not sandbox.is_dir():
        raise ValueError("sandbox must be a non-root directory")
    sandbox.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(package) as zf:
        result = zf.testzip()
        if result: raise ValueError(f"corrupt ZIP member: {result}")
        names = zf.namelist()
        if not names or any(n.startswith("/") or ".." in pathlib.PurePosixPath(n).parts for n in names):
            raise ValueError("unsafe package paths")
        roots = {pathlib.PurePosixPath(n).parts[0] for n in names}
        if len(roots)!=1: raise ValueError("expected exactly one mod folder")
        mod=next(iter(roots))
        if f"{mod}/info.json" not in names: raise ValueError("missing info.json")
        manifest=json.loads(zf.read(f"{mod}/info.json"))
        if manifest.get("name")!=mod: raise ValueError("manifest/root mismatch")
        dest=sandbox/"mods"/mod
        if dest.exists(): raise FileExistsError(f"refusing to overwrite existing sandbox mod: {dest}")
        dest.mkdir(parents=True)
        installed=[]
        try:
            for name in names:
                rel=pathlib.PurePosixPath(name)
                if len(rel.parts)<2 or rel.parts[0]!=mod: raise ValueError("unexpected package path")
                target=dest.joinpath(*rel.parts[1:])
                if target.exists(): raise FileExistsError(target)
                target.parent.mkdir(parents=True,exist_ok=True)
                data=zf.read(name); target.write_bytes(data)
                installed.append({"path":target.relative_to(sandbox).as_posix(),"sha256":sha(data)})
            receipt={"mod":mod,"files":installed,"package_sha256":sha(package.read_bytes())}
            (dest/RECEIPT).write_text(json.dumps(receipt,indent=2),encoding="utf-8")
            return dest
        except Exception:
            shutil.rmtree(dest,ignore_errors=True)
            raise

def uninstall(sandbox: pathlib.Path, mod: str) -> int:
    sandbox=sandbox.resolve(); dest=sandbox/"mods"/mod
    receipt_path=dest/RECEIPT
    if not receipt_path.is_file(): raise ValueError("no install receipt; refusing removal")
    receipt=json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("mod")!=mod: raise ValueError("receipt mod mismatch")
    for item in receipt["files"]:
        p=(sandbox/item["path"]).resolve()
        if sandbox not in p.parents: raise ValueError("receipt path escapes sandbox")
        if not p.is_file() or sha(p.read_bytes())!=item["sha256"]:
            raise ValueError(f"owned file changed/missing; refusing destructive cleanup: {p}")
    # Remove only recorded files plus our receipt; preserve all other content.
    for item in receipt["files"]: (sandbox/item["path"]).unlink()
    receipt_path.unlink()
    for p in sorted(dest.rglob("*"),reverse=True):
        if p.is_dir() and not any(p.iterdir()): p.rmdir()
    if dest.exists() and not any(dest.iterdir()): dest.rmdir()
    return len(receipt["files"])

def main():
    ap=argparse.ArgumentParser(description=__doc__); sub=ap.add_subparsers(dest="cmd",required=True)
    i=sub.add_parser("install"); i.add_argument("--package",type=pathlib.Path,required=True); i.add_argument("--sandbox",type=pathlib.Path,required=True)
    u=sub.add_parser("uninstall"); u.add_argument("--sandbox",type=pathlib.Path,required=True); u.add_argument("--mod",required=True)
    a=ap.parse_args()
    if a.cmd=="install": print("SANDBOX INSTALL OK:",install(a.package,a.sandbox))
    else: print("SANDBOX UNINSTALL OK: files removed =",uninstall(a.sandbox,a.mod))
if __name__=="__main__": main()
