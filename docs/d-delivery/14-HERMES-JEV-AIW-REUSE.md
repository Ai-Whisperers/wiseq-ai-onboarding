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
- **Where Jev earns its keep: the ops/cron/children lanes.** PY + WiseQ profiles, nightly crawls, delegated tasks running via OpenRouter get per-turn routing across the grid: deepseek-v4.1-flash (general), kimi-k3 (deep code), glm-5.3 (rigorous reasoning), glm-5.3-flash (long-doc extraction), minimax-m3 (fast tool-sequences), nemotron-3-nano:30b (trivial). This is the automated version of the PY hat-36 rule (60-70% cost cut on parse-heavy lanes).
- Grid note: minimax entries are the OAuth lane that 429-killed the WiseQ delegation batch on 2026-10-21 — with `hermes fallback add` (below) the grid becomes resilient instead of brittle.

**Hermes optimization checklist (this instance):**
1. **`hermes fallback add`** — the single highest-value fix. The 4-child research batch died to MiniMax OAuth 429 with no fallback chain; the system suggested the fix at the time; it was never applied. Apply to the shared instance AND both op profiles.
2. **Profiles per engagement** — `wiseq` and `pydrop` Hermes profiles: isolated config, sessions, memory, credentials. The security boundary (50-hats #43) and the client-cleanliness boundary in one move.
3. **Credential pools** (`hermes auth`) — 2-3 keys per provider on the crawler lanes so one rate-limit never stalls the nightly snapshot.
4. **Model aliases per task** — `parse → deepseek-v4.1-flash`, `decide → glm-5.3`, `tools → minimax-m3`; cron jobs pin aliases; Jev routes ad-hoc turns.
5. **Skill-ify the parsers** — Shopping-China card parser, bundle-spine decoder, email harvester v2 → Hermes skills (one skill_manage call each): future sessions load the procedure instead of re-deriving it.
6. **Webhooks `--deliver-only`** — uPay/Bancard payment events → Hermes runs, zero prompt cost on the event path.
7. **TUI widget** for the ops dashboard (orders/cash/price alerts) — native Hermes widgets beat checking files.
8. **AI-observability from day 1** — Langfuse OSS core (MIT; the `ee/` tier stays OFF per standing red line) or Laminar (Apache-2.0, OTel-native) into the PY docker-compose; OpenObserve for token-spend-as-P&L-line.

## 📦 B. AIW asset inventory — what we reuse (verified via GitHub API, 2026-10-22)

### Org repos (7 total, all live)

| Repo | What it is | Reuse for WiseQ/PY |
|---|---|---|
| **py-dropship-ai** | this repo | — |
| **wiseq-ai-onboarding** | this repo | — |
| **saskia-app** | Restaurant RMS: FastAPI+SQLite, SIFEN invoicing (sazon), production-hardened, Sentry+Resend+backups, WCAG work | **The PY shop's backend skeleton** — SIFEN module, payment-reconciliation patterns, test-isolation discipline, deploy flow. Proven PY-invoicing code we already own |
| **gaby-client-engine** | Client-acquisition ops for Ometz Dental: 1,090-lead engine, outreach pipeline | **The outreach machinery** for PY customer acquisition + the WiseQ B2B wave — CRM shape, cadence design, lead scoring reuse |
| **aiw-expenses** | Expense ledger + financial models + audit trail (Sonia ayuda tracking) | Financial-ledger patterns + audit discipline for both ops' books |
| **status** | Public status + run ledger (auto-generated, sanitized) | Status-page pattern for both ops' uptime story (pairs with Better Stack) |
| **mburucuya-potypy** | Official website (Gaby's practice) | The website template/flow for the PY storefront landing |

### Personal repos worth mining (81 total; the high-value subset)

| Repo | What it is | Reuse |
|---|---|---|
| **ai-whisperers-ops-toolkit** | "Bootstrap any VPS, client, or workspace" — the canonical setup repo | **The PY VPS provisioner** — the docker-compose from doc 13 lands on this foundation |
| **ai-whisperers-hermes-agent** | Hermes observability library + dashboard + cron health + alert router | **Directly**: agent observability (T2) without building — cron-health checks + alert routing already exist here |
| **paragu-ai-leads-monorepo** | 19 client lead-sites, shared packages, Cloudflare | Multi-site deploy patterns; shared UI tokens for any PY landing |
| **ai-whisperers-packages** | @ai-whisperers/ui, tokens, etc. | Design tokens for shop/landing work |
| **ParaguAI-leads** | CRM + outreach near FP Politécnica | Same machinery class as gaby-client-engine |
| **telescope-ai** | MCP server for telescope control | Proof-of-pattern for our thin MCP wrappers (bol, e-Boekhouden) — an MCP server we already wrote |
| **paragu-auditor** | Paraguay regulatory/compliance research | Feeds PY compliance docs (11) — update loop for CONATEL/DINAVISA/SET changes |
| **satellite-paraguay** | 6-paper earth-observation pipeline | Not direct reuse; demonstrates the research-pipeline pattern |
| **aiw-monitoring** | Real-time monitoring dashboard | Ops-dashboard base for the TUI/widget + web views |
| **netherlands-2026** | NL relocation research | NL-context knowledge base for the WiseQ engagement (minor) |

### Running systems & non-repo assets (from session memory, verified live earlier)

- **Fleet orchestrator** (`fleet/` package, VPS): multi-peer dispatch, kanban-backed ticketing, PEERS config — the *pattern* for per-engagement orchestration; the war-room SPA for visibility.
- **Hermes skills library** (ivan profile): email harvester patterns, direct-http-research, multi-research orchestration, price-monitor skill, structured-research-repo — loaded procedures, not just code.
- **BWS vault** (196 secrets applied at boot): the credential store for both ops — never .env, never repos.
- **Better Stack / Sentry / Cloudflare / Neon / Supabase** MCP integrations already enabled: uptime, error tracking, DNS/CDN, managed Postgres — the PY stack's ops layer is half-installed already.
- **War-room security gate** (X-War-Room-Token pattern): the auth pattern for any public ops endpoint we expose.
- **Telegram briefing cron patterns** (Ivan's hourly-fleet-update setup): the delivery rail for both ops' Monday reports / daily digests.

### Synthesis: the reuse-first stack

Both operations assemble almost entirely from owned parts:
**PY** = saskia-app backend patterns + ops-toolkit provisioning + ai-whisperers-hermes-agent observability + BWS + Better Stack + the doc-13 docker-compose + gaby-engine outreach machinery.
**WiseQ** = telescope-ai MCP-wrapper pattern + hermes-agent itself + the thin wrappers (bol/e-Boekhouden/Trustpilot) + Telegram-briefing rails + gaby-engine outreach for the 857-org B2B wave.

**What we genuinely build new** (the moat list, unchanged): bundle-spine matcher, school-order parser, CDE price-map agent, WhatsApp closer, repricing engine, Commerce-OS components. Everything else is reuse.

## ➕ C. New setups to consider (beyond doc 13)

1. **A third Hermes profile: `aiw-meta`** — the Commerce-OS productization lane (50-hats #31) separated from client work.
2. **Monorepo question**: the thin MCP wrappers (bol, e-Boekhouden, Trustpilot, changedetection, InvenTree) belong in ONE `commerce-os` repo (product) rather than scattered across client repos — decide before the third wrapper lands.
3. **paragu-auditor as a living service**: cron-check CONATEL/DINAVISA/SET/DNIT rule changes monthly → updates docs 11 automatically. Turn a research repo into a monitoring service.
4. **ai-whisperers-hermes-agent adoption for both ops**: wire cron-health + alert-router into the two profiles at setup time (not later) — observability is a day-1 setting per the 50-hats #40.
5. **Status page per op**: the `status` repo pattern, one page each — trust signal for WiseQ B2B buyers AND PY customers ("sistema monitoreado 24/7").

---

## 📌 In short

The verdict is **reuse-first**: AI Whisperers already runs 81 personal and 7 org repositories, and most of the stack does not need to be built at all — it needs to be assembled from things already in production elsewhere. This is the single strongest argument in the proposal for a realistic timeline, and the clearest answer to 'why should we trust a new partner with our stack'.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Tooling Mcp Installs](13-TOOLING-MCP-INSTALLS.md)** | Per-operation MCP install lists |
| **[Py Transfer Wiseq](../b-company/07-PY-TRANSFER-WISEQ.md)** | The specific components worth porting |
| **[Ai Stack Blueprint](../a-proposal/04-AI-STACK-BLUEPRINT.md)** | How reuse reshapes the blueprint |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
