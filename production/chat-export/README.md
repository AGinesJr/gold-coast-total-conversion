# Gold Coast Chat Production Export (Versions 1.0–2.4)

This directory indexes the deliverables produced during the Gold Coast production-planning conversation. The prior v1.0 blueprint was merged in PR #1. This change adds a consolidated index and v2.1–v2.4 technical narrative specifications and manifests.

## Conversation deliverable inventory

### Narrative / quest production
- Cyberpunk_Gold_Coast_Quest_Design_Document_v1.docx
- Cyberpunk_Gold_Coast_Quest_Bible_Production_Package_v1_1.docx
- Cyberpunk_Gold_Coast_Mission_Scripting_Package_v2_0.docx
- Cyberpunk_Gold_Coast_Dialogue_Database_v2_1.docx

### Dialogue compiler (v2.2–v2.3)
- Gold_Coast_Dialogue_Graph_v2_2.json
- Gold_Coast_Localization_VO_v2_2.csv
- Gold_Coast_VO_Localization_Sheets_v2_2.xlsx
- Gold_Coast_Dialogue_Validation_Report_v2_2.txt
- Cyberpunk_Gold_Coast_Complete_Narrative_Graph_Compiler_v2_3.docx
- Gold_Coast_Narrative_Graph_Compiler_v2_3.json
- Gold_Coast_Graph_Authoring_and_QA_v2_3.xlsx
- gold_coast_dialogue_compiler_v2_3.py
- Gold_Coast_Graph_Validation_Report_v2_3.json/.txt

### Campaign graph/runtime (v2.4)
- Cyberpunk_Gold_Coast_Full_Campaign_Graph_Lock_Runtime_Integration_v2_4.docx
- Gold_Coast_Full_Campaign_Graph_v2_4.json
- Gold_Coast_Full_Campaign_Authoring_QA_v2_4.xlsx
- Gold_Coast_Scenario_Test_Matrix_v2_4.json
- gold_coast_redengine_adapter_prototype_v2_4.py
- Gold_Coast_v2_4_QA_Report.json

## Important accuracy notes
- v2.2's 3,198 records are generated systemic placeholders/variants, not final exhaustive recorded dialogue.
- v2.3 is a graph/compiler scaffold; runtime branch coverage and REDengine execution were not established.
- v2.4 is a campaign graph candidate. Its QA reported 164 unreachable nodes; edge/condition/choice/ending runtime coverage and in-game smoke tests are NOT RUN.
- v2.1 source import into v2.4 remains pending reconciliation; the current v2.4 briefings explicitly say source import pending.
- This repository must not contain proprietary Cyberpunk 2077 game assets or extracted REDengine files.

See [v2.4 campaign lock status](V2_4_CAMPAIGN_GRAPH_LOCK_STATUS.md) and [manifest](ARTIFACT_MANIFEST.md).