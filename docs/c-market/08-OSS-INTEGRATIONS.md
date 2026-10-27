<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track C · Document 08* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# WiseQ OSS & Integrations Catalog — researched 2026-10-22

*Companion to the AI-stack blueprint (04). Raw GitHub-search data in `data/oss/` (10 topics, ~115 repos, ≥5★, non-archived). The insight up front: **the Dutch e-com tooling layer is thin — the moat is orchestration, not tools.** The searches below prove it.*

## 1. 🧭 Stack-gap analysis (what the research showed)

| Layer | Finding | Consequence |
|---|---|---|
| **bol.com tooling** | 11 repos ≥5★ total; top is a PHP client (picqer, 29★). No mature Python/TS ecosystem. | Bol integration = custom thin-client work against their official Retailer API (well-documented, OAuth2 via login.bol.com) — a 2-3 week agent project, not an install. bol's own docs cover offers/orders/shipments/content. |
| **Repricers** | Near-zero OSS (2 repos, ~6★). | Repricing rules live in OUR agent — no off-the-shelf shortcut. Good: margin-floor logic stays proprietary. |
| **Review automation** | Zero OSS. | Build via Trustpilot invitation API (their docs) — simple D+1 flow, high ROI given 25-review baseline. |
| **Product feeds** | Thin but existing (spree_google_merchant 19★ etc.). | Google Shopping/merchant feeds: hand-rolled XML from the canonical table. |
| **Shopify tooling** | Healthy (20 repos ≥5★, top 2133★). | Shopify Admin API first-class — the canonical spine syncs to/from it. |
| **Agentic commerce** | Active space (29 repos, top 2990★). | WiseQ's UCP/MCP endpoints are ahead of the curve — connect them to Hermes as first-class tools. |
| **GS1/EAN** | zint/zint (821★, barcode lib). | EAN purchasing is the business step (see §2); barcode rendering is trivial OSS. |
| **Edtech procurement** | Zero OSS. | School collectives (below) are relationship work + B2B portal, not software. |

## 2. 🕰️ EAN/GS1 in NL — the concrete fix for 0/230

