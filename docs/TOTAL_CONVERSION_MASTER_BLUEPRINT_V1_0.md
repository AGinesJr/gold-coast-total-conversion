# Gold Coast — Total Conversion Master Blueprint v1.0

**Date:** 2026-11-04  
**Target:** Cyberpunk 2077 Ultimate Edition (PC); exact executable/build to be pinned in Phase 0  
**Status:** Production specification and feasibility plan. This is not a claim of a playable total conversion.

## 1. Product definition

Gold Coast is a standalone-feeling total-conversion experience built on Cyberpunk 2077's existing REDengine 4 game, player, combat, vehicle, inventory, cyberware, AI, quest, dialogue, and presentation systems wherever reuse is technically and legally permitted. It replaces the player's primary identity, setting, campaign, regional presentation, factions, and progression experience with an original South Florida cyberpunk RPG.

Player promise: launch Gold Coast, begin a new campaign as Rook, choose Corpo / Streetkid / Nomad, explore the fictionalized Gold Coast region, confront competing corporate and street powers, uncover Project ECHO and ECHO-9, and determine the region's future through consequential decisions.

Gold Coast remains a mod requiring a legitimate Cyberpunk 2077 PC installation. It is not a standalone game or a redistribution of REDengine or proprietary base-game content.

## 2. Design principles

1. New player experience: Gold Coast is Rook's story, not V visiting Florida.
2. Original narrative identity: ECHO-9 / Elias Voss and Project ECHO replace the original campaign's central narrative role; Johnny Silverhand and V's Relic arc are not campaign dependencies.
3. Reuse the engine, replace the experience: reuse proven systems where possible; replace or re-author content that defines the setting and story.
4. Hybrid world strategy: transform and recompose existing environments, then add custom streaming sectors only where proven feasible.
5. Canon is governed: distinguish source-established facts, provisional working canon, and proposals. AI agents cannot silently promote proposals to canon.
6. AI-first, human-accountable: agents research, author, implement bounded tasks, validate, and prepare PRs; humans approve canon locks, licensing, high-risk architecture, merges, and releases.
7. Evidence over claims: implementation status requires build/test evidence. A generated specification or fixture is not runtime proof.
8. Modular, reproducible production: source data, scripts, assets, adapters, tests, and release packages remain separable and versioned.
9. Save safety: Gold Coast campaign state must be isolated and recoverable; never risk ordinary V saves.
10. Rights-aware distribution: do not commit or distribute extracted proprietary base-game assets unless a specific license permits it.

## 3. Canon baseline and status

The repository's existing canon ledger and v2.4 campaign artifacts remain authoritative starting references. The current planning conversation adds useful working labels but does not resolve every source-chat conflict.

Core anchors: Rook; Corpo / Streetkid / Nomad; ECHO-9 associated with Elias Voss; Project ECHO; corporate continuity/immortality versus human autonomy; 2077–2085 provisional campaign frame; Arasaka, Militech, Kang Tao, Petrochem and Night Corp; v2.4 companion identifiers Lux, Mara, Jackson and no-companion path; seven v2.4 ending names: Crown Eternal, Southern Occupation, Silicon Paradise, Zero Humanity, Free Gold Coast, Sawgrass Exodus, Atlantic Ghost.

Provisional district labels: The Crown, West Palm City, Silicon Coast, The Belt, The Arc, The Frontier, Sugarlands, Lake Corridor, Green Hell, Atlantis, The Abyss and Skyports. Street-faction working roster: Crown Boys, Iron Saints, Breakers, Velvets, Canal Rats, Sawgrass Nomads and Atlantic Ghosts. These labels, territories, leadership, chronology, alliances and story roles must be reconciled against earlier Gold Coast lore before being marked LOCKED.

Preserve existing historical/political anchors already recorded in the repository: West Palm blackout; Palm Beach Atlantis; Protectorate governance; Treaty of Boca; Project ECHO exposure; Palm Beach Holocaust; Free Gold Coast Assembly. Do not discard or reorder them without source reconciliation.

