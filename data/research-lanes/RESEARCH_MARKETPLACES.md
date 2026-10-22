# WiseQ — Marketplace Presence & Customer Reputation

**Lane:** Marketplaces & reputation (parent-side recovery — the dispatched subagent died to an instant HTTP 429 before gathering anything; this report was produced by the parent session directly).
**Date:** 2026-10-21 · **Target:** https://www.wiseq.nl (Wiseq B.V., KVK 84801964, Grootebroek NL)

---

## 1. Executive summary

WiseQ runs a **multi-channel operation**: its own Shopify shop (wiseq.nl), a **bol.com brand storefront** (seller/partner ID 4268085706), and an **Amazon.nl brand store** with ASINs registered since **~2020** — roughly five years before the current Shopify catalog went live (first product created 2025-09-30). Independent reputation is **thin but positive on Trustpilot (4.4/5, 25 reviews)**, while **Scamadviser carries an algorithmic "Very Likely Unsafe" flag (Trust Score 0)** inherited from a Webshopchecker report — a meaningful conversion-killer for a young shop that deserves active remediation. Products also flow into **education retail** (educatheek.nl stocks WISEQ Kids ANC), confirming a wholesale/B2B distribution side beyond consumer marketplaces.

---

## 2. bol.com presence

### What is verified

| Item | Value | Source |
|---|---|---|
| Brand page | https://www.bol.com/nl/nl/b/wiseq/600005572 | search-indexed |
| Seller/partner ID | **4268085706** (appears in every WISEQ category URL) | bol.com URL structure |
| Category listings | Koptelefoons (list 33078), Kinderkoptelefoons (list 70880), Opladers (list 4041), USB-C kabels (list 30948) | bol.com list URLs |
| Product page | https://www.bol.com/nl/nl/pb/wiseq/600005572 | search-indexed |

Bol.com actively maintains WiseQ category shelves across at least four product groups — headphones (the specialty), kids headphones, chargers, and USB-C cables. This matches the operator's own description of bol.com as the main marketplace channel.

### What could not be retrieved

- **bol.com blocks our egress IP** (131.178.102.196): both the brand page and category pages return "IP address is blocked" instead of content (verified 2026-10-21, parent-side extraction attempt).
- Seller rating score, review count, buy-box share, and price positioning vs. own shop are therefore **unverified**. Bol seller ratings typically live on the seller profile page (`/nl/nl/s/wiseq/<id>.html`) — inaccessible from this IP.

> **Gap flag (single-sourced / inaccessible):** bol.com seller score and review volume remain open items. The brand page and partner ID are confirmed to exist; nothing about rating quality is claimed here.

---

## 3. Amazon.nl presence

### Brand store

- **WISEQ Store:** https://www.amazon.nl/stores/WiseQ/page/C9F1064E-D9CA-40B4-B0BE-D9A46D7F8B1C (linked from both extracted ASINs, 2026-10-21).

### Verified listings

| ASIN | Product | Rating | Reviews | Price | Notes |
|---|---|---|---|---|---|
| B08GCHT6KC | WiseQ Unbreakable — Wireless Kids Headphones, 45h battery, Bluetooth 5.0, over-ear (Blue) | **2.5/5** | 3 | — | Title in English; listing shows "Sorry, we could not show the information" blocks for manufacturer/responsible-person data |
| B08PG3TCRN | WISEQ Hero — Kids Headphones, Bluetooth, volume-safe, 36h battery (Pink) | **4.4/5** | 45 | **€27.95** | "New (2) from €27.95 & FREE Delivery" — multiple offers incl. possibly FBA/other sellers |

Additional artifact: an Amazon-hosted product manual PDF ("Welkom bij WiseQ! Hoe Werkt de Koptelefoon? Belangrijke...") at m.media-amazon.com — confirms branded documentation shipped with Amazon listings.

### Reading

1. **The brand is ~5 years old on Amazon.** ASIN prefixes B08G (≈ Aug 2020) and B08P (≈ Nov 2020) predate the current Shopify shop (born 2025-09-30) by five years. WiseQ is not a new brand — the current shop is a **replatform/relaunch**, not a startup catalog.
2. **Amazon is neglected, not dead.** 45 reviews on Hero vs 3 on Unbreakable; English-language titles on a Dutch-market listing; broken manufacturer/responsible-person info blocks (an EU DPP/EPR compliance smell). The Hero listing still sells at €27.95 with 2 offers.
3. **Review asymmetry** (4.4★×45 on Hero vs 2.5★×3 on Unbreakable) — the Unbreakable listing's low score on a tiny sample is the kind of thing a marketplace-monitoring automation should catch and fight (review mining, listing fixes).

---

## 4. Independent review platforms

### Trustpilot — the anchor signal

- URL: https://www.trustpilot.com/review/wiseq.nl
- Score: **4.4/5 ("Excellent")**, **25 reviews**, profile "Geüpdatet op 22 sep 2026" (verified 2026-10-21)
- Review dates visible: 21 Aug 2026, 27 Sep 2026 (recent, active)
- **100% of negative reviews answered** by the company
- Trustpilot note: "Dit bedrijf heeft hun klanten niet recentelijk uitgenodigd, dus reviews zijn mogelijk niet representatief" — i.e., **they are not running automated review invitations** (an obvious, cheap growth lever: 25 reviews is thin for a shop claiming school + retail partnerships).

