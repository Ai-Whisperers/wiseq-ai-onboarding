# WiseQ — Consolidated Research Dossier

**Date:** 2026-10-21 · **Target:** https://www.wiseq.nl (Wiseq B.V., KVK 84801964, Grootebroek NL)
**Method:** 4-lane parallel research batch (all lanes ultimately executed parent-side after the child spawn pool was rate-limited by HTTP 429 — every finding below is backed by a saved artifact in this directory).

---

## Deliverables

| Lane | File | Size | Focus |
|---|---|---|---|
| Company & registry | RESEARCH_COMPANY.md | 7.7 KB | Wiseq B.V., 2018, timeline, scale |
| Catalog & data quality | RESEARCH_CATALOG.md | 8.2 KB | 230 products, pricing, bundles, data audit |
| Marketplaces & reputation | RESEARCH_MARKETPLACES.md | 9.9 KB | bol, Amazon, Trustpilot, Scamadviser |
| Marketing & competition | RESEARCH_MARKETING_COMPETITION.md | 11.2 KB | SEO hub, agents.md/UCP, tech stack, B2B, competitors |

Raw artifacts: raw-products-parent.json (230 products), raw-agents-md.txt, parent-*.json (searches, pages, sitemaps, techstack), parent-notes.md.

---

## The WiseQ story in one page

**WiseQ is an 8-year-old Dutch marketplace seller in the middle of a sophisticated rebrand.** Wiseq B.V. was founded in 2018, started selling on bol.com in **June 2018** (now 9.2/10, 42 reviews, 312 articles), registered wiseq.nl in Jan 2019, listed on Amazon.nl from ~2020. It began as a hearing-safe audio brand for adults ("Turn Music into Magic") and has pivoted to **kids' technology** — headphones with 85 dB volume limiting as the flagship, plus tablets, smartwatches, hearing protection, and a big charger/cable long tail (50% of SKUs). In **September 2025** it replatformed: 189 of its 230 Shopify products were bulk-created that month, with a 45-page SEO knowledge hub, a custom B2B wholesale layer (tiered pricing, invoice ordering, sample requests for schools), and — remarkably — an **AI-agent commerce strategy**: a curated `agents.md`, an agentic sitemap, and a live **UCP/MCP shopping endpoint**. It's a home-office BV (likely 1–5 people) running multi-channel e-commerce with real technical sophistication and real data debt.

## Cross-cutting findings

1. **The brand is far older and more credible than it looks — and its reputation tooling hasn't caught up.** 8 years of bol history, 9.2 seller score, yet only 25 Trustpilot reviews, no review app, no review invitations — and an algorithmic **Scamadviser "Trust Score 0" flag** (via a Webshopchecker report) that suppresses conversion precisely because the shop *looks* young. Cheapest high-ROI fix in the whole dossier.
2. **Shopify is a display layer, not the system of record.** 0/230 products track inventory, 0/230 have EAN barcodes, 0/230 have weights. Truth lives in ChannelDock + marketplace listings (bol has 312 articles vs 230 shop products — the channels have drifted apart). The EAN/bundle pains described in the audio are symptoms of this one structural fact: **there is no canonical product registry.**
3. **The bundle problem is quantified and regular.** 77 bundle-products (33%), built combinatorially (adapter × cable × length × color, SKU sequences like 371/372/373). Regular enough to reverse-engineer into a component graph programmatically — the OOS-propagation math can be a script.
4. **They are already AI-forward — meet them where they are.** AI-generated hero imagery (ChatGPT + Gemini filenames), experiment-versioned theme ("WiseQ - B2B meetbaar 17-10"), agents.md with anti-hallucination spec corrections, live UCP discovery. The right pitch is *operationalizing* agentic commerce (UCP analytics, feed QA, content cadence), not introducing AI.
5. **B2B/education is the active growth bet.** Custom wholesale layer, laptop carts (€550–1,149), klassenset pages, named-school SKUs (`SCHOOL-TAMARISK`), sample products, educatheek.nl wholesale, and the October 2026 theme experiments all point the same way. It's being run manually today.
6. **Marketing gaps are the classic solo-operator gaps**: absent from the "beste kinderkoptelefoon" listicles that own head terms (they win the autism/ADHD/schools long tail instead), thin socials (FB 1.6K, niche IG), no email ESP detected, 20 products with empty descriptions, Amazon legacy listings neglected (2.5★ dud on 3 reviews next to a 4.4★×45 asset).

## Engagement map — what an AI/automation partner could sell, in ROI order

| # | Opportunity | Evidence | Effort |
|---|---|---|---|
| 1 | **Reputation engine**: review invitations (post-purchase, bol+shop), Scamadviser/Webshopchecker remediation, Trustpilot volume | 25 reviews, 0 invitations, Scamadviser 0 | Low |
| 2 | **Canonical product registry + EAN backfill** → feeds for bol/Amazon/UCP | 0/230 EANs, channel drift 312 vs 230 | Medium |
| 3 | **Bundle component graph + OOS propagation** (ChannelDock-aware) | 77 combinatorial bundles, no stock in Shopify | Medium |
| 4 | **B2B school pipeline**: quote→invoice→sample tracking, reorder reminders, klassenset CRM | Custom B2B layer, named-school SKUs, Oct 2026 experiments | Medium |
| 5 | **Content cadence agent**: knowledge-hub pages at scale, listicle/PR outreach, newsletter (5% hook exists, no ESP) | 12 blog posts/yr manual, absent from listicles | Low-Med |
| 6 | **Marketplace relaunch**: Amazon listing refresh w/ review equity (Hero 4.4×45), price harmonization across channels | Legacy ASINs, broken compliance blocks | Low-Med |
| 7 | **Agentic-commerce operations**: UCP traffic analytics, agents.md freshness, structured-data QA | Live UCP/MCP endpoint already | Med |

## Open items (gaps this pass could not close)

- Directors/owners of Wiseq B.V. (Creditsafe paywall; LinkedIn authwall) — pullable from the paid KvK Handelsregister extract.
- bol.com seller-page detail (our egress IP is blocked by bol) — rating history, buy-box share.
- LinkedIn headcount/content, Instagram follower count, GA4/pixel presence post-consent.
- Financials (deposit, revenue) — not public for a BV of this size.

## Verification

- All 4 deliverables written and size-checked on disk (7.7–11.2 KB each).
- Primary claims cross-verified: registry (Creditsafe + site footer + bkoppeling), domain (SIDN WHOIS socket), catalog (products.json artifact, N=230 programmatically counted), UCP endpoint (HTTP 200 live check), bol since 2018 + 9.2/42 + 312 articles (bkoppeling snapshot), Trustpilot 4.4/25 (live extraction), Scamadviser 0 (live extraction).
- Single-sourced claims labeled in-lane (e.g., Facebook brand-era reading, logo-wall interpretation).
