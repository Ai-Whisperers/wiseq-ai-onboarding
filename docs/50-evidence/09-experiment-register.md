# Experiment register

| ID | Hypothesis | Dataset | Baseline | Alternatives | Result (2026-10-27) | Decision |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A** School pipeline | Synthetic path can draft offer→invoice→shipment with idempotency + approval | `fixtures/mailbox/` | Manual copy-paste (simulated elapsed N/A offline) | Rules fixture vs (later) AI extract | **Pass** — pytest A green; catalog/sample escalates; duplicates blocked | **Extend** e-Boekhouden with Hermes drafts |
| **B** Catalog integrity | Spine resolves; bad templates refused | Spine CSV + templates | Manual ChannelDock clone | Registry checks | **Pass** — 25 bundles resolve; NEEDS_CONFIRMATION refused; EAN gaps flagged | **Extend** registry; **Keep** CD bundles |
| **C** Shipping UE | Typed tariffs match golden; uplift not quotable | `tariffs_typed.json` | Spreadsheet narrative | Typed engine | **Pass** — all golden quotes match; uplift blocked | **Improve** Mastersheet→typed; never ROI on uplift |

## Deferred

| ID | Status |
| :--- | :--- |
| D Inventory/pricing | Registered for next wave — FiveX +10% fixtures present, no auto-write |
| E CS/reviews | Policy pack only |
| F–H | Not started |

## How to re-run

```bash
cd lab && pytest -q
```
