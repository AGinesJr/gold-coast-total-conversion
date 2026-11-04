# Gold Coast Total Conversion — Master Blueprint v1.0

**Status:** production plan / feasibility-first. This is not a claim of a playable implementation.

## 1. Product definition
Create a full-conversion experience set in a fictionalized South Florida cyberpunk region. The base game supplies tested player systems where reuse is technically and legally permitted; the project supplies its own world identity, narrative, missions, dialogue, encounter design, progression, visual direction, and regional map.

**Player promise:** explore a recognizable but transformed Gold Coast, make consequential choices among competing powers, and confront the cost of corporate continuity/immortality versus human freedom.

## 2. Canon baseline (provisional)
- Protagonist: Rook; Corpo, Streetkid, Nomad lifepaths.
- ECHO-9: reconstructed Elias Voss.
- Campaign span: 2077–2085.
- Working historical/political anchors: West Palm blackout; Palm Beach Atlantis; Protectorate governance; Treaty of Boca; Project ECHO exposure; Palm Beach Holocaust; Free Gold Coast Assembly.
- Corporations currently in scope: Arasaka, Militech, Kang Tao, Petrochem, Night Corp.
- Regional factions, district names/borders, event dates, ECHO rules, companion roster, mission ordering, and endings need source-chat reconciliation and explicit canon lock. Do not fill gaps by invention.

## 3. World and map strategy
Use a hybrid strategy: retain a coherent regional silhouette and recognizable real-world street/landmark relationships where useful, then fictionalize names, ownership, architecture, infrastructure, and routes. Do not assume a 1:1 real-world map is feasible.

Map layers:
1. **Macro:** regional travel, waterways, highways, corporate boundaries, security zones.
2. **District:** neighborhood identity, landmarks, faction control, services, ambient life.
3. **Playable cell:** collision, navigation, combat spaces, interiors, mission staging, streaming boundary.
4. **Mission dressing:** quest props, clues, temporary states, aftermath.

Each location record should include stable ID, coordinates/transform, district, traversal links, streaming requirements, faction ownership, encounter tags, quest-state hooks, asset provenance, and QA status. Validate streaming and memory constraints with a single block before mapping a whole county.

## 4. Campaign and quest architecture
Author quests as data-first graphs where practical:
- nodes: scenes, dialogue, objectives, encounters, gates, rewards, transitions;
- edges: explicit choice/condition/event transitions;
- state: player flags, faction reputation, companion availability, inventory, world-state, mission status;
- outcomes: success, failure, retry, abandon, replay, and ending resolution.

Every choice must have a documented consequence or explicitly be cosmetic. Avoid softlocks: define recovery, retry, and alternate routes. Event dispatch should connect ambient/combat barks to authored pools using tags (district, faction, combat state, companion, quest flags) with deterministic fallback and cooldowns.

## 5. First vertical slice (gate before expansion)
Build one representative playable neighborhood/block and a 15–30 minute mission (duration target is provisional):
- spawn and traversal loop;
- one hub/interior or meaningful landmark;
- one combat encounter and one noncombat resolution;
- one dialogue branch with a downstream state consequence;
- one companion/faction interaction if feasibility permits;
- objective HUD, fail/retry, save/load persistence;
- ambient event dispatch;
- packaged install/uninstall and clean test profile.

**Acceptance:** repeatable build; no critical crash/softlock; mission state survives save/load; all branches exercised by automated tests; assets have provenance; performance/memory baseline captured; QA checklist and known limitations published.

## 6. Workstreams
A. Canon & narrative — source reconciliation, canon ledger, campaign graph, dialogue style guide.
B. World design — regional map, district briefs, cell specifications, traversal and streaming.
C. Mod engineering — toolchain/version pinning, packaging, scripts, runtime integration, save safety.
D. Gameplay — combat/stealth/social encounter templates, rewards, progression, balancing.
E. Art/audio — original or licensed assets, material/lighting rules, VO and ambient libraries.
F. QA & release — automated checks, scenario coverage, install validation, regression, provenance.
G. AI production platform — agent task contracts, orchestration, telemetry, review queue.

## 7. AI-first production operating model
Use specialized agents for research, canon extraction, narrative drafting, map data, implementation, tests, build triage, and documentation. Agents must operate from versioned briefs and structured outputs; never let an agent silently alter canon or overwrite unrelated files.

Task contract: objective; context/source links; allowed paths; prohibited actions; expected artifacts; acceptance tests; dependencies; risk tier; rollback; reviewer. Agents create branches and PRs, not direct releases.

Autonomy:
- **Tier 0:** read/search/summarize.
- **Tier 1:** draft artifacts and tests.
- **Tier 2:** bounded code/data changes with CI and review.
- **Tier 3:** multi-step branch implementation, self-test, PR preparation.
- **Human-only gates:** canon lock, proprietary/third-party asset decisions, security, merge, release, destructive actions.

## 8. Candidate toolchain (verify versions and capabilities)
Investigate WolvenKit, REDmod, RED4ext, ArchiveXL, TweakXL, redscript, Cyber Engine Tweaks, Codeware, and World Builder. Treat this as a candidate list, not a guaranteed compatible stack. Record game build, tool versions, dependencies, known limitations, and reproducible install steps. A feasibility spike must prove world edits/streaming, quest or state integration, custom assets, packaging, and rollback.

## 9. Repository structure proposal
```
/docs       canon, blueprint, architecture, roadmap, decisions
/canon      structured timeline, factions, characters, locations
/narrative  quest graphs, scenes, dialogue, barks
/world      district briefs, location manifests, map metadata
/gameplay   encounter templates, balance and progression data
/assets     manifests and provenance only (no proprietary game dumps)
/tools      validators, build and packaging scripts
/tests      graph, condition, state, scenario, install tests
/releases   changelogs, known issues, compatibility matrix
```

## 10. Verification and coverage
- lint schemas, IDs, references, duplicate keys, localization tokens;
- graph reachability, dangling edges, condition satisfiability, ending reachability;
- choice/edge/condition/objective/failure/retry coverage;
- scenario matrix across lifepath × companion × quest state × faction state;
- deterministic replay and save/load checkpoints;
- asset provenance/license validation;
- clean install, upgrade, uninstall, and regression test;
- performance, memory, streaming, and crash telemetry.

## 11. Roadmap
1. **Feasibility:** version lock, toolchain spike, legal/provenance policy, map scale study.
2. **Vertical slice:** one cell + one mission, packaged and tested.
3. **Foundation:** reusable district/cell/quest/encounter pipelines.
4. **Campaign:** authored graph, companion/faction arcs, endings, scenario automation.
5. **World expansion:** district-by-district with quality gates.
6. **Release:** compatibility matrix, installation guide, known issues, community feedback loop.

## 12. Risks and gates
- Engine limitations → prototype before content commitments.
- Scope explosion → slice-first and district caps.
- Canon drift → versioned canon ledger and human lock.
- AI hallucination/unsafe edits → contracts, tests, review, audit logs.
- Proprietary asset misuse → no game-file redistribution; provenance and licensing gate.
- Save corruption/softlocks → explicit state migrations and recovery tests.
- Performance/streaming failure → representative cell budgets and profiling.

**Go/no-go:** expand only when the vertical slice can be built, installed, replayed, tested, and reviewed reproducibly.
