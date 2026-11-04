# Roadmap & Gates

The detailed execution tickets are maintained in [Production Backlog](PRODUCTION_BACKLOG.md). The full product and scope definition is in [Total Conversion Master Blueprint](TOTAL_CONVERSION_MASTER_BLUEPRINT_V1_0.md).

## Phase 0 — Research and technical discovery

- Confirm source canon and establish approved ledger.
- Pin current game/tool versions; evaluate licensing/distribution rules.
- Prove asset packaging, world-cell/streaming, campaign bootstrap, quest state, save/load and build rollback.
- Establish AI task orchestration and controlled Windows Build Runner.
- Define regional map scale and hardware/performance budgets.

**Exit:** documented go/no-go with reproducible asset, world, campaign, quest and autonomous-build proofs.

## Phase 1 — Gold Coast foundation

- Canon database and stable IDs.
- Campaign namespace and Rook/ECHO-9 data model.
- Gold Coast startup and lifepath prototype.
- District/location manifests.
- AI agent contracts and validation.

**Exit:** Gold Coast initializes independently of V's original story in an isolated test profile.

## Phase 2 — World vertical slice

- One West Palm City playable block.
- Landmark/interior, traversal loop, NPC population and faction presence.
- One combat and one noncombat path.
- One main quest with consequential branch, fail/retry and save/load.
- Install package and automated tests.

**Exit:** repeatable build; no critical crash/softlock; mission state survives save/load; performance/provenance evidence captured.

## Phase 3 — Reusable gameplay and campaign systems

- Quest schema/graph runner and lifecycle.
- Ambient/combat/reactive event dispatch.
- Faction reputation and regional state.
- Companion/lifepath state.
- Economy, contracts and investigations.
- Save migration and ending-state manager.
- v2.4 graph remediation and runtime adapter.

**Exit:** functioning original RPG campaign framework and verified scenario coverage.

## Phase 4 — Regional expansion

- Expand districts only after the first district gate passes.
- Add corporate headquarters, gang territories, interiors and landmarks.
- Add NPC schedules, regional events and encounters.
- Validate streaming, navigation, collision and performance per district.

**Exit:** all planned regions represented, accessible and tested.

## Phase 5 — Campaign production

- Main campaign and lifepath branches.
- Side quests, fixer contracts and investigations.
- Companion stories and approved relationship content.
- Corporate/faction arcs.
- Seven endings and post-campaign outcomes.
- Final dialogue, VO, localization and audio.

**Exit:** campaign, side content and endings completable with documented branch coverage.

## Phase 6 — Total conversion presentation

- New Game/menu presentation.
- Map, journal, contacts, loading screens and Gold Coast branding.
- Original radio identity and audio.
- Remove or suppress conflicting original-campaign presentation where safely possible.

**Exit:** coherent Gold Coast experience with unavoidable base UI limitations documented.

## Phase 7 — QA and release

- Full quest regression and scenario matrix.
- Save/load and migration.
- Performance optimization.
- Compatibility, clean install, upgrade and uninstall.
- Asset provenance and licensing audit.
- Release packaging, checksums, known issues and human approval.

**Exit:** release candidate has zero open blockers/critical issues and all required evidence.

Never scale content before the preceding gate passes. Never claim engine-ready campaign lock without runtime evidence.
