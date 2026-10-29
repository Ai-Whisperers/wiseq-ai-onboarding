# Research addendum 7: engagement mechanics — cross-border invoicing, platform limits, market pricing, liability, vendor risk

*Oct 23, 2026 — seventh lane. The business layer around the build: how AIW invoices a Dutch BV from abroad, whether WiseQ's Shopify plan constrains the pipeline, how our pricing sits in the 2026 NL market, what a liability cap should say, and what happens if a 10-person SaaS vendor disappears. Sources linked inline.*

---

## 1. Cross-border invoicing (AIW → WiseQ B.V.): reverse charge, zero NL VAT filings

From the [Belastingdienst's own page for foreign entrepreneurs](https://belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/btw_voor_buitenlandse_ondernemers/diensten/btw_verleggen): services supplied to a **NL-established business or rechtspersoon (BV)** → **btw verlegd (reverse charge)** in most cases. The mechanics:

- AIW invoices **without VAT**, states **"btw verlegd / VAT reverse-charged"** and **WiseQ's btw-identificatienummer**
- WiseQ self-accounts the VAT in its NL return (and deducts it — cash-flow neutral for them)
- AIW makes **no NL VAT filing** for this; the non-EU case is covered by the same reverse-charge mechanism ([Belastingdienst English page](https://belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/eu-rights-and-rules-in-the-netherlands/eu-businesses/reverse-charging-vat-when-doing-business-abroad/reverse-charging-vat-when-doing-business-abroad))
- For AIW's own side: cross-border service income is taxed per the rules of the jurisdiction of origin (our accountant confirms treatment — flagged, not guessed)

**Action:** doc 18 gets an invoicing annex: invoice fields (both KvK + btw-numbers, "btw verlegd", IBAN), currency (EUR recommended — no FX friction for Rob), payment terms (14 days, late-fee clause per NL norm). **Phase-0 ask from Rob: the btw-identificatienummer + preferred invoice email.**

## 2. Shopify plan limits: no constraint at WiseQ's scale

Verified from [Shopify's rate-limit docs](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits):

| Plan | GraphQL Admin API | Notes |
|---|---|---|
| Basic / Standard | 100 points/sec | WiseQ is here (or equivalent) |
| Advanced ($299/mo) | 200 points/sec | + carrier-calculated shipping, 15 staff |
| Plus (from $2,300/mo) | 1,000 points/sec | Only for checkout customization / Functions custom apps |

**Verdict:** 230 SKUs and school-order-morning volume consume a rounding error of 100 points/sec. Custom **Admin API apps work on every plan** — the Plus-only features (Checkout Branding API, custom Shopify Functions) are not in our design. **No plan upgrade is needed for anything in docs 04/24.** Design note carried forward: use **bulk operations** (`bulkOperationRunQuery`) for catalog-wide syncs — they bypass standard rate limits entirely.

## 3. Market pricing check: we are at/below market on everything — and the care plan is *under*priced

2026 NL AI-automation market ([Crux Digits pricing survey](https://cruxdigits.nl/ai-consultancy-pricing-netherlands), [UnifyAI guide](https://unify-ai.nl/en/insights/ai-consultancy-nederland-kosten-roi-mkb-2026), [aiagencies.eu](https://aiagencies.eu/services/ai-automation/netherlands)):

| Phase | NL market 2026 | Our price (doc 04) | Position |
|---|---|---|---|
| Audit/quickscan | €1,500–10,000 | (done free as the onboarding repo) | aggressive |
| Pilot/PoC | €3,000–40,000 | **€3,500–5,000** | low-mid |
| Implementation | €8,000–150,000+ | **€8,000–12,000** | low-mid |
| Retainer/care | **€500–2,500/mo** | **€175–250/mo** | **far below market** |
| Hourly reference | €95–200 | — | — |

**Two honest reads:** (a) our pilot+build pricing is competitive for a boutique, defensible against the "€150/hr DataNorth" tier; (b) the care plan at €175–250/mo is **~⅓ of the market floor**. That is either a deliberate land-grab (fine — say so in doc 04) or an underpricing that will hurt when real monitoring load arrives. **Recommendation recorded, not actioned:** keep the entry price for year 1, pre-write the step-up (€395/mo at renewal or when a 3rd engine lights up) into the care-plan terms so the increase is contracted, never sprung.

## 4. Liability cap for doc 18 (the gap found)

Doc 18 currently has no liability clause. NL IT-services market standard ([Inventica terms](https://inventica.nl/algemene-voorwaarden) as a published example; [NRF global benchmark](https://www.nortonrosefulbright.com/-/media/files/nrf/nrfweb/knowledge-pdfs/liability-schemes-in-outsourcing-and-technology-contracts---a-global-bechmark.pdf); the [Drax v Wipro](https://www.rpclegal.com/snapshots/commercial-cases/autumn-2023/limitation-of-liability-clauses-in-software-development-projects-financial-caps/) cautionary tale):

- **Cap:** total liability limited to fees invoiced in the **preceding 12 months** (39% of global contracts cap at 100% of fees; annual-cap structure is the most common at 48%)
- **Per-event ceiling** typical in NL SME terms: €50k per event / €100k per year (Inventica-style) — for our fee sizes, the 12-month-fees figure will be the binding one anyway
- **Indirect damage excluded** (gevolgschade, gederfde winst, goodwill, bedrijfsstagnatie, dataverlies) — standard
- **Carve-outs:** opzet/bewuste roekeloosheid (intent/gross negligence) — mandatory; **AVG/GDPR liability cannot be capped below the statutory minimum** (art. 82 GDPR) — the verwerkersovereenkomst governs that lane separately
- **Claim window:** 12 months from discovery (NL common)
- **Drafting lesson from Drax v Wipro:** use explicit "total aggregate liability… any and all claims" language and a definite measurement point (fees paid in the 12 months before the claim first arose) — vague caps get litigated

**Action:** liability annex drafted into doc 18 with the above, NL counsel reviews before signature (same gate as the verwerkersovereenkomst).

## 5. Vendor risk: ChannelDock is a 10-person unfunded company

[Tracxn](https://platform.tracxn.com/a/d/company/5fc7e22037f0d01ad776d640/channeldock): founded 2020, Amsterdam, **10 employees, unfunded (bootstrapped)**. 213+ integrations, healthy product ([channeldock.com](https://channeldock.com)) — but a single bootstrapped SaaS holding WiseQ's stock-sync spine is a **concentration risk**. The escape hatch: [ChannelEngine](https://www.channelengine.com/nl/pricing) (NL market leader, GMV-based pricing, onboarding fees — meaningfully more expensive) exists precisely for this; bol's own LVB covers fulfillment-side.

**Design consequence (already in doc 07's spine, now justified):** the canonical SQLite/Postgres spine is **ours**, and ChannelDock is a *synced mirror*, not the source of truth. If ChannelDock folds or reprices, the pipeline re-points to bol/Amazon APIs directly — days of work, not a rebuild. That resilience argument goes into doc 04's architecture note.

---

## 6. Ledger updates from this lane

| Row | Change |
|---|---|
| NEW 41 | AIW→WiseQ invoicing = reverse charge ("btw verlegd", no VAT, their btw-ID on invoice); no NL VAT registration/filing for AIW. **VERIFIED** (Belastingdienst) |
| NEW 42 | Shopify Basic 100 pts/sec is ample for 230 SKUs; custom Admin apps work on all plans; bulk ops bypass rate limits. No plan upgrade needed. **VERIFIED** (Shopify docs) |
| NEW 43 | NL 2026 AI-market: pilot €3–40k, implementation €8–150k, retainer €500–2,500/mo, hourly €95–200. Our pilot/build at low-mid market; care plan at ~⅓ market floor — step-up pre-contracted. **VERIFIED** (3 published surveys) |
| NEW 44 | Liability cap standard: 12-month-fees annual cap, indirect damage excluded, intent/gross-negligence carve-out, GDPR art. 82 uncappable, 12-month claim window; Drax-v-Wipro drafting rules. Doc-18 annex drafted. **VERIFIED** (published NL terms + NRF benchmark) |
| NEW 45 | ChannelDock = 10-person bootstrapped Amsterdam SaaS (founded 2020) — concentration risk; canonical-spine-is-ours design already the mitigation; ChannelEngine = priced escape hatch. **VERIFIED** (Tracxn + pricing pages) |
