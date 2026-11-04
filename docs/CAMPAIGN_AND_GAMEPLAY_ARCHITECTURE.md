# Gold Coast Campaign and Gameplay Architecture

## 1. Narrative premise

Rook returns to the Gold Coast carrying a damaged implant containing ECHO-9, a reconstructed personality associated with scientist Elias Voss. Project ECHO connects corporate research, consciousness continuity, political control and the struggle for human autonomy. Gold Coast's corporate and street powers compete to control the technology and the future of the region.

This premise is a working synthesis. Full source-chat story, timeline, character motivations and causality must be reconciled before canon lock.

## 2. Campaign identity

- Player character: Rook.
- Lifepaths: Corpo, Streetkid, Nomad.
- ECHO-9: reconstructed Elias Voss.
- Central project: Project ECHO.
- Central thematic conflict: corporate immortality/continuity versus human freedom.
- Campaign frame: 2077–2085, provisional.
- Corporate powers: Arasaka, Militech, Kang Tao, Petrochem, Night Corp.
- v2.4 companion identifiers: Lux, Mara, Jackson and a no-companion configuration.

Gold Coast must not depend on V, Johnny Silverhand or completion of the original Cyberpunk campaign.

## 3. Story and historical anchors

The existing repository identifies West Palm blackout, Palm Beach Atlantis, Protectorate governance, Treaty of Boca, Project ECHO exposure, Palm Beach Holocaust and Free Gold Coast Assembly. Preserve these as chronological anchors until source reconciliation determines exact dates, causality and story placement.

A prior planning draft suggested 2074 disappearance/death events and 2077–2085 milestones. Treat detailed year-by-year sequencing as provisional until compared with authored narrative documents.

## 4. Campaign structure

~~~text
GC_CAMPAIGN
  BOOTSTRAP
  PROLOGUE
  LIFEPATH_OPENINGS
    CORPO
    STREETKID
    NOMAD
  MAIN_CAMPAIGN
    ACT_01 / ACT_02 / ACT_03 / ACT_04
  SIDE_QUESTS
  FIXER_CONTRACTS
  FACTION_STORIES
  COMPANION_STORIES
  INVESTIGATIONS
  SECRET_MISSIONS
  ENDINGS
  POST_CAMPAIGN
~~~

Act count and mission ordering are placeholders, not locked canon.

## 5. Quest data contract

Every quest includes ID/title/category/act/source references; prerequisites; locations/NPCs/scenes/dialogue IDs; objective nodes and explicit transitions; choices and consequence declarations; quest facts/world-state changes; success/failure/abandon/retry/replay rules; checkpoints and save/load behavior; rewards/unlocks; ending/companion/faction dependencies; test scenarios and coverage.

Example:
~~~yaml
quest_id: GC_MAIN_001
category: main_story
status: PROPOSED
prerequisites: [GC_PROLOGUE_COMPLETE]
objectives:
  - id: OBJ_001
    type: reach_location
    target: LOC_EXAMPLE
  - id: OBJ_002
    type: interact
    target: ECHO_TERMINAL
choices:
  - id: CHOICE_001
    outcomes:
      - outcome_id: OUTCOME_A
        consequence_facts: [FACT_EXAMPLE_A]
      - outcome_id: OUTCOME_B
        consequence_facts: [FACT_EXAMPLE_B]
failure:
  checkpoint: GC_MAIN_001_CHECKPOINT_01
retry_policy: explicit
save_policy: persist_quest_facts
~~~

## 6. v2.4 campaign graph integration

Do not replace or casually regenerate the v2.4 graph. Maintain stable IDs. Current documented status:
- 41 quest chains (26 main, 15 side);
- 1,574 nodes and 1,901 edges;
- 164 unreachable nodes in static QA;
- 36 district/event pools and 108 placeholder VO slots;
- 313 scenario fixtures;
- seven ending names;
- edge execution, condition truth, choice execution, ending execution and in-game smoke tests NOT RUN;
- authored v2.1 dialogue import and final VO pending;
- Python EngineBridge is a test double, not REDengine integration.

Remediation:
1. recover/import authored v2.1 scenes/dialogue with provenance;
2. classify and repair all 164 reported unreachable nodes;
3. verify every choice edge and condition;
4. replace generic consequences with quest-specific state changes;
5. execute all scenario fixtures in a real graph runner;
6. test all ending routes;
7. replace VO placeholders and add actor/localization metadata;
8. implement and verify a real mod-framework adapter;
9. conduct in-game smoke tests and save/load recovery.

## 7. Quest lifecycle

Logical states: LOCKED, AVAILABLE, ACTIVE, COMPLETED, FAILED. Explicitly define objective start/complete/reset; checkpoint restore; failure; retry; abandon; replay eligibility; reward idempotency; save/load restoration. Avoid duplicate rewards and softlocks. Every nonterminal state needs a recovery path or documented design reason.

## 8. Event dispatch

Ambient/combat/reactive dialogue pools dispatch from game events using district, faction, event type, combat state, companion, quest facts, cooldown, priority and speaker availability. Use deterministic selection and safe fallback. Do not fire if speaker unavailable, scene already active or bark on cooldown.

## 9. Gameplay systems

Reuse base foundations where feasible; implement Gold Coast rules for faction reputation/hostility; district influence/regional control; corporate influence; civilian support; contracts/fixer progression; investigation/evidence; companion trust/availability; lifepath recognition; regional events; economy/rewards; ending conditions/world-state outcomes.

Suggested faction relationship scale: -100 to +100, neutral 0. Thresholds are tuning proposals, not canon.

## 10. Ending registry

Preserve seven v2.4 names:
1. Crown Eternal
2. Southern Occupation
3. Silicon Paradise
4. Zero Humanity
5. Free Gold Coast
6. Sawgrass Exodus
7. Atlantic Ghost

Each ending requires prerequisites, decision-variable thresholds, companion outcomes, faction/corporate outcomes, final quest graph, cinematic/dialogue, world-state delta, credits/epilogue and reachable test fixture. Exact conditions must be authored and approved; do not infer them from names.

## 11. Player experience separation

Gold Coast bootstrap initializes Rook, lifepath, campaign facts, ECHO-9 state, starting district, inventory/loadout and first quest. Prevent conflicting V campaign initialization. Prefer safe entry-point/launcher integration and campaign gating over destructive deletion of original campaign resources. Prove clean start, load, restart, death/retry and save isolation before expanding.
