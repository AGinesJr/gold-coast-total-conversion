# Gold Coast Total Conversion Master Blueprint v1.0

**Date:** 2026-11-04 · **Target:** Cyberpunk 2077 Ultimate Edition (PC) · **Status:** Pre-production; technical gates open

## Mission and definition of done
Transform Cyberpunk 2077 into a new-feeling open-world RPG in a South Florida-inspired Gold Coast. Cyberpunk remains the required game dependency; Gold Coast provides new player identity, setting, campaign, factions, quests, dialogue, regional progression, and endings. A release is complete when players can install it, start as Rook, select a lifepath, explore the transformed world, complete scoped content and all planned endings, save/reload reliably, and avoid critical progression blockers. AI completion claims are not acceptance evidence; test artifacts and human acceptance are required.

## Principles
1. New identity: Gold Coast is not V visiting Florida.
2. Independent narrative: Rook/ECHO-9, not V/Johnny/Relic.
3. Reuse base systems and assets where practical, technically sound, and legally permitted.
4. Modular implementation, explicit interfaces, stable IDs, versioned schemas.
5. AI-first production with bounded tasks, automated validation, independent review.
6. Reproducible builds with commit, tool versions, manifests, logs, checksums.
7. Asset provenance and distribution rights tracked.
8. Gold Coast saves isolated; never damage normal V saves.
9. Profile performance and lock tested dependencies.
10. Gate content expansion on technical proof.

## Base-game carryover inventory

### Systems retained as foundation (subject to compatibility testing)
- First-person movement/interactions; vehicle camera; driving and vehicle summoning/ownership/damage/combat.
- Gunplay, melee, stealth, cover, enemy AI, boss/encounter framework.
- Quickhacking, cyberware slots/capacity, ripperdocs, cyberdecks, Sandevistan, Berserk, Mantis Blades, Gorilla Arms, Monowire, Projectile Launch System.
- Power/Tech/Smart weapons, attachments, scopes, suppressors, grenades, consumables, healing, crafting, loot, inventory, attributes/perks/progression.
- Cars, motorcycles, luxury, corporate, police, armored, off-road and Nomad vehicle archetypes.
- Civilian, corporate-security, gang, police, military, vendor, doctor, engineer, robot, drone and turret archetypes; animation, facial animation and scene choreography libraries.
- Dialogue/scene presentation, quest/journal/objective framework, phone/messages, map/fast travel, database, inventory/cyberware UI, save/load and photo mode.
- Interiors, buildings, corporate campuses, luxury/industrial assets, roads, props, vegetation, lighting, weather, audio emitters, signs and billboard assets—each cataloged for suitability.

### Reuse classification
- **A Direct reuse:** unchanged.
- **B Rebrand:** names, signage, textures, materials, placement.
- **C Reconstruction:** substantially altered base environment/resource.
- **D Original:** new geometry, texture, animation, audio, or content.

These are proposals until resource-level suitability, technical compatibility, and legal distribution are checked. Referencing an installed game's asset is not permission to redistribute it.

## New Gold Coast content
- Campaign entry/start flow; Rook identity; Corpo, Streetkid, Nomad lifepaths and origin-specific dialogue.
- ECHO-9 state/identity system, Elias Voss records, Project ECHO mystery.
- Original main campaign, side quests, gigs/contracts, investigations, faction stories, companion arcs, romances, secrets, endings, epilogues and post-campaign state.
- Original characters, fixers, executives, gang leaders, companions, informants, investigators, dialogue and voice assets.
- District identity, map presentation, landmarks, signs, street names, logos, billboards, loading/menu art, lore database, regional audio/radio.
- New/transformed estates, research facilities, marinas, skyports, offshore installations, agricultural/industrial sites, terrain/vegetation and road network as needed.
- Regional reputation, faction relationships/territory, corporate influence, civilian support, investigation/evidence, regional events, contract economy, ending-state tracking.
- Gold Coast balancing, loot/vendor distribution, vehicle identity, encounters, NPC population, quest placement, fast travel and world-state consequences.

## Geography: 12 regions

