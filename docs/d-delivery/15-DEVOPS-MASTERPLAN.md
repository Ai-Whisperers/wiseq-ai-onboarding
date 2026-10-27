<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 15* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# DevOps Masterplan — Pipeline, Storage, Data, Observability

*2026-10-22. The "devops masterpiece" plan for both repos: what exists (CI green, nightly crawl live), what's missing, and the phased build order. Every recommendation is grounded in the repos' actual shape (docs+data today, app code phase 1+) and in verified platform behavior.*

## 0. 🧭 Current state (verified today)

| Layer | WiseQ repo | PY repo |
|---|---|---|
| CI validate | ✅ live (20 checks green) | ✅ live (19 checks green) |
| Scheduled pipeline | — | ✅ nightly 02:17 UTC crawl → auto-commit (ran green, 33s) |
| Repo size | 1.5 MB | 2.1 MB |
| Nightly artifact | — | 29 KB snapshot JSON |
| Secrets handling | scan in validator | scan in validator |
| Environments | none | none |

## 1. 🕰️ ⚠️ The two platform traps (grounded)

**Trap 1 — GitHub silently kills scheduled workflows after 60 days of repo inactivity.** No notification; the nightly crawl just stops. Mitigation: a keep-alive — any real commit counts, but a dedicated `keepalive` workflow (weekly commit bumping a `.timestamp` or the snapshot flow's own commits keep it alive) is the robust fix. *The snapshot workflow itself commits nightly when prices change — that IS the keep-alive — but only when prices change.* Rule: add an explicit weekly keepalive job with a `workflow_dispatch` fallback, and a Better Stack cron-monitor on the Actions API (alert if no run in 48h).

**Trap 2 — Snapshot bloat in git.** 29 KB/night ≈ 10.6 MB/year raw; with diffs, git history grows ~2×. Five sources → 50+ MB/yr. Mitigations (phased): (a) short-term, keep dated JSONs — small and diffable; (b) at ~6 months or 100 MB repo: move to monthly tarball + `latest.json` pointer, or Git LFS; (c) the real home is the **price-history DB** (below), not git — git carries only `latest.json` once the DB pipeline lands.

## 2. 💬 CI/CD upgrades (both repos)

1. **zizmor workflow-security linting** — saskia's own reference standard; SARIF output → GitHub Security tab. One workflow, runs on workflow-file changes.
2. **gitleaks-action** on every push/PR — deeper than our regex scan (entropy + history), zero config. Note: runner default is Node 24 since June 2026 — pin accordingly.
3. **PR-gating via branch protection** (when collaborators/Rob engage): require `validate`, allow force-push none, require linear history. Direct-push stays for solo phase; protection flips on at first external collaborator.
4. **CI badge + `make audit` local parity** — saskia pattern: every CI check runnable locally with one command (`python scripts/validate_repo.py` already is; document it).
5. **Dependabot** — today only on actions (weekly); when app code lands, extend to pip/npm ecosystem groups.
6. **Release flow** (phase 1+): tag → changelog gate → pip-audit hard gate (advisory in CI, blocking on release — the saskia split).

## 3. 📦 Storage & data architecture

**Principle: git = code + small config; data lake = the VPS/Neon; git carries pointers.**

| Data class | Today | Target |
|---|---|---|
| OSS catalogs (static research) | git JSON | git — fine (one-off) |
| CDE snapshots (append-daily) | git JSON dated | **price-history DB** (DuckDB/SQLite on VPS, nightly ETL from `latest.json`) + git keeps only `latest.json` |
| Bundle spine / registry (reference) | git CSV | git CSV (SSOT) + DB mirror at deploy |
| Lead-gen contacts (GDPR) | private workspace | **never git** — encrypted store (BWS-adjacent) + access log |
| Images/assets | none yet | Cloudflare R2 (already have creds) — git-free |
| Backups | none | restic nightly → R2, 30-day retention, **with a scheduled monthly restore test** |

> ⚠ **A backup nobody has restored is a hope, not a control.** The monthly restore job
> pulls a snapshot back into a scratch directory, verifies integrity and row counts, and
> records the result. It is part of the deliverable, not an optional extra — if we cannot
> prove a restore works, we do not claim you can recover.

**The DB plan (phase 1):** one Postgres (Neon free tier — MCP already enabled) per operation: `wiseq` (products/offers/prices/orders-cache/reviews) and `pydrop` (catalog/prices/suppliers/orders/cash). SQLite for local dev, Postgres in prod — same schema, migrations via a `migrations/` dir + `alembic`-style numbering, tested in CI (migration up/down smoke — saskia lesson). Nightly ETL: snapshots → `prices` table; the git repo then carries only the doc + schema, not the history.

**DuckDB analytics layer:** the Monday reports (drift, dispersion, margin) query DuckDB over the exported parquet/CSV — zero new infra, agent-friendly (SQL the agent can run), and it keeps Postgres transactional-only.

**R2 for assets:** product images (WiseQ catalog, PY listings) → R2 bucket per op, public URLs, git keeps manifest only.

## 4. 🧱 Pipeline evolutions

**WiseQ repo → deployable deliverables.** Phase 1 makes this repo produce artifacts: the bundle-spine importer (SQL + CSV), the drift-report generator (Python script + scheduled run), the competitor-watch configs (changedetection JSON). CI gains a job per artifact: `make spine` / `make drift-report` — outputs to `dist/` (git-ignored) + attaches to workflow run. Later: Docker image for the wrapper (ghcr.io, versioned, signed with cosign — flagship polish).

**PY repo → full ops pipeline.** Cron chain (VPS Hermes once infra lands, GH Actions until then):
```
02:17  crawl shoppingchina (live)          → snapshot JSON
02:30  crawl fastrax (when stealth built)  → snapshot JSON
06:00  ETL snapshots → price-history DB    → prices table
06:15  diff & alerts (>5% moves)           → Telegram/WhatsApp digest
07:00  monday: drift/dispersion report     → repo data/reports/ + message
```
Alerting rail: Telegram bot (existing briefing pattern) + failure alerts via the same rail (Resend email fallback — creds already in BWS).

## 5. 🗺️ Observability & SLOs

- **Heartbeats**: every cron/agent run writes a heartbeat row (ts, job, status, duration) — Better Stack heartbeat monitors (already enabled) alert on silence.
- **Uptime**: shop/landing URLs on Better Stack public status page (the `status` repo pattern) — trust signal for both ops.
- **Agent observability**: ai-whisperers-hermes-agent lib (cron-health + alert-router — already built, per doc 14) wired at profile setup.
- **SLO draft**: nightly snapshot pipeline ≥95% success/30d; validator <5 min; drift report delivered by 07:10 ≥98%; WhatsApp agent eval pass-rate ≥90% (when live).
- **Runbooks**: per workflow — what healthy looks like, what silence means, 3-step restart (50-hats #46).

## 6. 🔍 The DevOps masterpiece checklist (phased)

**Phase 0 — now (zero infra):**
- [ ] zizmor + gitleaks workflows (both repos)
- [ ] Keepalive workflow + Better Stack monitor on the crawl (trap 1)
- [ ] Dependabot (actions) + CI badges in README
- [ ] `make audit` docs + `dist/` gitignore

**Phase 1 — app code lands (shop, wrappers, spine importer):**
- [ ] Postgres schemas (Neon) + migration smoke in CI
- [ ] price-history DB + nightly ETL (snapshots → prices table); git keeps latest.json only
- [ ] Artifact jobs (spine/drift-report) + ghcr image for commerce-os wrappers
- [ ] Branch protection + PR flow at first collaborator
- [ ] restic → R2 backups, 30d retention
- [ ] **Monthly restore test** — pull a snapshot back, verify integrity + row counts, record the result

**Phase 2 — scale:**
- [ ] DuckDB analytics + Monday report automation
- [ ] cosign signing + provenance attestations on images
- [ ] Multi-env (dev/prod) with GitHub Environments + approvals on prod
- [ ] Load test the wrapper APIs (routes endpoint smoke — saskia pattern)

## 7. ⚙️ What we deliberately avoid

- **Kubernetes** — two small ops, one VPS + Neon + R2; k8s is resume-driven here.
- **Terraform** for 3 cloud resources — config-as-code in the compose + Neon dashboards; revisit at 10+ resources.
- **Monorepo merge** — the two repos serve different audiences (client-facing vs internal); cross-repo pointers (already in place) beat Lerna complexity.
- **Self-hosted GitLab/Gitea** — GitHub Actions free on public repos is the whole reason the pipeline costs €0.

---

## 📌 In short

Production-readiness, decided in advance: CI hardening (zizmor, gitleaks, branch protection), **Neon + DuckDB + R2** for storage, and explicit SLOs. The point of writing it before the build is that **operability is a design input, not an afterthought** — and the checklist that falls out of it is what Phase 1 is measured against.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Tooling Mcp Installs](13-TOOLING-MCP-INSTALLS.md)** | What gets installed |
| **[Dev Team Hats](16-DEV-TEAM-HATS.md)** | The build team's ranked improvements |
| **[Ai Stack Blueprint](../a-proposal/04-AI-STACK-BLUEPRINT.md)** | The stack this plan hardens |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
