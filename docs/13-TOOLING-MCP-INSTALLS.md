<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 13* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Tooling & Integration Plan

*2026-10-22. The concrete layer: which connectors, which installs, which custom builds — for the WiseQ engagement. Grounded in a live catalogue audit, connectors verified from research, and the OSS catalogues in docs 08 and 10.*

## 0. 🧭 The capability base

Connector-based tooling has matured enough that most of the integration surface is assembled from connectors rather than hand-built. We maintain a working catalogue of the available integrations and reach for them by default.

Three principles govern every choice in this document:

1. **Connectors before custom code.** A maintained connector is cheaper to own than a wrapper we maintain forever.
2. **Least privilege, every time.** Read-only first. Write scopes are added only when a specific automation needs them.
3. **Credentials in a vault.** Never in a repository, never in chat. Token retrieval is handled by the runtime, not by documents.

Where the WiseQ stack has no official connector, we build a **thin wrapper** — a small, well-documented MCP server with a handful of tools, built once and reusable across engagements.

## 1. 🕰️ The connector install list

| Priority | Connector | Type | Use |
|---|---|---|---|
| P0 | **Shopify Admin** (custom app, OAuth) | Custom install | Catalogue / orders / customers — the canonical-spine sync partner; scoped read+write on products, read on orders |
| P0 | **Shopify dev context** (API docs) | Package | Shopify API documentation context for the build agent |
| P0 | **filesystem + sqlite** | Already available | Canonical spine database + file artefacts |
| P1 | **e-Boekhouden** (custom, thin) | Build | Their API is REST; wrap ~12 endpoints as tools (invoice create/list, relation sync) |
| P1 | **bol Retailer API** (custom, thin) | Build | Offers / orders / shipments as tools; OAuth2 token in the vault |
| P1 | **Trustpilot** (custom, thin) | Build | Business API: invitation create, review list — the review engine's hands |
| P2 | **Klaviyo** (catalogue: available) | Install | If WiseQ adopts Klaviyo rather than a self-hosted ESP — flows / segments / reporting |
| P2 | **UVdesk** (custom, thin) | Build | Ticket queue read/write for the school-order inbox |
| P2 | **Canva** (catalogue) | Install | Product imagery quick edits |
| P2 | **Cloudinary** (catalogue) | Install | Image pipeline storage and transforms |
| P3 | **Umami** (custom, thin) | Build | Analytics read for the Monday report |
| P3 | **GS1 / barcode issuance** | Skip | EAN purchase is human + web form; no connector needed |

## 2. 💬 The install plan

### Access we need from WiseQ (mostly API credentials, light install)

1. **Shopify custom app** — WiseQ creates, we scope it: products read/write, orders read, inventory read/write, no customer-data scope beyond shipping. Least privilege, and GDPR-clean by construction.
2. **bol Seller Dashboard → API credentials** — the Retailer API client we build reads offers/orders and writes price/stock.
3. **e-Boekhouden API key** — read invoices, write sales entries.
4. **Trustpilot business API** — invitation endpoint only.
5. **Our infrastructure** — a dedicated, isolated profile for this engagement, so WiseQ's sessions, memory, and credentials stay separate from every other one. Credentials are held in a secrets vault; never in a repository, never in chat. This is a hard rule, not a preference.

## 3. 📦 New insights from the integration research

1. **Square and PayPal have official hosted MCP servers** — clear evidence the industry direction is agent-native payments. WiseQ's payment stack has no MCP yet, so our thin wrappers are both the pattern and potentially a reusable asset.
2. **Klaviyo is available in the catalogue** — if WiseQ prefers a SaaS ESP over a self-hosted option, the agent runs it natively on day one. A decision point for WiseQ, not a blocker.
3. **The Shopify MCP guide's key line** — *"if you're a merchant, you mostly don't build this; your store already participates."* Shopify is preparing agent-native commerce, and WiseQ's UCP/MCP endpoints already put it ahead of the default Shopify store. Our stack amplifies that lead rather than creating it.
4. **WhatsApp is going agent-native** — a self-hosted gateway covers low volume at near-zero marginal cost; the official Business API's per-conversation pricing takes over around ~2k conversations/month. That crossover gets re-checked before it matters.
5. **A hosted scraping service is available but paid** — a local, dependency-light crawler covers the market-intelligence surface at zero marginal cost. Decision: local-first, and only engage the hosted service if a specific site defeats the local crawler.
6. **Workflow-automation MCP exists in the catalogue** — the decide-here / execute-there split gets a native bridge; enable it when the first workflow ships, not before.

## 4. 🧱 Consolidated install checklist (ordered)

**Week 1 (zero-access prep, do now):**
- [ ] Enable the payment and workflow connectors from the catalogue — ready before they are needed
- [ ] Provision the engagement environment and bring up the service stack (agent runtime, change-detection, reverse proxy)
- [ ] Seed the price/stock watch URLs for WiseQ's suppliers and competitors
- [ ] Pull in the Shopify API documentation context and build the canonical-spine schema in SQLite

**Week 2–3 (needs WiseQ's access):**
- [ ] Shopify custom app + scopes; bol API credentials; e-Boekhouden key; Trustpilot business account
- [ ] Build the three thin wrappers (e-Boekhouden, bol, Trustpilot) — each ≤ 12 endpoints, documented, and built as reusable components
- [ ] Component-registry schema design, seeded from the 114-component registry already in this repository

**Month 2+:**
- [ ] UVdesk and Umami wrappers
- [ ] Advertising-platform connector live, with budget guardrails and approval gates
- [ ] Electronic-invoicing connector at the point the Dutch regime requires it
- [ ] Klaviyo-vs-self-hosted decision, together with WiseQ

## 5. 🗺️ What we deliberately do NOT install

- **A full ERP replacement** — nothing gets replaced; the existing stack stays.
- **A custom storefront platform** — not until the shop genuinely outgrows what it runs today.
- **Paid hosted scraping** — while the local crawler suffices.
- **Official messaging APIs** — while a self-hosted gateway covers the volume.
- **Any connector without a scheduled use** — a catalogue is a menu, not a shopping list; one owner per layer.

<div align="center">
<sub>Every connector above is scoped read-only until a specific automation justifies write access.</sub>
</div>