# WiseQ Mastersheet — structured extract

*Source: `Mastersheet.xlsx` (WiseQ ops workbook), described by client 2026-10-27 as the sheet for SEO keywords, shipping-price vs delivery-time decisions, ChannelDock shipping-rule templates for new SKUs, and warehouse box/envelope order links.*

**Full `.xlsx` is not committed** (2.1 MB; contains gift-card codes, promo codes, contact matrix, COGS, customer lists). Public-safe CSV exports: [`mastersheet/`](mastersheet/).

---

## Workbook map (21 sheets)

| Sheet | In public export? | Purpose |
| :--- | :--- | :--- |
| **Verzendtarieven & Verzendstrate** | ✅ `verzendtarieven.csv` | LVB / VVB / QLS / PostNL costs NL vs BE; LVB storage; BE LVB ROI notes |
| **Verzendregels Channeldock** | ✅ `verzendregels-templates.csv` | Clone-from-EAN templates when inserting new products |
| **Bestelformulier dozen** | ✅ `bestelformulier-dozen.csv` | MyParcel / Verpakgigant order links for boxes & envelopes |
| **Zoekwoordanalyses** | ✅ sample | iPhone / charger / cable keyword clusters + volumes |
| **Zoekvolume Google** | ✅ filtered | Google Ads keyword planner dump (headphones/school/autism slice) |
| **Prijsverhogingen** | ❌ (log only here) | Manual price brakes — overlaps FiveX auto +10% ≤10 stock |
| **BOL LVB BE** | ❌ summary only | Candidates / rules for BE LVB (price &lt; €16 nuance) |
| **Title update** | ❌ | Listing title ↔ EAN/reference working table |
| Kaartnummers / Kortingscodes / Contact matrix / Inkoopprijzen / Sales klanten | ❌ never | Secrets / PII / margins |
| Schoolbestellingen, Opvolging reviews, Wederverkopers, … | ❌ private | Ops working tabs |

---

## 1. Shipping price vs delivery promise

Decision frame from the sheet + manual:

| Promise | Typical carrier path | When used |
| :--- | :--- | :--- |
| **Order before 15:00 → next day (NL)** | Own warehouse / QLS / VVB NL | WiseQ NL default |
| **Order before 00:00 → next day** | **Bol LVB** | NL LVB; BE LVB when conversion math wins |
| **2–3 days** | Own BE brievenbus / VVB BE | WiseQ Electronics default without LVB |

### Tariff snapshot (from sheet — € excl. nuance columns)

| Mode | Size / type | Assortment | NL € | BE € | Notes |
| :--- | :--- | :--- | ---: | ---: | :--- |
| LVB | 3XS | Chargers | 2.78 | 5.11 | Storage €0.14; &lt;€16 LVB NL 2.58 |
| LVB | 2XS | MagSafe | 3.52 | 5.11 | |
| LVB | XS | Wireless earbuds | 5.11 | 5.11 | |
| LVB | S | Unbreakable/Hero/Junior/Kids ANC | 6.27 | 6.27 | |
| LVB | M | BT Wireless / Hardcase | 6.59 | 6.59 | |
| VVB | Brievenbus boxes | Chargers | 3.77 | 6.33 | |
| VVB | Parcel NL | Headphones | 5.56 | — | |
| VVB | Parcel BE | Chargers + headphones | — | 6.33 | |
| QLS | Brievenbus env. | Chargers &gt;50g | 2.61 | 4.35 | |
| QLS | Brievenbus boxes | Multi chargers | 2.99 | 4.35 | |
| QLS | Parcel | Headphones | 4.61 | 4.75 | |
| QLS | Europlus | **School shipments** | 10.54 | 10.54 | |
| PostNL | Partijenpost &lt;50g | Light cables / adapters | 1.85 | 4.42 | |
| PostNL | 50–100g | Combos / heavy cables | 2.32 | 4.42 | |
| PostNL | 100–200g | Heavy combos | — | 5.01 | |
| PostNL | 200–350g | Heavy combos | — | 6.21 | |

**Client ROI notes on sheet:** BE LVB (2–3 days → next day) claimed **+178% sales**; under €16 BE LVB pick&pack pricing differs from above €16 (sheet: €4.45 vs €3.63 example).

**Agent design:** nightly/weekly job = for each SKU × channel, compare *(carrier cost + storage + fee)* vs *(promised delivery band)* and flag misaligned ChannelDock rules or LVB candidates — exactly the “shippingprice vs deliverytime” check Rob described.

---

## 2. ChannelDock shipping rules for new products

Sheet note: *“deze tabel is gekoppeld aan handleiding”* — clone shipping rules from a **template EAN** by product class:

| New product class | Clone from (template EAN) | Caveats |
| :--- | :--- | :--- |
| Light cables | 8720254493077 (≈207) | |
| Heavy cables | 8720618246615 (≈215) | |
| 2× cable | 8720618849403 (≈2×208) | BE double-cable incomplete → rule **108** |
| 3× cable | 8720618849465 | |
| Adapters &lt;50g | 8720165910113 (≈101) | |
| Adapters &gt;50g | 8720618246110 (≈106) | Also refs 88,89,92,94,114,116 |
| Charge combo | 8720254493947 (≈310) | |
| Headphone case | 8720618849304 (N.Case) | HERZIEN — rule ids listed |
| Headphones | 8720618849083 (Unbreakable) | |
| MagSafe | 8720254493619 (≈231) | |
| MagSafe combo | 8720618246677 (≈331) | |
| USB hubs / smartwatch / tag | case-by-case | |

**Qty × country behaviour** (1 / 5 / 10 pcs, NL vs BE) lives **inside ChannelDock** on those template products (brievenbus vs parcel thresholds). New SKUs must inherit the correct template so ChannelDock auto-assigns labels — this is the “ungefrankeerde zendingen” prevention path from the manual.

**Phase-0/1 automation:** `new_sku → classify → clone ChannelDock shipping profile from template EAN → verify dry-run for NL×{1,5,10} and BE×{1,5,10}`.

---

## 3. Warehouse packaging order list

| Packaging | Internal name | Order URL |
| :--- | :--- | :--- |
| White mailbox box A4 | Grote brievenbusdozen | *(link missing in sheet — confirm with Rob)* |
| White mailbox box A5+ | Middelgrote brievenbusdozen | https://www.myparcel.nl/webshop/product/witte-brievenbusdoos-met-bovenklep-a5/ |
| White mailbox box A6 | Kleine brievenbusdozen | https://www.myparcel.nl/webshop/product/witte-brievenbusdoos-met-bovenklep-a6/ |
| Single-wall 22×20×15 | Headphones | https://www.myparcel.nl/webshop/product/verzenddoos-enkelgolf-22x20x15cm/ |
| Single-wall 20×15×10 | Hardcases | https://www.myparcel.nl/webshop/product/verzenddoos-enkelgolf-20x15x10cm/ |
| Single-wall 15×15×12 | Earbuds | https://www.myparcel.nl/webshop/product/verzenddoos-enkelgolf-15x15x12cm/ |
| Double-wall 60×40×40 | Bol shippers | https://www.myparcel.nl/webshop/product/verzenddoos-dubbelgolf-60x40x40cm/ |
| Single-wall 29.4×19.4×23.8 | Multi headphones | https://www.myparcel.nl/webshop/product/verzenddoos-enkelgolf-294x194x238cm/ |
| Single-wall 37×24×15 | Kids tablets | https://www.myparcel.nl/webshop/product/verzenddoos-enkelgolf-37x24x15cm/ |
| White die-cut A4+ 35×26×10 | Kids tablets 2 | https://www.myparcel.nl/webshop/product/witte-stansdoos-a4-3/ |
| Air cushion K20 | Tablet sleeves | https://verpakgigant.nl/product/k20-luchtkussen-enveloppen-350-x-470/ |
| Air cushion B12 | Light post | https://verpakgigant.nl/product/b12-luchtkussen-enveloppen-120-x-215/ |
| Air cushion C13 | QLS envelopes | https://verpakgigant.nl/product/c13-cd-formaat-luchtkussen-enveloppen-150-x-215/ |
| Dymo 4XL labels | — | via info@misterlabel.nl |

---

## 4. Keywords / findability

- **Zoekwoordanalyses:** clustered intent around iPhone adapters/chargers/cables + model years (high volumes on “snellader iphone”, “lightning kabel”, “iphone 16/17 …”).
- **Zoekvolume Google:** planner export; filtered export keeps headphones / school / autism / ADHD-adjacent terms (e.g. `koptelefoon s` ~27k, `autisme` ~22k) — feeds content + ads backlog, not Phase-0 ops.

---

## 5. Implications for the proposal

| Proposal area | Update |
| :--- | :--- |
| Unit economics (doc 26) | Replace generic PostNL bands with **WiseQ’s own tariff table** when quoting margins |
| Automation backlog | Add: shipping-rule clone checker; tariff vs promise auditor; packaging reorder alert |
| ChannelDock connector | Must read/write **delivery codes / shipping rules** per channel + qty breaks |
| Shadow demo | Include “new SKU → wrong shipping rule → ungefrankeerd” failure case |
| SEO / content Phase 2 | Keyword CSVs are the seed list Rob already maintains |

---

## Still private (ask Rob for controlled share if needed)

COGS tab, contact matrix, gift-card numbers, promo codes, full school/reseller lists — stay out of the public repo; use encrypted handover or Bitwarden for pilot credentials.

---

*Ingested 2026-10-27 · CSVs in [`mastersheet/`](mastersheet/) · related: [operating manual extract](OPERATING-MANUAL-EXTRACT.md)*