| ID | District | Inspiration | Identity |
|---|---|---|---|
| GC-001 | The Crown | Palm Beach Island | Old money, estates, corporate elites |
| GC-002 | West Palm City | West Palm Beach | Urban center, government, commerce, crime |
| GC-003 | Silicon Coast | Boca Raton | Neural tech and research |
| GC-004 | The Belt | Delray–Boynton | Working-class corridor, gangs, nightlife |
| GC-005 | The Arc | Lake Worth–Riviera | Dense neighborhoods and culture |
| GC-006 | The Frontier | Jupiter–Tequesta | Coastal frontier, military, wilderness |
| GC-007 | Sugarlands | Belle Glade | Agricultural exploitation, Petrochem |
| GC-008 | Lake Corridor | Lake Okeechobee region | Industrial transport/logistics |
| GC-009 | Green Hell | Everglades | Wilderness, Nomads, exploration |
| GC-010 | Atlantis | Atlantis/industrial expansion | Corporate/industrial expansion |
| GC-011 | The Abyss | Atlantic Ocean | Offshore installations and secrets |
| GC-012 | Skyports | Regional aviation infrastructure | Air mobility and elite access |

### Major locations
- LOC-001 Imperial Tower — Arasaka.
- LOC-002 Night House — Night Corp.
- LOC-003 The Garden — Project ECHO, inside Imperial Tower but a distinct location identity.
- LOC-004 Southern Crown — Militech.
- LOC-005 Atlantic Relay — Atlantic Ghosts.
- LOC-006 Zero Chamber — MUNICIPAL ZERO.
- LOC-007 Atlantis — corporate/offshore city concept.

### World/map strategy
Preferred **hybrid conversion**: transform existing Night City sectors/assets where viable and add custom streaming sectors/locations only where technical proof supports them. An entirely independent map is not assumed feasible. Prove streaming, terrain, roads, navigation, collision, sector boundaries, transitions and performance before committing to map scale.

First district: **West Palm City**. It must prove streets, commercial/residential/corporate architecture, waterfront, NPCs, faction activity, police, interiors, driving, combat and mission integration. A district is done only with boundaries/navigation, landmark/identity, roads/collision/streaming, NPCs, faction presence, interior/activity, environmental storytelling, access/fast travel and performance/regression report.

## Story canon
- Rook: former Militech intelligence operative; disappeared in 2074; resurfaces in 2077.
- Lifepaths: Corpo, Streetkid, Nomad.
- ECHO-9: damaged implant/shard containing reconstructed personality of scientist Elias Voss.
- Elias Voss was killed in 2074.
- Project ECHO: corporate immortality/consciousness program.
- Central conflict: corporate immortality/control versus human autonomy.
- Setting period: 2077–2085.

### Timeline baseline
| Year | Milestone |
|---|---|
| 2074 | Rook disappears; Elias Voss killed |
| 2077 | Rook returns with damaged implant/ECHO-9; regional crisis |
| 2078 | Assembly |
| 2079 | Militech expansion |
| 2080 | Kang Tao city expansion |
| 2081 | Unknown intelligence emerges |
| 2082 | Nomad alliance |
| 2083 | Fragile peace |
| 2084–2085 | Final consequences/resolution |

### Corporations (5)
Arasaka (Imperial Tower/Project ECHO); Militech (Southern Command); Kang Tao (Boca Neural Campus); Petrochem (Sugarlands); Night Corp (MUNICIPAL ZERO/Night House).

### Street factions (7)
Crown Boys; Iron Saints; Breakers; Velvets; Canal Rats; Sawgrass Nomads; Atlantic Ghosts. Leadership, territories, alliances and histories must be canon-locked before production.

### Seven ending concepts
1. Crown Eternal — corporate continuity.
2. Southern Occupation — Militech dominance.
3. Silicon Paradise — technology-led future.
4. Zero Humanity — human autonomy lost.
5. Free Gold Coast — regional independence.
6. Sawgrass Exodus — Nomad-led departure.
7. Atlantic Ghost — offshore power/disappearance.

Each ending requires conditions, decision graph, companion outcomes, world changes, final quest/scene, dialogue, credits and QA route.

## Campaign and quest architecture
Namespaces: GC_PROLOGUE; GC_LIFEPATH_CORPO/STREETKID/NOMAD; GC_ACT_01…N (act count TBD); GC_SIDE_QUESTS; GC_FIXER_CONTRACTS; GC_FACTION_STORIES; GC_COMPANION_STORIES; GC_ROMANCE_STORIES; GC_INVESTIGATIONS; GC_SECRET_MISSIONS; GC_ENDINGS.

Every quest record includes ID/title/category/act, prerequisites, location/NPC/dialogue IDs, objectives, facts/conditions, branches, rewards, failure conditions, checkpoints, save recovery, ending dependencies and QA tests. Validators must check unique IDs, references, graph reachability, branch conditions, recovery and ending prerequisites.

