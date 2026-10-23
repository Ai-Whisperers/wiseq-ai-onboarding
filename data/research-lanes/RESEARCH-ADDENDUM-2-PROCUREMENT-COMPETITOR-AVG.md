# Research addendum 2: school procurement thresholds 2026/27, the 3-quotes myth, Heutink's API, and the AVG contract layer

*Oct 23, 2026 — second follow-up lane. Corrects one of our own working assumptions (the 3-quotes rule), updates the EU threshold to the 2026/27 figure, discovers the competitor's public API, and maps the GDPR/AVG contract layer the engagement needs on day one. All sources linked inline. Browser-dependent verification (bol listing count) remains blocked — see §5.*

---

## 1. Procurement thresholds: the 2026/27 update, and why the individual-school path is even more open than addendum 1 said

**The EU threshold moved.** For 2026–2027 the European tender threshold for leveringen en diensten (lagere overheden / onderwijs) is **€216,000 excl. VAT**, not €221,000. Source: [Scholengroep Veluwezoom inkoopbeleid 2026-2027](https://scholengroepveluwezoom.schoudercom.nl/documenten/895759-260210-al-ms-inkoopbeleid-veluwezoom-dot-pdf) (table 2.2, "Drempelbedragen voor 2026-2027", with the note that the EU resets thresholds every two years).

**The internal ladders are more permissive than assumed.** The same school-group policy shows a typical modern internal ladder:

| Opdrachtwaarde (excl. btw) | Procedure |
|---|---|
| < €33,000 | **Enkelvoudig onderhands** — one quote, full freedom |
| €33,000–50,000 | Single OR multiple underhand (motivated choice) |
| €50,000–216,000 | Meervoudig onderhands (3–5 quotes) |
| ≥ €216,000 | European tender |

A second published policy ([Samenwerkingsverband swv2804](https://swv2804.nl/wp-content/uploads/sites/13/2022/07/inkoop-en-aanbestedingsbeleid.pdf)) even allows single-quote up to **€170,000** for its own purchases. Thresholds vary per board — but the pattern is consistent: **the sub-€33k band, where every WiseQ class-set order lives, is single-quote territory in modern school policies.**

**The correction to our own note:** addendum 1's caution ("many schools require 3 quotes above ~€1–5k") was **wrong** — that pattern belongs to municipal/Brussels practice (e.g. [Sint-Goedele Brussel](https://sint-goedele.brussels/overheidsopdrachten/): 3 quotes above €3,000), not to Dutch *basisschool* boards, whose current policies go single-quote far higher. Ledger updated. The design implication survives in weaker form: quote-ready PDFs with references are still good practice (schools must keep *bewijs* of price comparisons on file), but they are **not** a legal requirement at class-set order values.

**The anti-splitting rule is the real legal boundary — and it cuts in WiseQ's favor.** `Saucissoneren` (artificially splitting to dodge thresholds) is prohibited, and — critically — **orders from multiple schools under one bestuur must be aggregated** when computing the threshold. Consequence: the pipeline should treat *each school* as its own customer with its own order history, and flag if a single bestuur's aggregated annual purchases approach €33k/€50k/€216k internal thresholds. That's a cheap query once the data spine exists — and it protects WiseQ from the one realistic compliance risk in the channel.

---

## 2. Heutink has a public developer API — the competitor's machine-to-machine door is open

**Finding:** [developers.punt-uit.nl](https://developers.punt-uit.nl/) documents a public **Heutink API** (v4 current, v3 legacy): authentication via access token, resources for **Products, Inbounds, Outbounds, Shipments, Receipts, Labels, Subscriptions**, plus **webhooks** and a published Postman collection. Hosted under the *punt-uit.nl* domain (Heutink's B2B order platform).

**Why it matters — three ways:**

1. **It validates WiseQ's own UCP/MCP direction.** Doc 07 records that WiseQ already runs UCP + MCP shopping endpoints (verified live in our research). Heutink — 115 years old, 30,000 products, 130,000 transactions/year, 5,000 order lines/hour in peak ([Intershop case study](https://www.intershop.com/en/customers-details/heutink)) — publishing a token-authenticated API with webhooks confirms that **machine-to-machine school procurement is where the NL education market is moving.** WiseQ is not early; it is on time.
2. **It sharpens the moat story.** The pitch is no longer "Heutink can't do agentic reordering" (doc 09 §73) — Heutink's API makes agentic reordering *possible* for them too. The honest moat: WiseQ + AIW can **operate** the agentic layer end-to-end (orders in → offers out → stock propagated → bookkeeping drafted) with a 4-hour→15-min school pipeline, while Heutink's API is a building block schools/integrators must assemble themselves. Update doc 09's counter-strategy wording accordingly (flagged in ledger).
3. **It's a Phase-2 research lane, not a promise.** The API's terms, rate limits, and whether a *competitor's* account can legitimately query Heutink catalog/pricing are unverified. Park it: if WiseQ ever needs price-intelligence on Heutink class-set SKUs, the door exists.

**Ledger effect:** new row — "Heutink operates a public API (punt-uit.nl)" — VERIFIED (portal + docs inspected). Doc 09's "Heutink can't [do agentic reordering]" downgraded to INFERRED→**corrected**.

---

## 3. The AVG/GDPR contract layer: what the engagement needs on day one

**Finding:** the moment AIW processes any personal data for WiseQ (customer names/emails in orders, teacher contact data in school orders), AIW is a **verwerker** (processor) and a written **verwerkersovereenkomst** under art. 28 AVG is **mandatory** — regardless of contract name, the AP looks at the factual situation ([AP-aligned model guidance](https://captain.legal/nl/bedrijfsbeheer/verwerkersovereenkomst-avg-opstellen-word-en-pdf)). Key obligations to pre-write into doc 18's terms:

- Precise description of verwerkingen (order data, contact data — NOT payment credentials), duur, and betrokken categories
- Art. 32 security measures; sub-processor regime (name our hosting + AI-provider chain explicitly — Claude/OpenAI/Anthropic must appear as sub-verwerkers)
- Data-leak meldplicht "onverwijld" (so WiseQ can hit its 72-hour AP window), audit rights, and teruggave/vernietiging at exit (aligns with doc 18's escrow/handover design)
- **DORA overlap (since Jan 17, 2025):** Verordening (EU) 2022/2554 adds ICT-contract requirements (exit strategy, access rights, incident chains) that art. 28 AVG only partially covers — two referenced documents beat one hybrid ([source](https://captain.legal/nl/bedrijfsbeheer/verwerkersovereenkomst-avg-opstellen-word-en-pdf))
- School-specific practice confirmed: Veluwezoom's policy §Bijlage 2 explicitly requires a verwerkersovereenkomst before any supplier processes persoonsgegevens — **schools will ask WiseQ for proof AIW is a compliant sub-processor; having the contract ready accelerates school deals**

**Action recorded:** draft an art.-28-compliant verwerkersovereenkomst as an appendix to doc 18 before signature (template basis: [NBA model](https://nba.nl/tools-en-voorbeelden/model-bewerkersovereenkomst) + AP structure). Not legal advice — NL counsel reviews before Rob signs anything.

---

## 4. Bookkeeping connector economics (completing addendum 1's cost fork)

Addendum 1 established the Exact Online connector path (€12/mo). This lane adds the decision rule for Rob's Phase-0 call:

| If bookkeeping is… | Connector status | Cost | Pipeline effort |
|---|---|---|---|
| Exact Online | Mature (iWebDevelopment, Shopify App Store) | ~€12/mo | **Configuration** — bookkeeping step ≈ free |
| 5X | Consumes APIs (confirmed); exposes-none untested | €0–? | Custom bridge or CSV export loop |
| Anything else | Per-package check | varies | Case-by-case |

The single highest-leverage question in the first Phase-0 call: **"Welk boekhoudpakket draai je?"** — it decides whether the flagship pipeline's financial leg is a €12/mo config or a multi-week build.

---

## 5. Blocked: bol listing count re-verification

Ledger row 4 (312 bol listings vs 230 shop) remains **STALE**. Bol's seller pages bot-wall keyless HTTP (403) and the local browser harness is down (no Chromium process — environment issue). Options when the browser returns: (a) manual count by a human on any machine, 5 minutes; (b) browser pull via the harness. **Until then, the 312 figure must not be quoted as current** — the send note should reference "312 as of Oct 21" or omit.

---

## Ledger updates from this lane

| Row | Change |
|---|---|
| 19 (procurement thresholds) | **Updated:** EU threshold €216k for 2026/27 (was €221k); sub-€33k = single-quote in modern school policies; 3-quotes-above-€1-5k assumption **retracted** (Brussels/municipal pattern, not basisschool) |
| NEW 21 | Heutink public API (punt-uit.nl): products/shipments/webhooks — **VERIFIED**; doc 09 counter-strategy wording correction flagged |
| NEW 22 | Aggregation/saucissoneren rule: multi-school orders under one bestuur aggregate toward thresholds — pipeline design requirement (per-school order ledger + threshold proximity flag) |
| NEW 23 | AVG art. 28 verwerkersovereenkomst mandatory day-one; DORA 2022/2554 adds ICT-contract terms; schools (Veluwezoom Bijlage 2) require proof from suppliers — pre-draft as doc 18 appendix |
| 4 (bol count) | Still STALE — browser harness down; do not quote 312 as current |
