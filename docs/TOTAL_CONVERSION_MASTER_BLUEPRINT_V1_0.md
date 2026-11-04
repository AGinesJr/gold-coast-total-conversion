# Gold Coast — Total Conversion Master Blueprint v1.0

Date: 2026-11-04  
Target: Cyberpunk 2077 Ultimate Edition (PC); exact executable/build to be pinned in Phase 0  
Status: Production specification and feasibility plan. This is not a claim of a playable total conversion.

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

Core anchors:
- Protagonist: Rook.
- Lifepaths: Corpo, Streetkid, Nomad.
- ECHO-9: reconstructed personality associated with scientist Elias Voss.
- Central project: Project ECHO.
- Thematic conflict: corporate continuity / immortality versus human autonomy.
- Campaign frame: 2077–2085, provisional pending chronology reconciliation.
- Corporate powers: Arasaka, Militech, Kang Tao, Petrochem, Night Corp.
- v2.4 companion identifiers: Lux, Mara, Jackson, plus a no-companion path.
- v2.4 ending names: Crown Eternal, Southern Occupation, Silicon Paradise, Zero Humanity, Free Gold Coast, Sawgrass Exodus, Atlantic Ghost.

Provisional district labels from this planning conversation:
1. The Crown — Palm Beach Island inspiration.
2. West Palm City — West Palm Beach.
3. Silicon Coast — Boca Raton.
4. The Belt — Delray–Boynton corridor.
5. The Arc — Lake Worth–Riviera corridor.
6. The Frontier — Jupiter–Tequesta.
7. Sugarlands — Belle Glade / agricultural region.
8. Lake Corridor — Lake Okeechobee logistics region.
9. Green Hell — Everglades.
10. Atlantis — regional/offshore-industrial concept; distinguish from the existing Palm Beach Atlantis lore anchor.
11. The Abyss — Atlantic offshore region.
12. Skyports — regional aviation infrastructure.

Street-faction working roster: Crown Boys, Iron Saints, Breakers, Velvets, Canal Rats, Sawgrass Nomads, Atlantic Ghosts.

These district and faction labels, territories, leadership, chronology, alliances, and story roles must be reconciled against earlier Gold Coast lore before they are marked LOCKED.

Preserve existing historical/political anchors already recorded in the repository: West Palm blackout; Palm Beach Atlantis; Protectorate governance; Treaty of Boca; Project ECHO exposure; Palm Beach Holocaust; Free Gold Coast Assembly. Do not discard or reorder them without source reconciliation.

Canon status convention:
- SOURCE-ESTABLISHED: explicitly supported by an earlier source conversation or approved artifact.
- PROVISIONAL: working direction not fully reconciled.
- PROPOSED: newly suggested implementation or creative option.
- TBD: insufficient source evidence.
- LOCKED: explicitly approved by the project owner.

## 4. Base-game carryover inventory

Subject to exact game-version and mod-framework validation, investigate reuse of:
- first-person movement, traversal, interaction, camera and player controls;
- firearms, melee, stealth, combat AI, damage, enemy archetypes and encounter primitives;
- cyberware, cyberdecks, quickhacks, Sandevistan, Berserk, optics and ripperdoc progression;
- weapons, attachments, consumables, crafting, inventory, loot and vendor foundations;
- vehicles, motorcycles, driving physics, damage, vehicle combat, ownership and summon systems;
- NPC archetypes, civilian routines, police/security archetypes, robots, drones, turrets, animations, facial systems and scene choreography;
- quest, journal, dialogue, phone and contact systems where safely repurposed;
- character customization, clothing, photo mode, audio playback, save infrastructure and UI framework;
- reusable building kits, interiors, roads, props, vegetation, industrial/corporate assets, lighting and environmental effects.

Reuse classes: A = direct reuse; B = rebrand/reconfigure; C = reconstruct; D = original development. Reusing an archetype does not provide a finished Gold Coast character, mission, faction or encounter; identity, placement, behavior, dialogue and testing remain required.

## 5. New development scope

Gold Coast-specific work includes Rook's identity and lifepaths; ECHO-9 and Project ECHO; original campaign, quests, objectives, failure/retry/replay transitions, scenes, dialogue, consequences and endings; regional geography, landmarks, signage, roads, interiors, streaming sectors, navigation and NPC placements; corporate and street-faction identities, territories and relationships; original companions and relationship content if approved; regional economy, vendors, contracts, activities, encounters and world-state changes; Gold Coast menus, map labels, journal, loading screens, branding, radio, original audio and localization; installer, dependency checks, save migration and release documentation.

## 6. World conversion strategy

Preferred strategy: hybrid conversion. Inventory Night City sectors and assets. Select source areas by geometry, scale, road topology, environment type and streaming behavior. Recompose and rebrand suitable environments; conceal or replace incompatible landmarks; add custom landmarks and streaming sectors only after proof of concept.

Renaming districts or replacing textures does not create a new map. A genuinely new region requires world geometry, streaming-sector registration, collision, navigation, roads, boundaries, spawn points, encounters, fast travel and performance validation.

Initial source-environment mapping hypotheses:
- The Crown: luxury/corporate environments.
- West Palm City: downtown/commercial environments.
- Silicon Coast: corporate/technology campuses.
- The Belt and The Arc: dense commercial/residential streets.
- The Frontier and Green Hell: outskirts/Badlands terrain and vegetation.
- Sugarlands and Lake Corridor: industrial/logistics environments.
- Atlantis and The Abyss: custom offshore sectors or staged interiors if feasible.
- Skyports: rooftop/aviation environments.

