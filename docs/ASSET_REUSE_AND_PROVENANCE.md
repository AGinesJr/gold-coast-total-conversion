# Gold Coast Asset Reuse and Provenance Plan

## 1. Objective

Maximize reuse of Cyberpunk 2077's existing assets and systems while creating an original Gold Coast identity. Asset reuse is both a technical decision and a rights decision; record both.

## 2. Reuse inventory

### Player and gameplay foundations
Investigate reuse of first-person movement, interaction, camera, combat, stealth, hacking, cyberware, attributes/perks, progression, inventory, crafting, loot, vendors, consumables, weapon types, damage, enemy AI, police/security response, wanted behavior, vehicle handling, ownership/summoning, photo mode and save infrastructure.

### Cyberware and weapons
Potential foundations include Kiroshi optics, cyberdecks, quickhacks, Sandevistan, Berserk, Mantis Blades, Gorilla Arms, Monowire, Projectile Launch System, power/tech/smart weapons, attachments, grenades, healing and combat consumables. Gold Coast-specific names, balance, descriptions, distribution and vendors are separate authoring work.

### Vehicles
Potential reuse includes sports/luxury cars, sedans, motorcycles, off-road and armored vehicles, corporate/security vehicles, vehicle interiors, damage, driving physics, combat, ownership and summon systems. Gold Coast needs regional distribution, branding/liveries where feasible, dealerships, racing content and encounter placement.

### NPCs, enemies and animation
Potential archetypes: civilians, corporate staff/security, gang members, police, military, Nomads, vendors, fixers, ripperdocs, scientists, engineers, bodyguards, robots, drones, turrets and animals. Existing locomotion, combat, interaction, facial, scene, takedown, vehicle entry/exit and death animations may be reusable. New identities, outfits, schedules, placements, faction logic and dialogue are required.

### Environments
Potential source categories: downtown/high-rise, luxury apartments, corporate plazas, dense commercial streets, residential blocks, industrial plants, Badlands, waterfront, rooftops, garages, labs, clubs, markets, roads, vegetation and interiors. Select resources by actual geometry and dependencies, not only visual similarity.

## 3. Reuse classification

- A — Direct reuse.
- B — Rebrand/reconfigure.
- C — Reconstruct.
- D — Original development.

Each candidate record must state Gold Coast asset ID/intended use; original resource identifier (reference only); category; dependencies/variants; material/texture/LOD/collision/streaming concerns; modifications required; in-game evidence; redistribution status/legal review; owner and status.

## 4. New Gold Coast asset categories

Original or properly licensed content may be required for regional skyline landmarks; Imperial Tower and Project ECHO spaces; Palm Beach estates and waterfront architecture; civic buildings; neural research campus; agricultural/logistics facilities; Florida-inspired residential architecture; marinas, yacht terminals, resorts, ports and offshore installations; aviation/skyports; signage, road signs, district markers, corporate logos and faction graffiti; map art, title screen, loading screens, billboards and UI graphics; original clothing/decals, props, vegetation, terrain dressing and mission props; original radio, dialogue, music and sound effects.

## 5. Asset pipeline

Reference → concept → human visual approval → original/authorized 2D or 3D creation → materials/textures → collision/rigging/LODs as needed → import → in-game validation → optimization → provenance review → approved manifest.

AI-generated assets require inspection for artifacts, topology, UVs, materials, scale, collision, visual consistency, technical cleanup and rights.

## 6. Provenance record

~~~yaml
asset_id: GC_ASSET_0001
name: Gold Coast Corporate Billboard
asset_type: texture
origin: original
creator: Gold Coast Production
source_files:
  - assets/original/billboard/
ai_generated: true
license_status: review_required
base_game_dependencies: []
redistribution: permitted_after_review
validation_status: pending
~~~

For proprietary base-game assets, store resource identifiers and metadata where permitted, not extracted game archives or repackaged payloads in the public repository.

## 7. Distribution safeguards

Require users to own Cyberpunk 2077. Do not bundle the game or proprietary archives/models/textures/audio. Distribute only original or properly licensed assets. Track third-party licenses and attribution. Use original or authorized voice/music/sound assets. Review CDPR EULA, fan-content guidelines, mod policies and host-platform terms before release. Do not imply official CDPR endorsement.

This is a production policy, not legal advice.
