<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track B · Document 30* · [← Docs map](../README.md)</sub>

---

# WiseQ — complete client dossier

*Single map of who WiseQ is, how they operate, what hurts, what is already modern, and what remains unknown. Synthesizes public research (Oct 21–23), meeting (Oct 21), operating manual + Mastersheet (Oct 27), and audit discipline (doc 29). Prefer linked extracts over raw Handleiding until Rob approves publication.*

## 1. Identity and people

| | |
| :--- | :--- |
| Legal | Wiseq B.V. · KvK 84801964 · VAT NL863378201B01 |
| Base | Wijzend 56, 1613 KP Grootebroek, NL |
| Contact | info@wiseq.nl · +31 228 75 70 25 |
| Leadership | **Rob Nyari** — E-Commerce CEO; founder-led, small team (purchase manager, marketing function) |
| Founded | 2018; bol since June 2018 |

**Working style:** Rob is AI-curious, asked about MCPs/tokens/servers; wants “AI in my mailbox”; already runs a 24/7 office machine. Decisions should stay **approval-gated** and evidence-labeled.

## 2. What they sell (two businesses in one shop)

| Line | Shape | Role |
| :--- | :--- | :--- |
| **Kids-tech brand** | Headphones (Junior → Kids ANC), tablets, smartwatches, hearing protection, B2B carts/storage | Story, SEO, school B2B, Amazon Hero equity |
| **Charger/cable long tail** | ~50% of SKUs, €7–34 | Volume, bol assortment, LVB/VVB economics |

**Catalog snapshot (Shopify Oct 21):** 230 products, vendor WiseQ; **0/230 EAN** in export; **0/230 weight**; bundle spine decoded to **114 components + 25 bundles** (CI green structurally — not physical Gate 3).

**Brand (manual):** `#26b5b7` / `#1648ad`.

## 3. Legal / sales org (manual)

| Entity | bol accounts | Fulfilment idea |
| :--- | :--- | :--- |
| Operating BV | **WiseQ NL**, **WiseQ Electronics** | NL: before 15:00 → next day, LVB-heavy. BE: Electronics — brievenbus 2–3 days, packages VVB, LVB for conversion |
| Holding | **WiseQ België** | Should not run ops — **phasing out** (migration, not done) |

Connectors must be **multi-account** from day one.

## 4. Systems of record (corrected stack)

| System | Owns | Confidence |
| :--- | :--- | :--- |
| **ChannelDock** | Inventory, native **bundles**, shipping rules, returns, inbound, EAN labels | Client-confirmed ops; API/plan **untested** |
| **FiveX** | EAN/stock/sales reports, LVB replenishment, review export, auto +10% @ ≤10 stock | Client-confirmed use; write semantics **untested** — recommend-only |
| **e-Boekhouden** | School relations → offers → invoices | Named SoT; **not Exact**; API **untested** |
| **bol ×3** | Listings, LVB/VVB, strikes, invoices, reviews scoreboard | Multi-account |
| **Shopify** | Own shop + custom B2B (staffel, factuur, samples) | Public + meeting; Phase-0 Admin priority TBD |
| **MyParcel / DHL** | Insured school parcels | Manual |
| **QLS / PostNL** | Carrier + tickets / brievenbus | Manual |
| **Mastersheet (Excel)** | Tariffs, shipping-rule templates, packaging links, keywords, price brakes | Partial public CSVs; full xlsx private |
| **Google Drive** | CE / DoC library | Exists — agent must not invent certs |
| **Mailbox** | CS + school + sales | Provider **unnamed** |
| **Dymo** | EAN stickers | Out of agent scope |

**Agentic already live:** UCP discovery + MCP shopping server on Shopify — rare NL edge; orchestration is the missing layer, not replatform.

## 5. How the company actually runs (compressed)

### Daily
Assortment 100% online (all accounts) · ungefrankeerde ChannelDock queue · cancel confirms · bol review triage (target seller ≥9) · stand-up.

### Cadences
Tue/Thu QLS tickets · Fri bol invoice requests + FiveX review cleanup · Wed 10:00 strike / on-time · sea-freight inbound (book **300-series as bundles**) · LVB replenishment · bi-monthly LVB package-size audit · monthly goals / CS counts · EOY dump checklist.

### School / B2B pipeline (flagship pain)
Catalog/sample → follow-up → **e-Boekhouden** offer → invoice → MyParcel/DHL → warehouse · stichting upsell letters · reseller kenmerken (EDG, ITS, Onderwijsmagazijn).

**Meeting estimate:** ~4h school mornings (+ historical ~4h/week booking) — **hypothesis** until Gate 0.3 times ≥10 real orders.

### Bundle / purchase pain (reconciled)