West Palm City is the first world vertical slice.

## 7. Campaign and gameplay architecture

Use a Gold Coast campaign namespace and central state manager. Do not overwrite the original campaign wholesale as the first step.

Required layers: bootstrap/new-campaign initialization; lifepath openings; prologue and main acts; main quests, side quests, fixer contracts, faction stories, companion stories, investigations, secrets and endings; quest/objective lifecycle; ambient/combat/reactive dialogue dispatch; faction reputation; regional reputation; world-state; companion-state; ending variables; save/load validation and migration.

Every meaningful player choice must have a documented downstream consequence or be explicitly marked cosmetic.

### v2.4 integration requirement

Existing v2.4 artifacts document 41 quest chains (26 main + 15 side), 1,574 nodes, 1,901 edges, 36 district/event pools, 108 placeholder VO slots and 313 scenario fixtures. Static QA reports 164 unreachable nodes. Edge execution, condition truth coverage, choice execution, ending execution and in-game smoke tests are NOT RUN. Dialogue import and runtime API integration remain pending. Treat v2.4 as a campaign graph lock candidate, not a playable or engine-locked campaign. Reconcile with docs/v2.4/README.md, docs/v2.4/QA_REPORT.json and production/chat-export/V2_4_CAMPAIGN_GRAPH_LOCK_STATUS.md.

## 8. AI-first production model

Build a model-agnostic AI development studio with an orchestrator, canon/research analyst, geographic designer, asset researcher, world engineer, narrative architect, quest engineer, dialogue/localization writer, gameplay engineer, UI engineer, audio/asset producer, QA engineer, performance engineer, security/licensing reviewer and documentation/release agent.

Use the strongest current reasoning/coding model for architecture and hard debugging; a coding agent such as Codex for repository-level implementation; an independent model for high-risk review; long-context creative models for narrative; research-capable models for current modding documentation; image/3D/audio models for appropriate original assets. Model names and APIs change: record provider, model ID, date, configuration, task and cost.

Local AI can handle smaller classification, retrieval, transformations and experiments. The project owner's workstation (40 GB RAM, RTX 3070 laptop GPU with 8 GB VRAM, Intel i7) is suitable for selected lightweight workloads, not assumed to run the largest reasoning models or high-end 3D pipelines. Use hosted inference where needed.

## 9. Autonomous development loop

1. Orchestrator reads task, canon, technical docs and dependencies.
2. Create bounded task contract: inputs, allowed paths, forbidden actions, outputs, tests, risk tier, budget and reviewer.
3. Agent works in isolated branch/worktree.
4. Agent runs static validation and tests.
5. Independent reviewer inspects diff and evidence.
6. Agent opens PR; never pushes directly to main.
7. CI/build runner executes supported checks.
8. Human approves high-risk changes, canon changes, merges and releases.

Cloud agents cannot prove game behavior unless connected to a controlled Windows build runner. Runner uses isolated Cyberpunk test installation, fixed commits, pinned tools, restricted paths, command allowlists, logs, screenshots and rollback. Never allow arbitrary agent shell access to the user's normal game installation.

## 10. Repository and build architecture

Separate canon/narrative source; world/district/location manifests; gameplay/faction data; original assets and provenance; mod source and framework adapters; validators/build scripts; tests/fixtures; release manifests and documentation. Use structured source data, schema validation, deterministic build transforms and reproducible packaging. Keep proprietary game dumps out of Git.

## 11. First technical proof and vertical slice

Prove five things before mass content production:
1. Asset: import one original Gold Coast asset and verify in-game.
2. World: modify/add one test sector; validate streaming, collision, navigation and performance.
3. Campaign: initialize Gold Coast without accidentally starting V's original campaign.
4. Quest: implement one complete quest with dialogue, objective, branch consequence, reward, fail/retry and save/load recovery.
5. Autonomy: agent receives bounded task, changes files, runs validation, creates PR and supplies evidence; Windows runner produces a test result.

The first vertical slice is a West Palm City neighborhood/block plus one 15–30 minute mission (duration target provisional), one hub/interior or landmark, traversal, combat and noncombat paths, one consequential dialogue branch, objective HUD, failure/retry, save/load, ambient dispatch, install/uninstall and clean test profile.

## 12. Release definition

Gold Coast 1.0 must have independent-feeling new-campaign flow and Rook identity; all three lifepaths; complete original main campaign and seven planned endings subject to canon lock; all planned regional identities represented and accessible; five corporate powers and seven working street factions integrated where confirmed; original side content and supporting cast; stable combat/progression/save behavior; consistent Gold Coast presentation; tested installation, upgrade, removal, dependencies, compatibility and performance; no critical progression blockers; asset provenance/legal review; release notes, known issues and checksums.

Standalone-feeling means a complete new experience while still requiring the base game; it does not mean an independent executable.

## 13. Go/no-go gates

Do not scale to all districts until the vertical slice is repeatably buildable, installable, playable, save/load safe and tested. Do not call the campaign engine-locked until graph reachability and runtime coverage pass. Do not call release complete until clean installation and uninstall/rollback have been tested.

## Related production documents
- AI Studio Architecture
- World Conversion Plan
- Campaign and Gameplay Architecture
- Asset Reuse and Provenance
- Technical POC and Build Runner
- QA and Release Plan
- Production Backlog
- Risk Register
- Existing v2.4 campaign status
