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

1. Paste [send-message-keys](../start/rob/send-message-keys.md) to Rob  
2. Run [DEMO-SCRIPT](../../lab/hermes/DEMO-SCRIPT.md) when scheduled  
3. After Wave 1 keys: fill [stack-map](../../data/stack-map.md); replace vendor stubs with read clients  
4. CI: ensure `validate.yml` lab pytest step is on `main` (needs `workflow` scope if push blocked)  

## Do not

- Connect production MCP writes  
- Use 178%/80% in ROI  
- Auto-clone `NEEDS_CONFIRMATION` templates  
- Automate review-deletion asks  

## Locked decisions

Hermes Desktop first · e-Boekhouden · three bol accounts · companion VPS deferred · ADRs 001–002.
