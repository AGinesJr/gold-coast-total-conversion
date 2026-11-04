# Roadmap & Gates

## Phase 0 — Feasibility
- Confirm source canon and establish approved ledger.
- Pin current game/tool versions; evaluate licensing/distribution rules.
- Prove asset packaging, world-cell/streaming, quest state, save/load, and build rollback.
- Define regional map scale and hardware/performance budgets.
**Exit:** documented go/no-go with reproducible spike.

## Phase 1 — Vertical slice
- One playable block, landmark/interior, traversal loop, combat and noncombat path.
- One mission, consequential branch, objective/fail/retry, save/load.
- Ambient dispatch, install package, automated scenario tests.
**Exit:** no critical crash/softlock; all branches tested; repeatable build and provenance.

## Phase 2 — Production foundation
- Reusable quest, encounter, district and asset pipelines.
- Stable ID conventions, localization, state migration, test harness.

## Phase 3 — Campaign
- Main campaign graph, lifepath variants, companions/faction arcs, ending routes.
- Coverage across lifepath × companion × mission state × faction state.

## Phase 4 — World expansion
- Expand district by district; each cell meets performance, navigation, streaming and QA gates.

## Phase 5 — Release readiness
- Compatibility matrix, install/uninstall, known issues, documentation, licensing review, regression and community feedback.

Never scale content before the preceding gate passes.
