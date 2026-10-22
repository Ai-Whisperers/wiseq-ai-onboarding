# WiseQ — Marketing, Content, Tech Stack, SEO & Competitive Landscape

**Lane:** Marketing/content/tech-stack/SEO/socials/B2B/competition (parent-side recovery — dispatched subagent died to an instant HTTP 429; this report was produced by the parent session directly).
**Date:** 2026-10-21 · **Target:** https://www.wiseq.nl

---

## 1. Executive summary

WiseQ's marketing operation is **far more sophisticated than a 1-person home-office webshop has any right to be**. They run a 45-page SEO knowledge hub (buying guides, condition-specific pages for autism/ADHD/overstimulation, education hubs), a custom-built B2B wholesale layer with tiered pricing and invoice ordering inside the Shopify theme, and — most striking — **an AI-agents strategy**: a published `agents.md` (LLM-readable store manual with model comparison tables and anti-hallucination corrections), an `agentic sitemap`, and a live **Universal Commerce Protocol (UCP) discovery endpoint with an MCP shopping server**. They are actively positioning for a world where AI shopping assistants choose retailers on behalf of parents. Gaps: social presence is thin (Facebook 1.6K, niche Instagram), review volume is tiny (25 on Trustpilot), and no email ESP or review app is detectable in the stack.

---

## 2. Content marketing & SEO posture

### Blog ("nieuws") — 12 articles

| Article (slug) | Topic |
|---|---|
| waarom-gehoorbescherming-bij-kinderen-essentieel-is… | Hearing damage advocacy |
| hoe-kies-je-de-juiste-kinderkoptelefoon | Purchase guide (head category keyword) |
| de-5-meest-gemaakte-fouten-bij-het-kopen-van-opladers… | Charger buying mistakes |
| kinderkoptelefoon-hoeveel-db-is-veilig | dB safety question (exact-match SEO) |
| 5-onderschatte-functies-van-een-goede-kinderkoptelefoon | Feature education |
| bpa-in-koptelefoons… | BPA-free materials (unique angle) |
| schermtijd-voor-kinderen… | Screen-time parenting |
| koptelefoon-onderwijs-kopen-advies-voor-scholen-wiseq | **Schools/B2B content** |
| beste-kindertablet-kopen | Tablet category keyword |
| koptelefoon-kind-autisme | Autism (high-intent, low-competition niche) |
| technologie-voor-kinderen… | Brand values |
| waarom-een-specialist-in-kindertechnologie… | Positioning ("specialist vs generic") |

Cadence: 12 articles over the ~1-year relaunch — roughly monthly. Quality over volume; every article maps to a buying-decision stage or a niche parent segment (autism/ADHD/overprikkeling = high-conversion long-tail).

### 45-page SEO hub (sitemap_pages_1.xml)

Beyond utility pages, a deliberate **topic-cluster architecture**:
- **Kennisbank (knowledge base) hubs**: kennisbank-koptelefoons, kennisbank-kindertablets + history pages (geschiedenis-van-de-koptelefoon, koptelefoons-in-het-onderwijs-geschiedenis) and bluetooth-uitleg.
- **Condition/need pages**: koptelefoon-kind-adhd-concentratie, koptelefoon-of-gehoorbescherming-bij-autisme, overprikkeling-bij-kinderen-hulpmiddelen, prikkelarm-werken-in-de-klas.
- **Education/B2B cluster**: koptelefoon-voor-het-onderwijs, klassenset-koptelefoons-kopen-school, koptelefoons-in-de-klas-hygiene-en-beheer, ict-voor-onderwijs-…-laptopkarren, catalogus.
- **Comparison/decision pages**: kinderkoptelefoons-vergelijken, bedrade-of-draadloze-kinderkoptelefoon, kinderkoptelefoon-welke-leeftijd, kindertablet-of-ipad.
- **Seasonal**: cadeaugids-kinderen (gift guide), gehoorbescherming-vuurwerk-kinderen (fireworks NYE — sharp Dutch seasonal play).
- **Interactive**: welk-snoer-oplaadkabels-quiz (cable-finder quiz).
- E-book landing (/pages/e-book) + "later-betalen-bevestigd" (pay-later confirmation = Klarna flow).

