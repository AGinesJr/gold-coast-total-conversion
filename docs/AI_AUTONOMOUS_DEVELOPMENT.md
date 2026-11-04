# AI Autonomous Development

## Goal
Use AI models and agents to accelerate research, content authoring, implementation, QA, and documentation while keeping canon, IP, safety, merge, and release decisions accountable to humans.

## Roles
- Research/canon analyst: source extraction, contradiction report, citations.
- Narrative architect: quest graphs, branch consequence maps, dialogue drafts.
- World designer: district/cell manifests, traversal and encounter tags.
- Engineer: bounded implementation and adapters.
- Test engineer: graph, state, scenario, regression and install tests.
- Build/release agent: CI diagnosis, manifests, changelog, PR checklist.
- Coordinator: dependency DAG, task assignment, status, review queue.

## Task contract (required)
Every task states: goal; source context; allowed paths; prohibited actions; artifact format; acceptance criteria/tests; dependencies; risk tier; rollback; reviewer. Agents must not overwrite unrelated work or silently change locked canon.

## Autonomy tiers
- T0: read, search, summarize.
- T1: drafts, plans, tests, nonbinding proposals.
- T2: bounded code/data edits with automated checks and review.
- T3: multi-step branch implementation, self-test, PR preparation.
- Human approval required for canon locks, asset/license decisions, secrets/security, destructive operations, merge, and release.

## Loop
Issue/task → context bundle → isolated branch/worktree → agent change → validators/tests → reviewer diff + evidence → PR → human merge → release notes. Keep logs and model/tool versions for reproducibility.

## Quality controls
- Require structured output and source links for canon research.
- Distinguish fact, inference, proposal, and uncertainty.
- Test generated graphs for reachability and dead ends.
- Run independent review on high-impact changes.
- Never grant agents repository admin, publishing, or unrestricted asset deletion by default.
