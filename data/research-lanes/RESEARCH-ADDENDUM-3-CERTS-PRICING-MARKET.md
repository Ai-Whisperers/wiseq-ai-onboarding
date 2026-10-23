# Research addendum 3: certification cost bands, Trustpilot's real floor, market sizing, and a policy tailwind

*Oct 23, 2026 — third lane. Fills the TCO's largest "deliberately excluded" line with sourced bands, replaces the audit-flagged vague Trustpilot figure with the actual tariff, sizes the school market with fresh DUO/CBS data, and documents a one-week-old national policy that plays directly to WiseQ's category. All sources linked inline.*

---

## 1. Certification / lab-testing cost bands (the TCO's biggest known-unknown, now bounded)

Doc 04's TCO excluded lab testing as "uncosted until real quotes exist." It can now be **bounded**, per category, from 2026 market guidance:

| Product class at WiseQ | Regime | Indicative cost band (excl. VAT) |
|---|---|---|
| Simple toys (non-electronic) | Toy Safety Dir. 2009/48/EC (EN 71 parts) | **€500 – €3,000** per product |
| Electrically-powered products (kids tablets, headphones w/ electronics) | EN 62115 + EN 71 | **€1,000 – €5,000** (LVD+EMC analogue band) |
| **Radio/Bluetooth/WiFi products (most of WiseQ's catalog)** | RED 2014/53/EU | **€2,000 – €8,000** per product |
| Radio products where harmonised standards are NOT fully applied | RED → Notified Body (Module B) | **€8,000 – €18,000** per product |
| Worn radio transmitters (if any product is worn <20cm from the body) | RED + SAR testing | **€4,000 – €10,000 per configuration** |

Sources: [Zoloo CE-cost guide 2026](https://zoloo.co/en/blog/ce-keurmerk-aanvragen-kosten), [Cenitia notified-body guide](https://cenitia.com/library/when-you-need-a-notified-body), [Spilma RED test overview](https://spilma.com/en/red/tests), [Amazon toy-compliance summary](https://cataloops.com/blog/amazon-toy-compliance-2026).

**What this means for the proposal — three honest points:**

1. **Scale of the exposure.** If WiseQ's 114-component catalog is majority-Bluetooth (headphones, tablets, trackers), full RED compliance testing at midpoint ≈ €5k × ~100 SKUs ≈ **€500k** — which is why nobody does a whole catalog at once. The realistic path is **triage by risk**: existing DoCs from suppliers (WiseQ is likely an importer, not manufacturer, for much of the catalog — importer obligations are lighter), then testing only where gaps are real. That triage is itself an agent-sized task (gather DoCs per SKU, map to product class, flag gaps) — a **Phase-2 engine candidate**, not a Phase-1 promise.
2. **Amazon's annual-testing requirement** ([source](https://cataloops.com/blog/amazon-toy-compliance-2026)) requires ISO 17025 lab reports for EN 71 (+EN 62115 for electric) per toy ASIN — WiseQ sells on Amazon with 2020-era ASINs (doc 07 §4), so **some SKUs may already be non-compliant on Amazon today**. That's a discovery task for Phase 0, not a guess.
3. **Timing honesty, again:** notified-body routes take weeks-to-months (2–6 weeks lab time alone). Nothing about certification lands inside Q4. It reinforces the addendum-1 seasonality framing: Q4 = content/EAN fixes; certification triage = Q1 maintenance-window work.

**Ledger:** new row — certification cost bands VERIFIED (as published guidance, not quotes); TCO exclusion note in doc 04 now points to these bands.

---

## 2. Trustpilot's real pricing: the $0–799 band now has a floor

Live tariff ([business.trustpilot.com/pricing](https://business.trustpilot.com/pricing), pulled Oct 23, 2026):

| Plan | Price (12-mo commitment) | Invitations/mo |
|---|---|---|
| Starter | **$99/mo** | 100 |
| Plus | $319/mo | 300 |
| Premium | $799/mo | 1,000 |
| Enterprise | Contact sales | Unlimited |

**Implications for the review-engine math (doc 04/05):**

- The honest invitation budget for a 230-SKU shop at WiseQ's order volume is **Starter ($99/mo ≈ €92)**: 100 invitations/month against an order volume that plausibly fits inside it (Phase 0 measures actual monthly orders).
- **Conversion reality check:** at the typical 5–15% invitation→review conversion, 100 invitations ≈ 5–15 new reviews/month ≈ 60–180/year. The retired "250+ in a quarter" target would need the $799 tier AND an exceptional conversion — confirming the ledger's decision to retire it. The honest KPI is **invitation coverage**, not review counts (doc 05's position, now priced).
- Note the 12-month commitment: the TCO should show Trustpilot Starter as **~€1,100/yr** if the review engine runs, or €0 if deferred. Doc 04's care-plan table gets a footnote.

---

## 3. Market sizing: the school channel, with 2025/26 numbers

**The population** ([DUO via OCW in Cijfers](https://www.ocwincijfers.nl/sectoren/primair-onderwijs/leerlingen/aantallen-ontwikkeling-aantal-leerlingen)): 1,464,307 PO leerlingen in 2025 (basisonderwijs 1,357,024 — **first increase since 2010**, +2,739). The DUO org data already in `RESEARCH_LEADS-DUO.md` (~8,700 orgs) covers this population's institutions.

**The budget context** ([Versterkingsagenda coverage](https://eusvanhove.nl/versterkingsagenda-wie-geeft-er-les-in-het-vmbo)): €12.1 billion flows to primair onderwijs annually. Schools are explicitly instructed to spend "evidence-informed" on basics (taal/rekenen). A safe-audio category (WiseQ's core) maps to *concentratie/leesvaardigheid* use-cases — which is exactly the framing the new agenda emphasizes.

**The policy tailwind (one week old):** on Oct 16, 2026 staatssecretaris Tielen sent the **"Samen sterk voor Taal" Versterkingsagenda** to Parliament ([PO-Raad](https://www.poraad.nl/), [Nationale Onderwijsgids](https://nationaleonderwijsgids.nl/basisonderwijs/brede-aanpak-moet-taalvaardigheid-van-leerlingen-een-boost-geven)): renewed kerndoelen, referentieniveaus revision starting najaar 2026, and *30–70% of pupils must reach streefniveau* depending on school. Reading/listening-concentration tools (kids' headphones for taal-software, class sets) ride this wave directly.

**How to use it honestly:** the agenda does NOT fund headphones — it creates *attention and budget priority* for taal tools. The sales narrative for school offers becomes: "safe-audio class sets as part of the taal-versterking toolkit, quote-ready, 24h delivery." Not a compliance claim; a positioning note for doc 09 and the school-offer templates in Phase 1.

**Rough TAM sanity check (clearly labeled arithmetic, not a promise):** ~6,800 basisscholen (DUO), assume 10% ever buy a class set in a given year at ~€1,500 avg → ~€1M/yr addressable niche for the safe-audio class-set segment. Small — but an order of magnitude above a single school's €1–5k orders, and it's a *recurring* re-order channel (breakage, expansion). This is the "out-niche Heutink" segment sized for the first time.

---

## 4. Ledger updates from this lane

| Row | Change |
|---|---|
| NEW 24 | Certification cost bands per product class (RED €2–8k standard, €8–18k notified-body, SAR €4–10k/config) — VERIFIED as published guidance; doc 04 TCO note updated to point here |
| NEW 25 | Trustpilot Starter $99/mo = 100 invitations/mo, 12-mo commitment — VERIFIED (live pricing page); review-engine budget floors at ~€1,100/yr; retired 250+ target confirmed impossible at Starter tier |
| NEW 26 | NL PO market: 1.46M leerlingen 2025 (first rise since 2010); €12.1B PO budget; Versterkingsagenda Taal (Oct 16, 2026) creates tailwind for taal-tool categories — VERIFIED |
| NEW 27 | ChannelDock pricing re-confirmed live Oct 23: free ≤500 orders/mo, Voorraad from €45/mo, PIM €200/mo — matches doc 08 (no drift) |

*Browser-dependent items still blocked: bol listing count (row 4), any screenshot QA. No messaging performed — documentation only, per operator instruction.*
