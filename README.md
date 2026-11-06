# Gold Coast Total Conversion

A production framework for a Cyberpunk 2077 Ultimate Edition (PC) total conversion set in a fictionalized South Florida / Gold Coast Corporate Republic.

> **Status:** pre-production and feasibility. This repository does not yet contain a playable total conversion. All engine/tool capabilities must be proven against the pinned game build.

## Start here

- [Phase 0 Execution Plan](docs/PHASE_0_EXECUTION_PLAN.md) — autonomous pipeline-first execution, staged proof spikes and acceptance gates.
- [Phase 0 Runner Threat Model](docs/PHASE_0_RUNNER_THREAT_MODEL.md) — proposed Windows runner security boundary and allowlist.
- [Toolchain Discovery Lock](config/toolchain.lock.yaml) — candidate/unknown versions; no version is treated as verified without evidence.
- [Agent Task Schema](schemas/agent-task.schema.json) and [sample task](agent/tasks/GC-P0-0001-pipeline-bootstrap.yaml) — bounded agent contracts.

- [Total Conversion Master Blueprint v1.0](docs/TOTAL_CONVERSION_MASTER_BLUEPRINT_V1_0.md) — product definition, base-game reuse, original development scope, campaign separation, world strategy, AI-first pipeline, vertical slice and release gates.
- [Base-Game Carryover Matrix](docs/BASE_GAME_CARRYOVER_MATRIX.md) — reusable gameplay, cyberware, weapons, vehicles, NPCs, environments, UI and new development requirements.
- [AI Studio Architecture](docs/AI_STUDIO_ARCHITECTURE.md) — agent roster, model routing, autonomy tiers, task contracts, cost controls and Windows Build Runner.
- [World Conversion Plan](docs/WORLD_CONVERSION_PLAN.md) — 12 provisional district labels, asset mapping hypotheses, world data model and West Palm City first slice.
- [Campaign and Gameplay Architecture](docs/CAMPAIGN_AND_GAMEPLAY_ARCHITECTURE.md) — Rook, ECHO-9, campaign state, quest lifecycle, v2.4 integration and ending requirements.
- [Asset Reuse and Provenance](docs/ASSET_REUSE_AND_PROVENANCE.md) — base-game reuse inventory, original asset needs and rights safeguards.
- [UI, Audio and Presentation Plan](docs/UI_AUDIO_CONVERSION_PLAN.md) — menu, map, journal, identity cleanup, radio, dialogue and VO.
- [Technical POC and Build Runner](docs/TECHNICAL_POC_AND_BUILD_RUNNER.md) — five proof spikes, toolchain locking and controlled Windows runtime validation.
- [QA and Release Plan](docs/QA_AND_RELEASE_PLAN.md) — test strategy, known v2.4 blockers and release criteria.
- [Production Backlog](docs/PRODUCTION_BACKLOG.md) — initial prioritized implementation tickets.
- [Risk Register](docs/RISK_REGISTER.md) — technical, AI, scope, save and licensing risks.

## Existing project documents

- [Original production blueprint](docs/MASTER_BLUEPRINT.md)
- [Canon ledger](docs/CANON.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [AI autonomous development](docs/AI_AUTONOMOUS_DEVELOPMENT.md)
- [Roadmap and gates](docs/ROADMAP.md)
- [Architecture decisions](docs/DECISIONS.md)
- [v2.4 campaign graph status](docs/v2.4/README.md)
- [Chat artifact export index](production/chat-export/README.md)

## Creative foundation

- Rook: protagonist with Corpo, Streetkid and Nomad lifepaths.
- ECHO-9: reconstructed personality associated with Elias Voss.
- Project ECHO: central corporate/identity mystery.
- Campaign frame: 2077–2085, provisional.
- Five corporate powers in scope: Arasaka, Militech, Kang Tao, Petrochem and Night Corp.
- Existing historical/political anchors: West Palm blackout, Palm Beach Atlantis, Protectorate governance, Treaty of Boca, Project ECHO exposure, Palm Beach Holocaust and Free Gold Coast Assembly.

The district and street-faction labels in the new blueprint are provisional working names pending reconciliation with the source lore. See the canon ledger and master blueprint for status conventions.

## Current v2.4 campaign status

The repository documents 41 quest chains, 1,574 nodes, 1,901 edges, 36 district/event pools, 108 placeholder VO slots and 313 scenario fixtures. Static QA reports 164 unreachable nodes. Edge execution, condition truth, choice execution, ending execution and in-game REDengine smoke tests are not run. The Python adapter is a test double, not a real engine integration. Do not describe the campaign as playable or engine-locked until the release gates pass.

## Production principles

1. Prove a West Palm City vertical slice before expanding.
2. AI-first, human-accountable: agents prepare bounded branches and PRs; humans approve canon, licensing, high-risk changes, merges and releases.
3. Use explicit task contracts, model/tool version records and acceptance evidence.
4. Keep canon versioned and distinguish source-established, provisional, proposed, TBD and locked.
5. Treat engine claims as hypotheses until verified in the installed game.
6. Keep proprietary base-game assets out of Git and release packages unless explicitly licensed.
7. Protect ordinary V saves and use an isolated Gold Coast test installation.
8. Never claim tests passed unless they were actually executed.

## Legal and distribution

Players must own Cyberpunk 2077. Do not redistribute the base game or proprietary extracted game files/assets. Distribute only original or properly licensed content and review CDPR EULA, fan-content rules, mod policies and hosting-platform terms before public release. Gold Coast is an unofficial fan modification and must not imply CDPR endorsement.
