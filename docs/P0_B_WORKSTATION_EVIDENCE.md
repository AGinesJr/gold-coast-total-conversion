# P0-B Workstation Evidence — 2026-11-06

## Owner-reported environment
- OS: Windows 11 Home, build 26300
- Hardware: Intel i7, 40 GB RAM, NVIDIA RTX 3070 Laptop GPU (8 GB VRAM)
- Python 3.13.5; Node 22.17.0; .NET SDK 10.0.401
- WolvenKit 10.0.0-beta.1; Blender 4.4.1
- Game distribution: GOG Galaxy
- Game root: `G:\Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077`

## Runtime evidence (RED4ext log dated 2026-11-02)
- Product version: Cyberpunk 2077 2.50
- Executable file version: 3.0.88.46235
- RED4ext 1.31.0 initialized successfully; log reports 16 plugins loaded.
- Loaded framework versions: TweakXL 1.12.0; Codeware 1.21.2; AudioXL 0.9.1; ArchiveXL 1.28.6.
- Additional loaded plugins: Mod Settings 0.2.28, Input Loader 0.2.6, PhotoModeEx 1.5.0, ACU 4.1.1, RedCetWM 2.1.2, Immersive First Person 0.3.0, audioware 1.10.1-rc.0, FXBegoneNative 2.2.1, NotSoGoodDrawDistance 1.1.0, WindowUtilsNative 1.0.0, AppearanceRuntimePlugin 1.7.1, Tag Marker Atlas Fix 1.0.0.
- CET is installed; exact CET version not yet captured.
- redscript/cache exists; exact redscript release not yet captured.

## Known compatibility warnings in the captured runtime
RED4ext reports LizziesBDs 3.21.0, RedFunctions 0.14.2, and RedRCFInput 0.3.0 as incompatible with the current runtime (they request 3.0.80.51928). Script validation then reports missing native classes from RedFunctions and RedRCFInput. These are existing mod conflicts—not Gold Coast failures—and should be isolated/disabled in a staging profile before runtime proof.

## Vortex
- Vortex staging folder: `G:\Vortex Mods\cyberpunk2077`
- Game path matches the GOG root above.
- Vortex log confirms staging/deployment checks; RED4ext mod install was canceled in the captured session.
- Vortex docs recommend staging on the same drive as the game and not inside the game install. Source: [CDPR Modding Docs — Vortex](https://github.com/CDPR-Modding-Documentation/Cyberpunk-Modding-Docs/blob/main/for-mod-users/users-modding-cyberpunk-2077/getting-started/vortex-mod-manager.md).

## Compatibility interpretation
The observed core versions align with community documentation for patch 2.5: RED4ext 1.31.0, ArchiveXL 1.28.x, TweakXL 1.12.x, Codeware 1.21.x, redscript 0.5.32. This is framework release evidence, not certification that every installed gameplay mod is compatible. See [2.5 compatibility release notes](https://cyberpunkmods.com/cyberpunk-2-5-mod-compatibility) and [framework matrix](https://2077mods.com/compatibility).

## Phase 0 status
- P0-A pipeline foundation: merged in PR #9.
- P0-C metadata-only asset intelligence: merged in PR #11.
- P0-B: runtime and core framework versions substantially verified; CET/redscript exact versions and DLC inventory remain outstanding.
- P0-D/E/F: not yet proven. No game files were modified for this evidence capture.
- Safety boundary: do not deploy proof files into the normal game root. Build/package in CI first; runtime testing requires a clearly isolated staging profile/environment and owner approval.

## Next evidence items
1. Capture CET version from its log.
2. Confirm redscript release/version from its install metadata or compile log.
3. Verify installed DLC list (Ultimate Edition claim).
4. Create a package-only CI proof, then plan reversible staging install/uninstall.
