# Gold Coast Production Backlog

This is the initial backlog derived from Total Conversion Master Blueprint v1.0 and existing v2.4 campaign artifacts. Tickets are planning items; none is complete merely because it is listed.

Priority: P0 blocks technical direction/safety; P1 required for first playable; P2 required for campaign/regional production; P3 polish/post-slice expansion.

## Phase 0 — Repository and feasibility

| ID | Priority | Task | Acceptance evidence |
|---|---|---|---|
| GC-0001 | P0 | Lock installed game version | Version report/build identifier |
| GC-0002 | P0 | Validate framework compatibility | Tested dependency matrix |
| GC-0003 | P0 | Create toolchain lock files | Reproducible setup |
| GC-0004 | P0 | Audit canon against source chats/artifacts | Claim ledger and conflicts |
| GC-0005 | P0 | Audit asset rights/provenance policy | Approved policy/schema |
| GC-0006 | P0 | Prove one original asset import | In-game evidence |
| GC-0007 | P0 | Prove world-sector editing | Streaming/collision/navigation evidence |
| GC-0008 | P0 | Prove campaign bootstrap | New Game independent of V campaign |
| GC-0009 | P0 | Prove one quest runtime integration | In-game quest/save/load evidence |
| GC-0010 | P1 | Create AI orchestration contracts | Agent run report |
| GC-0011 | P1 | Create Windows Build Runner | Exact commit build and evidence |

## Phase 1 — First playable

| ID | Priority | Task | Acceptance evidence |
|---|---|---|---|
| GC-0101 | P1 | Create West Palm City district manifest | Schema-valid locations/boundaries |
| GC-0102 | P1 | Build one playable West Palm City block | Traversal and performance report |
| GC-0103 | P1 | Create one landmark/interior | Provenance and runtime evidence |
| GC-0104 | P1 | Implement Rook identity prototype | Correct campaign identity |
| GC-0105 | P1 | Implement lifepath selection | Three tested paths |
| GC-0106 | P1 | Implement ECHO-9 interaction | Dialogue/state persistence |
| GC-0107 | P1 | Implement one main quest | Branch, objective, fail/retry, save/load |
| GC-0108 | P1 | Add one faction/encounter | NPC/faction evidence |
| GC-0109 | P1 | Package install/uninstall prototype | Clean test-profile install/removal |

## Phase 2 — Reusable systems

GC-0201 quest schema/validator; GC-0202 stable ID/reference validator; GC-0203 graph runner/reachability repair; GC-0204 objective/failure/retry/replay lifecycle; GC-0205 ambient/combat/reactive dispatcher; GC-0206 faction reputation; GC-0207 regional/world-state manager; GC-0208 companion state; GC-0209 save migration/campaign isolation; GC-0210 localization/VO pipeline.

## Phase 3 — v2.4 remediation

GC-0301 recover/import v2.1 authored scenes/dialogue; GC-0302 classify/repair 164 reported unreachable nodes; GC-0303 implement bespoke quest consequences; GC-0304 execute legal graph edges/choices; GC-0305 execute condition true/false coverage; GC-0306 execute 313 scenario fixtures in a real graph runner; GC-0307 verify seven endings; GC-0308 replace VO placeholders and add actor/localization metadata; GC-0309 implement real REDengine/mod-framework adapter; GC-0310 in-game campaign smoke tests.

Do not regenerate IDs or overwrite graph data during repair without migration plan.

## Phase 4 — Regional/campaign expansion

GC-0401 district template; GC-0402 district-by-district conversion; GC-0403 corporate headquarters/mission spaces; GC-0404 faction territories/quest lines after canon lock; GC-0405 companion relationships; GC-0406 main campaign/lifepath variants; GC-0407 side quests/fixer contracts; GC-0408 regional events; GC-0409 endings/epilogues; GC-0410 UI/audio/localization.

## Phase 5 — Release

GC-0501 performance optimization; GC-0502 save/load regression; GC-0503 compatibility matrix; GC-0504 clean install/upgrade/uninstall; GC-0505 licensing/provenance audit; GC-0506 installer/package; GC-0507 release notes/known issues/checksums; GC-0508 human release approval.

## Initial agent assignments

Start with AG-00 Orchestrator, AG-01 Canon Guardian, AG-03 Asset Researcher, AG-04 World Engineer, AG-06 Quest Engineer and AG-11 QA Engineer. Add agents only when workflows are ready.

## Definition of task completion

A ticket is complete only when its PR contains acceptance evidence: changed paths, build/test logs, screenshots where relevant, dependencies, known limitations and rollback instructions.
