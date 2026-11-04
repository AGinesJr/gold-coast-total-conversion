# Gold Coast v2.4 — Full Campaign Graph Lock & Runtime Integration

**Status: Campaign graph lock candidate; not engine/runtime locked.**

This milestone represents 41 quest chains (26 main + 15 side), generic quest lifecycle and branching, 7 endings, district/event dialogue dispatch, scenario fixtures, and a REDengine adapter contract.

## Generated artifacts from the ChatGPT production session
- `Gold_Coast_Full_Campaign_Graph_v2_4.json` — canonical graph export (1,574 nodes / 1,901 edges)
- `Gold_Coast_Full_Campaign_Authoring_QA_v2_4.xlsx` — Nodes, Edges, Quest States, Event Pools, Scenarios sheets
- `Gold_Coast_Scenario_Test_Matrix_v2_4.json` — 313 scenario fixtures
- `gold_coast_redengine_adapter_prototype_v2_4.py` — EngineBridge test double and allowlisted command shim
- `Gold_Coast_v2_4_QA_Report.json` — static QA summary
- `Cyberpunk_Gold_Coast_Full_Campaign_Graph_Lock_Runtime_Integration_v2_4.docx` — production spec
- `Cyberpunk_Gold_Coast_v2_4_Full_Campaign_Graph_Lock_Bundle.zip` — package archive

## Graph design
- Choice branches: stealth/force/social; mercy/expose/profit.
- Lifepath branches: CORPO, STREETKID, NOMAD.
- Companion interruption branches: LUX, MARA, JACKSON; plus no-companion path.
- Quest states: LOCKED → AVAILABLE → ACTIVE → COMPLETED / FAILED; retry and replay paths.
- Endings: Crown Eternal, Southern Occupation, Silicon Paradise, Zero Humanity, Free Gold Coast, Sawgrass Exodus, Atlantic Ghost.
- 12 districts × AMBIENT / COMBAT / REACTIVE event pools (36 pools; 108 VO slots).

## QA truth
Static QA currently reports **FAIL** due to 164 unreachable nodes. Edge execution, condition truth-value coverage, choice execution, ending execution, and in-game smoke tests are **NOT RUN**. Dialogue and event lines remain placeholders pending source reconciliation.

The v2.1 dialogue source was not available in the generation workspace, so verbatim cinematic import is not claimed. The adapter is a Python test double, not REDengine API integration.

## Lock gates
1. Import v2.1 scenes with provenance and stable IDs.
2. Repair unreachable nodes and validate all graph paths.
3. Replace generic choices/consequences with quest-authored state changes.
4. Run lifepath × companion × quest-state tests and full edge/choice/condition coverage.
5. Replace placeholder VO; finish localization and actor mapping.
6. Bind verified mod-framework APIs and run in-game smoke tests.
