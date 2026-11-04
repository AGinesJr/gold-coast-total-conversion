# Architecture Decision Records

## ADR-001 — Slice-first production
**Status:** Proposed. Build one representative playable cell/mission before mass world or campaign production. Reason: prove engine constraints, performance, and pipeline early.

## ADR-002 — Canon is versioned data
**Status:** Proposed. Maintain a canon ledger with provenance and explicit LOCKED/PROVISIONAL/TBD statuses; agents cannot silently alter locked canon.

## ADR-003 — AI agents prepare PRs, humans merge
**Status:** Proposed. Bounded agents work in isolated branches with tests and evidence; humans own canon, IP, security, merge and release.

## ADR-004 — Hybrid regional map
**Status:** Proposed. Preserve recognizable South Florida relationships while fictionalizing geography and building streaming cells; exact fidelity/scale decided after prototype.

## ADR-005 — No proprietary game-file redistribution
**Status:** Required project guardrail. Store manifests and provenance, not proprietary base-game dumps; review third-party asset terms before release.

## ADR-006 — Candidate toolchain only
**Status:** Proposed. WolvenKit/REDmod/RED4ext/ArchiveXL/TweakXL/redscript/CET/Codeware/World Builder are evaluated and version-locked only after compatibility tests.
