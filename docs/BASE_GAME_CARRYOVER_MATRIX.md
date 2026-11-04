# Base-Game Carryover Matrix

This document separates reusable Cyberpunk 2077 foundations from Gold Coast-specific implementation. “Reusable” means a candidate for technical validation, not a guarantee that a resource can be modified or redistributed.

## 1. Player and core RPG systems

| Base-game capability | Carryover plan | Gold Coast work |
|---|---|---|
| First-person movement/camera | Retain | Test in transformed spaces |
| Interaction framework | Retain | New interaction targets and prompts |
| Character creation/customization | Reuse where possible | Rook identity, appearance, lifepath presentation |
| Attributes/perks | Reuse/rebalance | Gold Coast progression balance |
| XP/level progression | Reuse/rebalance | Quest rewards and progression pacing |
| Inventory/equipment | Retain | New item identities and loot tables |
| Clothing/appearance | Retain | Regional outfits, factions, corporate uniforms |
| Crafting/upgrading | Retain where suitable | New recipes/material economy if needed |
| Vendors/economy | Reuse framework | Regional vendors, prices, rewards and services |
| Journal/quest tracking | Reuse framework | Gold Coast journal and mission presentation |
| Save/load | Reuse cautiously | Campaign isolation, migration, recovery |

## 2. Combat, weapons and cyberware

| Base-game capability/assets | Carryover plan | Gold Coast work |
|---|---|---|
| Firearms and damage | Retain | Balance, distribution, naming/descriptions |
| Power / Tech / Smart weapon classes | Retain | Corporate/faction equipment identity |
| Weapon attachments | Retain | Regional availability and balance |
| Melee combat | Retain | Enemy archetypes and encounter tuning |
| Stealth/takedowns | Retain | Infiltration missions and AI tuning |
| Quickhacking | Retain | Story-specific hack targets and objectives |
| Cyberdecks | Retain | Gold Coast equipment descriptions/progression |
| Sandevistan | Retain | Availability and balance |
| Berserk | Retain | Availability and balance |
| Kiroshi optics | Retain | Investigation and surveillance content |
| Mantis Blades | Retain | Loot/vendor/faction placement |
| Gorilla Arms | Retain | Combat and activity integration |
| Monowire | Retain | Combat/infiltration integration |
| Projectile Launch System | Retain | Balance and equipment distribution |
| Ripperdocs | Reuse framework | Gold Coast NPCs, interiors and inventories |
| Grenades/consumables | Retain | Regional loot and vendor tables |
| Enemy AI/damage/status | Retain | New factions, archetypes and encounter setups |

## 3. Vehicles and traversal

Candidate carryover: cars, motorcycles, luxury vehicles, sedans, sports cars, off-road vehicles, armored/corporate/security vehicles, vehicle interiors, driving physics, damage, vehicle combat, vehicle ownership/summoning, traffic and navigation primitives.

New work: regional vehicle distribution, liveries/branding where supported, dealerships, garages, street races, off-road routes, faction patrols, transport contracts, vehicle spawn points and Gold Coast road network. Do not assume new aircraft or boat gameplay is available just because skyports/marinas exist in the setting; prototype the relevant vehicle classes separately.

## 4. NPCs, enemies and animation

Potential reusable archetypes: civilians, corporate staff, corporate security, gang members, police, military, Nomads, vendors, fixers, ripperdocs, scientists, engineers, bodyguards, robots, drones, turrets and animals.

Potential animation reuse: locomotion, idle, talking, smoking, drinking, eating, working, combat, shooting, reloading, melee, death, interaction, takedowns, facial animation, scene choreography and vehicle entry/exit.

New work: Gold Coast appearance assignments, names, schedules, district placements, faction ownership, hostility, dialogue, mission behaviors, companion relationships and encounter composition.

## 5. World/environment assets

Candidate categories: high-rise buildings, luxury apartments, corporate plazas, residential blocks, commercial streets, factories, refineries, industrial logistics, Badlands terrain, vegetation, waterfronts, roads, rooftops, garages, labs, clubs, markets, interiors, lighting, weather and environmental effects.

| Gold Coast need | Likely approach |
|---|---|
| Corporate towers/offices | A/B, with original landmark work |
| Luxury estates | C/D |
| Civic buildings | B/C/D |
| Neural research campus | A/C/D |
| Industrial refineries/logistics | A/B/C |
| Florida-style residential architecture | C/D |
| Waterfront/marina/yacht terminal | C/D |
| Everglades ecology | C/D |
| Offshore facilities | C/D |
| Skyports/aviation spaces | C/D |
| District signs/road signs | B/D |
| Corporate ads/faction graffiti | B/D |
| Gold Coast map/loading/title art | D |

## 6. UI, audio and presentation

Potential framework reuse: main menu, pause menu, map, journal, inventory, cyberware, character, phone/messages, contacts, vendor UI, quest HUD, subtitles, radio playback, photo mode and loading presentation.

New work: Gold Coast title/menu identity; Rook/lifepath presentation; regional map and labels; district database; journal and quest text; phone contacts/messages; Gold Coast corporate/faction logos; loading screens; radio station identity; original or licensed music, dialogue, barks, sound effects and localization.

## 7. Reuse decision record

For every candidate, record:
- game resource identifier (reference only);
- intended Gold Coast use;
- A/B/C/D classification;
- dependencies and variants;
- technical validation status;
- performance/streaming/collision concerns;
- modifications required;
- license and redistribution status;
- evidence and reviewer.

Do not include proprietary base-game resource payloads in the public repository or downloadable mod unless explicit permission allows it.
