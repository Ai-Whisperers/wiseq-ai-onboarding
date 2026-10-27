# Current state and workflow audit

*Phase 0 evidence pack. Sources: [`OPERATING-MANUAL-EXTRACT.md`](../../data/client/OPERATING-MANUAL-EXTRACT.md), [`MASTERSHEET-EXTRACT.md`](../../data/client/MASTERSHEET-EXTRACT.md), docs 01–28. Prefer extracts over raw Handleiding until Rob approves publication.*

## How to read this inventory

For each workflow: **trigger → actor/systems → inputs/outputs → manual steps → frequency → failure modes → simplify-before-software → evidence needed**.

Evidence status: **C** = client-provided · **P** = public research · **H** = hypothesis · **L** = lab-testable offline.

---

## A. Sales and customer operations

| Workflow | Trigger | Actor / systems | Manual pain | Freq | Failures | Simplify first | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| School catalog/sample request | Email | Mailbox → templates | Copy into offer path | Daily/seasonal | Wrong address, missing school name | Template checklist | C · L Exp A |
| School offer → invoice | Accept | **e-Boekhouden** relations/offers/invoices | Duplicate relations, wrong lines | Per order | Double invoice | Idempotency key = order id | C · L |
| School shipment | Invoice paid/accepted | MyParcel/DHL | Label after incomplete invoice | Per order | Ship without invoice | Gate: invoice must exist | C · L |
| Own-shop B2B (Shopify) | Web order | Shopify + custom B2B layer | Light in manual | Continuous | Drift vs bol | Confirm Phase-0 priority | P · C |
| Reseller orders (EDG, ITS, …) | Email/PO | e-Boekhouden + kenmerk rules | Special invoice fields | Weekly | Wrong BTW/CC | Rule table, not AI | C |
| CS mailbox triage | Inbox | Mailbox | Hours/week | Daily | Mis-file, missed SLA | Labels + drafts only | C · H |
| Returns / cancellations | Portal/email | ChannelDock + bol | Confirm queue daily | Daily | Unconfirmed cancel | Read-only queue digest | C · L |

## B. Marketplace operations (×3 accounts)

| Account | Role | Migration |
| :--- | :--- | :--- |
| WiseQ NL | Primary NL seller | Active |
| WiseQ Electronics | BE-facing / packages | Active |
| WiseQ België | Holding | Phasing out — treat as migration, not done |

| Workflow | Trigger | Systems | Pain | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assortment 100% online | Daily checklist | bol ×3 + ChannelDock | Silent offline SKUs | C · L |
| Delivery promises | Order cutoffs | bol + CD rules | Wrong promise → strikes | C · L |
| Reviews / seller score ≥9 | New reviews | FiveX + bol | Follow-ups; policy-sensitive | C · draft-only |
| LVB replenishment | Weekly | FiveX reports | Stockouts | C · L Exp D later |
| Price brake +10% @ ≤10 stock | Stock signal | FiveX auto | May be wrong for fast movers | C · investigate before copy |
| Strikes / on-time | Wed review | bol | High impact | C · human gate |
| Listing hijackers / CE | Complaint | Drive certs + mail | Unsafe CE sticker workaround — never automate | C |

## C. Inventory, purchasing, warehouse

| Workflow | Systems | Notes | Evidence |
| :--- | :--- | :--- | :--- |
| SoR inventory | ChannelDock | Bundles native; 300-series must book as bundles | C |
| Bundle spine (AIW) | CSV spine | Structural CI only; not physical reconcile | P · Gate 3 |
| Ungefrankeerde zendingen | ChannelDock | Daily #1 friction | C · L |
| Sea freight inbound | CD + Mastersheet | Bundle bijmaken = failure mode | C |
| Packaging reorder | Mastersheet links | MyParcel/Verpakgigant | C |
| Purchase intelligence | Excel | Founder Excel averages | C · H · backlog #3 |

## D. Shipping and unit economics

| Decision | Inputs | Caveat |
| :--- | :--- | :--- |
| Carrier vs promise | Country, class, weight, qty, LVB/VVB/QLS/PostNL | Tariff CSV has notes-in-numbers; not a calc engine yet |
| New SKU shipping rules | Template EAN by class | `NEEDS_CONFIRMATION` rows must refuse auto-clone |
| BE LVB uplift | Client notes 80% vs 178% | **Not for ROI** until Rob defines metric |

## E. Finance, admin, compliance

| Workflow | System | Gate |
| :--- | :--- | :--- |
| Offers/invoices/relations | e-Boekhouden | API feasibility untested |
| Reconciliation | Manual | Duplicate prevention required |
| CE / DoC library | Google Drive | Cite or escalate — never invent |
| AVG / marketplace policy | — | Before any send automation |

## F. Marketing and growth

| Workflow | Status |
| :--- | :--- |
| SEO keywords | Mastersheet samples public |
| Review invitations | Bol-first; Trustpilot secondary; no 250+ promise |
| B2B lead-gen | Method in repo; no PII |
| Site demos | Static showcase only |

## System inventory (summary)

See [`DATA-FLOW-AND-SYSTEM-OF-RECORDS.md`](03-data-flow-sor.md) and [`data/stack-map.md`](../../data/stack-map.md).

---

*Author: AI Whisperers · 2026-10-27 · companion: [PROGRESS-LOG](15-progress-log.md)*
