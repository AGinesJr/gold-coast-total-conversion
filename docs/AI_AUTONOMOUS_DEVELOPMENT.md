# AI Autonomous Development

## Goal

Use current AI models and autonomous agents to accelerate research, content authoring, implementation, QA and documentation while keeping canon, IP, safety, security, merge and release decisions accountable to humans.

## Operating documents

- [AI Studio Architecture](AI_STUDIO_ARCHITECTURE.md) — agent roster, model routing, autonomy tiers, task contracts, budgets and Windows Build Runner.
- [Total Conversion Master Blueprint](TOTAL_CONVERSION_MASTER_BLUEPRINT_V1_0.md) — project-wide design and production rules.
- [Production Backlog](PRODUCTION_BACKLOG.md) — initial prioritized work.
- [Technical POC and Build Runner](TECHNICAL_POC_AND_BUILD_RUNNER.md) — actual runtime evidence workflow.

## Roles

Orchestrator; canon/research analyst; narrative architect; geographic/world designer; asset/provenance researcher; engineer; quest/dialogue/gameplay/UI/audio specialists; test engineer; performance engineer; security/licensing reviewer; build/release agent; documentation agent.

## Model routing

Use a provider-agnostic routing layer:
- high-reasoning model for architecture and difficult debugging;
- coding agent such as Codex for repository-level multi-file work, tests and PRs;
- independent coding/reasoning model for high-risk review;
- long-context creative model for narrative and dialogue;
- research-capable model for current documentation and compatibility;
- image/3D/audio models for original assets;
- local models for suitable lightweight classification, retrieval and transformations.

Record provider, model ID, date, configuration, cost and evaluation result. Re-evaluate model choices as capabilities and pricing change.

## Task contract

Every task states: goal; source context; allowed paths; prohibited actions; artifact format; acceptance criteria/tests; dependencies; risk tier; budget; rollback; reviewer.

## Autonomy tiers

- T0: read, search, summarize.
- T1: drafts, plans, tests and nonbinding proposals.
- T2: bounded code/data edits with automated checks and review.
- T3: multi-step branch implementation, self-test and PR preparation.
- Human approval: canon locks, asset/license decisions, secrets/security, destructive operations, startup/save architecture, merge and release.

## Loop

Issue/task → context bundle → isolated branch/worktree → agent change → validators/tests → independent review → PR → Windows build runner when runtime evidence is needed → human merge → release notes. Keep logs and model/tool versions for reproducibility.

## Quality and safety controls

Require source links for canon research; distinguish fact, inference, proposal and uncertainty; test graphs for reachability and dead ends; independently review high-impact changes; do not grant repository admin, publishing or unrestricted asset deletion by default; never let cloud agents modify the normal game installation; never report unexecuted tests as passed.

## Cost controls

Use small/fast models for routine work, stronger models for complex engineering, and independent review for critical work. Set per-task model-call/token/time/retry budgets. Cache approved context and use local inference only when quality is sufficient. Escalate when budgets are exhausted rather than looping indefinitely.