Canon status convention: SOURCE-ESTABLISHED, PROVISIONAL, PROPOSED, TBD, LOCKED. See docs/CANON.md.

## 4. Base-game carryover

Subject to exact game-version and mod-framework validation, investigate reuse of player movement/camera/interaction; firearms, melee, stealth, combat AI and damage; cyberware, cyberdecks, quickhacks, Sandevistan, Berserk and ripperdocs; weapons, attachments, consumables, crafting, inventory, loot and vendors; vehicles, driving, vehicle combat and summon/ownership; NPC archetypes, routines, security/police, robots, drones, turrets, animation and facial/scene systems; quest, journal, dialogue, phone and contact systems; character customization, clothing, photo mode, audio playback, save infrastructure and UI; building kits, interiors, roads, props, vegetation, industrial/corporate assets, lighting and environmental effects.

Reuse classes: A direct reuse; B rebrand/reconfigure; C reconstruct; D original development. Reusing an archetype does not provide a finished Gold Coast character, mission, faction or encounter. See docs/BASE_GAME_CARRYOVER_MATRIX.md and docs/ASSET_REUSE_AND_PROVENANCE.md.

## 5. New development scope

Gold Coast-specific work includes Rook's campaign identity and lifepaths; ECHO-9 and Project ECHO; original campaign, quests, objectives, failure/retry/replay, scenes, dialogue, consequences and endings; regional geography, landmarks, signage, roads, interiors, streaming sectors, navigation and NPC placements; corporate/street faction identities and relationships; companions and approved relationship content; regional economy, vendors, contracts, activities, encounters and world-state changes; Gold Coast menus, map, journal, loading screens, branding, radio, original audio and localization; installer, dependency checks, save migration and release documentation.

## 6. World conversion

Preferred strategy: hybrid conversion. Inventory Night City sectors and assets; select source areas by geometry, scale, road topology, environment type and streaming behavior; recompose/rebrand suitable environments; conceal/replace incompatible landmarks; add custom landmarks and streaming sectors only after proof of concept.

Renaming districts or replacing textures does not create a new map. A genuinely new region requires world geometry, streaming-sector registration, collision, navigation, roads, boundaries, spawn points, encounters, fast travel and performance validation.

West Palm City is the first world vertical slice. See docs/WORLD_CONVERSION_PLAN.md.

## 7. Campaign and gameplay

Use a Gold Coast campaign namespace and central state manager. Do not overwrite the original campaign wholesale as the first step. Required layers: bootstrap/new-campaign initialization; lifepath openings; prologue and main acts; main/side quests, fixer contracts, faction/companion stories, investigations, secrets and endings; objective lifecycle; ambient/combat/reactive dialogue dispatch; faction/region/world/companion state; ending variables; save/load validation and migration.

Every meaningful choice has a documented downstream consequence or is explicitly cosmetic. See docs/CAMPAIGN_AND_GAMEPLAY_ARCHITECTURE.md.

### v2.4 integration requirement

Existing v2.4 artifacts document 41 quest chains (26 main + 15 side), 1,574 nodes, 1,901 edges, 36 district/event pools, 108 placeholder VO slots and 313 scenario fixtures. Static QA reports 164 unreachable nodes. Edge execution, condition truth coverage, choice execution, ending execution and in-game smoke tests are NOT RUN. Dialogue import and runtime API integration remain pending. Treat v2.4 as a campaign graph lock candidate, not a playable or engine-locked campaign. Reconcile with docs/v2.4/README.md, docs/v2.4/QA_REPORT.json and production/chat-export/V2_4_CAMPAIGN_GRAPH_LOCK_STATUS.md.

## 8. AI-first production

Build a model-agnostic AI development studio: orchestrator; canon/research analyst; geographic designer; asset researcher; world engineer; narrative architect; quest engineer; dialogue/localization writer; gameplay/UI/audio engineers; QA/performance/security/licensing/documentation agents.

