# Gold Coast QA and Release Plan

## 1. Quality philosophy

An AI agent saying “done” is not acceptance evidence. Features move through specified → implemented → statically validated → built → runtime tested → approved. Never mark a runtime gate passed from a design document or generated fixture.

## 2. Test layers

| Layer | Coverage |
|---|---|
| Unit | Individual data transforms, functions, adapters and state operations |
| Schema | YAML/JSON shape, required fields, types, enums |
| Referential | Stable IDs, asset/quest/dialogue/location references |
| Graph | Reachability, dangling edges, cycles, condition satisfiability, ending paths |
| Scenario | Lifepath × companion × quest-state × faction-state combinations |
| Integration | Quest, event, faction, save and UI interactions |
| World | Streaming, collision, navigation, spawn, interior and fast travel |
| Runtime | Actual mod loading, campaign startup, quest completion, save/load |
| Performance | Frame time, memory, streaming stalls, crash behavior |
| Release | Clean install, upgrade, uninstall, rollback and compatibility |

## 3. v2.4 known QA baseline

Current repository evidence reports 41 quests; 1,574 graph nodes; 1,901 edges; 164 unreachable nodes; 36 event pools and 108 placeholder VO slots; 313 scenario fixtures; duplicate IDs 0; bad conditions 0. Edge execution, condition truth, choice execution, ending execution and in-game smoke tests are NOT RUN.

This is a blocker list, not a pass. Re-run validators against current source before making claims about changed counts.

## 4. Required scenarios

Campaign: each lifepath starts; first mission begins/completes; every choice resolves; failure/retry/checkpoint/replay work; no softlocks; all seven planned endings reachable; companion/no-companion branches work; quest state persists across save/load/restart.

World: every district/sector loads; no required assets missing; collision/navigation work; required interiors enter/exit; NPCs spawn correctly; fast travel works; transitions do not trap player; performance budgets met.

Gameplay: combat and stealth encounters completable; weapons/cyberware function; faction reputation/hostility update; rewards are idempotent; contracts and regional events trigger correctly; police/security responses consistent.

Save: save/load during active quest; after branch choice; after district transition; with companion active; before/after ending; migration and invalid-save recovery; no cross-contamination with ordinary V saves.

Installation: clean install on supported game build; missing dependency detection; upgrade; uninstall without deleting unrelated mods; checksum/package manifest verification.

## 5. Visual QA

Check for Night City/V/Johnny/Relic campaign references where Gold Coast content should appear; missing/incorrect district labels; unbranded landmarks; broken textures/materials; NPC outfit/identity mismatch; subtitle/UI overflow; incorrect objectives; missing audio; map/fast-travel inconsistency.

Computer-use automation may assist, but some sequences require a human tester or custom in-game test hooks. Do not claim full autonomous playtesting until repeatability is demonstrated.

## 6. Blocking severity

Blocker: prevents new game, campaign progress, save integrity, core world loading or safe installation.  
Critical: major quest/ending broken, repeated crash, severe progression loss.  
High: major feature unavailable or significant performance regression.  
Medium: limited content or presentation defect with workaround.  
Low: cosmetic/documentation issue.

Release candidate must have zero open blockers and critical issues; remaining issues must be documented and accepted.

## 7. Proposed release stages

0.0.1 Technical prototype; 0.0.2 World prototype; 0.0.3 Campaign bootstrap; 0.1.0 First playable; 0.2.0 Vertical slice; 0.3.0 District expansion; 0.5.0 Campaign alpha; 0.8.0 Content-complete beta; 0.9.0 Release candidate; 1.0.0 Total conversion release.

These are planning targets, not claims of existing builds.

## 8. Release package

Include distributable Gold Coast files; dependency/version checker; install/update/uninstall instructions; game/framework compatibility matrix; release manifest/checksums; QA summary/known issues; asset/third-party notices; credits/disclaimer; save backup/rollback guidance.

Do not bundle the base game or proprietary extracted files. Review CDPR and mod-host terms before public distribution.
