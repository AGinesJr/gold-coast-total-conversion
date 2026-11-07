# P0-D Install/Uninstall Rollback Harness (filesystem simulation)

This harness installs the metadata-only proof ZIP into a caller-provided **sandbox directory**, not a Cyberpunk game directory. It refuses overwrites, records SHA-256 ownership receipts, and uninstalls only unchanged files it created. Unknown files are preserved.

Run:
```powershell
python scripts/package_redmod.py build --source tests/fixtures/redmod_stub/GoldCoastPrototype --output build/GoldCoastPrototype.zip
python scripts/test_install_rollback.py install --package build/GoldCoastPrototype.zip --sandbox "$env:TEMP\GC-P0D-Sandbox"
python scripts/test_install_rollback.py uninstall --sandbox "$env:TEMP\GC-P0D-Sandbox" --mod GoldCoastPrototype
```

**Boundary:** this is a filesystem lifecycle simulation. It is not REDmod deployment, game load, or runtime verification. Actual game install/removal proof remains blocked until an isolated copy/installation is available and explicitly authorized. Never pass the live game root as `--sandbox`.
