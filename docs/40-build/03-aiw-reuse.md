<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track A · Document 14* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Hermes/Jev Optimization + AIW Asset Reuse Inventory

*2026-10-22. Companion to docs 13 (tooling/MCP). Covers: (A) the Hermes-instance optimization decisions incl. the Jev router verdict, (B) the full inventory of what AIW already owns — org repos, personal repos, running systems, skills — that these two operations will reuse instead of rebuild.*

## 🤖 A. Jev & Hermes optimization (documented decisions)

**Jev verdict: keep enabled, target it at the right lanes.**
- Live status (verified 2026-10-22): enabled, decision model `typesafe/jev-1.13` via OpenRouter's decisions endpoint, confidence threshold 0.5, per-turn routing, ~40k audited decisions, fallback deepseek-v4.1-flash/medium.
- **Current behavior: inert on the operator seat** — every turn logs `skip: provider_not_routed` because the interactive profile runs `zai/glm-5.3` direct (not OpenRouter-routed). That's correct by design: the operator keeps full-quality GLM.
- **Where Jev earns its keep: the ops/cron/children lanes.** The WiseQ profile, nightly crawls, delegated tasks running via OpenRouter get per-turn routing across the grid: deepseek-v4.1-flash (general), kimi-k3 (deep code), glm-5.3 (rigorous reasoning), glm-5.3-flash (long-doc extraction), minimax-m3 (fast tool-sequences), nemotron-3-nano:30b (trivial). This is the automated version of our house rule for parse-heavy lanes (60-70% cost cut).
- Grid note: minimax entries are the OAuth lane that 429-killed the WiseQ delegation batch on 2026-10-21 — with `hermes fallback add` (below) the grid becomes resilient instead of brittle.