## Gameplay systems
Retain the base foundation; implement Gold Coast-specific regional reputation, faction hostility/alliance/territory, corporate influence, civilian support, evidence/investigation, fixer economy/events, companion trust/loyalty, lifepath consequences, ending-state and world-state managers. Proposed reputation range -100 to +100; thresholds require balance testing.

## UI and presentation
Gold Coast New Game/title/menu, lifepath selection, loading art, map/district labels, journal, lore/database, phone/contacts/messages, profile, inventory descriptions, cyberware/vehicle presentation, radio identity, pause menu and credits. Classify each component as native override, framework extension, custom overlay or retained/contextualized after technical discovery. Do not claim full replacement until tested.

## Technical toolchain (candidate; version-lock/test)
REDmod, WolvenKit, RED4ext, ArchiveXL, TweakXL, redscript, Cyber Engine Tweaks, Codeware, World Builder, RedHotTools, Blender, Python, PowerShell, Git/Git LFS and GitHub Actions. Verify exact compatibility with installed game build; no assumed latest-version compatibility.

## New Game and save isolation
Detect game/framework versions; detect install/campaign; initialize Rook/lifepath/equipment/world/faction/ECHO facts; start Gold Coast prologue; prevent original campaign takeover; restore campaign on load; validate saves/migration; recover safely. Do not delete original campaign resources first. Prove separation in an isolated test installation. Logical save model: campaign ID/version, identity/lifepath, quest/faction/companion/ending/world states, migration and recovery metadata—subject to actual game save capabilities.

## AI studio
Human-directed, AI-executed. Orchestrator decomposes work; specialized agents operate bounded paths/branches; deterministic validation and independent review precede PR integration. Humans approve canon changes, bootstrap/save changes, destructive actions and releases. Initial agents: AG-00 Orchestrator, AG-01 Canon Guardian, AG-03 Asset Researcher, AG-04 World Engineer, AG-06 Quest Engineer, AG-11 QA. See AI production document.

## QA and acceptance
Five levels: unit, integration, quest, world, gameplay. Release blockers: no repeatable critical/progression crash; New Game/bootstrap works; saves valid; required assets resolve; no critical quest blockers; endings reachable/consistent; no unauthorized asset distribution; no persistent streaming freeze/severe unexplained regression; district performance reports. Visual tests: replaced areas show Gold Coast names/signs/UI and no unintended V/Night City references or missing assets.

## Release/legal
Package original project work and legally distributable assets only. Require Cyberpunk ownership. No game archives/extracted CDPR assets absent authorization. Track third-party/AI asset provenance. Review CDPR fan-content rules, EULA and terms before public release; unofficial project/no implied endorsement. Plan free fan mod unless separately licensed.

## Phases and gates
0 Research: game/tool lock, asset inventory, prove world/quest/script/import, repo/agent setup → reproducible build.  
1 Foundation: canon, namespace, Rook/ECHO, bootstrap, branding, manifests → independent initialization.  
2 Vertical slice: West Palm City, landmark, NPCs, faction/fixer/mission → playable neighborhood.  
3 Systems: lifepaths, reputation, quest, companion, investigation, economy, endings → RPG framework.  
4 Regions: all 12 represented, corporate/faction locations/interiors/activities → accessible populated regions.  
5 Campaign: main/side/fixer/faction/companion/romance/secret content/seven endings → completable campaign.  
6 Presentation: menus/map/journal/phone/radio/loading/credits → standalone-feeling identity.  
7 QA: regression, saves, performance, compatibility, provenance, packaging → release candidate.  
8 Release: installer, docs, support, versioned v1.0.

## Definition of v1.0
Rook and all lifepaths; ECHO-9/Project ECHO; five corporations and seven factions in gameplay; twelve regions represented/accessed with varied density; original main campaign and scoped side content; companion arcs as approved; seven endings; Gold Coast world/UI/audio identity; stable saves/install/removal/dependencies/tests/docs.

## Exclusions from initial release
Expanded property ownership, extra racing, additional companion/romance branches, more contracts, dynamic warfare, extra vehicles, New Game Plus and additional epilogues are post-release candidates and must not block campaign completion.

## Open decisions
Exact game/framework versions; map extent/sector viability; district boundaries/distances; campaign acts/quest counts; companion/romance roster; voice strategy; music/radio rights; UI replacement limits; faction leaders/territories/alliances; ending decision graphs/postgame; performance baseline; installer/distribution channel. Track in decision records with evidence, owner, status and approval.