| Source | Claim | Resolution |
| :--- | :--- | :--- |
| Meeting Oct 21 | “ChannelDock doesn’t understand” recombination | **Partial**: ChannelDock **has** native bundles; failure mode is inbound/booking discipline + “bijmaken” polluting purchase data |
| Manual Oct 27 | Book 300-series as bundles; bijmaken = failure | Align design with **assist + validate**, not rebuild PIM |
| AIW spine | 25 bundles / 114 components | Research SoT for EAN registry; reconcile to live CD in Gate 3 |

## 6. Markets, reputation, growth

| Channel | Snapshot | Care |
| :--- | :--- | :--- |
| bol | Oldest channel; seller score culture ≥9 | **Primary review scoreboard** |
| Amazon.nl | Hero strong; Unbreakable weak/stale | Compliance + listing cleanup |
| Trustpilot | 13 / 4.5 organic (Oct 23) | Secondary to bol |
| Scamadviser | Trust Score 0 flag | Remediation backlog |
| Competitors | Two dated specialists + generalists; BuddyPhones/Puro/JLab in market scan | Price watch later |
| Growth ideas Rob liked | School-event promos, personalized outreach, supplier price watch, consistent AI imagery, elderly/hearing & parental controls (horizon) | Measure before promise |

**BE LVB uplift:** manual ~+80% vs sheet +178% — **client observations, conflicting; not ROI inputs**.

## 7. Documented pain → opportunity (ranked)

| Pain | Evidence type | Prepare / automate |
| :--- | :--- | :--- |
| School offer→invoice→ship handoffs | Meeting + manual | Shadow demo (lab A) → gated e-Boekhouden |
| Ungefrankeerd / wrong shipping rules | Manual + Mastersheet | Template validation (lab B/C) → CD read queue |
| Assortment / levertijd drift | Manual #1 rule | Multi-account monitor |
| Excel purchase averages | Meeting | Purchase-intel job after EAN spine |
| Bundle stock / recombination | Meeting + manual | Registry + CD booking assist |
| Review follow-ups | Manual (policy-sensitive) | Draft-only; compliance first |
| Low Trustpilot volume | Public | bol-first then Trustpilot invites (honest caps) |
| 0 EANs in Shopify | Snapshot | GS1 €225/yr path + backfill |
| Amazon dud listings | Public | Checklist + batch refresh |
| Scamadviser 0 | Public | Remediation playbook |

## 8. Constraints and non-negotiables

- Read-only first; writes last; money last (doc 23).  
- No automated “remove your rating” without policy sign-off.  
- No CE sticker peel automation.  
- No production secrets in public repo; raw manual publication gated.  
- Hermes Desktop = Rob’s seat; always-on cron needs companion later.  
- Four-dimension evidence labels on client claims (doc 29).

## 9. Still unknown (blockers for live data)

See also [Preparation catalog](../50-evidence/01-preparation-catalog.md) and [Read-only access guide](../start/rob/read-only-access.md).

1. ChannelDock plan + API token + PIM yes/no  
2. e-Boekhouden REST token (read)  
3. bol client credentials per active account  
4. Mailbox provider + read method  
5. FiveX export samples / API  
6. Anonymized school offer→invoice examples  
7. Timed baseline (≥10 school orders)  
8. Annual online turnover band (Thuiswinkel) — **verbal ~€1.5M on 2026-10-28; confirm online vs total**  
9. Shopify Phase-0 scope  
10. Raw Handleiding public-OK?  
11. Confirm 2× Adapter template + BE uplift definition  
12. België account migration timeline  
13. Bol listing-quality export (~300 SKUs) mentioned 2026-10-28  
14. Commercial scope: ops Phase 0–1 vs Rob’s “full growth package” (≥€2k base-fee signal)

## 10. Source index

| Artifact | Role |
| :--- | :--- |
| [01 Company profile](02-company-profile.md) | Public registry + channels |
| [03 Meeting notes](04-meeting-2026-10-21.md) | Founder pain (addendum below in that file) |
| [07 Meeting 2026-10-28](07-meeting-2026-10-28.md) | Revenue band, growth pillars, fee signal |
| [28 Manual summary](03-operating-manual.md) | Proposal-facing corrections |
| [Extract](../../data/client/OPERATING-MANUAL-EXTRACT.md) | Builder SoT |
| [Mastersheet extract](../../data/client/MASTERSHEET-EXTRACT.md) | Tariffs / templates |
| [25 Catalog scorecard](05-catalog-scorecard.md) | EAN / spine |
| [18 Submissions status](../50-evidence/18-rob-submissions-status.md) | Files vs open asks |
| [Workflow audit](../50-evidence/02-workflow-audit.md) | Process inventory |
| [SoR map](../50-evidence/03-data-flow-sor.md) | Data ownership |
| [Preparation catalog](../50-evidence/01-preparation-catalog.md) | What we prepare offline vs need from Rob |

---

<sub>AI Whisperers · 2026-10-28 · living doc — update when Rob answers open asks</sub>
