# Architecture Decision Records

## ADR-001 — Slice-first production
**Status:** Proposed. Build one representative playable cell/mission before mass world or campaign production. Reason: prove engine constraints, performance and pipeline early.

## ADR-002 — Canon is versioned data
**Status:** Proposed. Maintain canon ledger with provenance and explicit SOURCE-ESTABLISHED / PROVISIONAL / PROPOSED / TBD / LOCKED statuses. Agents cannot silently change locked entries.

## ADR-003 — AI agents prepare PRs, humans merge
**Status:** Proposed. Bounded agents work in isolated branches with tests/evidence. Humans own canon, IP, security, merge and release.

## ADR-004 — Hybrid regional map
**Status:** Proposed. Preserve recognizable South Florida relationships while fictionalizing geography and building streaming cells. Exact fidelity/scale decided after prototype.

## ADR-005 — No proprietary game-file redistribution
**Status:** Required project guardrail. Store manifests and provenance, not proprietary base-game dumps; review third-party asset terms before release.

## ADR-006 — Candidate toolchain only
**Status:** Proposed. WolvenKit, REDmod, RED4ext, ArchiveXL, TweakXL, redscript, CET, Codeware, World Builder and RedHotTools are evaluated and version-locked only after compatibility tests.

## ADR-007 — AI-first, model-agnostic production studio
**Status:** Proposed. Use specialized agents and a provider-agnostic model router. Record model/provider versions, cost, task inputs and evaluation. Use human gates for canon, licensing, high-risk architecture, merge and release.

## ADR-008 — Cloud agents require a controlled Windows Build Runner
**Status:** Proposed. Cloud agents can prepare source changes and PRs, but actual game runtime validation requires a controlled Windows environment, isolated game install, command allowlist, logs and rollback.

## ADR-009 — West Palm City is the first world vertical slice
**Status:** Proposed. Build one playable neighborhood/block with landmark/interior, traversal, NPCs, combat/noncombat, quest branch, save/load and performance validation before scaling all districts.

## ADR-010 — v2.4 graph remains a candidate until runtime gates pass
**Status:** Required QA guardrail. Preserve stable graph IDs and source artifacts. Remediate reported unreachable nodes, execute scenario/choice/condition/ending coverage, import authored dialogue and validate a real runtime adapter before calling the campaign engine-locked.

## ADR-011 — Gold Coast campaign must be isolated from V's original campaign
**Status:** Proposed. Prefer safe bootstrap and campaign gating over destructive replacement. Test new game, restart, load, save and rollback in isolated profiles before production expansion.