- **GS1 Nederland**: **code package 10 = €61 PER YEAR** (10 article codes/GTINs + 10 GLNs + 1M SSCC). Single code pack (1–5) = €36 one-off. **GS1 EDI annual contribution: €0 for turnover €0–5M (category A–D)**; €200 at €5–11M, etc. All amounts **excl. 21% VAT**. (bol's own partner docs recommend buying direct from GS1 and verifying registration in GS1's portal — resold codes often unregistered.)
- WiseQ needs EANs for **114 components** (see bundle spine) + **25 bundles** = **139 GTINs** — and since WiseQ sells on both bol.com and Amazon, per-listing GTINs are required for **all 139**. **Live tariff (until Dec 1 2026, verified Oct 23 from [gs1.nl](https://www.gs1.nl/producten-services/digital-identity/huidige-tarieven/)): one codepakket 1.000 at €196/yr covers all of them — plus GS1 Contribution €29/yr (sub-€1M turnover band) = €225/yr total, excl. VAT.** ⚠ Correction history: "€732 one-off" (wrong product, wrong frequency) → "14 × 10-packs = €854/yr" (right frequency, wrong packaging — stacking 10-packs is more expensive than the 1,000-pack). Full 230-SKU coverage needs **no extra codes** within the same 1,000-pack.
- **Prefix note:** the GTIN must be actively *registered* in Verified by GS1, not merely purchased — required for the live Amazon EU listings (.de/.fr/.it/.es). That's an operational task we can automate.
- Cheap vs. the manual-EAN-Excel hours Rob spends today. **First week one-liner: order GS1 10-packs, assign to the 114-component registry (CSV already delivered), propagate to Shopify variants + ChannelDock.**

## 3. 💬 Integration surface (verified links)

- **bol Retailer API** — OAuth2 (login.bol.com SSO), endpoints for offers/orders/shipments/product content; dlt-hub documents a Python source. Access via bol Seller Dashboard application.
- **e-Boekhouden.nl API** — the likely bookkeeping package (NL SMB standard; Rob's transcript mentioned "boekhouden software" generically). Full REST API with webshop/CRM/bank couplings; alternatives Moneybird (API-first, dev-friendly) and Exact Online (heavier, full ERP).
- **ChannelDock & 5X** — **both DO have APIs** (verified 2026-10-22, correcting an earlier note in this repo that said "no public API docs found in searches"):
  - *ChannelDock*: REST API + webhooks, **included from the "Voorraad" plan (from €45/mo excl. VAT)**, **excluded from the free tier**. Free tier also caps at 100 products / 500 orders per month — so a 230-product operation is necessarily on a paid plan. 213+ live integrations (Shopify, bol.com, Amazon, WooCommerce, …). ChannelDock is a bol.com Bronze Partner. PIM is a separate €200/mo module that includes bundle composition ("Bundels samenstellen"). Inventory sync runs every 15 min.
  - *5X*: has a first-party **API koppelingen** section (Settings → API Links) that consumes bol.com Client ID/Secret and covers analytics, orders, ads, repricing, inventory and finance exports. 5X is also a native ChannelDock integration.
  - **Ask in Phase 0:** which ChannelDock plan are they on, and do they already pay for PIM? That determines what we automate and whether the bundle-spine work is partly a configuration task rather than a build.
- **Trustpilot** — invitation/business APIs public; D+1 post-delivery invitation flow is standard.
- **Thuiswinkel Waarborg** — 92-96% consumer recognition, the dominant NL trust mark. **Current verified cost (2026-10-22, thuiswinkel.org): €75 one-time + €390/yr certification, PLUS a revenue-tiered contribution — €518/yr at €0–100k turnover, rising to €1,294/yr at €500k–1M; €45/yr per extra platform (bol.com/Amazon).** So realistic year 1 is **€983–€1,759 excl. VAT depending on turnover class.** (This replaces earlier, conflicting figures in this repo of "€465 year one" and "~€500–1,000/yr".) **We do not know WiseQ's turnover — ask them; it sets the tier.** Recommended alongside Scamadviser remediation (Trust Score 0 finding) — strongest available counter to the trust gap.
- **School collectives** — schools increasingly buy via collectives/inkoopcollectieven (Onderwijs Inkoop Groep, Contractables etc.); WiseQ's B2B layer (staffelprijzen, Bestel op factuur) maps to this market. Getting listed in collective catalogs = volume channel; edtech procurement has no OSS, it's sales work.

## 4. 📦 OSS shortlist per layer (from `data/oss/`)

| Layer | Repo | ★ | Use |
|---|---|---|---|
| Barcode | zint/zint | 821 | Render EAN-13 barcodes for labels/packing slips |
| Shopify | AhmadHassan-BTed/ShopifyAutoAuth + 19 others ≥5★ | 2,133 | Admin API patterns; catalog sync patterns |
| Agentic | CloddsBot + 28 others | 2,990 | Agent-commerce patterns; UCP/MCP interop |
| Bol PHP client | picqer/bol-retailer-php-client | 29 | Reference implementation for the official API's endpoints |
| Product feed | spree_google_merchant | 19 | Google Shopping feed XML pattern |

*(Full lists in `data/oss/*.json`; search was GitHub API, ≥5★, non-archived, 2026-10-22.)*

## 5. 🧱 Additional considerations surfaced

1. **Bol drift audit** (312 vs 230): the picqer client + Retailer API makes a full offers-list export a one-day job → diff vs Shopify → kill/merge the 82 ghosts.
2. **Moneybird vs e-Boekhouden**: if Rob's bookkeeping is up for renewal, Moneybird's API-first design makes the agent integration cleaner; otherwise stay with e-Boekhouden (couplings exist).
3. **Trustpilot + Thuiswinkel together**: review engine (D+1 invitations) + the mark fixes the two trust suppressors (13 reviews, Scamadviser 0) in one motion.
4. **Google Shopping feed**: bol is covered via Retailer API; Google Merchant is the next cheapest channel — feed generated nightly from the canonical spine.
5. **School collectives as B2B channel 2.0**: staffelprijzen layer exists; next step is getting into 2-3 collective catalogs (sales motion, not software — but our 857-org lead list is the target list).

---

## 📌 In short

The NL e-commerce tooling layer is **thin at the edges and absent in the middle** — Bol, Shopify, GS1 and GS1 XML are covered by proprietary incumbents, but nothing coordinates them. That is the moat: orchestration is the gap everyone else ignores. Two corrections landed here on 2026-10-22: **ChannelDock and 5X both do have APIs** (ChannelDock's REST API + webhooks are plan-gated from €45/mo), and the **GS1 €733/yr is recurring, not one-off**.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Oss Catalog 100](10-OSS-CATALOG-100.md)** | 100 curated repos by stack layer |
| **[Ai Stack Blueprint](../a-proposal/04-AI-STACK-BLUEPRINT.md)** | Which integrations the blueprint depends on |
| **[Compliance Regulatory](11-COMPLIANCE-REGULATORY.md)** | The compliance constraints on each choice |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
