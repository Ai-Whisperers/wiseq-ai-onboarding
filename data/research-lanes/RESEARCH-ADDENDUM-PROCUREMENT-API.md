# Research addendum: procurement law, bol API mechanics, bookkeeping connectors, seasonality clock

*Oct 23, 2026 — follow-up lane after the external audit. Closes claims-ledger rows 4, 15 (partially), and adds two findings that change how the proposal should be pitched. All sources linked inline.*

---

## 1. School procurement law: the individual-school path is legally frictionless

**Finding:** Dutch primary schools are `aanbestedingsplichtig` (tender-obligated) as publiekrechtelijke instellingen — but only above the **European threshold of €221,000 excl. VAT** (2024 figure;leveringen/diensten for lagere overheden). Below that, schools buy `onderhands` (direct contracting) with full freedom. Source: [SURF handreiking inkopen onderwijs](https://www.surf.nl/files/2019-02/inkopen-onderdelen-van-de-leeromgeving.pdf) and municipal inkoopbeleid examples ([CVDR715573](https://lokaleregelgeving.overheid.nl/CVDR715573/1)).

**Why this matters for WiseQ:** a class set of headphones — the exact product of the 4-hour school-order mornings — is a €1–5k order, two orders of magnitude below the threshold. **No tender, no procedural burden: a school can buy from WiseQ as easily as from a local shop.** The friction in the school channel is *operational* (email → offer → invoice → re-keying), not legal. That is precisely what the proposed pipeline automates.

**The strategic boundary this confirms:** the big money — multi-year `raamovereenkomsten` for leermiddelen, e.g. [Stichting Primenius €9.14M, won by Heutink](https://tenderview.ai/aanbestedingen/ea-leermiddelen-stichting-primenius-g35v2jvs) — goes through European tender and is won by institution-grade total suppliers (Heutink, ~100 yrs, totaalleverancier). Doc 09's "can't out-catalog Heutink, out-niche them" now has its legal footing: **the sub-threshold individual-school market is where an SME wins, and it's procedurally wide open.** Size that market in Phase 0 (DUO data already in `RESEARCH_LEADS-DUO.md` covers ~8,700 basisscholen-adjacent orgs).

**One caution:** under-threshold purchases still require schools to follow their own internal inkoopbeleid (many require 3 quotes above €1–5k, invoice-term preference, etc.). The offer pipeline should therefore emit *quote-ready* PDFs with quote references — a small design requirement for doc 04, noted for Phase 1.

---

## 2. bol Retailer API: mechanics confirmed, demo environment exists

**Finding:** the [bol Retailer API v10](https://api.bol.com/retailer/public/redoc/v10/retailer.html) exposes exactly the endpoints the school-order and repricing agents need: offers (CRUD + price/stock update), orders (list/get/cancel), shipments (create/list), invoices (upload), shipping labels, plus product-rank insights. OAuth2 via a bol retailer account. Two operationally important details from the [functional docs](https://api.bol.com/retailer/public//Retailer-API/index.html):

- **A demo environment mirrors all endpoints** (except PDF responses) — Gate 1.2 of the [acceptance criteria](../../docs/60-governance/02-acceptance-criteria.md) can be exercised *before* touching live data, the moment we have any retailer account access.
- **Processing is asynchronous** (process-status polling after every write) — the agent design must treat writes as confirm-later, which fits our existing guardrail pattern (never assume success).

**Ledger effect:** claim "bol integration = 2–3 week custom client" (doc 08) stays, now with endpoint-level confirmation.

---

## 3. Bookkeeping: the 5X inconsistency resolved, and a cheaper path exists

**Internal inconsistency found:** [doc 08](../../docs/30-market/01-oss-integrations.md) states 5X *has* a first-party "API Links" section; [doc 04](../../docs/20-offer/01-blueprint.md) flags 5X's API as **unverified**. Both are half-right, and the distinction matters:

- 5X **consumes** APIs (it accepts bol.com Client ID/Secret and pulls orders/ads/finance into itself — a client, not a server).
- Whether 5X **exposes** an API we can read from is **still unresolved**. Ledger row 15 stays open until Gate 1.2 tests it.

**The de-risk:** if WiseQ's bookkeeping is (or moves to) **Exact Online**, mature Shopify↔Exact connectors already exist from **€12/mo** ([iWebDevelopment](https://iwebdevelopment.com/koppelingen); also a [Shopify App Store listing](https://apps.shopify.com/exact-online-3)) covering orders, customers, items, stock, and VAT/OSS codes. That would make the bookkeeping step a **configuration, not a build** — and strengthens doc 04's Phase-0 question "which bookkeeping package do you actually run?" into a genuine cost fork: Exact Online = €12/mo connector vs. 5X = custom bridge vs. CSV = manual drift.

---

## 4. The seasonality clock is NOW

Doc 12's peak-season calendar says gift-bundle SKUs get merchandised **from Oct 15**. Today is Oct 23 — **WiseQ is inside the Sinterklaas/Black-Friday/Christmas window with 25 unmerchandised bundles and 0/230 EANs on the marketplace side.** Toys & games is one of bol's strongest Sinterklaas/Christmas categories ([category seasonality data](https://boloo.co/en/blog/waar-is-veel-vraag-naar-producten)); Q4 is the make-or-break quarter for NL webshops ([RTL Z](https://rtl.nl/nieuws/rtl-z/artikel/5658741/feestdagen-webshop-bol-checkout-sokkendirect-ai-optimalisatie)).

**Honest framing:** this does NOT mean "hire us and save this Q4" — the acceptance gates (docs 23) take weeks, not days, and rushing into peak is how errors reach customers. The honest version for the send note: *every week of delay moves the first measurable win deeper into Q1; the pilot's review point lands after peak, when the summer dip gives a clean maintenance window.* What peak-timing DOES justify now: the EAN/GTIN registration and bundle content fixes (fast, low-risk, high-peak-leverage) as a standalone pre-pilot micro-engagement, if Rob wants motion before Phase 0.

---

## Ledger updates from this lane

| Row | Change |
|---|---|
| 4 (bol 312 listings) | Still STALE — seller page remains bot-walled; browser pull pending |
| 15 (5X API) | Nuanced, not resolved: 5X consumes APIs (confirmed); exposes-none unconfirmed. Phase-0 question upgraded to a cost fork (Exact Online €12/mo vs 5X build) |
| NEW — procurement | Sub-€221k school purchases need no tender (VERIFIED, sources above); individual-school market is procedurally open — pipeline automates the real (operational) friction |
| NEW — seasonality | Q4 peak window active as of mid-Oct; first measurable pilot win realistically Q1 2027 |
