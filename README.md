# Gold Coast Total Conversion

A production framework for a Cyberpunk 2077 total-conversion project set in a fictionalized South Florida / Gold Coast Corporate Republic.

> **Status:** pre-production / technical discovery. This repository does not yet contain a playable mod. Canon and REDengine implementation details marked TBD require validation.

## Vision
Build a story-rich, street-level Gold Coast experience using Cyberpunk 2077 Ultimate Edition as the gameplay foundation where legally and technically appropriate. Preserve proven base systems (combat, cyberware, vehicles, NPC behaviors, quest infrastructure) while developing original setting, characters, missions, dialogue, world presentation, and progression.

## Canon snapshot
- **Rook:** protagonist; Corpo, Streetkid, or Nomad lifepath.
- **ECHO-9:** reconstructed personality of Elias Voss; identity, continuity, and immortality form a central conflict.
- **Campaign window:** 2077–2085 (provisional).
- **Regions:** The Crown, West Palm City, Silicon Coast, The Belt, The Arc, The Frontier, Sugarlands, Lake Corridor, Green Hell, Atlantis, The Abyss, Skyports.
- **Corporations:** Arasaka, Militech, Kang Tao, Petrochem, Night Corp.
- **Street factions:** Crown Boys, Iron Saints, Breakers, Velvets, Canal Rats, Sawgrass Nomads, Atlantic Ghosts.
- **Story anchors:** West Palm blackout, Palm Beach Atlantis, Protectorate governance, Treaty of Boca, Project ECHO exposure, Palm Beach Holocaust, Free Gold Coast Assembly. These anchors remain working canon and must be reconciled in the canon ledger.

## Production documentation
- [**Total Conversion Master Blueprint v1.0**](docs/MASTER_BLUEPRINT_v1.0.md) — consolidated vision, reuse inventory, world/story, systems, technical approach, QA, release and gates.
- [AI Autonomous Production Architecture](docs/AI_AUTONOMOUS_PRODUCTION.md) — agents, routing, task contracts, autonomy controls, Build Runner.
- [Technical Production Plan](docs/TECHNICAL_PRODUCTION_PLAN.md) — toolchain, repository, asset/world/campaign/build/test pipeline.
- [Canon Baseline](docs/CANON_BASELINE.md) — current canon snapshot and approval rules.
- [Roadmap and Initial Backlog](docs/ROADMAP_BACKLOG.md) — phases, first tickets, planning allocation.
- [Agent Operating Rules](.agents/AGENTS.md) — bounded task and acceptance rules.

## Existing project records
- [Original master blueprint](docs/MASTER_BLUEPRINT.md)
- [Canon ledger and unresolved decisions](docs/CANON.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [AI development model](docs/AI_AUTONOMOUS_DEVELOPMENT.md)
- [Original roadmap](docs/ROADMAP.md)
- [Architecture decisions](docs/DECISIONS.md)

The v1.0 documents are a consolidation/production expansion, not an automatic replacement of prior canon. Reconcile story anchors and timeline conflicts through decision records before treating the canon as locked.

## Production principles
1. Prove a vertical slice before expanding.
2. AI-first, human-accountable: agents research, draft, implement bounded tasks, run checks, and prepare PRs; humans approve canon, licensing, sensitive changes, merges, and releases.
3. Explicit task contracts, acceptance tests, and rollback.
4. Track asset origin, permissions, source, transformations, and distribution restrictions.
5. Treat engine claims as hypotheses; verify installed game/mod-tool versions.
6. Player progress is private; no user-to-user ranking.

## Current milestone
**Phase 0 — Technical discovery:** establish exact game/framework versions, validate asset/world/quest pipelines, prove campaign startup isolation, and stand up the AI build-and-test loop before scaling content.

## Legal and distribution
Do not redistribute proprietary game files or assets. Require explicit review of licenses, mod policies, third-party assets, and platform terms before release.