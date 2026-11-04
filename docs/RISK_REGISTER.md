# Gold Coast Risk Register

| ID | Risk | Severity | Mitigation / gate |
|---|---|---|---|
| R-001 | REDengine/modding APIs cannot support required world/campaign replacement | Critical | Prototype startup, sector, quest and runtime hooks before scale-up |
| R-002 | New map/streaming scope exceeds available interfaces | Critical | Hybrid map; custom sectors only after POC |
| R-003 | Original V campaign conflicts with Gold Coast bootstrap | Critical | Campaign namespace, controlled entry point, non-destructive gating |
| R-004 | Quest graph contains unreachable/broken branches | Critical | Graph runner, edge/condition/ending coverage; remediate v2.4's 164 nodes |
| R-005 | v2.1 authored dialogue missing from repository payload | High | Recover original artifacts, import with stable IDs/provenance |
| R-006 | Placeholder VO makes story feel unfinished | High | VO/localization pipeline and acceptance gate |
| R-007 | Python adapter mistaken for actual REDengine integration | Critical | Label as test double; require real adapter and in-game proof |
| R-008 | Game updates break framework compatibility | High | Version lock and compatibility matrix |
| R-009 | AI-generated code/data invalid | High | Schemas, compilation, tests, independent review |
| R-010 | AI agents introduce canon contradictions | High | Canon status registry, source links, human approval |
| R-011 | Agent modifies unrelated/destructive resources | Critical | Path allowlists, isolated branches, restricted runner, audit logs |
| R-012 | Cloud agent cannot test actual game | High | Windows Build Runner and evidence-return workflow |
| R-013 | Asset quality/optimization insufficient | High | In-game review, LOD/material/collision/performance checks |
| R-014 | Save corruption or migration failure | Critical | Isolated saves, migration tests, recovery and backups |
| R-015 | Performance degradation across districts | High | Representative-cell budgets, profiling and streaming tests |
| R-016 | AI inference/asset costs exceed budget | Medium/High | Model routing, per-task budgets, local models for suitable tasks |
| R-017 | Proprietary game assets redistributed without permission | Critical | Provenance manifest, no base-game dumps, licensing review |
| R-018 | Third-party AI/audio/3D output rights unclear | High | Provider terms review, source records, original/licensed assets |
| R-019 | Scope expansion delays playable release | High | Vertical slice, milestone gates, scope control |
| R-020 | UI replacement incomplete due engine constraints | Medium/High | Prioritize player-facing surfaces; document unavoidable base UI |
| R-021 | Companion/romance implementation conflicts with base systems | High | Prototype one companion branch before expanding cast |
| R-022 | Installer damages unrelated mods/game files | Critical | Isolated staging, manifest-based install, safe uninstall tests |

## Review cadence

Review risks at each milestone and before architecture changes, framework updates, public test builds or release. A risk closes only when evidence demonstrates mitigation works.

## Release blockers

R-001 through R-004, R-007, R-011, R-014, R-017 and R-022 must be resolved or explicitly accepted by the project owner before public release.
