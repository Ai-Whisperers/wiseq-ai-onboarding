<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 23* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Acceptance criteria: what "done" has to mean before anything touches production

*This document exists because an external audit of this repository (Oct 22, 2026 — see [doc 22](../archive/2026-10-external-audit-response.md)) asked the right question: what evidence would make these claims trustworthy? Our answer: a written acceptance standard, agreed **before** the pilot starts, that defines when each part of the system is considered proven. Nothing below is claimed as already passed. This is the bar we sign up to.*

---

## The principle

**Read-only first, writes last, money last of all.** Every stage below has a defined pass condition. If a stage fails, we stop, report, and fix — we do not proceed on optimism. WiseQ can halt at any stage for any reason, and everything built up to that point is theirs ([doc 18](01-terms.md)).

---

## Stage gates

### Gate 0 — Data handover (before any work)

| # | Criterion | Evidence |
|---|---|---|
| 0.1 | Manual, software inventory, and sandbox data received | Files in the shared vault, logged with date |
| 0.2 | Sandbox credentials are read-only or fully sandboxed | Screenshot of permission screen |
| 0.3 | Baseline measured: ≥10 real school orders timed end-to-end (touch time and elapsed time recorded separately) | Timing log, countersigned by WiseQ staff |

**Why 0.3 matters:** the "4-hour mornings" figure is a founder estimate from one working session. Doc 04's savings arithmetic is a hypothesis until 0.3 replaces it. We commit to publishing the measured number **even if it is worse for us than the estimate.**

### Gate 1 — Integration verification (read-only, ~week 1)

| # | Criterion | Evidence |
|---|---|---|
| 1.1 | Each system (Shopify, ChannelDock, bookkeeping, bol, email) documented: endpoint, auth, plan tier, rate limits | `integration-notes/` in the repo |
| 1.2 | Successful read-only API call against each system from sandbox credentials | Logged request/response pairs |
| 1.3 | Systems that fail 1.2 are named openly, with the failure reason | Written in the weekly report — not silently dropped |

### Gate 2 — Order workflow tests (~week 2)

| # | Criterion | Evidence |
|---|---|---|
| 2.1 | Representative **normal** orders processed correctly in sandbox | Test log with ≥20 order scenarios |
| 2.2 | Edge cases handled without silent failure: duplicate emails, missing EAN, price exceptions, partial shipment, cancellation, API timeout | One test per edge case, expected-vs-actual |
| 2.3 | Every failure produces a human-readable alert, not a silent drop | Alert log |

### Gate 3 — Bundle spine reconciliation (Phase 0 exit)

| # | Criterion | Evidence |
|---|---|---|
| 3.1 | Every bundle in [the spine](../../data/wiseq-bundle-spine.csv) reconciled against the physical manual: components, quantities, variants | Signed reconciliation sheet — CI referential integrity (already passing) is necessary but not sufficient |
| 3.2 | Discrepancies listed with disposition (fixed / flagged / needs WiseQ decision) | Discrepancy table in the repo |

### Gate 4 — Financial reconciliation (before any write access)

| # | Criterion | Evidence |
|---|---|---|
| 4.1 | Agent-generated offers match a manually computed reference set for ≥30 orders, incl. VAT and discounts | Diff report: zero unexplained differences |
| 4.2 | Stock movements reconcile against ChannelDock records | Reconciliation report |
| 4.3 | Rollback demonstrated: a bad run can be reverted within one working day, with data intact | Rollback drill, witnessed |

### Gate 5 — Measured pilot (Phase 1 exit)

| # | Criterion | Evidence |
|---|---|---|
| 5.1 | Touch time per school-order morning: measured before vs. after, same order mix | The number from 0.3 vs. the same measurement repeated on the live pipeline |
| 5.2 | Error and exception rates: manual baseline vs. pipeline | Counted from logs, not estimated |
| 5.3 | Actual operating cost (AI tier, infra) vs. the €40–90/mo band in [doc 04](../20-offer/01-blueprint.md#-12-month-total-cost-of-ownership-tco) | Invoices + usage meter |
| 5.4 | Review-invitation experiment (if running): invitations sent, delivered, converted — reported whatever the result | Trustpilot + email logs |

**On 5.4 specifically:** the "25 → 250+ reviews" idea is a hypothesis with no conversion model behind it. If invitations convert at 5%, the honest outcome is documented as 5% — not massaged.

---

## What we are NOT claiming

- That any gate above has been passed already (none have — nothing has been built).
- That passing the gates guarantees commercial outcomes (sales lift, review growth). The gates prove the **system** works as specified; commercial results are reported as measured, not promised.
- That this document replaces the [compliance checklist](../30-market/04-compliance.md) — product-safety and regulatory items stay there, per-SKU, in Phase 0.

---

## The deal this implies

If the audit's framing is right — that this repo is "a promising proposal supported by substantial discovery work" — then the honest contract is: **pilot money buys measured evidence, not promised outcomes.** These gates are what the evidence has to look like. Rob can hold us to every row.

---

## Continue reading

| Next | Why |
|---|---|
| **[Audit response](../archive/2026-10-external-audit-response.md)** | What we fixed after the external audit, and where we conceded |
| **[Terms & continuity](01-terms.md)** | What WiseQ keeps if we stop |
| **[The blueprint](../20-offer/01-blueprint.md)** | What we propose to build, and what it costs |
