# Handoff — continue without re-research

## Branch

`feature/wiseq-test-lab-assistant` (from `main` after Mastersheet ingest + Oct-27 audit commit).

## What exists

| Path | Role |
| :--- | :--- |
| `docs/50-evidence/` | Phase 0 evidence pack + Hermes Desktop notes |
| `docs/10-client/01-complete-dossier.md` | Complete client dossier |
| `docs/start/rob/` | Rob pack (case, open asks, read-only guide) |
| `docs/60-governance/03-critical-audit-2026-10-27.md` | Critical audit response |
| `lab/` | Synthetic test lab, pytest scenarios A–C, Hermes skills |
| `data/client/` | Client SoT (publication-gated raw manual) |

## Implementation roadmap

| Phase | Deliverable | Status |
| :--- | :--- | :--- |
| 0 | Audit pack + Desktop notes + Desktop-first | Done |
| 1 | `lab/` fixtures + adapters + pytest | Done |
| 2 | Milestone 1 Hermes skills + acceptance | Done (pack ready) |
| 3 | Exp A–C register + keep/extend/replace | Done |
| 4 | Rob demo → capability matrix fill → read-only tokens | Next |
| 5 | Controlled writes after Gates 1–2 | Later |
| 6 | Always-on companion VPS for cron | Later |

```text
EAN registry → school / bundles / purchase
Desktop interactive → optional always-on companion
Lab green → vendor sandbox → prod read → draft → write
```

## Commands

```bash
python scripts/validate_repo.py
cd lab && pip install -e ".[dev]" && pytest -q
```

Hermes Desktop:

```text
hermes --profile wiseq-lab doctor
hermes desktop --cwd <repo>/lab
# trust repo skills; YOLO off
```

## Do next

1. Send Rob [Open asks](../start/rob/open-asks.md) + [Read-only guide](../start/rob/read-only-access.md)  
2. Offline prep from [preparation catalog](01-preparation-catalog.md) §B  
3. Demo Rob: three lab scenarios + digest skill  
4. After keys: fill stack-map capability matrix from live **read** smoke  
5. Experiments D–E only if prioritized  

## Do not

- Connect production MCP  
- Use 178%/80% in ROI  
- Auto-clone `NEEDS_CONFIRMATION` templates  
- Automate review-deletion asks  
- Edit the Cursor plan file as a deliverable  

## Locked decisions

Hermes Desktop first · synthetic-only Milestone 1 · e-Boekhouden · three bol accounts · always-on VPS companion deferred.
