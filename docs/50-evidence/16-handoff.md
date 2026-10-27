# Handoff — continue without re-research

## Branch

`main` (PR #14 merged). Offline prep pack added after merge.

## What exists

| Path | Role |
| :--- | :--- |
| `docs/50-evidence/` | Phase 0 evidence + checklists |
| `docs/10-client/01-complete-dossier.md` | Complete client dossier |
| `docs/start/rob/` | Case, open asks, read-only guide, **send-message-keys** |
| `docs/adr/` | Desktop-first + e-Boekhouden |
| `lab/` | Scenarios A–C, ~32 school goldens, vendor **stubs**, Hermes skills + demo script |
| `data/client/` | Client SoT (publication-gated raw manual) |

## Implementation roadmap

| Phase | Deliverable | Status |
| :--- | :--- | :--- |
| 0–3 | Audit, lab A–C, Desktop skills, docs restructure | Done |
| 3b | Offline prep (checklists, goldens, ADR, stubs, demo script) | Done |
| 4 | **Send Rob keys message** → Desktop demo → capability matrix | **Next (human)** |
| 5 | Controlled writes after Gates 1–2 | Later |
| 6 | Always-on companion VPS for cron | Later |

## Do next (human / after keys)

1. WhatsApp Rob: [send-message-keys](../start/rob/send-message-keys.md) (points him at [cred template](../start/rob/whatsapp-cred-template.md))  
2. When keys arrive: follow [IVAN-RECEIVE-WHATSAPP](../start/rob/IVAN-RECEIVE-WHATSAPP.md) → vault → smoke  
3. Run [DEMO-SCRIPT](../../lab/hermes/DEMO-SCRIPT.md) when scheduled  
4. Fill [stack-map](../../data/stack-map.md); replace vendor stubs with read clients  
5. CI lab pytest: [CI-WORKFLOW-FOLLOWUP](../_internal/CI-WORKFLOW-FOLLOWUP.md) when token has `workflow` scope  

## Do not

- Connect production MCP writes  
- Use 178%/80% in ROI  
- Auto-clone `NEEDS_CONFIRMATION` templates  
- Automate review-deletion asks  

## Locked decisions

Hermes Desktop first · e-Boekhouden · three bol accounts · companion VPS deferred · ADRs 001–002.
