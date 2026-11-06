# Phase 0 — Autonomous Pipeline First

**Status:** Active; owner green-lit Phase 0 on 2026-11-05.  
**Strategy:** prove a bounded, auditable agent → validation → PR → evidence loop before asking that loop to build Gold Coast content.  
**Scope:** repository automation and technical discovery. This phase does not install tools on the owner's PC, modify the normal Cyberpunk installation, or claim any game-runtime proof.

## Why this order

The original blueprint remains the product/canon baseline, but the expanded toolchain changes the sequencing: build the automation spine first, then let it safely execute small technical proof tasks. EDGEkit/EDGEquest, WolvenKit, and world tools are candidates—not assumed capabilities.

## Phase 0 workstreams

| ID | Workstream | First artifact | Exit evidence |
|---|---|---|---|
| P0-A | Repository automation foundation | Task contract schema, templates, validator, CI | Valid task passes; malformed task fails; CI report attached |
| P0-B | Toolchain/version research | `config/toolchain.lock.yaml` | Exact game build and candidate versions recorded with source URLs, dates, compatibility state; unknowns explicit |
| P0-C | Asset/resource catalog prototype | Catalog schema + sample metadata-only records | Catalog validates; provenance and rights fields required; no extracted assets in Git |
| P0-D | EDGEkit/WolvenKit evaluation | Tool evaluation task + acceptance checklist | One disposable asset/resource workflow demonstrated or documented no-go |
| P0-E | World-edit feasibility | World POC task contract | One isolated sector/block experiment with evidence, rollback and known limitations |
| P0-F | Quest/runtime feasibility | EDGEquest minimal-quest task contract | Dialogue/objective/choice/failure/retry/save-load tested in game, or limitations recorded |
| P0-G | Controlled Windows runner | Runner design + threat model | Allowlisted job executes in isolated staging; logs/artifacts returned; destructive actions denied |
| P0-H | Autonomous task loop | End-to-end task report | Agent task → checks → branch/PR → runner evidence → reviewer; owner merges |

## Initial order (dependency-aware)

1. **P0-A / pipeline bootstrap (now):** establish task schema, validator, CI, reusable task template and evidence conventions.
2. **P0-B / toolchain lock:** obtain the actual installed Cyberpunk executable/build, DLC state, OS and tool versions. Until physically inspected, lock entries remain `unknown` or `candidate`, never fabricated.
3. **P0-C / resource catalog:** define metadata-only records and provenance/license checks; index assets locally on the Windows machine later.
4. **P0-D / asset pipeline spike:** use WolvenKit as baseline; evaluate EDGEkit/REDcode for agent integration. Prove one original asset package in a disposable install.
5. **P0-E / world spike:** test one small sector with a documented baseline, edit, collision/streaming/spawn checks and rollback.
6. **P0-F / campaign + quest spike:** test startup isolation and a single EDGEquest or hand-authored quest, including save/load. Do not import the entire v2.4 graph yet.
7. **P0-G / runner hardening:** only after P0-D/E/F tasks are bounded and repeatable; isolate the game, allowlist commands, capture logs/screenshots/checksums.
8. **P0-H / end-to-end autonomy:** let agents execute only approved contracts; independent QA reviews; all changes land in PRs; owner merges.
9. **Go/no-go:** publish a Phase 0 report with proof links, blockers, costs, compatibility matrix and recommended Phase 1 scope.

## Autonomy and approval policy

- **T0 read/research:** agents can browse public docs, inspect repository files and create source-linked findings.
- **T1 draft:** agents can draft plans, schemas, test data and code proposals.
- **T2 bounded repository edit:** agent may edit only task `allowed_paths`, run approved checks, and commit to a task branch.
- **T3 implementation PR:** agent may open a PR with acceptance evidence and reviewer report.
- **Human-only gates:** game installation changes, destructive world operations, credentials, licensing, canon locks, startup/save architecture decisions, main merge, release/publication.
- Agents never push to `main`, use arbitrary shell, or treat generated output as proof without logs.

## Phase 0 acceptance criteria

- [ ] Task contract schema validates all task templates.
- [ ] Validator has positive and negative tests and runs in GitHub Actions.
- [ ] Toolchain lock distinguishes `verified`, `candidate`, `unknown`, and `blocked`; every verified entry includes evidence.
- [ ] Asset catalog schema requires provenance, source, license status, and game/tool version.
- [ ] Windows runner threat model and command allowlist reviewed.
- [ ] Asset, world, campaign/quest and autonomous build proof spikes have actual evidence or explicit no-go findings.
- [ ] All runtime claims cite logs, commit, tool/game versions, artifacts and screenshots as appropriate.
- [ ] Phase 0 go/no-go is approved before Phase 1 scope expands.

## Task/evidence conventions

Every task contains: stable ID, objective, context refs, allowed paths, forbidden actions, deliverables, acceptance checks, risk tier, budget/retry cap, reviewer, rollback. Evidence is stored as a report or GitHub Actions artifact; proprietary assets and save files remain outside the repository.

## Current facts vs unknowns

- PR #7 Master Blueprint v1.0 is merged into `main`.
- v2.4 campaign remains a graph/test candidate; runtime integration is not proven.
- No local Cyberpunk executable/build, DLC state, framework versions, or Windows runner connectivity has been verified in this session.
- EDGEkit/EDGEquest are preview/candidate tools and require hands-on acceptance tests.
- No game files have been changed by Phase 0 repository work.
