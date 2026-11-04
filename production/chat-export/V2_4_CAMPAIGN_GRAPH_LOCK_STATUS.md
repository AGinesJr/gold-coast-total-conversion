# v2.4 — Full Campaign Graph Lock & Runtime Integration

## Scope represented
- 41 quest chains (26 main campaign beats + 15 side chains)
- 1,574 nodes and 1,901 edges in generated graph JSON
- 36 district/event pools (12 districts × AMBIENT/COMBAT/REACTIVE)
- 108 placeholder VO line slots (3 per pool)
- 313 scenario fixtures: 60 lifepath × companion × quest-state combinations, quest-state transition fixtures, and seven ending fixtures
- Seven ending nodes
- Objective start/complete, failure, retry, replay paths
- Three approach options and three generic outcome options per quest
- CORPO/STREETKID/NOMAD recognition branches; Lux/Mara/Jackson interruption routing
- Python EngineBridge adapter test double with allowlisted command contract

## QA snapshot
- Static reachability: FAIL — 164 nodes reported unreachable
- Edge execution: NOT RUN
- Condition truth-value coverage: NOT RUN
- Choice execution coverage: NOT RUN
- Ending runtime coverage: NOT RUN
- REDengine/game smoke tests: NOT RUN

## Blockers before lock
1. Repair graph reachability and explicitly model legal retry/replay entry points.
2. Import/reconcile authored v2.1 scene dialogue verbatim (source import is pending; briefings are placeholders).
3. Replace generic consequence templates with bespoke quest outcomes.
4. Execute scenario runner and achieve complete edge/choice/condition/ending coverage or documented exemptions.
5. Replace event VO placeholders with final dialogue, actor assignments, localization and recording metadata.
6. Map adapter contract to verified Cyberpunk mod-framework APIs and test in-game.

**Status: CAMPAIGN GRAPH LOCK CANDIDATE — NOT ENGINE-LOCKED OR PLAYABLE.**

No proprietary base-game files/assets are included.