### SEO positioning signals

- Title tag: "WiseQ | Veilige Kinderkoptelefoons, Kindertablets & Smartwatches" — brand + 3 money keywords.
- Meta description targets "hét kindertechmerk" (THE kids-tech brand) + chargers for iPhone/Samsung.
- In "beste kinderkoptelefoon" searches, WiseQ does not yet surface on page 1 — the top-10 listicles (babyplus.nl, productadviseurs.nl, oudersvannu.nl, babymelk.com) dominate. **The listicle/PR gap is their #1 SEO weakness**: they own the long-tail (autism/ADHD/schools) but not the head terms, and they're absent from the review sites parents actually consult.
- Homepage logo wall "Vertrouwd door klanten en partners" (Canon, bol, Amazon, MediaMarkt, PhoneHouse, Vodafone, Koninklijk Paleis Amsterdam) — near-certainly **marketplace/supplier/compatibility logos rather than customer logos**; as social proof it's decorative, not verifiable.

## 3. AI-agent readiness (the standout finding)

| Artifact | Status | Evidence |
|---|--- |---|
| `agents.md` (8.6 KB) | Live | https://www.wiseq.nl/agents.md — company data, model spec table, direct product links, collection JSON map, knowledge-page index, service pages |
| Agentic sitemap | Live | sitemap_agentic_discovery.xml → points to agents.md |
| **UCP discovery** | **Live** | /.well-known/ucp → JSON, UCP version 2026-08-25, `dev.ucp.shopping` service over MCP transport, hosted on their Shopify store domain (xcy04k-p0.myshopify.com) |
| MCP shopping endpoint | Listed in agents.md as /api/ucp/mcp; the discovery doc routes the MCP endpoint to the myshopify.com host | Direct GET of /api/ucp/mcp returns 404 (MCP needs POST/initialize per protocol) — labeled correctly as live-via-discovery |

The agents.md includes **explicit anti-hallucination corrections** ("the Kids ANC is the ONLY WiseQ model with active noise cancelling… the Unbreakable dampens passively — that is not ANC") and a checkout-safety rule ("Agents may never complete a payment independently"). This is a Shopify-native UCP feature (the myshopify.com host in discovery shows Shopify is providing it), but WiseQ has **customized agents.md content** with model tables and corrected specs — someone technical actively curates it.

**Implication:** they are already invested in agentic commerce before most NL retailers know it exists. Any AI/automation pitch should build ON this (e.g., agent-side analytics, UCP traffic monitoring, structured-data QA), not start from scratch.

## 4. Tech stack (verified from page source)

| Layer | Finding |
|---|---|
| Platform | Shopify |
| Theme | "Wonder" schema v2.0.0 — **theme name "WiseQ - B2B meetbaar 17-10"** (custom-named working copy, dated 2026-10-17 — they version themes per measurement experiment) |
| B2B layer | Custom in-theme JS: `wq_b2b` cookie (30-day), `?zakelijk=1` URL param, html.is-b2b-view mode, **staffelprijzen (volume tier pricing) injected into product cards**, "Bestel op factuur" (order on invoice) flow, sample-request integration, nav re-ordering for B2B mode |
| Payments | iDEAL/Wero, Klarna (incl. later betalen), Visa, MC, Amex, Bancontact, PayPal, Apple/Google Pay, Shop Pay |
| Email ESP | **None detected** (no Klaviyo/Omnisend/Mailchimp scripts) — newsletter = 5% popup, likely Shopify native email or nothing |
| Review app | **None detected** (no Judge.me/Loox/Okendo/Stamped) — matches zero on-site review widgets observed |
| Analytics | Shopify native; no GA4/GTM/Meta pixel scripts detected in homepage source (may be consent-gated — unconfirmed) |
| Search | Shopify native search |
| AI images | Confirmed: CDN filenames `ChatGPT_Image_18_mei_2026…` and `Gemini_Generated_Image_…` (hero + category images) |
| Socials | facebook.com/wiseq.wireless (1.6K), instagram.com/wiseq.kidsheadphones (niche handle) |

