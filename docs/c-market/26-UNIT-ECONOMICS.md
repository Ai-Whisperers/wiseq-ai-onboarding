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

## Shipping — PostNL 2026 (online frankering, excl. VAT)

| Product | Price |
| :--- | :--- |
| Brievenbuspakje+ ≤2 kg | **€4.55** |
| Pakket ≤10 kg → huisadres | **€7.45** |
| Pakket ≤10 kg → PostNL-punt | €6.95 |
| Buspakje BE (w/ track) | €9.50–10.00 |

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
