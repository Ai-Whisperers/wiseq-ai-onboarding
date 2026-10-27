<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track F · Document 29* · [← Docs map](../README.md)</sub>

---

# Critical audit response — 2026-10-27

*Response to the “Critical audit: WiseQ AI Onboarding repository” review of commits `f2c2eab` / `baf01b5` (client manual + Mastersheet ingestion).*

## Verdict we accept

The audit’s core distinction is correct: **client-supplied text ≠ independently verified ≠ safe to automate**. We keep the discovery direction, fix the concrete inconsistencies below, and treat Phase 0 as **read-only / evidence-driven** until capability tests pass.

---

## Fixes shipped with this response

| Audit finding | Action |
| :--- | :--- |
| “Verified” overloaded | Claims ledger header upgraded to **four dimensions**; claims **48–57** re-labeled | 
| 80% vs 178% BE LVB uplift | Both retained as **client-reported, conflicting**; **not used in ROI forecasts**; Rob confirm asked |
| `2x Adapter ?` template mismatch | CSV flagged `NEEDS_CONFIRMATION`; cannot drive automation until Rob/ChannelDock check |
| Stale Exact decision wording | Doc 06 / 04 / 24 rewritten around **e-Boekhouden** |
| Tariff CSV not a calc engine | Extract + unit-econ docs: typed caveats; notes ≠ numbers |
| Raw manual public exposure | [`data/client/README.md`](../../data/client/README.md) publication gate; Rob approval required for raw dump |
| Review-contact tactics | Explicit **do-not-automate** policy in client extract + this doc |
| Stack map overconfidence | Capability matrix skeleton; vendor feature ≠ account entitlement |

---

## Evidence-status model (going forward)

| Dimension | Allowed values |
| :--- | :--- |
| **Source provenance** | `client-provided` · `vendor-docs` · `independently-measured` · `aiw-internal` |
| **Technical verification** | `untested` · `sandbox-tested` · `production-tested` |
| **Business validation** | `assumed` · `client-confirmed` · `quantitatively-validated` |
| **Implementation** | `not-started` · `draft` · `tested` · `deployed` |

A claim may be `client-provided` + `client-confirmed` and still `untested` technically. That is the normal Phase-0 state — not a license to write to production.

---

## Commercial claim: BE LVB uplift

| Source | Figure | Status |
| :--- | :--- | :--- |
| Operating manual | **+80%** sales when BE moves to next-day via LVB | Client-reported |
| Mastersheet notes | **+178%** (one cell also mangled as `€178%`) | Client-reported; definition unknown |

**Neither figure is a forecast.** Proposal/ROI text must not pick one until Rob defines: metric (units/orders/revenue/conversion), period, products, controls for price/stock/ads/seasonality.

Open ask → Rob: which figure stands, and can you share the measurement note?

---

## Shipping-rule template: `2x Adapter ?`

Row had clone-note EAN `8720254493947` (≈310 combo) but `template_ean` `8720618246110` (adapters &gt;50g). Marked **NEEDS_CONFIRMATION** in CSV. Headphone-case row remains incomplete (rule ids only). Automation must refuse to clone from `NEEDS_CONFIRMATION` / empty templates.

---

## Review-handling policy (strengthened)

From the raw manual: low bol ratings trigger follow-ups and deletion requests.

**AIW rules for any agent work:**

1. Separate **customer-service resolution** from **review-influence** asks.  
2. **No automated** “please remove/change your rating” messages without written confirmation the exact template complies with current bol rules.  
3. Non-response ≠ consent to keep mailing; contact limits + suppression list required.  
4. Lawful basis, retention, and audit trail documented before any send path exists.  
5. Phase 0–1: **draft recommendations only**; human sends.

Seller score ≥9 is a **business objective**, not evidence that every tactic is allowed or effective.

---

## Integration readiness (agree with audit table)

ChannelDock REST-from-Voorraad remains **vendor-feature knowledge**. WiseQ’s plan, token, and permissions stay **untested**. Same pattern for FiveX, e-Boekhouden, MyParcel, QLS, mailbox, multi-account bol.

Phase 0 exit = filled **capability matrix** (see [`data/stack-map.md`](../../data/stack-map.md)), not a longer connector wish-list.

---

## Priority order we adopt (matches audit §9)

1. Close data inconsistencies (this doc).  
2. Publication review with Rob on raw manual.  
3. Remaining inputs: CD plan/API, FiveX exports, sandbox school orders, mailbox, turnover.  
4. Read-only prototype: assortment online, ungefrankeerd queue, cancellations, stock drift.  
5. School-order shadow demo with idempotency + human gates.  
6. Controlled writes only after permission/failure/audit/rollback tests.

---

## What would make us call it “ready” (accept audit §10)

Account identities correct · shipping templates validated NL/BE × qty · tariffs reconcile to dated sources · school demo survives retries without duplicate invoices · price drafts show evidence + approval · review path policy-compliant · every material claim labeled by the four dimensions · public repo only holds publication-approved material.

---

<sub>Prepared by AI Whisperers · 2026-10-27 · related: [doc 22](../archive/2026-10-external-audit-response.md) (Oct 22 audit)</sub>
