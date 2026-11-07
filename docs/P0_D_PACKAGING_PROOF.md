# P0-D — REDmod Packaging Proof

## Purpose
Prove a repeatable repository-side package build and integrity-validation workflow before any deployment to Cyberpunk 2077.

## Scope (this PR)
- Build a deterministic ZIP with the REDmod one-folder layout: `<ModName>/info.json` plus content folders.
- Validate ZIP integrity, safe paths, a single top-level mod folder, and manifest/folder-name agreement.
- Emit a SHA-256 sidecar.
- Exercise the workflow with a metadata-only fixture containing no game assets or executable mod logic.
- Run packaging tests in GitHub Actions.

## Explicit non-claims
This is **not** a WolvenKit resource archive build, REDmod precompile/deploy, game launch, runtime load, uninstall, save compatibility, or playable-content proof. The fixture has no `.archive`, `.reds`, `.lua`, or TweakDB payload. Installation/removal remains P0-D follow-on work requiring an isolated staging game and owner authorization.

## Run locally (Python 3.12+)
```powershell
python scripts/package_redmod.py build --source tests/fixtures/redmod_stub/GoldCoastPrototype --output build/GoldCoastPrototype.zip
python scripts/package_redmod.py validate --package build/GoldCoastPrototype.zip
python -m unittest tests.test_redmod_packaging -v
```

## Acceptance
- Build produces ZIP and `.sha256` sidecar.
- ZIP passes CRC and path checks.
- Exactly one top-level directory is present.
- `info.json` exists at package root and its `name` matches that directory.
- Negative tests reject malformed/missing manifests and folder mismatch.
- CI runs all Phase 0 and package tests.
- No proprietary game assets are committed or packaged.

## References
- [CDPR REDmod creator documentation](https://github.com/CDPR-Modding-Documentation/Cyberpunk-Modding-Docs/blob/main/for-mod-creators-theory/modding-tools/redmod/README.md)
- [CDPR REDmod support page](https://www.cyberpunk.net/en/modding-support)
