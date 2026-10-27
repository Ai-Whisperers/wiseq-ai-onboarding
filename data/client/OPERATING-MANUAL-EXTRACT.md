# WiseQ operating manual — structured extract

*Source: [`Handleiding_opzet.txt`](Handleiding_opzet.txt) (client-provided, ingested 2026-10-27). This file is the **machine-usable source of truth** distilled from the manual. Prefer this over re-reading the raw dump for stack/automation design.*

**Status:** Phase-0 item #1 (company manual) — **received**.

---

## 1. Legal / channel structure

| Entity | Sales accounts | Notes |
| :--- | :--- | :--- |
| Operating BV | **WiseQ NL**, **WiseQ Electronics** | Two bol.com seller accounts |
| Holding BV | **WiseQ België** | Holding should not run ops — **being phased out** |
| NL fulfilment strategy | Ship NL customers from **WiseQ NL** | Target: order before 15:00 → next day; uses **LVB** |
| BE fulfilment strategy | Ship BE via **WiseQ Electronics** | Brievenbus 2–3 days own rules; packages via **VVB**; also has LVB |

**Design implication:** connectors and digests must be **multi-account** (3 bol shops today; target 2). Holding phase-out is a migration job, not a mystery.

---

## 2. Confirmed software stack *(answers prior open questions)*

| System | Role in manual | Implication for proposal |
| :--- | :--- | :--- |
| **ChannelDock** | Inventory SoR, bundles, shipping rules, returns, zeezending bookings, EAN labels | Bundle composition exists as **ChannelDock bundle feature** (not only PIM upsell) — see §4 |
| **FiveX / 5X** | Product reports (EAN, reference, stock, sales), LVB replenishment, auto price +10% when stock ≤10, product-review export | **CSV/report export confirmed** — browser automation may still be needed for some UI; API still unproven |
| **e-Boekhouden** | School offers → invoices → relations | Bookkeeping vendor **named** — Exact Online MCP path is wrong default; research e-Boekhouden API / MCP |
| **bol.com** | LVB, VVB, strikes, invoices, promotions, CE requests, list-hijack | Multi-account Retailer API |
| **QLS** | Carrier; tickets Tue/Thu; strike escalation emails | Ticket/ops rail |
| **MyParcel + DHL** | B2B school shipments (insured DHL, hand-in at DHL point) | School pipeline shipping leg |
| **PostNL** | Brievenbus / partijenpost; invoice disputes | Already in unit-economics doc |
| **Dymo Connect** | EAN stickers 57×32 / 57×36 mm | Label ops |
| **Excel Mastersheet** | Tabs e.g. `Levertijden`, `Kaartnummers` | Purchase/levertijd/price change log — Phase-0 must get a copy or schema |
| **Google Drive** | CE certificates / conformiteitsverklaringen | Cert library already exists — agent maintains, doesn't invent |
| **Shopify / own shop** | Mentioned indirectly (webshop order example) | Still primary own-channel; manual is bol/ops-heavy |

**Still open from doc 06:** ChannelDock plan tier + API token; annual turnover; sandbox school orders; mailbox provider.

---

## 3. Daily / weekly / monthly ops (automation backlog fuel)

### Daily
1. **100% assortment online** across all sales accounts — if OOS but inbound ≤8 days, put on longer delivery time (both relevant accounts); clear false long lead times when stock exists.
2. **ChannelDock ungefrankeerde zendingen** — assign shipping rules; weight/dimension fix if rule won't apply (“zand uit de machine”).
3. **Confirm cancellations** manually.
4. **Bol review triage** — goal score ≥9; 7–8 → template follow-up; ≤6 → resolve + ask deletion; cadence 2 mails week 1 then 1/week × 5.
5. Stand-up prep.

### Tue / Thu
- QLS tickets catch-up.

### Friday
- Bol invoice requests (all three accounts).
- Product-review cleanup via FiveX (non-product reviews → bol; match reviewers via ChannelDock name search ~1–2 weeks prior).

### On sea freight arrival
- Packing list to warehouse + office; create ChannelDock inbound; **book 300-series as bundles** (adapter+cable); NL vs BE barcodes; reset delivery times on all accounts (NL norm before 15:00→tomorrow; BE 2–3 days).