Route architecture and hard debugging to strong reasoning models; repository implementation to a coding agent such as Codex; high-risk review to an independent model; narrative to long-context creative models; current tool research to research-capable models; original media to image/3D/audio models; routine classification/retrieval to local models where quality is sufficient. Record provider, model ID, date, configuration, task and cost. Model names/APIs change; avoid hardcoded model assumptions.

The available workstation (40 GB RAM, RTX 3070 laptop GPU with 8 GB VRAM, Intel i7) can support selected local workloads, not assumed largest reasoning models or high-end 3D pipelines. See docs/AI_STUDIO_ARCHITECTURE.md.

## 9. Autonomous development loop

Orchestrator reads task/canon/technical docs; creates bounded task contract; agent works in isolated branch/worktree; runs static validation/tests; independent reviewer checks diff/evidence; agent opens PR; CI/Windows runner executes applicable checks; human approves high-risk changes, canon, merge and release. Agents never push directly to main.

Cloud agents cannot prove game behavior unless connected to a controlled Windows Build Runner. Use an isolated Cyberpunk test installation, fixed commits, pinned tools, restricted paths, command allowlists, logs, screenshots and rollback. Never expose arbitrary shell access to the user's normal game installation.

## 10. Technical architecture and asset rights

Use structured source data, schemas, deterministic build transforms, mod-specific adapters and reproducible packaging. Keep proprietary game dumps out of Git. Store original assets, permitted references, metadata and provenance only. See docs/TECHNICAL_ARCHITECTURE.md, docs/TECHNICAL_POC_AND_BUILD_RUNNER.md and docs/ASSET_REUSE_AND_PROVENANCE.md.

## 11. First technical proof and vertical slice

Prove: (1) original asset import; (2) world-sector edit with streaming/collision/navigation; (3) campaign bootstrap independent of V; (4) complete quest with branch/reward/fail/retry/save/load; (5) AI task → PR → Windows build evidence.

First vertical slice: West Palm City neighborhood/block plus one 15–30 minute mission (duration provisional), landmark/interior, traversal, combat/noncombat paths, consequential dialogue branch, objective HUD, failure/retry, save/load, ambient dispatch, install/uninstall and clean test profile.

## 12. UI/audio and release

Replace or rebrand player-facing menu, New Game, lifepath, loading, map, journal, profile, phone, inventory/cyberware, vehicle, database, pause and quest HUD surfaces where supported. Build original/authorized radio, dialogue, ambient barks, soundscapes, UI audio and localization. Full native UI replacement may be constrained; document what cannot safely be replaced. See docs/UI_AUDIO_CONVERSION_PLAN.md.

Gold Coast 1.0 requires independent-feeling new-campaign flow and Rook identity; three lifepaths; complete original campaign and seven planned endings subject to canon lock; all planned regional identities represented/accessed; confirmed corporate/faction content; original side content; stable combat/progression/save behavior; coherent Gold Coast presentation; tested install/upgrade/removal/dependencies/compatibility/performance; zero critical progression blockers; provenance/legal review; release notes, known issues and checksums.

Standalone-feeling means a complete new experience while still requiring the base game; it does not mean an independent executable.

## 13. Go/no-go gates

Do not scale to all districts until the vertical slice is repeatably buildable, installable, playable, save/load safe and tested. Do not call the campaign engine-locked until graph reachability and runtime coverage pass. Do not call release complete until clean installation and uninstall/rollback have been tested.

## 14. Related production documents

- docs/AI_STUDIO_ARCHITECTURE.md
- docs/WORLD_CONVERSION_PLAN.md
- docs/CAMPAIGN_AND_GAMEPLAY_ARCHITECTURE.md
- docs/BASE_GAME_CARRYOVER_MATRIX.md
- docs/ASSET_REUSE_AND_PROVENANCE.md
- docs/UI_AUDIO_CONVERSION_PLAN.md
- docs/TECHNICAL_POC_AND_BUILD_RUNNER.md
- docs/QA_AND_RELEASE_PLAN.md
- docs/PRODUCTION_BACKLOG.md
- docs/RISK_REGISTER.md
- docs/v2.4/README.md
