# Gold Coast Total Conversion

A production framework for a Cyberpunk 2077 total-conversion project set in a fictionalized South Florida / Gold Coast Corporate Republic.

> **Status:** pre-production planning. This repository does not yet contain a playable mod. Canon and REDengine implementation details marked TBD require validation.

## Vision
Build a story-rich, street-level Gold Coast experience using Cyberpunk 2077 Ultimate Edition as the gameplay foundation where legally and technically appropriate. Preserve proven base systems (combat, cyberware, vehicles, NPC behaviors, quest infrastructure) while developing original setting, characters, missions, dialogue, world presentation, and progression.

## Production planning set
- [Production blueprint & first vertical slice](docs/MASTER_BLUEPRINT.md)
- [Canon ledger and unresolved decisions](docs/CANON.md)
- [Technical architecture and toolchain](docs/TECHNICAL_ARCHITECTURE.md)
- [AI-assisted/autonomous production operating model](docs/AI_AUTONOMOUS_DEVELOPMENT.md)
- [Phased roadmap and gates](docs/ROADMAP.md)
- [Architecture decisions](docs/DECISIONS.md)

## Creative foundation (provisional)
- Rook: player protagonist with Corpo, Streetkid, and Nomad lifepaths.
- ECHO-9: reconstructed Elias Voss; identity, continuity, and immortality form a central thematic conflict.
- Campaign window: 2077–2085 (provisional).
- Regional anchors include West Palm blackout, Palm Beach Atlantis, Protectorate governance, Treaty of Boca, Project ECHO exposure, Palm Beach Holocaust, and Free Gold Coast Assembly.
- Power blocs under consideration: Arasaka, Militech, Kang Tao, Petrochem, Night Corp, plus regional institutions and factions to be canon-locked.
- A detailed, navigable street-level map should preserve recognizable real-world South Florida geography while fictionalizing and transforming it for the setting.

These are **working canon**, not a final immutable bible. District names/borders, faction roster, chronology, ECHO mechanics, endings, and precise map scale remain to be approved.

## Production principles
1. **Prove a vertical slice before expanding.** One district block, traversal loop, encounter, mission, dialogue branch, save/load, and end-to-end QA.
2. **AI-first, human-accountable.** Agents can research, draft, implement bounded tasks, run checks, and prepare PRs. Humans approve canon, licensing, security-sensitive changes, merges, and releases.
3. **Use explicit contracts.** Every task declares inputs, outputs, allowed files, acceptance tests, and rollback.
4. **Keep provenance.** Track asset origin, permissions, source, transformations, and distribution restrictions.
5. **Treat engine claims as hypotheses.** Verify each capability in the installed game/mod-tool versions before designing around it.
6. **No user-to-user ranking.** Progress and evaluation are private to each player's campaign.

## Start here
Read the master blueprint, then create the first feasibility spike and vertical-slice backlog. Do not scale content production until packaging, world streaming, quest-state persistence, and repeatable QA are demonstrated.

## Legal and distribution
This project must not redistribute proprietary game files or assets. Require explicit review of licenses, mod policies, third-party assets, and platform distribution terms before release.
