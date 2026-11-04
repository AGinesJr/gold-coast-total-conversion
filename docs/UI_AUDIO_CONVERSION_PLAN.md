# Gold Coast UI, Audio and Presentation Conversion Plan

## 1. Goal

Make the player's experience consistently identify as Gold Coast. Preserve functional base UI systems where practical, but replace visible narrative, geographic and branding references that conflict with Rook's campaign.

Full replacement of every native interface element may not be possible through supported mod APIs. Track limitations explicitly rather than promising total replacement before testing.

## 2. UI conversion matrix

| Interface | Gold Coast treatment | Validation |
|---|---|---|
| Main menu | Gold Coast title and visual identity | Launch/restart test |
| New Game | Gold Coast campaign entry | Does not initialize V's campaign |
| Lifepath selection | Corpo / Streetkid / Nomad | All paths initialize correctly |
| Loading screens | Original Gold Coast art/lore | No broken assets or text |
| World map | Gold Coast districts/locations | Labels and travel points match world |
| Journal | Gold Coast campaign and quest presentation | Objectives/state persist |
| Character/profile | Rook identity and progression | No V identity conflict |
| Phone/messages | Gold Coast contacts and story messages | Contact and message triggers |
| Inventory | Gold Coast descriptions and item identity | Items remain functional |
| Cyberware | Gold Coast descriptions and progression | Installation/upgrade behavior |
| Vehicle interface | Gold Coast vehicle identity | Ownership/summon behavior |
| Database/lore | Gold Coast setting, people and factions | Entries resolve to canon IDs |
| Pause/settings | Gold Coast branding where feasible | Native settings remain accessible |
| Quest HUD | Gold Coast objectives and mission names | Branch/objective state correct |
| Radio menu | Gold Coast station identity | Audio playback and station selection |

## 3. Identity cleanup

Audit player-facing content for references to V, Johnny Silverhand, the Relic, Night City district names, original fixers, original campaign mission names and original corporate story prompts. Suppress or replace only where technically safe. Do not globally delete shared resources that other systems depend on.

## 4. Audio plan

Audio categories:
- original Gold Coast radio station identities;
- original or properly licensed music;
- Rook and ECHO-9 dialogue;
- companion and faction dialogue;
- ambient district barks;
- combat barks;
- reactive quest/world dialogue;
- environmental soundscapes for coast, urban districts, industrial sites and wilderness;
- UI and mission feedback sounds;
- localization and subtitle metadata.

Existing audio playback and dialogue presentation may be reusable. Original voice, music and sound recordings require their own rights and provenance records.

## 5. Dialogue and VO pipeline

Each line should include stable line ID, speaker ID, text, scene/quest context, trigger conditions, localization key, actor/voice assignment, recording status, subtitle constraints, audio asset reference, rights/provenance, and QA status.

Use synthetic voice for prototypes only unless the provider terms, voice rights and intended release use have been reviewed. Do not clone a real actor or public figure without appropriate authorization.

## 6. Presentation acceptance

- Gold Coast title and New Game path are clear.
- Lifepath selection works.
- Gold Coast map labels correspond to actual accessible locations.
- Journal, quest HUD and dialogue reflect current quest state.
- No major original-campaign narrative references appear in Gold Coast missions.
- Subtitles, fonts and UI fit supported resolutions.
- Radio and dialogue assets load reliably.
- Missing optional audio has a safe fallback.
- All included assets have provenance and distribution approval.
