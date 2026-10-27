# WiseQ lab memory seed (synthetic)

Profile: `wiseq-lab`
Mode: **simulated only** — never claim production actions occurred.

## Facts

- Bookkeeping: **e-Boekhouden** (not Exact).
- Bol accounts: WiseQ NL, WiseQ Electronics, WiseQ België (phasing_out).
- ChannelDock has native bundles; 300-series inbound must book as bundles.
- FiveX +10% at stock ≤10: **recommend only** in lab.
- Reviews: bol-first; never automate rating deletion requests.
- Brand: `#26b5b7` / `#1648ad`.
- BE LVB uplift 80% vs 178%: **do not forecast**.
- Shipping templates with validation_status ≠ OK: **refuse clone**.

## Workspace

Lab root contains fixtures, scenarios, and pytest. Prefer running scenario modules over inventing data.

## Approval

Consequential commits require Rob to say `APPROVE <id>`. YOLO off.
