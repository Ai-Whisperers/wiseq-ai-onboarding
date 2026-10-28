<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track F · Document 27* · [← Docs map](../README.md)</sub>

---

# Evidence index — how to trust every number

*Short map from client-facing claims → inspectable artifacts. Master ledger: [`data/CLAIMS-LEDGER.md`](../../data/CLAIMS-LEDGER.md) (57 rows). Client-SoT claims use the **four-dimension** model ([doc 29](../60-governance/03-critical-audit-2026-10-27.md)).*

## Status meanings

| Status | Meaning |
| :--- | :--- |
| **VERIFIED** | Reproducible from an artifact or live public source |
| **INFERRED** | Plausible reading of evidence; not independently established |
| **HYPOTHESIS** | Testable proposal — measure in Phase 0 / gates |
| **STALE** | Snapshot older than policy window; re-verify before quoting |
| **client-provided** (+ tech/biz/impl dims) | In client docs — not the same as independently measured or automation-safe |

## Where the big numbers live

| Claim (short) | Status | Artifact |
| :--- | :--- | :--- |
| 0/230 EANs in Shopify export | VERIFIED | [RESEARCH_CATALOG](../../data/research-lanes/RESEARCH_CATALOG.md) · [scorecard](../10-client/05-catalog-scorecard.md) |
| Spine 114 + 25, 0 unresolved | VERIFIED (structural) | CSVs + CI |
| GS1 **€225/yr** whole catalog | VERIFIED (tariff Oct 23) | [Addendum 4](../../data/research-lanes/RESEARCH-ADDENDUM-4-GS1-AMAZON-COMPETITIVE.md) |
| Trustpilot **13 / 4.5**, all organic | VERIFIED (re-pull Oct 23) | Ledger #47 |
| School mornings ~4h | HYPOTHESIS | [Meeting notes](../10-client/04-meeting-2026-10-21.md) · Gate 0.3 |
| Payback ~2–3 months | HYPOTHESIS | [Blueprint](../20-offer/01-blueprint.md) · Gates 5.x |
| bol listing count 312 | STALE | Re-pull before quoting |
| Lead-gen 857 orgs w/ email | VERIFIED (method) | [leadgen-summary](../../data/leadgen-summary.md) — no PII in repo |
| Bookkeeping = e-Boekhouden | client-provided · tech untested | [doc 28](../10-client/03-operating-manual.md) · claim 48 |
| BE LVB uplift 80% vs 178% | client-provided · CONFLICT | [doc 29](../60-governance/03-critical-audit-2026-10-27.md) — not for ROI |
| 2× Adapter shipping template | NEEDS_CONFIRMATION | [`verzendregels-templates.csv`](../../data/client/mastersheet/verzendregels-templates.csv) |
| Lab scenarios A–C pass offline | sandbox-tested | [`lab/`](../../lab/README.md) · [experiment register](../50-evidence/09-experiment-register.md) |
| Hermes Desktop Milestone 1 | vendor-docs + local doctor | [capability notes](../50-evidence/06-hermes-desktop.md) |
| Revenue ~€1.5M / yr | client-stated (2026-10-28) | [Meeting 07](../10-client/07-meeting-2026-10-28.md) — confirm online vs total |
| Rob fee floor ≥€2k | client-stated (signal only) | [Meeting 07](../10-client/07-meeting-2026-10-28.md) — not our SOW price |
| Manual + Mastersheet received | client-provided | [Submissions status](18-rob-submissions-status.md) |

## Addenda map (Oct 23 depth)

Full list in [`data/README.md`](../../data/README.md). Client summaries: [unit economics](../30-market/05-unit-economics.md) · terms annex in [doc 18](../60-governance/01-terms.md).

## Continue reading

| Next | Why |
| :--- | :--- |
| [Audit response](../archive/2026-10-external-audit-response.md) | What we fixed after Oct-22 external review |
| [Critical audit response](../60-governance/03-critical-audit-2026-10-27.md) | Manual/Mastersheet evidence + safety response |
| [Acceptance criteria](../60-governance/02-acceptance-criteria.md) | Gates that turn hypotheses into measurements |
| [Rob submissions status](18-rob-submissions-status.md) | Two files + meetings vs open asks |
| [Critical review](../archive/2026-10-critical-review.md) | Adversarial pass on this proposal |
