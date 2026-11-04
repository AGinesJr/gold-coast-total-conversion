# AI Autonomous Production Architecture

## 1. Operating model

Human-directed, AI-executed. Agents research, write, code, catalog assets, generate data/tests, document, and prepare PRs. Humans approve canon changes, high-risk architecture, destructive operations, and releases. Accept work only with changed files, validation logs, tests, review notes and reproducible instructions.

## 2. Agent roster

| ID | Role | Deliverable |
|---|---|---|
| AG-00 | Orchestrator | Task breakdown, routing, integration/status |
| AG-01 | Canon Guardian | Contradiction reports, canon validation |
| AG-02 | Geographic Designer | District/location specifications |
| AG-03 | Asset Researcher | Resource inventory and reuse matrix |
| AG-04 | World Engineer | Sector/placement work and validation |
| AG-05 | Narrative Director | Campaign and character arcs |
| AG-06 | Quest Engineer | Quest specifications/implementation |
| AG-07 | Dialogue Writer | Dialogue records and voice scripts |
| AG-08 | Gameplay Engineer | Reputation, economy and gameplay systems |
| AG-09 | UI Engineer | Menus, journal, map presentation |
| AG-10 | Audio Producer | Audio manifest and integration |
| AG-11 | QA Engineer | Unit/integration/quest/world/regression tests |
| AG-12 | Performance Engineer | Profiling/optimization reports |
| AG-13 | Provenance/Compliance | Rights, source and release audit |
| AG-14 | Documentation Agent | Technical/user docs and changelog |

Start with AG-00, AG-01, AG-03, AG-04, AG-06 and AG-11; add roles as dependencies mature.

## 3. Task contract

Every task states task ID/title/agent/priority/status; inputs/source references; allowed and forbidden paths/actions; dependencies/assumptions; deliverables/acceptance criteria; validation commands/evidence; token/call/time/retry budget; escalation triggers; review and rollback.

Example contract fields:
- task_id: GC-WORLD-001
- agent: AG-04
- title: West Palm City district prototype
- inputs: canon, district brief, world-editing technical docs
- allowed_paths: src/world/, data/districts/, wolvenkit/projects/
- forbidden: modify base-game files, overwrite main, publish release, alter canon without approval
- deliverables: district manifest, world files, placement report, test results, screenshots
- acceptance: loads, assets resolve, collision/navigation validated, performance report
- review_required: true

## 4. Model routing

Route by complexity/risk, not brand loyalty:
- Routine metadata/classification/formatting → economical or local model.
- Standard configuration/data/code → coding agent.
- Complex quest integration/debugging → strong reasoning + coding agent.
- Architecture/startup/save/security → high reasoning, independent review and human gate.
- Lore/dialogue → long-context creative model with canon retrieval.
- Concept/texture → image model, then provenance/quality review.
- 3D → specialized generation, Blender cleanup and in-game validation.
- QA → coding/computer-use agent plus deterministic scripts.
- Documentation → economical long-context model.

Keep provider adapters replaceable; log model/version/cost. Do not assume one model is best for every task.

## 5. Autonomous lifecycle

1. Select backlog task and check dependencies.
2. Retrieve approved canon/technical context.
3. Orchestrator creates bounded task and isolated branch/worktree.
4. Agent edits only permitted paths/actions.
5. Deterministic validation executes.
6. Independent review checks correctness, security and canon.
7. Agent fixes findings within retry budget.
8. PR includes evidence and limitations.
9. CI/Build Runner executes integration tests.
10. Human approves merge for protected/high-risk paths.
11. Merge and update status.

## 6. Autonomy tiers

- Tier 0: read/research/report.
- Tier 1: edit allowed files, run safe tests, commit branch.
- Tier 2: create PR and request review.
- Tier 3: merge low-risk PR only if explicit policy/checks permit; default disabled.
- Tier 4: publish/release/destructive actions—human approval always.

No unrestricted main-branch, game-install, credential or release access.

## 7. Shared knowledge

Three sources of truth:
1. Canon: docs/canon (story, geography, characters, factions, timeline).
2. Technical: docs/technical (tested formats, docs, compatibility and patterns).
3. Execution: task/issue tracker, PRs, bugs, decisions and test evidence.

Retrieve narrow context; do not dump asset archives/full repository into every prompt. Use stable IDs. Canon changes require a decision record and human approval.

## 8. Windows Build Runner

Cloud agents cannot validate a game on another PC without a controlled interface. A local runner should receive approved commit/build requests, use an isolated Cyberpunk test installation, check versions, run asset scripts/REDmod/WolvenKit, deploy to test directories, launch permitted smoke tests, capture logs/screenshots/crash reports/manifests, and return artifacts/results.

Security: allowlisted commands/paths; no arbitrary shell from untrusted prompts; no writes to primary game; secrets outside repo; full audit logs; destructive operations require approval; reproducible rollback.

## 9. Budget/reliability

Each task has token/call/time/retry ceilings and escalation conditions. Stop/report on exhaustion. Cache stable references and test results; route routine work to low-cost/local models; reserve premium reasoning for difficult/high-risk tasks. Measure cost per accepted deliverable, not output volume.

## 10. Evaluation metrics

Accepted PRs/attempted PRs; first-pass validation rate; rework count; regressions; cost per accepted task; time-to-acceptance; canon violations; missing-evidence rate. Evaluate verified outcomes, not generated output quantity.

## 11. Initial assignments

- AG-00: backlog/task/PR automation.
- AG-01: canon consolidation and unresolved decisions.
- AG-03: asset inventory taxonomy/research.
- AG-04: world-sector technical proof.
- AG-06: quest schema and first quest proof.
- AG-11: validation harness/regression plan.

All work depends on repository access, exact game/tool version discovery and isolated test-install readiness.