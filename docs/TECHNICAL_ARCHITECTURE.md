# Technical Architecture (candidate)

## Constraints
Cyberpunk 2077 Ultimate Edition is the baseline, but exact game build and mod API support must be version-pinned and proven. Do not treat tool names below as compatibility guarantees.

## Candidate ecosystem to evaluate
WolvenKit (asset/archive workflow), REDmod, RED4ext, ArchiveXL, TweakXL, redscript, Cyber Engine Tweaks, Codeware, World Builder. Select only tools with current compatibility evidence; record versions, dependencies, limitations, and license.

## Layering
- **Content source:** canon YAML/JSON, dialogue, quest graph, location manifests, encounter configs.
- **Validation:** schema/ID/reference/graph/condition checks, localization checks, provenance checks.
- **Build:** deterministic transforms, asset conversion, archive/package assembly, manifest generation.
- **Runtime:** scripts and extensions only where supported; adapters isolate mod API specifics.
- **QA:** game launch/install checks, quest scenarios, save/load, performance and logs.

## Proposed repository
`docs/`, `canon/`, `narrative/`, `world/`, `gameplay/`, `assets/manifests/`, `tools/`, `tests/`, `releases/`.

## Feasibility spikes
1. Reproducible environment + game/tool version inventory.
2. One original asset and material through import/package/install.
3. One world cell/streaming boundary and collision/navigation test.
4. One quest-state transition, save/load, and retry behavior.
5. Runtime event dispatch with deterministic fallback.
6. Clean install/uninstall and rollback.

## Build discipline
Pin versions; use manifests and checksums; separate source from generated output; no proprietary game assets in Git; clean build must be reproducible. Keep mod-specific adapters behind interfaces so tool replacement does not rewrite narrative source.
