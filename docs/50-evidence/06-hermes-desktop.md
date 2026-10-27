# Hermes Desktop — capability notes (WiseQ)

*Verified on builder Windows machine 2026-10-27. Official docs: [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop).*

## What was verified on this machine

| Check | Result |
| :--- | :--- |
| Hermes Agent version | **v0.22.5** (2026.9.24) · stable · local `bf0203a794a0` |
| Install path | `C:\Users\Ivan\AppData\Local\hermes\` (git install) |
| Python | 3.14.9 · OpenAI SDK 2.24.0 |
| `hermes doctor` | Green on security/MCP/Python/config; optional Telegram/Discord not installed |
| Config | `%LOCALAPPDATA%\hermes\config.yaml` (v51) · `.env` present |
| Default profile | `default` · model `anthropic/claude-opus-4.6` · gateway **stopped** |
| Desktop launcher | `hermes desktop` builds/launches Electron app; `hermes-setup.exe` present; desktop-build-stamp `builtAt` 2026-09-23 |
| Skills system | `hermes skills` supports trust/install/list; repo-local `./.hermes/skills` and `./.agents/skills` when project trusted |
| YOLO | CLI `--yolo` and Desktop per-session YOLO (bypasses dangerous-command approvals) — **must stay off for wiseq-lab** |

## Architecture relevant to Rob

Hermes Desktop is **not a separate product**. It uses the same agent core as CLI/gateway: same config, API keys, sessions, skills, memory. Work started in Desktop resumes in CLI and vice versa.

Interfaces that share state:

1. **Desktop app** (primary for Rob)
2. **CLI / TUI** (`hermes`, `hermes --tui`)
3. **Webapp** via gateway (`hermes webapp`) — loopback by default; treat like host access

## Profile isolation for WiseQ

```text
hermes --profile wiseq-lab doctor
```

Creates an isolated profile under the Hermes home (Windows: under `%LOCALAPPDATA%\hermes\profiles\wiseq-lab\` when using profiles). **Never** mix WiseQ skills/memory with a personal default profile.

Workspace for lab work:

```text
hermes desktop --cwd "C:\Users\Ivan\Documents\wiseq-ai-onboarding\lab"
```

Or open Desktop and set project/workspace to `lab/`.

## Skills packing for Milestone 1

Repo skills live in [`lab/hermes/skills/`](../../lab/hermes/skills/). Install path for Desktop:

1. Trust this repo: `hermes skills trust` from the onboarding repo root (or copy skills into the profile skills dir).
2. Prefer **YOLO off**; consequential lab “commits” require explicit approval language in skills.
3. Seed memory from [`lab/hermes/memory/`](../../lab/hermes/memory/) only — synthetic + public extracts.

## Scheduled jobs / always-on honesty

- Cron/schedules run through the Hermes gateway process.
- If Desktop/gateway is **stopped** (current default profile state on this machine: gateway stopped), scheduled digests **do not run**.
- Milestone 1 = **interactive** delegation while Desktop is open.
- Always-on companion (WiseQ VPS Hermes gateway, doc 24) remains **Phase 4+**.

## Security boundaries for wiseq-lab

| Rule | Why |
| :--- | :--- |
| YOLO off | Prevents silent dangerous host commands |
| No production MCP tokens in Milestone 1 | Lab uses fixture adapters only |
| Webapp loopback only | Remote Webapp = full host agent access |
| Profile backup | Export/backup `wiseq-lab` profile dir + `memories/` periodically (laptop ownership) |
| Simulated tag | All lab tool outputs must say `simulated=true` until vendor adapters exist |

## Backup / restore (laptop ownership)

Desktop state lives on Rob’s machine. Continuity plan:

1. Weekly zip of profile dir + `memories/` + relevant `sessions/` into encrypted backup (Bitwarden attachment or Rob’s backup drive).
2. Document restore: reinstall Hermes Desktop → restore profile folder → `hermes --profile wiseq-lab doctor`.
3. Skills that belong to WiseQ also live in git (`lab/hermes/`) so they survive laptop loss.

## Not verified in this pass

- Interactive GUI click-through of Desktop chat with wiseq-lab skills (requires Rob’s model key session).
- Creating production `wiseq` profile with live MCP.
- Remote backend connection from Desktop to a VPS gateway.

## Sources

- Local: `hermes --version`, `hermes doctor`, `hermes desktop --help`, `hermes skills --help` (2026-10-27)
- Docs: https://hermes-agent.nousresearch.com/docs/user-guide/desktop
