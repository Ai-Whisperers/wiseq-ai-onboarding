<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="30">
</div>

# Data — evidence attic

Client-facing narrative lives in [`docs/`](../docs/README.md). This folder holds the **inspectable artifacts** those docs cite. No personal contact data is stored here.

## Quick index

| Artifact | What it is | Cited by |
| :--- | :--- | :--- |
| [`CLAIMS-LEDGER.md`](CLAIMS-LEDGER.md) | 47 material claims — status, source, date, reproduce path | Root README · [doc 27](../docs/f-governance/27-EVIDENCE-INDEX.md) |
| [`leadgen-summary.md`](leadgen-summary.md) | B2B lead-gen **method + counts only** (no PII) | README · [doc 02](../docs/b-company/02-WHAT-WE-DID.md) |
| [`wiseq-bundle-spine.csv`](wiseq-bundle-spine.csv) | 25 decomposed bundles → components | CI · docs [07](../docs/b-company/07-PY-TRANSFER-WISEQ.md) / [23](../docs/f-governance/23-ACCEPTANCE-CRITERIA.md) / [25](../docs/b-company/25-CATALOG-SCORECARD.md) |
| [`wiseq-component-registry.csv`](wiseq-component-registry.csv) | 114 component SKUs | CI spine integrity |
| [`research-lanes/`](research-lanes/) | Lane reports + dossier + addenda 2–7 | Evidence base |
| [`oss/`](oss/) | Per-topic GitHub search JSON (31 topics) | [Doc 10](../docs/c-market/10-OSS-CATALOG-100.md) |
| [`client/`](client/) | **Client SoT** — operating manual + extract | [Doc 28](../docs/b-company/28-CLIENT-OPERATING-MANUAL.md) |
| [`stack-map.md`](stack-map.md) | Phase-0 connector map (draft from manual) | [Doc 06](../docs/a-proposal/06-NEXT-STEPS.md) |

## Research lanes

**Original lanes (Oct 21)**

| File | Focus |
| :--- | :--- |
| [`RESEARCH_COMPANY.md`](research-lanes/RESEARCH_COMPANY.md) | Entity, timeline, registry |
| [`RESEARCH_CATALOG.md`](research-lanes/RESEARCH_CATALOG.md) | 230 SKUs, data quality |
| [`RESEARCH_MARKETPLACES.md`](research-lanes/RESEARCH_MARKETPLACES.md) | bol, Amazon, Trustpilot, Scamadviser |
| [`RESEARCH_MARKETING_COMPETITION.md`](research-lanes/RESEARCH_MARKETING_COMPETITION.md) | SEO, UCP, competitors |
| [`WISEQ-DOSSIER.md`](research-lanes/WISEQ-DOSSIER.md) | Cross-cutting synthesis |
| [`raw-agents-md.txt`](research-lanes/raw-agents-md.txt) | Captured agents.md |

**Addenda (Oct 23)** — depth passes after the external audit

| # | File | Topic | Client summary |
| ---: | :--- | :--- | :--- |
| — | [`…-PROCUREMENT-API.md`](research-lanes/RESEARCH-ADDENDUM-PROCUREMENT-API.md) | bol Retailer API + 5X nuance | Doc 08 / 13 |
| 2 | [`…-2-…`](research-lanes/RESEARCH-ADDENDUM-2-PROCUREMENT-COMPETITOR-AVG.md) | School procurement + AVG | Doc 11 / 18 |
| 3 | [`…-3-…`](research-lanes/RESEARCH-ADDENDUM-3-CERTS-PRICING-MARKET.md) | Cert bands, Trustpilot tiers | Doc 11 |
| 4 | [`…-4-…`](research-lanes/RESEARCH-ADDENDUM-4-GS1-AMAZON-COMPETITIVE.md) | **GS1 €225**, Amazon GPSR | Doc 04 / 08 |
| 5 | [`…-5-…`](research-lanes/RESEARCH-ADDENDUM-5-UCP-FEES-CERTS-REPUTATION.md) | UCP/ACP, bol fees, Scamadviser | Doc 04 |
| 6 | [`…-6-…`](research-lanes/RESEARCH-ADDENDUM-6-UNIT-ECONOMICS.md) | PSP, PostNL, OSS VAT | **[Doc 26](../docs/c-market/26-UNIT-ECONOMICS.md)** |
| 7 | [`…-7-…`](research-lanes/RESEARCH-ADDENDUM-7-ENGAGEMENT-MECHANICS.md) | Reverse charge, liability, pricing | Doc 18 |

## OSS topic stubs

These JSON files have a query but **near-zero curated items** — do not treat them as a full catalog until refilled:

`content-generation` · `review-automation` · `product-matching` · `inventory-sync` · `invoice-parse` · `edtech`

## Freshness

Rows marked **STALE** in [`CLAIMS-LEDGER.md`](CLAIMS-LEDGER.md) are re-verified before quoting to the client. Next scheduled re-check: bol seller count + Trustpilot totals.

Reproduce integrity locally:

```bash
python3 scripts/validate_repo.py
```

---

<sub>[← Docs map](../docs/README.md) · [Root README](../README.md) · Revision 2026-10-27</sub>
