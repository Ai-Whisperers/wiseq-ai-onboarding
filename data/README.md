# Data — evidence attic

*Client-facing narrative lives in [`docs/`](../docs/). This folder holds the inspectable artifacts those docs cite.*

## Index

| Artifact | What it is | Cited by |
| :--- | :--- | :--- |
| [`CLAIMS-LEDGER.md`](CLAIMS-LEDGER.md) | 47 material claims with status, source, date, reproduce path | README · [doc 27](../docs/f-governance/27-EVIDENCE-INDEX.md) |
| [`leadgen-summary.md`](leadgen-summary.md) | B2B lead-gen **method + counts only** (no PII) | README · doc 02 |
| [`wiseq-bundle-spine.csv`](wiseq-bundle-spine.csv) | 25 decomposed bundles → components | CI · docs 07 / 23 / 25 |
| [`wiseq-component-registry.csv`](wiseq-component-registry.csv) | 114 component SKUs | CI · spine integrity |
| [`research-lanes/`](research-lanes/) | Original lane reports + dossier + addenda 2–7 | Evidence base |
| [`oss/`](oss/) | Per-topic GitHub search JSON (31 topics) | Doc 10 |

## Research lanes

**Original lanes (Oct 21):** `RESEARCH_COMPANY.md` · `RESEARCH_CATALOG.md` · `RESEARCH_MARKETPLACES.md` · `RESEARCH_MARKETING_COMPETITION.md` · `WISEQ-DOSSIER.md` · `raw-agents-md.txt`

**Addenda (Oct 23):**

| # | File | Topic |
| ---: | :--- | :--- |
| — | `RESEARCH-ADDENDUM-PROCUREMENT-API.md` | bol Retailer API + 5X nuance |
| 2 | `RESEARCH-ADDENDUM-2-PROCUREMENT-COMPETITOR-AVG.md` | School procurement + AVG |
| 3 | `RESEARCH-ADDENDUM-3-CERTS-PRICING-MARKET.md` | Cert bands, Trustpilot tiers, PO market |
| 4 | `RESEARCH-ADDENDUM-4-GS1-AMAZON-COMPETITIVE.md` | GS1 €225 correction, Amazon GPSR, kids-audio market |
| 5 | `RESEARCH-ADDENDUM-5-UCP-FEES-CERTS-REPUTATION.md` | UCP/ACP, bol fees, Thuiswinkel, Scamadviser |
| 6 | `RESEARCH-ADDENDUM-6-UNIT-ECONOMICS.md` | PSP, PostNL, OSS VAT |
| 7 | `RESEARCH-ADDENDUM-7-ENGAGEMENT-MECHANICS.md` | Reverse charge, Shopify limits, market pricing, liability, ChannelDock risk |

## OSS topic stubs

These JSON files have a query but **near-zero curated items** — do not treat them as a full catalog until refilled:

`content-generation` · `review-automation` · `product-matching` · `inventory-sync` · `invoice-parse` · `edtech`

## Freshness

Rows marked **STALE** in the claims ledger are re-verified before quoting to the client. Next scheduled re-check: bol seller count + Trustpilot totals.
