<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="30">
</div>

# Data — evidence attic

Client-facing narrative lives in [`docs/`](../docs/README.md). This folder holds the **inspectable artifacts** those docs cite. No personal contact data is stored here.

## Quick index

| Artifact | What it is | Cited by |
| :--- | :--- | :--- |
| [`CLAIMS-LEDGER.md`](CLAIMS-LEDGER.md) | 57 material claims — legacy statuses + four-dimension model for client SoT | Root README · [doc 27](../docs/50-evidence/17-evidence-index.md) · [doc 29](../docs/60-governance/03-critical-audit-2026-10-27.md) |
| [`leadgen-summary.md`](leadgen-summary.md) | B2B lead-gen **method + counts only** (no PII) | README · [doc 02](../docs/archive/2026-10-research-log.md) |
| [`wiseq-bundle-spine.csv`](wiseq-bundle-spine.csv) | 25 decomposed bundles → components | CI · docs [07](../docs/10-client/06-bundle-spine-reuse.md) / [23](../docs/60-governance/02-acceptance-criteria.md) / [25](../docs/10-client/05-catalog-scorecard.md) |
| [`wiseq-component-registry.csv`](wiseq-component-registry.csv) | 114 component SKUs | CI spine integrity |
| [`research-lanes/`](research-lanes/) | Lane reports + dossier + addenda 2–7 | Evidence base |
| [`oss/`](oss/) | Per-topic GitHub search JSON (31 topics) | [Doc 10](../docs/30-market/03-oss-catalog.md) |
| [`client/`](client/) | **Client SoT** — extracts + raw manual (**publication gate**) | [Doc 28](../docs/10-client/03-operating-manual.md) · [`client/README.md`](client/README.md) |
| [`client/mastersheet/`](client/mastersheet/) | Shipping tariffs, rule templates (+ validation_status), packaging, keywords | [Mastersheet extract](client/MASTERSHEET-EXTRACT.md) |
| [`stack-map.md`](stack-map.md) | Phase-0 connector map + capability matrix skeleton | [Doc 06](../docs/20-offer/03-next-steps.md) · [doc 29](../docs/60-governance/03-critical-audit-2026-10-27.md) |

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
| 6 | [`…-6-…`](research-lanes/RESEARCH-ADDENDUM-6-UNIT-ECONOMICS.md) | PSP, PostNL, OSS VAT | **[Doc 26](../docs/30-market/05-unit-economics.md)** |
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