### Scamadviser — the risk signal

- URL: https://www.scamadviser.com/check-website/wiseq.nl
- Verdict: **"Very Likely Unsafe", Trust Score 0** (verified 2026-10-21)
- Trigger: "This website has been reported to us as possible scam by **Webshopchecker**" (webshopchecker.nl)
- Scamadviser's own positives on the same page: valid SSL, "website has existed for quite some years", safe payment methods (money-back), DNSFilter considers it safe, sells real products.
- Negatives: "We identified popular products frequently sold by scammers" (chargers/cables are scam-magnet categories).

**Interpretation:** this is an **algorithmic penalty typical for young/low-traffic electronics shops** (the Shopify domain is ~1 year old in its current form; charger/cable SKUs are on Scamadviser's scam-frequency lists). It is not evidence of fraud — Trustpilot, KVK registration, physical address, and bol/Amazon presence all point the other way. But it IS a live business risk: Dutch consumers check Scamadviser/Webshopchecker before first purchases at unknown shops, and a 0-score listing suppresses conversion. **Remediation is cheap and worth recommending: respond to Webshopchecker's report, claim the Scamadviser profile, publish company details.**

### Not found / not present

- **Kiyoh:** no WiseQ profile surfaced in searches (only unrelated Kiyoh pages).
- **WebwinkelKeur:** no WiseQ profile surfaced.
- **Marktplaats:** no WiseQ seller account surfaced (only an unrelated "LalaShops" retailer). *(Absence claims are search-based, not exhaustive — labeled accordingly.)*
- **ReviewSpot / Google Maps reviews at Grootebroek address:** not retrieved this pass.

---

## 5. Wholesale / education channel (bonus finding)

- **educatheek.nl** (education-focused retailer) stocks the **WISEQ Kids ANC - Active Noise Cancelling - Zwart** as a catalogue item: "Op voorraad", publisher/brand field "WISEQ", education-market copy ("compatibel met Nintendo Switch of Playstation 5"). URL: https://www.educatheek.nl/wiseq-kids-anc-active-noise-cancelling-zwart
- Confirms the B2B/wholesale motion the About page and "Zakelijke klant"/"Proefexemplaar aanvragen" pages imply — WiseQ supplies other education retailers, not just end consumers.

---

## 6. Synthesis for the AI/automation engagement

1. **Marketplace ops are already multi-channel and messy in exactly the way the audio transcript described**: bol (main, unmeasurable from here), Amazon (neglected, 2020-era listings with broken compliance blocks), own shop (Shopify, active). An aggregation/monitoring layer (stock, price, review asymmetries, listing quality) across all three is the natural first automation.
2. **Reputation tooling gap:** 25 Trustpilot reviews with zero automated invitation flow + a Scamadviser 0 flag = the single highest ROI quick win (post-purchase review invitations via Trustpilot/Kiyoh + Scamadviser profile remediation).
3. **Amazon relaunch opportunity:** 5-year-old ASINs with existing review equity (45 on Hero) but stale English titles, 3-review dud listings, and missing EU responsible-person data. A listing-refresh + review-management pass monetizes existing assets.
4. **EAN/data quality:** 0/230 Shopify products expose barcodes (parent catalog probe, raw-products-parent.json) — marketplace feeds to bol/Amazon must be maintaining EANs out-of-band (ChannelDock?), or listings are matched loosely. This is the data-quality backbone any automation must fix first.

---

## Sources

1. https://www.bol.com/nl/nl/b/wiseq/600005572 — bol brand page (search-verified; content IP-blocked)
2. https://www.bol.com/nl/nl/l/wiseq-koptelefoons/33078/4268085706 — bol category list (IP-blocked)
3. https://www.bol.com/nl/nl/l/wiseq-kinderkoptelefoons/70880/4268085706 — search hit
4. https://www.bol.com/nl/nl/l/wiseq-opladers/4041/4268085706 — search hit
5. https://www.bol.com/nl/nl/l/wiseq-usb-c-kabels/30948/4268085706 — search hit
6. https://www.bol.com/nl/nl/pb/wiseq/600005572 — search hit
7. https://www.amazon.nl/WiseQ-Unbreakable-Draadloze-koptelefoon-Kinderkoptelefoon/dp/B08GCHT6KC — extracted 2026-10-21
8. https://www.amazon.nl/WISEQ-Koptelefoon-Kinderen-Draadloos-Bluetooth/dp/B08PG3TCRN — extracted 2026-10-21
9. https://www.trustpilot.com/review/wiseq.nl — extracted 2026-10-21
10. https://nl-be.trustpilot.com/review/wiseq.nl?page=2 — extracted 2026-10-21
11. https://www.scamadviser.com/check-website/wiseq.nl — extracted 2026-10-21
12. https://www.educatheek.nl/wiseq-kids-anc-active-noise-cancelling-zwart — extracted 2026-10-21
13. https://m.media-amazon.com/images/I/71BG3JU0+yL.pdf — WiseQ headphone manual on Amazon CDN (search hit)
14. Local artifacts: parent-marketplace-searches.json, parent-marketplace-pages.json, raw-products-parent.json

**Source count:** 13 URL sources + 3 local artifacts. Access-blocked: bol.com (IP ban), Kiyoh/WebwinkelKeur (no profile found).
