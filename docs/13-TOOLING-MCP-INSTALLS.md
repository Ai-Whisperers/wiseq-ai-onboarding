<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 13* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Tooling, MCP Setup & Install Plan — Both Operations

*2026-10-22. The concrete layer: which MCP servers, which installs, which custom builds — for the WiseQ engagement and the PY operation. Grounded in the live Hermes catalog (`hermes mcp catalog`), verified MCP servers from research, and the OSS catalogs (docs 08/10 here, doc 08 PY).*

## 0. 🧭 What's already in the AIW Hermes instance (verified live)

Enabled right now: **github, figma, airtable, cloudflare, context7, datadog, deepwiki, dropbox, fireflies, intercom, klaviyo, linear, notion, postman, semgrep, stripe, supabase, todoist, twelfe-data, vercel, wolfram, brave-search, drawio, exa, filesystem, slack, sqlite** + Bitwarden Secrets (196 secrets applied).

Notable catalog items **available but not enabled** that map directly to our needs: **n8n-official, paypal, square, sentry, mixpanel, amplitude, grafana, cloudinary, canva, gamma**.

## 1. 🕰️ The MCP install list (per operation)

### WiseQ engagement — enable/install:

| Priority | MCP | Type | Use |
|---|---|---|---|
| P0 | **Shopify Admin MCP** (custom app, OAuth) | Custom install | Catalog/orders/customers — the canonical-spine sync partner; scope it read+write on products, read on orders |
| P0 | **Shopify dev-mcp** (context) | npm | Shopify API docs context for the build agent |
| P0 | **filesystem + sqlite** (already on) | — | Canonical spine DB + file artifacts |
| P1 | **e-Boekhouden MCP** (custom, thin) | Build | Their API is REST; wrap ~12 endpoints as MCP tools (invoice create/list, relation sync) |
| P1 | **bol Retailer API MCP** (custom, thin) | Build | Offers/orders/shipments endpoints as tools; OAuth2 token in vault |
| P1 | **Trustpilot MCP** (custom, thin) | Build | Business API: invitation create, review list — the review engine's hands |
| P2 | **Klaviyo** (catalog: available) | `hermes mcp install klaviyo` | If WiseQ adopts Klaviyo instead of BillionMail — flows/segments/reporting |
| P2 | **UVdesk MCP** (custom) | Build | Ticket queue read/write for the school-order inbox |
| P2 | **canva** (catalog) | install | Product imagery quick-edits |
| P2 | **cloudinary** (catalog) | install | Image pipeline storage/transforms |
| P3 | **Umami MCP** (custom, thin) | Build | Analytics read for the Monday report |
| P3 | **GS1/bippo** | Skip | EAN purchase is human + web form; no MCP needed |

### PY operation — enable/install:

