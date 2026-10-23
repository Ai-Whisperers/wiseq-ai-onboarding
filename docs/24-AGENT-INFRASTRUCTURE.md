<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 24* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Agent infrastructure blueprint — the Hermes setup that runs this project

*Oct 23, 2026. What AIW actually stands up if the engagement starts: the profile architecture, the MCP layer (re-verified this week — several doc-13 assumptions just got cheaper), the skill set, the safety rails, and the day-one to steady-state sequence. Grounded in the live AIW instance (43 MCP servers, 195 skills, profiles ivan+kiki) and this week's platform releases.*

---

## 0. 🧭 What changed since doc 13 (verified Oct 23)

| Doc 13 assumption | Reality this week | Consequence |
|---|---|---|
| "e-Boekhouden MCP (custom, thin) — build ~12 endpoints" | **Exact Online MCP now exists, twice**: [lemon-official/exact-mcp](https://github.com/lemon-official/exact-mcp) (self-hosted, OAuth in-server, Fernet-encrypted tokens, OData-constrained) and [Praat met je Boekhouding — Exact Online](https://www.pulsemcp.com/servers/praatmetjeboekhouding-exact-online) (75 tools, OAuth 2.1, EU-hosted) | If WiseQ runs Exact: **install, not build**. The custom wrapper only remains for 5X or another package |
| Shopify = custom app + dev-mcp | **[Shop MCP](https://shopify.dev/changelog/posts/add-shopping-and-shop-pay-checkout-to-any-agent-with-shop-mcp) live at `mcp.shop.com`** (Oct 13): `search_catalog`/`get_product` keyless, carts + Shop Pay checkout; **[UCP CLI](https://shopify.dev/docs/agents)** (`npm i -g @shopify/ucp-cli`) + Shopify AI toolkit | Catalog intelligence becomes zero-credential day one; the custom Admin app is still needed for *merchant-side* writes (our pipelines), but buyer-side agentic presence is a URL |
| (not covered) | **[Bolyra Gateway MCP](https://www.pulsemcp.com/servers/bolyra-gateway)**: reverse proxy adding per-tool permission policies, credential verification, signed audit receipts to any MCP server | The write-gating layer for client-facing MCPs can be bought, not built |
| "bol Retailer MCP — build" | Still true; no official bol MCP found | Stays a thin custom wrapper (endpoints already mapped, addendum 1) |

**Net: the integration surface shrank again.** Three of the seven custom builds in doc 13 are now installs or near-installs.

---

## 1. 🏗️ Profile architecture: one Hermes profile per operation

The AIW VPS already runs multi-profile Hermes (ivan, kiki). WiseQ gets its own:

```
hermes --profile wiseq        # the engagement's isolated instance
├── config.yaml               # its own model routing, MCP set, approval modes
├── .env                      # ONLY credentials (BWS-synced, never git)
├── skills/                   # the 9 engagement skills (§3)
├── state.db                  # sessions — GDPR scope: contains customer data
├── cron/                     # scheduled jobs (school-order sweep, OSS watchdog…)
└── workspace/                # cloned wiseq-ops repo (the code we write)
```

**Why a profile and not a container-per-agent:** one profile = one gateway, one credential surface, one place to audit, sessions share the engagement memory; containers multiply surfaces. The fleet pattern (many dispatch workers) is for *our* build capacity, not for *their* operations — exactly how AIW separates ivan (operations) from fleet (dispatch).

**Data residency note (AVG art. 28):** `state.db` holds order/customer data processed for WiseQ → it lives on the EU-side VPS, covered by the verwerkersovereenkomst (addendum 2 §3), deleted/returned at contract end per doc 18. The profile boundary IS the GDPR boundary — one directory to export, one to wipe.

---

## 2. 🔌 The MCP layer (per priority, re-verified)

### P0 — day one (zero or client-light credentials)

| MCP | Install | Why |
|---|---|---|
| **Shop MCP** (`https://mcp.shop.com`) | URL add | Keyless catalog search/lookup across 1B+ products — competitor price intelligence from day one, no keys |
| **Shopify dev-mcp** (`npx -y @shopify/dev-mcp@latest`) | npm | Admin GraphQL schema introspection — the build agent writes correct queries first time |
| **filesystem, sqlite** | already on | The canonical spine (bundle CSVs → SQLite) |
| **github** | already on | The wiseq-ops repo: PRs, CI, reviews |
| **brave-search / exa** | already on | Compliance/competitor research lanes |
| **context7, deepwiki** | already on | Library docs for the wrapper builds |

### P1 — week 2–3 (needs Rob's access; the Gate-1.2 moment)

| MCP | Install | Note |
|---|---|---|
| **Shopify Admin custom app** | Rob creates, we scope | products r/w, orders r, inventory r/w, Fulfillment — least privilege |
| **Exact Online MCP** | self-host `lemon-official/exact-mcp` (or the EU-hosted 75-tool one, client's choice) | **New since doc 13** — kills the bookkeeping build *if* WiseQ runs Exact. OAuth stays inside the server |
| **bol Retailer wrapper** | **build** (~10 tools: offers list/update-price/update-stock, orders, shipments, commission-read) | Thin; endpoints mapped in addendum 1; async process-status pattern required |
| **Trustpilot wrapper** | **build** (~4 tools: invitation create/list, reviews read) | Small; API is straightforward REST |

### P2 — when the engines light up

| MCP | For |
|---|---|
| **Bolyra Gateway proxy** (eval) | Per-tool policies + signed audit receipts in front of the write-capable MCPs — aligns with doc 23 Gate 4; evaluate vs Hermes' own approval modes before building |
| **ChannelDock wrapper** (build, ~8 tools) | Stock sync + bundle composition (their PIM module does bundles — read their data model first) |
| **Klaviyo** (catalog: available) | If WiseQ picks SaaS ESP |
| **PostNL wrapper** (build, ~5 tools) | Label creation + track&trace for the school-pipeline shipping step |
| **Umami/GA4 read wrapper** | Monday report analytics |

### Not installed (unchanged from doc 13 §5)
Odoo/ERPNext, Medusa/Saleor, Firecrawl while Scrapling suffices, any MCP without a scheduled use.

---

## 3. 🧠 The skill set (what the profile knows)

Nine engagement skills, seeded from AIW's 195 and adapted — each carries its own runbook:

1. **wiseq-operations** — the master protocol: daily order sweep, escalation rules, who-approves-what, the "never surprise Rob" rule
2. **shopify-admin-ops** — Admin GraphQL patterns, bulk mutations, rate-limit budget, webhook reconciliation (the dropped-webhook lesson from Order MCP docs)
3. **bol-retailer-ops** — the async process-status discipline, commission-read-before-reprice (addendum 5's live-rate rule), offer-state machine
4. **school-pipeline** — the flagship: email→offer→invoice flow, staffelprijzen tiers, aggregation/threshold flags (addendum 2's anti-saucissoneren rule), quote-PDF requirements
5. **oss-vat-watchdog** — the €10k retroactive threshold monitor (addendum 6), quarterly filing calendar
6. **compliance-triage** — GPSR/EN-71/RED per-SKU checklist (addendums 3–4), Amazon compliance dashboard audit procedure
7. **reputation-engine** — Trustpilot invitation ethics (never selective), Scamadviser remediation playbook (addendum 5)
8. **incident-runbooks** — per workflow: healthy looks like / silence means / 3-step restart (doc 15 §5)
9. **client-communication** — Dutch output conventions, tone, the native-review gate for anything customer-facing

Skills 2–5 are **built during Phase 1 by us, in the wiseq-ops repo** — they are deliverables Rob keeps (doc 18: the repo, skills, and runbooks transfer at handover — the operation is operable without us by design).

---

## 4. 🛡️ Safety rails (the layer that makes it client-grade)

1. **Approval modes per tool class**: read-only MCPs run free; write-capable MCPs (price updates, stock writes, invitations) run behind Hermes' approval gate — **Phase 1: human approves every write; Phase 2: auto-approve writes that pass guardrail checks, humans approve exceptions** (mirrors doc 23's gates: Gate 4 unlocks financial writes only after reconciliation passes)
2. **Guardrails as code**: margin floor (never price below X% margin), OSS threshold alert, max-invitations/day, stock-write delta ceiling (>50% change = freeze + ask) — each a small policy function, versioned in the ops repo, tested in CI
3. **Bolyra or native**: evaluate the gateway proxy for audit receipts (signed per-tool-call receipts = strong doc-23 Gate-4 evidence) against Hermes' own approval log — pick one, not both
4. **Heartbeats + SLOs** (doc 15 §5): every cron writes a heartbeat; Better Stack alerts on silence — the *monitoring the monitors* layer
5. **Secrets**: all credentials in BWS, `.env` synced by the profile, zero secrets in the ops repo (CI enforces — same validator pattern as the onboarding repo)

---

## 5. 🕰️ The standing schedule (steady state)

```
06:30  order sweep          — new orders since last run; classify (school/consumer/
                              bol/Amazon); draft responses; flag exceptions
07:00  morning digest       — one message to Rob: orders, stock alerts, compliance
                              flags, anything needing his yes
hourly OSS watchdog          — cross-border revenue running total vs €10k threshold
nightly stock reconcile      — Shopify ↔ ChannelDock ↔ bol; drift report
nightly competitor sweep     — Shop MCP keyless search on key SKUs + price watch
weekly  monday report        — DuckDB over price history: drift, dispersion, margin
weekly  compliance scan      — Amazon GPSR dashboard deltas, new ASIN flags
monthly restore test         — the doc-15 rule: prove the backup restores
```

Every job: heartbeat + failure alert via the briefing rail. **One daily digest to Rob, not forty messages** — the school-morning problem was message overload; our operations must not recreate it.

---

## 6. 📦 What this costs (incremental, over existing AIW infra)

| Item | Cost |
|---|---|
| wiseq profile on the existing VPS | €0 (headroom exists) |
| MCP installs (Shop, dev-mcp, Exact) | €0 |
| Custom wrappers ×3–4 (bol, Trustpilot, ChannelDock, PostNL) | build time in Phase 1, already priced |
| Neon Postgres wiseq DB | free tier → ~€19/mo at scale (doc 15) |
| Better Stack / BWS / R2 | already on AIW accounts |
| Model spend | the doc-04 €40–90/mo band, measured in Gate 5.3 |

No new platform spend until the pilot proves itself — the engagement runs on infrastructure that is already running.

---

## 7. 🤝 Handover alignment (doc 18 made concrete)

At contract end, WiseQ receives: the ops repo (code + skills + runbooks), the profile export (sessions, memory, cron definitions), all credentials (rotated to their custody), the databases, and this document's architecture map. **A successor operator — human or agent — can run the profile from the runbooks alone.** That is the test doc 18 promises and this blueprint is designed to pass.

---

## 📌 In short

A dedicated Hermes profile on the existing VPS; 6 already-on MCPs + 3 installs + 3 thin builds; nine skills (five of them deliverables); writes gated until Gate 4 passes; one daily digest to Rob; heartbeats on everything; handover by design. The stack shrank again this week — Exact and Shop MCPs turned two builds into installs. What remains custom is precisely the WiseQ-specific value: the school pipeline, the spine, the watchdogs.

---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Tooling MCP installs](13-TOOLING-MCP-INSTALLS.md)** | The original install plan this updates |
| **[DevOps masterplan](15-DEVOPS-MASTERPLAN.md)** | Storage, backups, SLOs |
| **[Acceptance criteria](23-ACCEPTANCE-CRITERIA.md)** | The gates that unlock each layer |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
