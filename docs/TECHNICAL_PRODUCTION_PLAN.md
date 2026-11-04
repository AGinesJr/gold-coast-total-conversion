# Gold Coast Technical Production Plan

## 1. Goals
Create a reproducible pipeline for assets, world, quests, gameplay, campaign, testing and packaging while preserving the player's normal Cyberpunk installation and saves.

## 2. Candidate toolchain (versions TBD)

| Tool | Purpose |
|---|---|
| REDmod | Official mod workflows/packaging where applicable |
| WolvenKit | Resource browsing, editing, importing and project packaging |
| RED4ext | Native extension base |
| ArchiveXL | Custom resources/streaming sectors if supported |
| TweakXL | TweakDB modifications |
| redscript | Gameplay scripts |
| Cyber Engine Tweaks | Lua/debug/runtime interactions |
| Codeware | Additional APIs/UI/events where needed |
| World Builder | World-node/placement workflow |
| RedHotTools | Runtime world inspection |
| Blender | Original geometry and asset preparation |
| Python | Data validation and asset/build automation |
| PowerShell | Windows runner/build orchestration |
| Git/Git LFS | Source and large original assets |
| GitHub Actions | Static validation, docs/schema checks and manifests |

Verify compatibility against the exact game executable and framework versions. Do not assume latest-version compatibility.

## 3. Version locks

Maintain game, framework, toolchain, schema and agent-model locks. Every build records game executable version, framework/tool versions, source commit, build-script version, asset manifest, test report and checksum.

## 4. Repository architecture

```text
README.md / LICENSE.md / CONTRIBUTING.md / PROJECT_STATUS.md
.github/workflows/
.agents/
docs/{canon,world,narrative,characters,factions,gameplay,technical,production,decisions}/
data/{districts,locations,characters,factions,quests,dialogue,items,vehicles,encounters,endings}/
src/{bootstrap,campaign,quests,world,factions,gameplay,progression,save,ui,integrations}/
assets/{concepts,original_models,textures,audio,animations,logos,manifests}/
wolvenkit/{projects,imports,build-config}/
tools/{asset-catalog,quest-validator,lore-validator,dependency-checker,build,packaging}/
tests/{unit,integration,quest,world,save,performance,regression}/
agent-workspace/{tasks,reports,reviews,evaluation}/
releases/{manifests,checksums}/
```

Do not commit extracted base-game files, secrets, temporary files or unauthorized third-party assets.

## 5. Git workflow

- main: reviewed/releasable source.
- develop: integration branch.
- feature/<subsystem>-<task>: bounded agent work.
- Agents use isolated branches/worktrees; no direct main push.
- PRs include summary, rationale, files, dependencies, tests, logs/screenshots, limitations and rollback.
- Protected paths: bootstrap, save, campaign entry, dependency locks and release workflow.

## 6. Asset pipeline

Reference → concept → review → model/texture/audio production → collision/rigging as needed → import → in-game test → optimize → approved manifest.

Asset manifest fields: ID/name/type; source/origin/creator; original resource reference (if applicable); AI-generated flag/model/tool; license and redistribution status; source paths; dependencies; validation status; version/hash.

## 7. World conversion

Preferred hybrid:
1. Catalog Night City sectors/resources.
2. Select adaptable environments for Gold Coast regions.
3. Remove/conceal incompatible identity/landmarks.
4. Rebrand/reconstruct resources.
5. Add custom landmarks/sectors only after proof.
6. Build routes, collision, navigation, NPC placements/transitions.
7. Test streaming, save/load, density and performance.
8. Maintain district manifests and rollback snapshots.

Provisional mapping: Crown—Corpo Plaza/luxury; West Palm City—Downtown/commercial; Silicon Coast—corporate/technology; Belt—dense commercial/residential; Arc—residential/cultural; Frontier—outskirts/Badlands; Sugarlands—industrial/agricultural-adjacent; Lake Corridor—logistics/industrial; Green Hell—Badlands/vegetation; Atlantis/Abyss/Skyports—custom sectors as required.

## 8. Campaign bootstrap

Detect game/framework versions and Gold Coast install/campaign; initialize Rook/lifepath/equipment/world/faction/ECHO facts; start Gold Coast prologue; prevent original campaign takeover; restore state on load; validate saves/migration; recover startup failures. Do not remove original campaign resources first. Prove isolation in a separate test install.

## 9. Quest/data validation

Enforce unique IDs, valid prerequisites and references (locations/NPC/dialogue), objective types/targets, conditions, branch reachability, rewards/failure/recovery, ending dependencies and QA links. Fail on unresolved references, duplicate IDs, invalid graph nodes, inaccessible required targets, missing checkpoint/recovery or circular prerequisites unless explicitly allowed.

## 10. Windows Build Runner

1. Verify approved commit/clean workspace.
2. Check game/tool versions.
3. Fetch source and permitted local resources.
4. Run schema/lore/asset/dependency validators.
5. Run REDmod/WolvenKit build steps.
6. Package to isolated staging.
7. Deploy to isolated game test install.
8. Run deterministic tests and smoke launch.
9. Capture logs/screenshots/crash data.
10. Produce manifest/checksum/report.
11. Return artifact/status.

Use allowlisted commands, isolated paths, no secrets in logs, and no writes to primary game install.

## 11. Test matrix

Game/framework compatibility; asset resolution/import; world sector streaming/collision/navigation; New Game and each lifepath; quest graph/branches; NPC/faction behavior; inventory/cyberware/weapons/driving; saves at checkpoints and district transitions; companion/ending variables; regression; district performance/memory; install/remove/upgrade.

## 12. Release package

Gold Coast original source/build artifacts; dependency manifest; installer/instructions; version/game compatibility; known issues; checksums; provenance/licensing audit; uninstall/rollback. No game archives or unlicensed extracted assets.