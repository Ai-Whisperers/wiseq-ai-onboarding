<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track C · Document 26* · [← Docs map](../README.md)</sub>

---

# Unit economics — payments, shipping, OSS VAT

*Client summary of [addendum 6](../../data/research-lanes/RESEARCH-ADDENDUM-6-UNIT-ECONOMICS.md). Every externally researchable cost coefficient is here; COGS and order mix still need WiseQ’s books (Phase 0).*

## Payments — watch Bancontact

| Method | Typical published rate | Note |
| :--- | :--- | :--- |
| iDEAL | €0.29–0.35 | Baseline NL |
| EEA cards | ~1.5–1.8% + €0.25 | Plan-dependent |
| **Bancontact** | Mollie **1.40% + €0.25** vs Stripe **flat €0.35** | BE buyers default here — at WiseQ basket sizes this choice can outweigh card-rate differences |

**Phase-0 ask:** current Shopify PSP + payment-method mix from real orders.

## Shipping — use WiseQ’s own tariff table

Generic PostNL consumer bands are secondary. **Source of truth:** client Mastersheet → [`verzendtarieven.csv`](../../data/client/mastersheet/verzendtarieven.csv) / [extract](../../data/client/MASTERSHEET-EXTRACT.md).

| Mode (examples) | NL € | BE € |
| :--- | ---: | ---: |
| LVB 3XS chargers | 2.78 | 5.11 |
| LVB S headphones (Unbreakable/Hero/…) | 6.27 | 6.27 |
| VVB brievenbus chargers | 3.77 | 6.33 |
| QLS parcel headphones | 4.61 | 4.75 |
| QLS Europlus **school** | 10.54 | 10.54 |
| PostNL partijenpost &lt;50g | 1.85 | 4.42 |

**Decision rule Rob described:** compare shipping cost vs delivery promise (before **15:00** next-day own stock vs before **00:00** LVB next-day). BE LVB noted on sheet as large conversion lift (~178%).

## Cross-border VAT — OSS €10k trap

- EU B2C distance-sales threshold **€10,000/year** (all EU countries combined).
- Crossing it is **retroactive for the calendar year** — Belgian VAT can suddenly apply to earlier months.
- bol.be revenue counts. Phase-0 must-check: WiseQ’s non-NL EU B2C total vs threshold.
- Design: Phase-1 **OSS-threshold watchdog** (alert ~€8.5k with weeks left in year).

## Known vs unknown

| Coefficient | Status |
| :--- | :--- |
| bol commission bands | Known; live API read preferred |
| PSP / shipping / GS1 / SaaS fees | Known (this doc + addenda 3–5) |
| **COGS per SKU** | Needs Rob |
| **Order volume / mix** | Needs Rob |
| **Bookkeeping package** | Needs Rob |

## Continue reading

| Next | Why |
| :--- | :--- |
| [AI Stack Blueprint · TCO](../a-proposal/04-AI-STACK-BLUEPRINT.md#-12-month-total-cost-of-ownership-tco) | Full year-1 arithmetic |
| [Competitors & Deals](09-COMPETITORS-DEALS.md) | Deal shape benchmarks |
| [Next Steps](../a-proposal/06-NEXT-STEPS.md) | Phase-0 questions that unlock the unknowns |
