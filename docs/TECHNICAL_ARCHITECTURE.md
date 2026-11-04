# Technical Architecture (candidate)

## Constraints

Cyberpunk 2077 Ultimate Edition is the baseline, but exact game build and mod API support must be version-pinned and proven. Do not treat tool names below as compatibility guarantees.

## Candidate ecosystem to evaluate

WolvenKit (asset/archive workflow), REDmod, RED4ext, ArchiveXL, TweakXL, redscript, Cyber Engine Tweaks, Codeware, World Builder and RedHotTools. Select only tools with current compatibility evidence; record versions, dependencies, limitations and license.

## Layering

- **Content source:** canon YAML/JSON, dialogue, quest graph, location manifests, encounter configs.
- **Validation:** schema/ID/reference/graph/condition checks, localization checks, provenance checks.
- **Build:** deterministic transforms, asset conversion, archive/package assembly, manifest generation.
- **Runtime:** scripts and extensions only where supported; adapters isolate mod API specifics.
- **QA:** game launch/install checks, quest scenarios, save/load, performance and logs.
- **AI orchestration:** task contracts, isolated branches, model routing, context retrieval, review and telemetry.
- **Windows Build Runner:** controlled local game build/runtime testing from a specific Git commit.

## Repository

See the [Total Conversion Master Blueprint](TOTAL_CONVERSION_MASTER_BLUEPRINT_V1_0.md), [Technical POC and Build Runner](TECHNICAL_POC_AND_BUILD_RUNNER.md), and [AI Studio Architecture](AI_STUDIO_ARCHITECTURE.md).

## Mandatory feasibility spikes

1. Reproducible environment and game/tool version inventory.
2. One original asset and material through import/package/install.
3. One world cell/streaming boundary and collision/navigation test.
4. Gold Coast campaign bootstrap independent of V's campaign.
5. One quest-state transition, save/load, retry behavior and actual in-game test.
6. Runtime event dispatch with deterministic fallback.
7. Clean install/uninstall and rollback.
8. AI agent-to-PR-to-Windows-build evidence loop.

## Build discipline

Pin versions; use manifests and checksums; separate source from generated output; no proprietary game assets in Git; clean build must be reproducible. Keep mod-specific adapters behind interfaces so tool replacement does not rewrite narrative source. Use an isolated test game and never let agents modify the user's normal game installation.
