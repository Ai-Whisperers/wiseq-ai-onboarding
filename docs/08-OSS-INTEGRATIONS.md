<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
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

- **GS1 Nederland**: single code pack (1–5) €36 one-off; **code package 10 = €61 PER YEAR** (10 article codes/GTINs + 10 GLNs + 1M SSCC). **GS1 EDI annual contribution: €0 for turnover €0–5M** (categories A–D); €200 at €5–11M. All amounts excl. 21% VAT. (bol's own partner docs recommend buying direct from GS1 and verifying registration in GS1's portal — resold codes often unregistered.)
- WiseQ needs EANs for **114 components** (see bundle spine) **+ 25 bundles = 139 GTINs** → **14 × €61 = €854/yr, recurring every year** (€1,033 with VAT) — ⚠ an earlier figure in this doc said 12 packs/€733, but 12 packs covers only **120** codes; 139 needs **14**. **Full 230-SKU coverage = 23 packs = €1,403/yr** (€1,698 w/ VAT). ⚠ **Correcting an earlier figure in this repo:** this was written as a "€732 one-off". It is **not one-off** — the 10-pack is an annual product, and the total **repeats every year** while those codes stay registered. bol and Amazon both require a GTIN per listing, so bundle SKUs must be registered too, not just components.
- Cheap vs. the manual-EAN-Excel hours Rob spends today. **First week one-liner: order GS1 10-packs, assign to the 114-component registry (CSV already delivered), propagate to Shopify variants + ChannelDock.**

## 3. 💬 Integration surface (verified links)

- **bol Retailer API** — OAuth2 (login.bol.com SSO), endpoints for offers/orders/shipments/product content; dlt-hub documents a Python source. Access via bol Seller Dashboard application.
- **e-Boekhouden.nl API** — the likely bookkeeping package (NL SMB standard; Rob's transcript mentioned "boekhouden software" generically). Full REST API with webshop/CRM/bank couplings; alternatives Moneybird (API-first, dev-friendly) and Exact Online (heavier, full ERP).
- **ChannelDock & 5X** — ⚠ **corrected 2026-10-22: both DO have APIs.** An earlier version of this doc said "no public API docs found in searches"; that was a search failure, not a fact. ChannelDock ships a **REST API + webhooks** from the **Voorraad plan (from €45/mo)** upward — not on the free plan, which caps at 100 products (WiseQ has 230, so they are almost certainly already on a paid plan). **Consequence for scoping:** the browser-automation-first approach described here is no longer the primary path for ChannelDock. Note also that ChannelDock sells a **PIM module (€200/mo)** that advertises "Bundels samenstellen" (bundle composition) — so part of the planned bundle work may be a configuration task rather than a build. **Which plan are they on, and do they already have PIM?** is now a Phase 0 question in [doc 06](06-NEXT-STEPS.md).
- **Trustpilot** — invitation/business APIs public; D+1 post-delivery invitation flow is standard.
- **Thuiswinkel Waarborg** — 92-96% consumer recognition, the dominant NL trust mark. **Corrected 2026-10-22 (thuiswinkel.org, verified):** €75 one-time + €390/yr certification **plus a turnover-tiered contribution** — €518/yr at €0–100k turnover, €776 at €100–250k, €1,035 at €250–500k, €1,294 at €500k–1M — so **year 1 is €983–€1,759 depending on turnover class**, plus **€45/yr per extra platform** (they also sell on bol.com and Amazon). The earlier "~€500-1,000/yr ballpark" in this doc was directionally right but hid that it is revenue-tiered. Recommended alongside Scamadviser remediation (Trust Score 0 finding) — strongest available counter to the trust gap.
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
3. **Trustpilot + Thuiswinkel together**: review engine (D+1 invitations) + the mark fixes the two trust suppressors (25 reviews, Scamadviser 0) in one motion.
4. **Google Shopping feed**: bol is covered via Retailer API; Google Merchant is the next cheapest channel — feed generated nightly from the canonical spine.
5. **School collectives as B2B channel 2.0**: staffelprijzen layer exists; next step is getting into 2-3 collective catalogs (sales motion, not software — but our 857-org lead list is the target list).

---

## 📌 In short

The NL e-commerce tooling layer is **thin at the edges and absent in the middle** — Bol, Shopify and GS1 are covered by proprietary incumbents, but nothing coordinates them. That is the moat: orchestration is the gap everyone else ignores. Two corrections landed here on 2026-10-22: **ChannelDock and 5X both do have APIs** (ChannelDock's REST API + webhooks are plan-gated from €45/mo), and the **GS1 €733/yr is recurring, not one-off**.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Oss Catalog 100](10-OSS-CATALOG-100.md)** | 100 curated repos by stack layer |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | Which integrations the blueprint depends on |
| **[Compliance Regulatory](11-COMPLIANCE-REGULATORY.md)** | The compliance constraints on each choice |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
