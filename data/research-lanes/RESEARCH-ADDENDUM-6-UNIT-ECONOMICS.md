# Research addendum 6: unit economics — payments, shipping, cross-border VAT

*Oct 23, 2026 — sixth lane. The pipeline's financial legs, priced. One hidden trap found (Bancontact pricing), one compliance trap confirmed (OSS retroactivity), and the shipping cost bands that close the margin picture. Sources linked inline.*

---

## 1. Payments: the iDEAL baseline and the Bancontact trap

Published rates, Oct 2026 ([ecomstream iDEAL fee survey](https://ecomstream.eu/ideal-fees) — the authoritative one, 22 acquirers/63 PSPs tabled; [SoftwareWatcher](https://softwarewatcher.com/compare/mollie-vs-stripe); [Mue fee PDF](https://agent.mue.app/downloads/european-payment-processor-fees-stripe-mollie-adyen.pdf)):

| Provider | iDEAL | EEA consumer card | Bancontact | Monthly |
|---|---|---|---|---|
| **Mollie** | €0.32–0.35 | 1.80% + €0.25 | **1.40% + €0.25** | €0 (€20 Pro from €2k rev) |
| **Stripe** | €0.29 | 1.5% + €0.25 | **flat €0.35** | €0 |
| Adyen | €0.33 (split) | Interchange++ (0.6% markup) | — | min. invoice |
| Banks (ABN/Rabo) | €0.27–0.30 | — | — | €10–25 + setup |

**The Bancontact trap:** WiseQ sells into Belgium via bol — Belgian consumers default to Bancontact. Mollie prices it **percentage-based (1.40% + €0.25)**; Stripe prices it **flat €0.35**. On a €50 Belgian order: Mollie ≈ €0.95, Stripe ≈ €0.35. On a €100 class-set component: €1.65 vs €0.35. **At WiseQ's basket sizes, provider choice on this one method can outweigh the entire card-rate difference.** Phase-0 homework: pull the current PSP from Shopify checkout settings + the actual payment-method mix from order data (the sandbox will show it) — then the pipeline prices payment costs per order, not by vendor marketing.

**Also noted:** Wero (the EU wallet scheme) pricing is frozen at iDEAL-level through **Dec 31, 2028** ([ecomstream](https://ecomstream.eu/ideal-fees)) — no near-term payment-cost shock, but a watching brief for 2029.

---

## 2. Shipping: PostNL 2026 business bands

From [PostNL's official 2026 tariff booklet (July edition)](https://www.postnl.nl/api/assets/blt43aa441bfc1e29f2/blt5e65605bca8690e0/tarievenboekje-12-juli-2026.pdf):

| Product (online frankering, excl. VAT) | Price |
|---|---|
| Brievenbuspakje+ (≤2kg, fits mailbox) | **€4.55** |
| Klein pakket ≤3kg → PostNL-punt | €5.85 |
| Pakket ≤10kg → huisadres | **€7.45** |
| Pakket ≤10kg → PostNL-punt | €6.95 |
| Aangetekend ≤10kg | €11.25 |
| Buspakje naar België (0–500g, w/t&t) | €9.50 |
| Klein pakket België (1–2kg, w/t&t) | €10.00 |

Plus volume-tiered business rates below base (partijenpost from ~€0.70/letter), and [PostNL Fulfilment from €1.40/order](https://www.postnl.nl/zakelijk/logistieke-oplossingen/fulfilment/tarieven/) pick-pack (excl. distribution/packaging) — relevant only if WiseQ ever outsources logistics; at their scale, self-ship + brievenbuspakje is the margin play.

**Margin framing for a typical WiseQ order** (kids headset ~€29.95 incl. VAT, shipped as brievenbuspakje):
- Revenue excl. VAT: €24.75 → bol commission ~€4.57 (addendum 5) → shipping €4.55 → payment ~€0.35 → **~€15.28 left for product cost + packaging + everything else**
- The unit-economics spine (doc 07's canonical table) now has every coefficient except true product cost — which only Rob's data can fill. **The margin-floor repricing agent is now fully specifiable except for COGS.**

---

## 3. Cross-border VAT: OSS and the retroactive €10k trap

The rules ([vanpasse OSS guide](https://vanpasse.nl/kennisbank/belastingen/oss-aangifte), [bolmoneybird cross-border guide](https://bolmoneybird.nl/en/blog/bolcom-cross-border-vat-oss-moneybird-en), [Winkelfactuur 2026 VAT guide](https://winkelfactuur.nl/nl/blog/factuur-buitenland-btw-regels)):

- **€10,000/year threshold** (all EU countries combined) for B2C distance sales; above it, the **customer's country VAT rate** applies
- **The trap: crossing the threshold is retroactive for the entire calendar year** — Belgian-rate VAT suddenly owed on months of already-invoiced orders. Bol.be sales count toward the threshold; WiseQ (230 SKUs on bol NL+BE) plausibly crosses it. **Phase-0 must-check: current cross-border B2C revenue vs the threshold.**
- OSS registration = one quarterly Dutch return (deadlines: Q1→Apr 30, Q2→Jul 31, Q3→Oct 31, Q4→Jan 31), per-country revenue/VAT reporting, Belastingdienst redistributes
- Belgium specifics: standard rate also 21%, but reduced is **6%** (vs NL 9%) — matters if any WiseQ products qualify for reduced rates
- **And the bookkeeping leg is cheap:** bol→bookkeeping connectors exist from **€9.95/mo/koppeling** ([koppel-je-boekhouding.nl](https://koppel-je-boekhouding.nl/bol-com-koppelen-aan-boekhouding), 90-day trial) with per-line country-based VAT handling — reinforcing addendum 1's finding that the financial leg is configuration, not build, *if* WiseQ's stack is connector-supported (Moneybird/Exact/etc.)

**Design consequence for doc 04's pipeline:** the financial agent needs an **OSS-threshold watchdog** (running total of non-NL EU B2C revenue, alert at ~€8.5k with 6+ weeks left in year) — trivial to build, expensive to discover late. Added to the Phase-1 backlog.

---

## 4. The complete unit-economics picture (what's now known vs unknown)

| Coefficient | Status | Source |
|---|---|---|
| bol commission (fixed+variable) | ✅ Known bands; live read required | Addendum 5 |
| Payment fees (iDEAL/card/Bancontact) | ✅ Published; mix needs Phase-0 data | This addendum §1 |
| Shipping (PostNL bands) | ✅ Published | This addendum §2 |
| VAT regime (NL/OSS/B2B-verleging) | ✅ Rules mapped; WiseQ's position needs Phase-0 check | This addendum §3 |
| GS1/EAN | ✅ €225/yr whole catalog | Addendum 4 |
| Trustpilot / ChannelDock / Thuiswinkel / GS1 subscriptions | ✅ All live-pulled | Addendums 3–5 |
| **Product cost (COGS) per SKU** | ❌ Only Rob's data | Gate 0 |
| **Actual order volume/mix** | ❌ Only Rob's data | Gate 0 |
| **Bookkeeping package identity** | ❌ One question to Rob | Phase-0 call |

Every externally-researchable coefficient in the unit economics is now documented. What remains is deliberately gated on client data — exactly as the acceptance criteria (doc 23) require.

---

## 5. Ledger updates from this lane

| Row | Change |
|---|---|
| NEW 35 | PSP rates: iDEAL €0.29–0.35 (Stripe/Mollie), cards 1.5–1.8%+€0.25; **Bancontact: Stripe flat €0.35 vs Mollie 1.4%+€0.25 — provider choice on this one method outweighs card-rate differences at WiseQ basket sizes**. **VERIFIED** (published rates) |
| NEW 36 | PostNL 2026 business tariffs: brievenbuspakje €4.55, pakket ≤10kg €6.95–7.45, BE buspakje €9.50–10.00 (online frankering, excl. VAT). **VERIFIED** (official tariff booklet) |
| NEW 37 | OSS €10k threshold is retroactive for the calendar year once crossed; bol.be counts; quarterly Dutch filing. Phase-0 must-check + OSS-watchdog agent spec'd. **VERIFIED** |
| NEW 38 | bol→bookkeeping connectors exist from €9.95/mo with per-line country VAT handling — financial leg stays "configuration, not build" if stack is supported. **VERIFIED** |

*No messaging performed. Browser remains down (bol count row 4 STALE; screenshot QA pending). This concludes the externally-researchable economics tier.*