| Priority | MCP | Type | Use |
|---|---|---|---|
| P0 | **Evolution API MCP** ([aiteks-ltda/mcp-evolution-whatsapp-api](https://github.com/aiteks-ltda/mcp-evolution-whatsapp-api)) | npm/git install | WhatsApp send/receive/groups via our self-hosted Evolution gateway |
| P0 | **sqlite/filesystem** (already on) | — | Canonical product/price table |
| P0 | **Scrapling/Scrapy** as callable tools | Python lib (not MCP) | Nightly CDE crawl — cron invokes scripts; agent reads results |
| P1 | **changedetection.io API** (custom thin MCP) | Build | Watch management: add/check price-watch URLs |
| P1 | **InvenTree MCP** (custom, thin) | Build | ~10 API endpoints (parts, stock, suppliers) as tools |
| P1 | **uPay/Bancard webhook listener** | Custom (webhook → Hermes) | Payment events land as `--deliver-only` webhooks (pattern already proven in AIW) |
| P2 | **Meta Ads MCP** (oliverames/meta-mcp-server) | npm/git | Campaign create/pause/inspect with budget guardrails |
| P2 | **Google Business Profile** (custom) | Build | Review replies + weekly post |
| P3 | **SIFEN/SIAT invoice MCP** (custom) | Build | Emit factura electrónica per sale at SIMPLE regime |

## 2. 💬 The install plan (servers & software)

### WiseQ side (mostly API access, light install):

1. **Shopify custom app** (Rob creates; we scope it): products r/w, orders r, inventory r/w, no customer-data scope beyond shipping — least privilege, GDPR-clean
2. **bol Seller Dashboard → API credentials** (Rob): the Retailer API client we build reads offers/orders, writes price/stock
3. **e-Boekhouden API key** (Rob): read invoices, write sales entries
4. **Trustpilot business API** (Rob): invitation endpoint only
5. **Our infra**: the AIW VPS already runs Hermes — a second profile (`hermes --profile wiseq`) isolates the engagement; BWS vault stores all credentials (never in repos — hard rule)

### PY side (real installs — one VPS, docker-compose):

```yaml
# docker-compose.pydrop.yml (the phase-0 stack)
services:
  hermes:            # orchestrator (profile: pydrop)
  evolution-api:     # WhatsApp gateway (container, 9.9k★)
  changedetection:   # price/stock watches (35k★)
  inventree:         # stock registry (7.7k★) — phase 1
  n8n:               # simple notification flows
  umami:             # shop analytics (39.5k★) — phase 1
  billionmail:       # ESP when the list needs it — phase 2
  caddy:             # reverse proxy + auto-TLS
```

Plus host-level: **SQLite → Postgres at scale** (Neon MCP already enabled for managed Postgres), nightly `restic` backups off-site, uptime monitoring via **Better Stack** (already enabled), cron via Hermes jobs.

## 3. 📦 New insights from the MCP research

1. **Square + PayPal have official hosted MCP servers** (in catalog) — evidence the industry direction is agent-native payments; WiseQ/PY payment stacks (uPay/Bancard) have no MCP yet → our thin wrappers are the pattern, and potentially a first-in-market asset.
2. **Klaviyo is in the catalog** — if WiseQ prefers SaaS ESP over self-hosted BillionMail, the agent runs it natively day one. Decision point for Rob, not a blocker.
3. **The Shopify MCP guide's key line** (gamut.so): "if you're a merchant, you mostly don't build this — your store already participates" — i.e., Shopify is preparing agent-native commerce; WiseQ's UCP/MCP endpoints put them AHEAD of the default Shopify store. Our stack amplifies that lead.
4. **WhatsApp is going agent-native** (Bluetucks/Wati analyses): Evolution API + MCP is the bridge today; WhatsApp's official Business API pricing (per-conversation) still favors our gateway approach for phase 0-1 volume.
5. **Firecrawl has an official MCP** — but it's a paid SaaS; Scrapling (89k★, local) covers CDE scraping at 0 marginal cost. Decision: local-first, Firecrawl only if a site defeats Scrapling.
6. **n8n-official MCP exists in catalog** — the Hermes-decides/n8n-executes split (PY doc 04) gets a native bridge; enable when the first n8n flow ships.

## 4. 🧱 Consolidated install checklist (ordered)

**Week 1 (zero-access prep, do now):**
- [ ] `hermes mcp install n8n-official paypal square` (catalog) — payments/flows ready
- [ ] PY VPS: provision + docker-compose up (hermes, evolution, changedetection, caddy)
- [ ] Evolution API: number provisioning + warmup schedule (anti-ban protocol, PY doc 07 H.40.1)
- [ ] changedetection.io: seed Fastrax + Shopping China + Tupi category URLs
- [ ] Shopify dev-mcp (docs context) + build the canonical-spine schema in sqlite

**Week 2-3 (needs Rob's access):**
- [ ] Shopify custom app + scopes; bol API credentials; e-Boekhouden key; Trustpilot business
- [ ] Build the 3 thin MCP wrappers (e-Boekhouden, bol, Trustpilot) — each ≤ 12 endpoints, MIT-licensed pattern, reusable Commerce-OS components
- [ ] InvenTree install + component registry import (WiseQ 114-component CSV seeds the schema design)

**Month 2+:**
- [ ] UVdesk + Umami wrappers; Meta Ads MCP live with budget guardrails; SIFEN MCP at SIMPLE-regime time; Klaviyo-vs-BillionMail decision with Rob

## 5. 🗺️ What we deliberately do NOT install

- **Odoo/ERPNext** (phase 3+ only — the hipopótamo rule)
- **Medusa/Saleor** until the shop outgrows Tiendli/Shoperly or Shopify
- **Firecrawl SaaS** while Scrapling suffices
- **WhatsApp Cloud API** official while Evolution covers phase 0-1 volume (cost crossover re-check at ~2k conversations/mo)
- **Any MCP without a scheduled USE** — the catalog is a menu, not a shopping list; one owner per layer (doc 08 rule 4)

---

## 📌 In short

A **verified** inventory against the live Hermes catalog, with per-operation install lists (Shopify, bol, e-Boekhouden, Trustpilot) and an explicit list of what we will **not** install. The week-1 checklist is deliberately small: connect, read, summarise, ask a human before anything writes. No MCP gets production credentials in the first week.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Hermes Jev Aiw Reuse](14-HERMES-JEV-AIW-REUSE.md)** | The reuse-first decision behind this list |
| **[Devops Masterplan](15-DEVOPS-MASTERPLAN.md)** | Hosting and storage for these services |
| **[Next Steps](06-NEXT-STEPS.md)** | The week-1 checklist |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
