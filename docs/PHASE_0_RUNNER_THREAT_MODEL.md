# Phase 0 — Windows Build Runner Threat Model (Draft)

## Assets to protect
- Owner's normal Cyberpunk install, saves and unrelated mods.
- GitHub credentials, API keys, model-provider secrets and private data.
- Gold Coast working tree, generated artifacts and provenance records.
- Game stability, reproducibility, and project integrity.

## Trust boundaries
Cloud agent/model output is untrusted input. GitHub task contracts and reviewed code are the control plane. The Windows runner is a separate execution boundary and must not accept arbitrary model-generated shell commands.

## Minimum runner controls
1. Dedicated Windows account or isolated VM/workspace; dedicated Gold Coast game installation/profile and separate saves.
2. Runner accepts only signed/allowlisted task IDs and approved commit SHAs—not free-form command strings.
3. Fixed command registry with parameter validation; no arbitrary PowerShell, cmd, Python, or executable path supplied by an agent.
4. Restrict filesystem writes to approved staging, test install and artifact directories; normal game install read-only.
5. Secrets stored in Windows Credential Manager/CI secret store; never in repo, logs, task YAML or screenshots.
6. Log task ID, requester, commit SHA, tool/game versions, commands, start/end, exit codes and artifact checksums.
7. Network egress allowlist; no downloading unknown binaries during a runtime job.
8. Time, CPU, memory, disk and retry limits; cancel/kill process tree on timeout.
9. Reset/restore test profile and saves before each run; snapshot/rollback package and deployment state.
10. Human approval required for game install changes, destructive cleanup, save migration, release/publish and any scope expansion.

## Runner API contract (proposed)
- Input: task ID, approved commit SHA, test profile ID, requested allowlisted job, budget.
- Output: run ID, command log, toolchain lock snapshot, test results, screenshots/video if approved, crash/log bundle, artifact manifest and SHA-256 checksums, limitations.
- Failure modes: reject unknown task, commit, tool version, command, path, profile or over-budget request; fail closed.

## Threats and mitigations
| Threat | Control |
|---|---|
| Prompt injection in docs/mod pages/assets | Treat retrieved content as data; no instruction execution; source and hash record |
| Malicious task changes | JSON Schema + path allowlist + reviewer + branch protections |
| Supply-chain compromise | Pin releases/checksums; verify signatures where available; dependency inventory |
| Accidental base-game overwrite | Separate install; read-only normal install; constrained staging paths |
| Secret leakage | Secret store, redaction, least privilege, no secrets in artifacts |
| Agent loop/cost runaway | Per-task budget, max retries/time, escalation rather than autonomous retry |
| False runtime pass | Evidence-based acceptance; runner logs/screenshots and human review |

**Status:** design draft. No runner service or game deployment is enabled by this document.
