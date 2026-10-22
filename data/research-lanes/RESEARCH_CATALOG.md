# WiseQ — Product Catalog, Pricing & Data Quality

**Lane:** Catalog (parent-side recovery — dispatched subagent died to an instant HTTP 429; analysis run directly on the saved `products.json` artifact).
**Date:** 2026-10-21 · **Source:** https://www.wiseq.nl/products.json?limit=250 (230 products, 1,016 KB raw artifact: raw-products-parent.json)

---

## 1. Executive summary

The Shopify catalog holds **230 products, 100% vendor "WiseQ"** (full own-brand white-label operation). It was **bulk-created in a single migration sprint: 189 of 230 products (82%) date to September 2025**, with only ~40 products added since — confirming the 2025 replaunch. The catalog is really **two businesses in one shop**: (A) the branded kids-tech line the site fronts (23 kids headphones, tablets, smartwatches, hearing protection), and (B) a **long-tail charger/cable/accessory operation (114 products = Oplaadset 76 + Oplaadkabel 38)** that drives marketplace volume. Data quality has systemic gaps that map exactly to the automation opportunity: **zero inventory tracking in Shopify, zero EAN barcodes, zero product weights, per-color products instead of variants, and SKU bugs** — plus hidden internal products (school orders, samples, a €1,390 outlier) exposed in the public feed.

---

## 2. Catalog composition (230 products, by type)

| Product type | n | Price min–max (€) | Median |
|---|---|---|---|
| Oplaadset (charger set) | 76 | 9.95–33.95 | 17.95 |
| Oplaadkabel (charge cable) | 38 | 6.95–14.95 | 9.95 |
| Kinderkoptelefoon (kids headphone) | 23 | 18.95–49.95 | 24.95 |
| USB-adapter | 16 | 7.50–21.95 | 11.95 |
| Tablethoes (tablet case) | 9 | 17.65 | 17.65 |
| Draadloze lader (wireless charger) | 9 | 18.95–37.95 | 27.95 |
| GPS tracker | 9 | 17.11–41.95 | 26.95 |
| Gehoorbescherming (hearing protection) | 8 | 21.95 | 21.95 |
| USB-hub / charging stations | 7 | 12.99–399.00 | 45.95 |
| Audiokabel | 6 | 5.95–10.95 | 7.95 |
| Kindertablet | 4 | 124.95–159.95 | 159.95 |
| Laptopkar (laptop cart, schools) | 3 | 550–1,149 | 899 |
| Smartwatch | 3 | 74.95 | 74.95 |
| Koptelefoon (adult ANC) | 2 | 63–109 | 109 |
| Koptelefoon opbergsysteem/storage | 2 | 399 | 399 |
| Cases, holders, earbuds, misc | 7+ | 4.95–29.95 | — |
| Internal types: Schoolbestelling, Toeslag, (none) | 9 | 0–1,390 | — |

**Reading:** chargers+cables = **49.6% of the catalog** but a €7–34 price band; kids audio = the brand story with €19–50 price points; the B2B gear (laptop carts €550–1,149, storage systems €399, 16-port hubs) is high-ticket with completely different economics. The kids headphones are the margin/brand core; the charger long tail is the volume/marketplace play.

## 3. The flagship line: kids headphones (23 SKUs, 5 families + samples)

| Family | Price | Positioning |
|---|---|---|
| Junior (3 colors) | €18.95 | Wired, ages 3–9, "hufterproof" |
| One (3) | €19.95 | Wired, flexible, 3–15 yrs |
| BTwireless (6) | €19.95–24.95 | Wireless entry, 8h battery |
| Hero (5) | €27.95 | Wireless, 38h battery |
| Unbreakable (3) | €34.95 | Wireless, 45h, 93→85 dB switch |
| Kids ANC (3) | €49.95 | Wireless ANC flagship, 35h |
| Adult line: ANC.Sports / ANCx100 | €63 / €109 | Legacy adult audio ("Turn Music into Magic" era) |

Clean good-better-best ladder (€19→€28→€35→€50). Each color is a **separate product with exactly 1 variant** — no color variants on one product — which multiplies listings (marketplace-friendly, PDP-unfriendly) and matches the "same product, many listings" marketplace pattern.

## 4. Bundle architecture (the audio transcript's pain, quantified)