**Hermes optimization checklist (this instance):**
1. **`hermes fallback add`** — the single highest-value fix. The 4-child research batch died to MiniMax OAuth 429 with no fallback chain; the system suggested the fix at the time; it was never applied. Apply to the shared instance AND both op profiles.
2. **Profiles per engagement** — the `wiseq` Hermes profile is isolated from every other engagement: separate config, sessions, memory, credentials. The security boundary (50-hats #43) and the client-cleanliness boundary in one move.
3. **Credential pools** (`hermes auth`) — 2-3 keys per provider on the crawler lanes so one rate-limit never stalls the nightly snapshot.
4. **Model aliases per task** — `parse → deepseek-v4.1-flash`, `decide → glm-5.3`, `tools → minimax-m3`; cron jobs pin aliases; Jev routes ad-hoc turns.
5. **Skill-ify the parsers** — Shopping-China card parser, bundle-spine decoder, email harvester v2 → Hermes skills (one skill_manage call each): future sessions load the procedure instead of re-deriving it.
6. **Webhooks `--deliver-only`** — uPay/Bancard payment events → Hermes runs, zero prompt cost on the event path.
7. **TUI widget** for the ops dashboard (orders/cash/price alerts) — native Hermes widgets beat checking files.
8. **AI-observability from day 1** — Langfuse OSS core (MIT; the `ee/` tier stays OFF per standing red line) or Laminar (Apache-2.0, OTel-native) into the WiseQ docker-compose; OpenObserve for token-spend-as-P&L-line.

## 📦 B. AIW capability inventory — what we reuse

*Verified against our live infrastructure, 2026-10-22. We describe these as **capabilities we already run**, not by repository or client name: the client-facing value is that the stack is not greenfield, and the specific repos are ours, not yours to assess.*

### Capabilities that transfer directly

| Capability we already run | What it is | Reuse for WiseQ |
|---|---|---|
| **Production commerce backend** | FastAPI + SQLite, tax-module invoicing, production-hardened, Sentry + Resend + backups, WCAG work | **The backend skeleton** — invoicing module, payment-reconciliation patterns, test-isolation discipline, deploy flow. Code we already own and run in production |
| **Client-acquisition engine** | Lead intake → scoring → outreach cadence at ~1,000-lead scale | **The outreach machinery** for the WiseQ B2B wave — CRM shape, cadence design, lead scoring reuse |
| **Expense ledger + audit trail** | Financial models, ledger discipline, immutable audit log | Ledger patterns + audit discipline for the WiseQ books |
| **Status + run ledger** | Public status page, auto-generated, sanitized | Status-page pattern for the uptime story (pairs with Better Stack) |
| **Marketing-site template** | A production client website, template and flow | The template/flow for a WiseQ storefront landing |
| **Thin MCP server** | A working MCP server for an unrelated device domain | Proof-of-pattern for our thin MCP wrappers (bol, e-Boekhouden) |

### Supporting infrastructure worth mining

| Capability | What it is | Reuse |
|---|---|---|
| **Ops bootstrap toolkit** | "Bootstrap any VPS, client, or workspace" — the canonical setup repo | **The companion VPS provisioner** — the docker-compose from doc 13 lands on this foundation |
| **Hermes observability library** | Observability library + dashboard + cron health + alert router | **Directly**: agent observability (T2) without building — cron-health checks + alert routing already exist here |
| **Multi-site deploy monorepo** | 19 client lead-sites, shared packages, Cloudflare | Multi-site deploy patterns; shared UI tokens for any landing |
| **Design-token package** | Shared UI components and tokens | Design tokens for shop/landing work |
| **Regional CRM + outreach** | Lead capture and outreach for a local market | Same machinery class as the client-acquisition engine |
| **Regulatory research service** | Regulatory/compliance research corpus with a scheduled update loop | Feeds the compliance docs — update loop for rule changes |
| **Research-pipeline pattern** | A 6-paper research pipeline | Not direct reuse; demonstrates the research-pipeline pattern |
| **Real-time monitoring dashboard** | Ops dashboard | Ops-dashboard base for the TUI/widget + web views |
| **NL market research corpus** | NL market knowledge base | NL-context knowledge base for the WiseQ engagement (minor) |

### Running systems & non-repo assets (from session memory, verified live earlier)

- **Fleet orchestrator** (VPS): multi-peer dispatch, kanban-backed ticketing, per-peer config — the *pattern* for per-engagement orchestration; an operations dashboard for visibility.
- **Hermes skills library**: email harvester patterns, direct-http-research, multi-research orchestration, price-monitor skill, structured-research-repo — loaded procedures, not just code.
- **Credential vault** (secrets applied at boot): the credential store for the engagement — never .env, never repos.
- **Better Stack / Sentry / Cloudflare / Neon / Supabase** MCP integrations already enabled: uptime, error tracking, DNS/CDN, managed Postgres — the ops layer is half-installed already.
- **Public-endpoint security gate** (shared-header token pattern): the auth pattern for any public ops endpoint we expose.
- **Messaging briefing cron patterns** (scheduled digests): the delivery rail for the Monday reports / daily digests.

### Synthesis: the reuse-first stack

The WiseQ engagement assembles almost entirely from owned parts:
**WiseQ** = the commerce-backend patterns + ops-toolkit provisioning + the Hermes observability library + the credential vault + Better Stack + the doc-13 docker-compose + the client-acquisition engine for the 857-org B2B wave + our own thin MCP wrappers (bol/e-Boekhouden/Trustpilot) + the briefing rails.

**What we genuinely build new** (the moat list, unchanged): bundle-spine matcher, school-order parser, CDE price-map agent, WhatsApp closer, repricing engine, Commerce-OS components. Everything else is reuse.

## ➕ C. New setups to consider (beyond doc 13)

1. **A third Hermes profile: `aiw-meta`** — the Commerce-OS productization lane (50-hats #31) separated from client work.
2. **Monorepo question**: the thin MCP wrappers (bol, e-Boekhouden, Trustpilot, changedetection, InvenTree) belong in ONE `commerce-os` repo (product) rather than scattered across client repos — decide before the third wrapper lands.
3. **The regulatory research service as a living service**: cron-check the relevant rule changes monthly → update the compliance docs automatically. Turn a research corpus into a monitoring service.
4. **ai-whisperers-hermes-agent adoption for both ops**: wire cron-health + alert-router into the two profiles at setup time (not later) — observability is a day-1 setting per the 50-hats #40.
5. **Status page**: the status-page pattern, one page — trust signal for WiseQ B2B buyers ("system monitored 24/7").

---

## 📌 In short

The verdict is **reuse-first**: most of the stack does not need to be built at all — it needs to be assembled from capabilities already in production elsewhere, ours to bring. This is the single strongest argument in the proposal for a realistic timeline, and the clearest answer to 'why should we trust a new partner with our stack'.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Tooling Mcp Installs](02-tooling-mcp.md)** | Per-operation MCP install lists |
| **[Bundle spine & reuse](../10-client/06-bundle-spine-reuse.md)** | The specific components worth porting |
| **[Ai Stack Blueprint](../20-offer/01-blueprint.md)** | How reuse reshapes the blueprint |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
