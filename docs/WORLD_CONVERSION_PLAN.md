# Gold Coast World Conversion Plan

## 1. Objective

Transform Cyberpunk 2077's Night City presentation into a fictionalized South Florida / Gold Coast region. Preferred approach: hybrid conversion—reuse and recompose existing environments, rebrand selected assets, reconstruct incompatible spaces, and add custom world sectors only after technical proof.

A full map replacement is a major REDengine engineering task. District renaming, texture swaps or map artwork alone do not constitute a new playable region.

## 2. District register (provisional labels)

| ID | Working district | Geographic inspiration | Intended identity | Initial strategy |
|---|---|---|---|---|
| GC-001 | The Crown | Palm Beach Island | Old money, estates, corporate elites | Luxury/corporate reuse + original landmarks |
| GC-002 | West Palm City | West Palm Beach | Civic center, commerce, street life | Downtown/commercial conversion; first slice |
| GC-003 | Silicon Coast | Boca Raton | Neural tech, research, corporate campus | Corporate/technology reconstruction |
| GC-004 | The Belt | Delray–Boynton | Working-class corridor, nightlife | Dense commercial/residential reuse |
| GC-005 | The Arc | Lake Worth–Riviera | Neighborhoods, culture, mixed-use streets | Residential/commercial reconstruction |
| GC-006 | The Frontier | Jupiter–Tequesta | Coastal frontier, military and settlements | Outskirts/coastal assets |
| GC-007 | Sugarlands | Belle Glade region | Agricultural-industrial exploitation | Industrial assets + original dressing |
| GC-008 | Lake Corridor | Lake Okeechobee region | Logistics, transport, industry | Industrial/road assets |
| GC-009 | Green Hell | Everglades | Wilderness, Nomads, dangerous exploration | Badlands vegetation/terrain + original ecology |
| GC-010 | Atlantis | Regional/offshore-industrial concept | Corporate expansion | Custom sector or staged world-space proof |
| GC-011 | The Abyss | Atlantic Ocean | Offshore facilities and secrets | Custom offshore sector / interiors |
| GC-012 | Skyports | Regional aviation infrastructure | Air mobility and elite access | Rooftop/aviation assets and custom traversal |

These are planning names. Reconcile them with earlier lore and the existing Palm Beach Atlantis historical anchor before canon lock. Do not conflate the Atlantis district concept with that historical event.

## 3. Geographic/world data model

Every record must have stable ID and canonical name; district ID and canon status; transform/coordinates and coordinate system; streaming sector and dependencies; traversal links and road/water connections; collision/navigation metadata; faction/corporate ownership; NPC/encounter spawn groups; interior/fast-travel links; quest/event hooks; asset references/provenance; performance budget and QA status.

Hierarchy:
~~~text
GOLD_COAST_WORLD
  REGION
    DISTRICT
      PLAYABLE_CELL
        LANDMARK / INTERIOR / ROAD / WATERWAY
        NPC_PLACEMENTS / ENCOUNTERS / QUEST_HOOKS
~~~

## 4. Asset reuse categories

A = direct reuse; B = rebrand/reconfigure; C = reconstruct; D = original development. Do not assume an asset is reusable solely because it looks suitable in a screenshot. Check resource dependencies, collision, LODs, materials, streaming, performance and redistribution rights.

## 5. Source-environment mapping hypotheses

- luxury/corporate districts → The Crown;
- downtown/commercial environments → West Palm City;
- corporate campuses → Silicon Coast;
- dense residential/commercial streets → The Belt and The Arc;
- outskirts/Badlands → The Frontier and Green Hell;
- industrial/logistics zones → Sugarlands and Lake Corridor;
- offshore and aviation areas → custom-sector feasibility studies.

These are discovery targets, not approved one-to-one conversions. Asset research must produce candidate resource IDs, preview evidence, dependencies, modification effort and rights status.

## 6. First district: West Palm City

The first playable district must prove recognizable Gold Coast visual identity, skyline/landmark composition, streets/traversal, road and vehicle navigation, one meaningful interior/hub, waterfront feature if feasible, signage/advertising, civilian and faction NPCs, one security encounter, one combat and one noncombat activity, one quest hook, streaming/collision/memory/frame-time validation.

## 7. District completion gate

A district is complete only when boundary, skyline/landscape identity, traversal, navigation, collision, population, faction presence, landmark, interior, activity, environmental storytelling, quest integration, streaming, performance and asset provenance are reviewed.

## 8. World pipeline

Reference research → asset catalog → reuse classification → concept approval → asset creation/reconstruction → import → placement → streaming/collision/navigation validation → NPC/encounter population → mission integration → performance test → district approval.

## 9. Technical risks

New landmass/world-space work may require more than existing mod tools expose through supported interfaces. Validate sector registration, world-node placement, streaming boundaries, navigation, spawn systems, map presentation and fast travel independently. If a full new map is not viable, preserve the hybrid plan and use staged/custom areas connected through the proven world.