- **77 products (33%) carry bundle keywords** (set/bundel/combo/pack/duo) in title or tags.
- The Oplaadsets are **systematic combinatorial bundles**: one adapter × cable type (USB-C/Lightning) × length (1M/2M/3M) × color — e.g. `38W Snellader 3 Poorten` exists as SKU 371/372/373 for 1M/2M/3M, each a separate "product". 76 Oplaadsets = the cross-product of ~16 adapters × cable options.
- Consequence: when **one adapter or cable component goes out of stock, dozens of bundle listings silently break** — and since Shopify holds no component link (there is no bundle machinery visible), the component→bundle mapping must live **out-of-band in ChannelDock** (or worse, in someone's head). This is precisely the "bundle goes OOS, match the individual cables" problem described in the audio.

## 5. Data quality audit (the automation wedge)

| Check | Result | Implication |
|---|---|---|
| EAN/barcode populated | **0/230** | Marketplace feeds can't match on GTIN; bol/Amazon matching is by title/brand — fragile, duplicate-prone |
| `inventory_management` | **None on all 230** | Shopify tracks NO stock — inventory truth is entirely external (ChannelDock); the shop can oversell or undersell silently |
| Weight (`grams`) | **0 on all 230 variants** | No carrier-calculated shipping possible; shipping costs are flat guesses |
| SKU scheme | Mixed: numeric (371-373), dotted (`Tab.Hoes.Groen10.2`), named (`SCHOOL-TAMARISK`, `Sample.Kids.ANC.Black`) | 3+ incompatible conventions in one catalog |
| SKU bug | `Tab.Hoes.<color>10.2` used on **10.9-inch** products (color/size swapped in the pattern) | Real data corruption in variants; an automated QA would flag instantly |
| Options/variants | Almost none — single-variant products; option axes exist only as 6× "Titel" + 1× "School" | Color/length are separate products instead of variants → no shared reviews/stock per family |
| Body/description | median 953 chars, 20 products EMPTY, only 23/230 use H2/H3 structure | 20 publishable products with no description; structure inconsistent — LLM-assisted rewrite is high-leverage |
| Prices | €0.00 on internal items (Schoolbestelling, Toeslag €3.57), €1,390 outlier in "(none)" type | Internal/scaffold products leak into the public products.json and potentially into feeds |
| Hidden B2B products | `Sample.*` (5 school sample SKUs), `SCHOOL-TAMARISK` (named school account as a product) | School orders are being run through hidden Shopify products — manual bookkeeping workaround, automatable |

## 6. Catalog growth trajectory (created_at)

```
2025-09: 189  ← migration/replatform sprint (82% of catalog)
2025-10..2026-10: ~40 products, steady 1-8/month dribble
```
The shop is in **maintain-and-expand mode**: ~1 new product/week at best, with B2B items (laptop carts, hubs, sample SKUs) appearing through 2026. AI imagery on the marketing surface (ChatGPT/Gemini filenames in hero/collection assets — though product-gallery images carry clean renamed filenames: 0 AI-tool filenames across 1,277 product images).

## 7. What this means for the engagement

1. **The single-source-of-truth problem is structural**: Shopify = display layer only (no stock, no EAN, no weights); ChannelDock = inventory truth; bol/Amazon = legacy channels with their own listings (312 articles on bol > 230 in shop). Any automation starts with a **canonical product registry keyed on a generated internal GTIN map** — exactly what the audio's EAN work already gestures at.
2. **Bundle component math is automatable today**: the combinatorial Oplaadset structure is regular enough to reverse-engineer (SKU sequences, title patterns, tags) into a component graph; OOS propagation becomes a script, not a human.
3. **20 empty descriptions + 207 unstructured ones** = a week of LLM-assisted copywriting with the agents.md spec table as ground truth.
4. **Variant consolidation** (6 BTwireless colors → 1 product, 6 variants) would concentrate reviews/SEO and cut feed noise — a measurable A/B they could run with their "B2B meetbaar" experiment culture.

---

## Sources

1. https://www.wiseq.nl/products.json?limit=250 — 230 products, fetched 2026-10-21 (artifact: raw-products-parent.json, 1,016 KB)
2. https://www.wiseq.nl/agents.md — model/spec ground truth
3. Cross-lane: RESEARCH_COMPANY.md (replatform timeline), RESEARCH_MARKETPLACES.md (bol 312 articles), parent-techstack.json

**Source count:** 3 direct + 1 primary artifact analyzed in full (230 products, 1,277 images, 228 SKUs).
