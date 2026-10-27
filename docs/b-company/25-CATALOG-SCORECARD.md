<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track B · Document 25* · [← Docs map](../README.md)</sub>

---

# Catalog data-quality scorecard

*One page for ops and decision-makers. Numbers from the Oct 21 Shopify export + the CI-validated bundle spine. Full narrative: [RESEARCH_CATALOG.md](../../data/research-lanes/RESEARCH_CATALOG.md).*

## Snapshot

| Metric | Value | Status |
| :--- | :--- | :--- |
| Live Shopify products | **230** | Verified export |
| Own-brand (vendor WiseQ) | **100%** | Verified |
| Products with barcode / EAN field | **0 / 230** | Gap |
| Products with weight | **0 / 230** | Gap |
| Inventory tracked in Shopify | **0 / 230** | By design — ChannelDock is SoR |
| Title-keyword “bundle-like” SKUs | **77 (33%)** | Heuristic |
| Bundles **decomposed** in spine | **25** | CI-validated |
| Component SKUs in registry | **114** | CI-validated |
| Unresolved spine references | **0** | CI-validated |
| Critical GTINs to register (components + bundles) | **139** | Planning figure |
| GS1 cost (whole catalog) | **€225/yr** | 1,000-pack + contribution (until Dec 1 2026 tariff) |

## Two businesses in one shop

| Lane | Rough share | Price band | Role |
| :--- | :--- | :--- | :--- |
| Chargers + cables long tail | ~50% of SKUs | €7–34 | Marketplace volume |
| Kids headphones (brand story) | 23 SKUs | €19–50 | Margin / brand |
| B2B gear (carts, storage, hubs) | Small n, high ticket | €399–1,149 | School channel |

## What “done” looks like (Gate 3)

Per [acceptance criteria](../f-governance/23-ACCEPTANCE-CRITERIA.md): every spine bundle reconciled against the physical manual (quantities, variants) — referential integrity alone is not enough.

## Continue reading

| Next | Why |
| :--- | :--- |
| [Reuse-First / bundle spine](07-PY-TRANSFER-WISEQ.md) | How the 25 bundles were decoded |
| [Next Steps](../a-proposal/06-NEXT-STEPS.md) | ChannelDock plan / PIM questions that change scope |
| [Unit economics](../c-market/26-UNIT-ECONOMICS.md) | What each SKU actually costs to sell |
