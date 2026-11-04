# Technical Proof of Concept and Windows Build Runner

## 1. Purpose

Prove critical REDengine/modding assumptions before committing to full-map or full-campaign production. Cloud agents can write code and data, but game runtime validation requires a controlled Windows environment.

## 2. Version-lock baseline

Record Cyberpunk executable/build and Ultimate Edition/DLC state; REDmod; WolvenKit; RED4ext; ArchiveXL; TweakXL; redscript; Cyber Engine Tweaks; Codeware; World Builder; RedHotTools; Python; Blender; build scripts; operating system.

Do not assume listed tools are mutually compatible or support the installed game build. Validate each dependency, pin known-good versions, and record source, documentation and test date.

Suggested lock files:
~~~text
config/game-version.lock
config/frameworks.lock
config/toolchain.lock
config/asset-schema.lock
config/agent-models.lock
~~~

## 3. Five mandatory proof spikes

### POC-1: Original asset pipeline
Select an original Gold Coast asset; import through chosen workflow; package/install to isolated test game; verify resource, material references, collision/LODs if relevant; capture screenshot/log and reproducible steps.

### POC-2: World editing
Create/modify one test cell or sector; verify registration, streaming, placement, collision, navigation, spawn behavior, map access and memory; document unsupported operations and workarounds.

### POC-3: Campaign bootstrap
Create Gold Coast campaign entry point; initialize Rook and selected lifepath; set initial quest/world facts; prevent original V campaign from taking control; test new game, restart, load, death and save isolation.

### POC-4: Quest/runtime integration
Implement one quest with dialogue, objectives, branch consequence, reward, failure, retry, checkpoint and save/load. Existing v2.4 Python EngineBridge is a test double until a real game API adapter is proven. Test in-game behavior and capture evidence.

### POC-5: Autonomous build loop
Orchestrator creates bounded task; agent works on branch; runs static checks and unit tests; PR is created; Windows runner checks out exact commit; runner builds/deploys to isolated game; returns logs, screenshots and artifact manifest; human reviews evidence.

## 4. Build Runner architecture

~~~text
AI Orchestrator
  -> GitHub branch/commit
  -> authenticated Build Runner request
  -> checkout exact commit
  -> version/dependency verification
  -> validators and asset build
  -> WolvenKit/REDmod packaging as applicable
  -> isolated test installation
  -> launch/smoke test
  -> logs/screenshots/crash report
  -> immutable artifact + checksum
  -> orchestrator and PR evidence
~~~

The runner is a Windows workstation service or controlled agent, not an assumed cloud-model capability. The available workstation has 40 GB RAM, RTX 3070 laptop GPU with 8 GB VRAM and Intel i7; benchmark actual workloads before setting targets.

## 5. Security controls

Use a dedicated Windows account or isolated workspace; separate test installation and test saves; restrict writes to approved staging paths; expose allowlisted build/test commands; never pass arbitrary shell commands from an untrusted model; store credentials in OS secret storage or CI secrets, never Git; record commands, commits, tool versions, timestamps and outputs; require human approval for destructive actions and releases; provide rollback and clean test-profile reset.

## 6. CI responsibilities

Cloud CI can run YAML/JSON schema checks; stable ID/reference validation; dialogue/localization checks; quest graph reachability; scenario fixture generation/execution where engine-independent; Python tests/static analysis; asset manifest/provenance checks; dependency/version-lock checks; package manifest/checksum generation.

Windows runner is required for game-specific resource compilation; runtime mod loading; world streaming/collision/navigation; game launch and in-game quest smoke tests; performance and crash testing.

## 7. Evidence requirements

A proof is not passed by assertion. Attach commit SHA, command log, tool/game versions, output artifact, test report, screenshots/video where useful, known limitations and reviewer sign-off.
