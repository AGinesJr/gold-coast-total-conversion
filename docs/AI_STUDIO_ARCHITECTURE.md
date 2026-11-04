# Gold Coast AI Studio Architecture

## 1. Operating model

Human-directed, AI-executed. The project owner controls creative direction, canon approvals, licensing decisions, security-sensitive permissions, merges and releases. Agents research, draft, implement bounded changes, test, document and prepare PRs.

## 2. Agent roster

| ID | Role | Primary deliverables |
|---|---|---|
| AG-00 | Orchestrator / producer | Task DAG, routing, status, integration plan |
| AG-01 | Canon guardian | Source reconciliation, contradiction reports, canon IDs |
| AG-02 | Geographic designer | Regional map, district briefs, location hierarchy |
| AG-03 | Asset researcher | Asset catalog, reuse classification, provenance |
| AG-04 | World engineer | Sector/placement changes, world validation |
| AG-05 | Narrative architect | Campaign outline, character arcs, choice maps |
| AG-06 | Quest engineer | Quest graph, objective lifecycle, implementation |
| AG-07 | Dialogue/localization | Dialogue records, barks, VO/localization metadata |
| AG-08 | Gameplay engineer | Factions, reputation, economy, encounters, progression |
| AG-09 | UI engineer | Menus, map labels, journal and presentation |
| AG-10 | Audio/asset producer | Original audio, texture, visual and asset pipeline |
| AG-11 | QA engineer | Schemas, graph tests, scenario tests, regression |
| AG-12 | Performance engineer | Profiling, streaming and memory reports |
| AG-13 | Security/licensing reviewer | Provenance, dependency and release compliance |
| AG-14 | Documentation/release | Docs, manifests, changelog, installer notes |

Start with AG-00, AG-01, AG-03, AG-04, AG-06 and AG-11. Add specialists when their pipeline exists.

## 3. Model routing

Use provider/model abstraction rather than hardcoding model names:
- high-reasoning model: architecture, difficult debugging and ambiguous technical decisions;
- coding agent (Codex or equivalent): multi-file repository work, tests and PR preparation;
- independent coding/reasoning model: review of critical changes;
- long-context creative model: campaign, character, dialogue and lore synthesis;
- research-capable model: current modding documentation, compatibility and licensing;
- image generation: concept art, original 2D graphics and visual references;
- 3D generation/assisted modeling: original geometry and props;
- speech/audio generation: provisional voice and original audio, subject to rights and quality review;
- local models: lightweight classification, retrieval, transformation, tagging and offline experiments.

Record provider, model ID, date, task type, configuration, input references, output artifacts, cost/usage and evaluation result. Re-evaluate models periodically; model names and benchmarks are not permanent.

## 4. Autonomy tiers

- T0 Read: search, inspect, summarize, catalog.
- T1 Draft: nonbinding lore, design, code proposals, tests and documentation.
- T2 Bounded edit: modify allowlisted paths; run validators and tests; no merge.
- T3 Branch implementation: multi-step tasks in isolated branches/worktrees; self-test; open PR with evidence.
- Human gate: canon lock, licensing, credentials/secrets, destructive operations, startup/save architecture, production deployment, merge and release.

## 5. Task contract

~~~yaml
task_id: GC-EXAMPLE-0001
agent: AG-06
objective: Implement one bounded quest transition
context:
  - docs/CAMPAIGN_AND_GAMEPLAY_ARCHITECTURE.md
  - docs/v2.4/README.md
allowed_paths:
  - narrative/
  - src/quests/
  - tests/quest/
forbidden_actions:
  - push_to_main
  - publish_release
  - alter_locked_canon
  - modify_user_game_install
deliverables:
  - source_changes
  - tests
  - implementation_report
acceptance:
  - schema_valid
  - references_resolve
  - transition_test_passes
risk_tier: medium
budget:
  max_model_calls: 12
  max_retries: 2
reviewer: AG-11
rollback: revert_task_branch
~~~

## 6. Autonomous loop

Backlog → context retrieval → dependency check → task contract → isolated branch/worktree → implementation → static validation → tests → independent review → PR → CI/build runner → human merge approval.

Agents must not push directly to main; change locked canon without approval; delete/overwrite unrelated work; access credentials unnecessarily; modify the normal game installation; execute arbitrary untrusted shell commands; publish releases; or represent unexecuted tests as passed.

## 7. Shared knowledge

Maintain three versioned knowledge layers:
1. Canon: characters, locations, timeline, factions, corporations, story facts, status and sources.
2. Technical: file formats, framework docs, pinned versions, proven patterns, failed experiments and constraints.
3. Execution: tasks, decisions, PRs, bugs, build reports, costs and test evidence.

Agents retrieve task-specific context. They do not ingest proprietary game archives wholesale.

## 8. Cost and capacity controls

Classify tasks A routine → small/fast model; B standard structured data → coding model; C complex quest/gameplay → strong coding model; D startup/save/world streaming/security → high-reasoning model plus independent review; E major narrative/visual direction → creative model plus human approval.

Set per-task call/token/time/retry budgets. Cache approved canon and technical references. Use local inference only where the local model meets quality requirements. Escalate on budget exhaustion rather than looping indefinitely.

## 9. Windows Build Runner

Cloud agents cannot prove game runtime behavior unless connected to a controlled workstation. Build Runner runs on a dedicated Windows development environment and checks out a specific commit, verifies game/tool versions, builds original resources and packages, deploys only to an isolated test installation, launches supported smoke tests, captures logs/screenshots/crash data, and returns immutable artifacts and reports.

Use a command allowlist, restricted filesystem paths, isolated credentials, execution logs, rollback, and human approval for destructive operations. Never expose unrestricted shell access to an agent.

## 10. Evaluation metrics

Track task acceptance rate, first-pass test pass rate, regression rate, escaped defects, PR rework, cost per accepted task, model latency, context retrieval quality, build reproducibility and human review time. Optimize for accepted, tested work—not lines of generated code.