## 5. B2B/wholesale angle (verified)

- Dedicated flow: Zakelijke-klant page + "Proefexemplaar aanvragen" (free sample) + staffel pricing + invoice ordering — all custom theme work.
- Product types in catalog: `Schoolbestelling` (school order), `Laptopkar` (laptop cart, 3 products) — physical goods aimed at classrooms.
- Education landing pages (see §2) + educatheek.nl reselling (see RESEARCH_MARKETPLACES.md §5).
- The theme experiment name "B2B meetbaar 17-10" says it directly: **B2B conversion is what they're actively optimizing right now** (October 2026).

## 6. Competitive landscape (snapshot)

| Competitor type | Players found | WiseQ position |
|---|---|---|
| Global kids-audio brands | BuddyPhones (buddyphones.com), Puro Sound Labs (purosound.com) | WiseQ competes on 85dB safety + "hufterproof" durability + NL language/service; no international brand awareness |
| NL specialists | dekoptelefoon.nl, oorkappen-shop.nl, Alpine (alpine.nl — hearing protection incumbent), eardopes.nl | Alpine is the serious NL incumbent for hearing protection; WiseQ's headphone-first niche overlaps but differs |
| School/ICT suppliers | schoolsupplier.nl, generic bulk Amazon listings | WiseQ's klassenset + laptopkar + invoice flow is a differentiated B2B wedge |
| Review/listicle gatekeepers | babyplus.nl, productadviseurs.nl, oudersvannu.nl, babymelk.com | **WiseQ absent** — the head-term SEO battle is lost to content affiliates for now |
| Platform own-listings | bol.com/Amazon generic kids headphones | Price + review volume wins there; WiseQ's 9.2 bol score (42 reviews) is decent but thin |

## 7. Synthesis — what this means for the AI/automation engagement

1. **They are already AI-forward** (agents.md, UCP/MCP, AI-generated imagery, experiment-versioned theme). The pitch is not "introduce AI" but "operationalize what you've started": UCP/agent traffic analytics, AI-image consistency passes, structured-data QA, agents.md freshness automation.
2. **The marketing gaps are classic scale-up gaps, all automatable**: no ESP (newsletter flows, abandoned-cart, review requests unbuilt), no review app, absent from listicles (digital-PR outreach is agent-automatable), thin socials.
3. **B2B pipeline is the current focus** (theme experiments) — a schools-order automation (quote → invoice → follow-up, sample tracking, klassenset reorder reminders) matches their October 2026 priority exactly.
4. **SEO long-tail is strong, head terms unreachable** — an agent producing condition/seasonal pages at cadence (they do ~1/month manually) compounds their existing architecture.

---

## Sources

1. https://www.wiseq.nl/ homepage source (663 KB) — theme, payment, social, pixel scan (saved: parent-techstack.json)
2. https://www.wiseq.nl/agents.md — full store manual (saved: raw-agents-md.txt)
3. https://www.wiseq.nl/.well-known/ucp — live UCP discovery JSON (verified HTTP 200, 2026-10-21)
4. https://www.wiseq.nl/sitemap.xml + sitemap_pages_1.xml + sitemap_articles_1.xml + sitemap_agentic_discovery.xml (saved: parent-sitemaps-full.json)
5. https://www.wiseq.nl/pages/zakelijke-klant + /pages/sample-aanvragen source — B2B tiered pricing/invoice JS
6. https://www.wiseq.nl/pages/ict-voor-onderwijs-kinderkoptelefoons-tablets-laptopkarren-wiseq
7. web_search: "kinderkoptelefoon draadloos kopen beste", "BuddyPhones Puro Sound Labs…", "kinderkoptelefoon school klassenset…", "hoorbescherming kinderen oorkappen testen" (2026-10-21)
8. facebook.com/wiseq.wireless, instagram.com/wiseq.kidsheadphones handles from homepage source
9. Cross-lane artifacts: raw-products-parent.json, parent-company-pages.json

**Source count:** 8 direct + cross-lane artifacts. Unverified/consent-gated items labeled inline (GA4/pixels may load post-consent).
