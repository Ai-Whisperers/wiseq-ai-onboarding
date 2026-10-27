<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 24 (v2 — revised Oct 23: deployment on the client's own server)* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Agent infrastructure blueprint v2 — fresh Hermes on the WiseQ server, reusing AIW's proven assets

*Oct 23, 2026. Revised architecture: WiseQ provisions its own server; we install a clean Hermes from scratch and port everything reusable from the AIW operation. This is the strongest possible continuity story — doc 18's "the operation survives AIW" becomes literal: the system runs on their box, their keys, from day one. This document is the complete setup map: install path, the port manifest (what transfers / what adapts / what must never leave AIW), secrets, hardening, and the day-0-to-steady-state sequence.*

---

## 0. 🧭 Why this architecture (and what changed from v1)

| | v1 (AIW VPS, second profile) | **v2 (this doc): client server, fresh install** |
|---|---|---|
| Hardware | AIW's VPS | **WiseQ's server** — sovereignty, no AIW dependency |
| Hermes | existing instance | **fresh install** — clean version, clean state |
| Credentials | AIW's BWS vault | **WiseQ's own vault** — they own the keys |
| Data residency | EU-side by assertion | EU-side **by physics** — AVG art. 28's easiest possible story |
| Continuity (doc 18) | promised | **structural** — if AIW vanishes, nothing moves |
| AIW's role | operator | **builder + transition partner** — we set up, harden, document, hand over |

The trade we accept: we lose the "infrastructure already running" argument and gain the far stronger one — *their operation is theirs from day zero*. Setup effort is a one-time cost this document prices.

---

## 1. 🖥️ Day 0 — the fresh install (verbatim path)

**Server requirements** (checked against the Hermes install docs): Linux (Ubuntu 24.04 LTS recommended), 2 vCPU / 4 GB RAM floor (comfortable: 4 vCPU / 8 GB — a €15–25/mo Hetzner-class box), 40 GB disk, Docker optional (only if we containerize services later), Tailscale (or WireGuard) for operator access — **never expose the gateway publicly**.

```bash
# 1. Fresh Hermes (official installer — sets up uv, Python, venv, launcher)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 2. First-run: provider keys, model pick, health check
hermes setup        # wizard
hermes model        # pick routing
hermes doctor       # verify

# 3. A dedicated profile keeps the operation isolated from any personal use
hermes --profile wiseq   # creates ~/.hermes/profiles/wiseq/ (config, skills, state)

# 4. Update cadence (AIW lesson: pin + deliberate upgrades, never auto)
#    monthly: hermes update → hermes doctor → smoke the cron jobs
```

**Provider/model setup — Rob owns these keys** (doc 18: keys in his custody from day one):
- Recommended: **OpenRouter** single key → any model, per-model spend caps, one invoice. Alternative: direct provider keys, or Nous Portal OAuth if they prefer subscription pricing.
- Routing starting point (from AIW's measured usage): a strong general model for orchestration (the doc-04 €40–90/mo band), a cheap/fast model for high-volume cron ticks, vision only where needed (product imagery). `hermes model` sets this; we tune in Phase 0 with real load.
- Spend telemetry: provider dashboards + a monthly cost report in the Monday digest (the aiw-cost-monitor pattern, ported — see §2).

---

## 2. 📦 The port manifest — what AIW assets transfer

AIW's instance holds **184 skills** and hard-won operational patterns. Three buckets:

### ✅ Bucket A — portable, port as-is (~30 skills)

| Cluster | Skills | Why for WiseQ |
|---|---|---|
| Hermes itself | `hermes-agent` (hub) | The operating manual |
| Engineering discipline | `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `durable-test-assertions`, `executing-plans`, `finishing-a-development-branch` | The quality bar that made the onboarding repo survive an external audit |
| GitHub workflow | `github`, `github-auth`, `github-repo-management`, `github-issues` | The ops repo's PR/CI discipline |
| MCP | `mcp-builder`, `mcp-management` | For the 3 thin wrapper builds (bol, Trustpilot, ChannelDock) |
| Documents | `productivity`: pdf, docx, xlsx, powerpoint | Client deliverables: quotes, invoices, Monday reports |
| Research | `research` core, `grounded-citations`, `structured-research-repo`, `web/blocked-page-recovery` | Marketplace/competitor lanes (bol IS bot-walled — this skill is why we know how to get through) |
| Monitoring | `monitor-cron-safe-silence` | The alert-on-silence discipline |
| Safety | `prompt-injection-defense` | Inbound email/orders are untrusted input — non-negotiable for an order-taking agent |
| Writing | `long-markdown-deliverable-authoring`, `multi-hat-persona-analysis` | Documentation that doesn't truncate; review discipline |
| Onboarding pattern | `named-non-user-onboarding-pack` | When WiseQ staff (not just Rob) start interacting |

### 🔧 Bucket B — patterns that adapt (we re-implement on their box, ~8)

| AIW asset | Becomes |
|---|---|
| The **repo validator** pattern (68 checks, retracted-claim guards) | `wiseq-ops` repo CI: same validator skeleton, WiseQ's claims-ledger rules |
| **Cron discipline** (heartbeat rows, TTL discipline, Step-Zero job identification) | Their cron fleet from day one — port the rules, not the jobs |
| **Cost telemetry** (aiw-cost-monitor) | Monthly model-spend report per engine |
| **Backup + monthly restore-test** (doc 15's rule) | restic → their choice of off-site (R2/Hetzner storage box) |
| **Gateway auth coupling lesson** (public URL binds ↔ token mode) | Their dashboard: **loopback + Tailscale-only, token auth on** — the AIW war-room incident (an open origin once spawned a paid subagent) is encoded here as a hard rule |
| **Keep-alive trap** (GitHub kills scheduled workflows after 60d idle) | Their Actions-based jobs get the weekly keepalive |
| **Version-stamped assets** (`?v=sha` cache-busting) | Any web artifact they serve |
| **Write-gating / guardrails-as-code** (v1 §4) | Unchanged — approval modes + policy functions |

### ⛔ Bucket C — never leaves AIW (and why)

- **All ~45 `aiw-*` skills** — reference AIW-internal infrastructure (war-room, fleet, BWS, org state)
- **`fleet-*`, `war-room-*`, `saskia-*`, `paraguay-*`, family/personal skills** — other clients' patterns and private context; porting them would leak AIW's and third parties' information
- **AIW's memory and session data** — obviously; the fresh instance gets a **new, seeded memory**: a WiseQ onboarding file (company facts, catalog truth, operating rules, "who is Rob", escalation preferences) written by us during setup — NOT a copy of anything from AIW's profiles
- **BWS vault contents** — their secrets go in **their** vault: OS keychain + `.env` (profile-scoped), or a fresh Bitwarden org if they prefer shared access. Zero AIW-held credentials on this box, in either direction

**IP note:** Bucket A skills are AIW-authored procedures. Doc 18's terms grant WiseQ a perpetual license to the skills and runbooks deployed on their operation — they're part of the deliverable, like the code.

---

## 3. 🔌 The MCP layer (unchanged from v1, re-verified Oct 23)

**P0 day one (zero/light creds):** Shop MCP (`mcp.shop.com` — keyless catalog intelligence), Shopify dev-mcp (npm), filesystem, sqlite, github, brave/exa, context7, deepwiki.

**P1 week 2–3 (Gate 1.2, needs Rob's access):** Shopify Admin custom app (least-privilege scopes), **Exact Online MCP** (self-host `lemon-official/exact-mcp` or EU-hosted 75-tool — install, not build, if Exact), bol Retailer wrapper (**build**, ~10 tools, async process-status discipline), Trustpilot wrapper (**build**, ~4 tools).

**P2 engines:** ChannelDock wrapper, PostNL wrapper, Klaviyo (if SaaS ESP), Bolyra gateway proxy (eval for signed audit receipts).

**Credentials placement:** every MCP secret → their vault → profile `.env`. The ops repo never carries secrets (CI-enforced, same validator rule as this repo).

---

## 4. 🧠 Skills written FOR WiseQ during Phase 1 (deliverables, doc 18)

Same nine as v1 — `wiseq-operations`, `shopify-admin-ops`, `bol-retailer-ops`, `school-pipeline`, `oss-vat-watchdog`, `compliance-triage`, `reputation-engine`, `incident-runbooks`, `client-communication` — authored in the `wiseq-ops` repo, versioned, tested, and owned by WiseQ. Plus the seeded memory file (§2 Bucket C). These are not ports; they're the engagement's actual product.

---

## 5. 🛡️ Hardening the fresh box (AIW's scars, pre-applied)

1. **Gateway: loopback bind + Tailscale-only remote access + token auth** — the auth-coupling lesson means we never flip the public-URL setting casually; remote operator access rides the tailnet
2. **Approval modes**: read-only MCPs free; write-capable MCPs behind the approval gate (Phase 1: human approves every write; Phase 2: guardrail-auto-approve)
3. **Guardrails as code**: margin floors, stock-write delta ceilings, OSS-threshold alert, max invitations/day — policy functions in the ops repo, tested in CI
4. **Untrusted-input discipline**: inbound order emails and marketplace messages pass through the prompt-injection-defense pattern before any tool call
5. **Updates**: pinned versions, monthly deliberate upgrade + `hermes doctor` + cron smoke test — no auto-updates on a production box
6. **Backups**: nightly restic (state.db, config, vault export) → off-site, **monthly restore test with recorded result** — a backup nobody restored is a hope, not a control
7. **Monitoring the monitors**: every cron writes a heartbeat; alert-on-silence via Better Stack (their free tier) or a simple healthchecks.io; failure alerts land in the daily digest rail

---

## 6. 🕰️ Setup sequence

**Day 0 (we drive, Rob watches):** server provisioned → Hermes installed → profile `wiseq` → provider keys (Rob's) → model routing smoke → Bucket A skills ported → seeded memory written → hardening §5 → `hermes doctor` green.

**Week 1 (zero client access):** ops repo bootstrapped (validator, CI, branch protection) → canonical spine schema in sqlite (bundle CSVs import) → cron skeleton with heartbeats → Shop MCP competitor baseline (keyless) → runbook templates.

**Weeks 2–3 (Gate 1.2 — Rob's access lands):** Shopify custom app, bol creds, Exact/bookkeeping decision → MCPs live read-only → the 3 wrapper builds → first order-sweep dry runs against sandbox data → **Gate 2 tests**.

**Steady state:** 06:30 order sweep, 07:00 single digest to Rob, hourly OSS watchdog, nightly reconcile + competitor sweep, weekly Monday report + compliance scan, monthly restore test.

**Transition exit (per doc 18):** runbooks complete, skills owned, keys in WiseQ custody, AIW access gracefully revoked — the operation runs without us. We remain on the care plan (monitoring, upgrades, new engines) as long as it earns its fee.

---

## 7. 💶 What it costs (their side)

| Item | Cost |
|---|---|
| Server (2–4 vCPU, 4–8 GB EU) | €15–25/mo (Hetzner-class) |
| Hermes | €0 (open source) |
| Bucket A skill license | included in the engagement (doc 18) |
| Model spend | the doc-04 €40–90/mo band, measured + reported monthly |
| Neon Postgres (when the DB lands) | free tier → ~€19/mo |
| Better Stack / backups target | free tier / ~€5/mo storage |
| **Total steady-state infra** | **~€60–115/mo** — comfortably inside the TCO band already quoted |

One-time setup effort (install, port, harden, document, handover) is Phase 1's build work — already inside the €8–12k Phase-1 fee, not extra.

---

## 📌 In short

Their server, a fresh Hermes, ~30 ported skills + 8 adapted patterns + 9 new WiseQ-specific skills, their vault, their keys, loopback+tailnet hardening, heartbeats on everything, and a handover that is structural rather than promised. Everything AIW learned the expensive way — gateway auth coupling, open-origin spawns, cron silence, restore tests, retracted-claim guards — arrives pre-encoded. **The client doesn't rent our infrastructure; they inherit our scar tissue.**

---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Terms & continuity](../f-governance/18-TERMS-OWNERSHIP-CONTINUITY.md)** | The handover this architecture makes literal |
| **[Acceptance criteria](../f-governance/23-ACCEPTANCE-CRITERIA.md)** | The gates that unlock each layer |
| **[DevOps masterplan](15-DEVOPS-MASTERPLAN.md)** | Storage, backups, SLOs (adapted in §2 Bucket B) |
