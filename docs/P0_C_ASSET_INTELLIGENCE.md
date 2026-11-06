# P0-C — Asset Intelligence & Provenance

## Purpose
Create a searchable inventory of resources that Gold Coast may reference, reuse in-game, recreate, license, or exclude. Catalog records are **metadata only**. Never commit extracted Cyberpunk game assets, proprietary textures, meshes, audio, or other payloads.

## Record lifecycle
1. Create a YAML record using `schemas/asset-catalog-record.schema.json`.
2. Assign a unique stable `asset_id`; do not use a filename as identity if it may change.
3. Record a source category, source URI/path, provenance, rights status, and intended reuse decision.
4. For base-game resources, set `license_status: base_game_no_redistribution` and `reuse_decision: reuse_in_game_only` (or `exclude`). Catalog a reference/path/hash only; do not store the resource bytes.
5. For original resources, retain author/tool/source project information and mark rights as approved only when the creator and license are documented.
6. For third-party resources, record the upstream URL, author, license/version, attribution requirements, and modification status. Unknown terms stay `review_required` or `unknown`.
7. Verification levels: `unverified` (record exists), `metadata_verified` (source and metadata checked), `in_game_verified` (loaded/tested with evidence). Never promote based on a successful static validation alone.

## Indexing
Run from the repository root:
```powershell
python scripts/build_asset_index.py
```
Optional:
```powershell
python scripts/build_asset_index.py --catalog catalogs --out artifacts/asset-index.json
```
The index contains only catalog metadata and record paths. It validates each record against the JSON Schema, enforces base-game no-redistribution, and rejects duplicate IDs. Generated indexes are reproducible in content except for the UTC generation timestamp.

## Candidate resource families
- World/building/prop references by region and district
- Mesh, texture, material, and appearance references
- NPC/vehicle/animation references
- Audio/dialogue references
- TweakDB and world-node identifiers (where lawful and technically appropriate)
- Original Gold Coast assets and approved third-party assets

## Provenance and rights gate
Before any resource is included in a distributable mod:
- identify its creator/source;
- document permission/license and attribution;
- confirm derivative/modification rights;
- check whether redistribution is permitted;
- exclude proprietary base-game bytes from the repository and release;
- record an explicit reuse decision and reviewer.

## P0-C exit criteria
- [ ] Schema validation succeeds for every catalog record.
- [ ] Duplicate asset IDs fail indexing.
- [ ] Base-game records cannot be labeled redistributable/approved.
- [ ] Unknown provenance/license remains visibly unresolved.
- [ ] Index output contains metadata only, no asset payload.
- [ ] A sample index is generated and checked into a PR only if it is small, useful, and contains no private machine paths.
- [ ] P0-D resource packaging is selected only after P0-B game/framework evidence is complete.