### Other cadences
- LVB replenishment from FiveX report vs LVB stock → warehouse sign-off → bol ship + labels.
- Every 2 months: LVB package-size audit (bol overcharges XS as S).
- Wednesday 10:00: bol strike evaluation (93% on-time); wipe-a-strike / VVB failover protocols.
- Monthly: financial goals; CD bundle stock deductions; school emails to top of funnel; CS ticket counts per employee.
- Quarterly: 1:1s; like 5★ reviews.
- EOY data dump checklist (stock, reships, ads, carriers, titles, holiday days, terms, this manual).

---

## 4. Bundle / EAN / ChannelDock (validates our spine thesis)

- Bundles are first-class in ChannelDock: set stock 0 → edit settings → mark bundle → add mother products by name/EAN + qty.
- Incoming sea freight: **oplaadcombinaties must book as bundles** or purchase/stock data breaks (300-series).
- “Bijmaken” of 300-series from loose adapter+cable is treated as **failure mode** (stock pollution, extra warehouse load) — same problem our Phase-1 recombination engine targets.
- Reference EANs for shipping-rule templates listed in manual (light/heavy cables, adapters, MagSafe, headphones, etc.).
- EAN stickers: ChannelDock print icon or tec-it barcode → Dymo.

---

## 5. School / B2B sales pipeline *(maps to flagship automation)*

```
Catalog/sample request → info mail + catalog
  → follow-up (2 weeks catalog / 3 weeks sample)
  → offer request → e-Boekhouden relation + offer (products, 2yr warranty, shipping/admin)
  → accept → invoice in e-Boekhouden
  → insured DHL via MyParcel (hand-in)
  → invoice to customer + warehouse
  → if stichting: extra catalogs + physical upsell letter to sister schools
```

**Templates exist** for offer, order confirm, catalog request, sample request, stichting upsell letter.

**Resellers named:** EDG Media, ITS Service, Onderwijsmagazijn (+ schools). EDG has specific invoice kenmerk + CC list + BTW-high.

---

## 6. Reputation / reviews (client priority ≠ Trustpilot-first)

- Primary scoreboard in this manual is **bol.com seller/product reviews**, not Trustpilot.
- New products: printed A5 thank-you card asking for bol review.
- List-hijackers: sommatiebrief → notice & takedown.
- FiveX used to find 1★ reviews and match orders.

**Proposal implication:** Phase-2 “reviews first” should mean **bol + Trustpilot/Kiyoh**, not Trustpilot alone — align doc 06 recommendation.

---

## 7. Brand (storefront)

| Token | Value |
| :--- | :--- |
| Light blue | `#26b5b7` |
| Dark blue | `#1648ad` |

---

## 8. Guardrails / ethics notes for AIW build

These are **client policies as written**. Automations must not silently expand them:

- Bol review deletion / follow-up cadences — human-gated; AVG/platform-policy review before any agent sends.
- CE sticker “peel from another cable” workaround — **do not automate**; route CE requests to Drive cert library + human.
- Promo codes / gift-card portals — never store in public repo or agent chat logs.
- Strike wipe / full-assortment VVB switch — high-impact; approval gate + Rob escalation at ≥3 strikes.

---

## 9. Automation candidates ranked from this manual alone

| Priority | Job | Why |
| :--- | :--- | :--- |
| P0 | Assortment-online monitor (3 accounts) | Daily, explicit #1 rule |
| P0 | ChannelDock unassigned shipping-rule queue | Daily “zand uit de machine” |
| P0 | Cancellation confirm queue | Daily manual |
| P1 | School offer→invoice→MyParcel draft (e-Boekhouden) | Flagship; templates exist |
| P1 | FiveX→LVB replenishment suggestion | Weekly warehouse loop |
| P1 | Delivery-time / price-brake sync (Mastersheet + both accounts) | Easy to forget |
| P1 | Strike / on-time digest (Wed) | High business risk |
| P2 | Bol invoice-request batch (Fri) | Weekly |
| P2 | Review triage drafts (human send) | Heavy process already |
| P2 | Sea-freight inbound checklist + bundle booking assist | Event-driven |
| P2 | LVB package-size drift check | Bi-monthly |

---

## 10. Open asks still needed

1. ChannelDock plan tier + API access  
2. e-Boekhouden API / user rights for read-only pilot  
3. FiveX export samples (product report + review extract)  
4. Mastersheet schema (or anonymized `Levertijden` tab)  
5. Anonymized school offer→invoice examples  
6. Annual online turnover (Thuiswinkel)  
7. Mailbox provider for triage  
8. Confirm whether Shopify Admin access is in scope for Phase 0 alongside bol/CD  

---

*Extract author: AI Whisperers · 2026-10-27 · raw: [`Handleiding_opzet.txt`](Handleiding_opzet.txt)*
