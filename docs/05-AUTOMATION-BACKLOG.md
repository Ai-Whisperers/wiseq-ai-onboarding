# Automation Backlog — every opportunity found, scored

*Compiled from research + the 2026-10-21 session. Impact = time saved or revenue gained; Effort = build complexity. 🔥 = do first.*

## Operations

| # | Automation | Impact | Effort | Notes |
|---|---|---|---|---|
| 🔥 1 | **School-order pipeline** (email → offer → invoice → ChannelDock booking) | 4h/morning → minutes | Med | Flagship; founder-confirmed pain |
| 🔥 2 | **Bundle recombination booking** (component EAN movements when combos split) | Ends purchase-data pollution | Med | Needs EAN registry first |
| 🔥 3 | **Purchase intelligence** (6-mo per-EAN averages, actual-product basis) | Replaces manual Excel; fewer errors | Low | Nightly job + report |
| 4 | Mailbox triage + draft replies | Hours/week | Low | Founder explicitly wished for this |
| 5 | Invoice-XML parsing (supplier QR→XML → inventory + price updates) | Hours/week | Low | Pattern proven in sister project |
| 6 | New-relation onboarding (extract school details → bookkeeping draft) | Minutes/order | Low | Part of #1 |
| 7 | Return/review-drivende automated emails (5X rules) | Fewer returns | Low | Configure in 5X + trigger |

## Data & catalog

| # | Automation | Impact | Effort |
|---|---|---|---|
| 🔥 8 | **Canonical EAN registry** (EAN↔SKU↔components) | Foundation for 1,2,3 | Med |
| 9 | EAN/GTIN backfill into Shopify (0/230 today) | Feed quality everywhere | Med |
| 10 | Weights + inventory_policy backfill (0/230 today) | Correct shipping calc | Low |
| 11 | Empty-description rewrite (20 products) + structured copy for all | Conversion | Low |
| 12 | Variant consolidation (6 colors → 1 product) A/B | Reviews concentrate, feeds cleaner | Med |
| 13 | Channel drift sync (bol 312 vs shop 230) | One truth | Med |

## Revenue

| # | Automation | Impact | Effort |
|---|---|---|---|
| 🔥 14 | **Review-invitation engine** (post-delivery, shop + bol) | 25 → 250+ reviews | Low |
| 15 | Amazon listing refresh + compliance blocks | Salvage 4.4★ equity | Low |
| 16 | Scamadviser/Webshopchecker remediation | Conversion | Low |
| 17 | B2B campaign engine on lead-gen data (event-aware personalization) | New pipeline | Med |
| 18 | Newsletter + abandoned-cart flows (ESP setup) | Recovered revenue | Low |
| 19 | Content cadence agent (hub pages, listicle outreach) | Organic growth | Med |
| 20 | Competitor + supplier price monitoring | Margin defense | Med |
| 21 | UCP/agent traffic analytics | Extend agentic lead | Low |

## Later / exploratory

- Screen-time-control service on tablets (manufacturer preinstall path) — new product line
- Elderly hearing-assist line evaluation — new market (big-corp competition acknowledged)
- Flanders + DACH expansion operations
- WhatsApp ordering loop for B2B reorders (pattern proven in sister project)
