<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 15* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# DevOps Masterplan — Pipeline, Storage, Data, Observability

*2026-10-22. The infrastructure and delivery plan for this engagement: what exists today, what is missing, and the phased build order. Every recommendation is grounded in the repository's actual shape — documentation and data today, application code from Phase 1 — and in verified platform behaviour.*

## 0. 🧭 Current state (verified today)

| Layer | Status |
| :--- | :--- |
| Repository validation on every push | ✅ live — 20 checks green |
| Workflow-security linting | ✅ live |
| Secret-pattern scanning (working tree + full history) | ✅ live |
| Scheduled pipelines | — none yet; starts with the Phase-1 nightly jobs |
| Environments | none — added when production deploys begin |
| Continuous deployment | not applicable until Phase 1 |

The baseline is deliberately in place before any application code exists. Gates added alongside code are gates that get bypassed under deadline.

## 1. 🕰️ ⚠️ The two platform traps

**Trap 1 — GitHub silently disables scheduled workflows after 60 days of repository inactivity.** No notification, no failure email: the job simply stops. *A data job that only commits when values change is therefore not a keep-alive — it stops the day the data is stable.* Rule: an explicit weekly keep-alive job with a manual-dispatch fallback, plus a heartbeat monitor on the Actions API that alerts if no run has occurred in 48 hours.

**Trap 2 — Snapshot bloat in git.** A 29 KB nightly snapshot is ~10.6 MB/year raw, and git history roughly doubles that once diffs are counted; five sources puts it past 50 MB/year. Mitigations, phased: (a) short term, keep dated JSON — small and diffable; (b) at ~6 months or 100 MB, move to a monthly tarball plus a `latest.json` pointer; (c) the durable home is the **price-history database** (below), not git — once the database pipeline lands, git carries only `latest.json`.

## 2. 💬 CI/CD upgrades

1. **Workflow-security linting** — our reference standard; SARIF output feeds the GitHub Security tab. One workflow, triggered on workflow-file changes.
2. **Secret scanning** on every push and PR — deeper than a pattern scan, because it scores entropy and walks full history. Pin the runner runtime explicitly.
3. **PR-gating via branch protection** (when collaborators/Rob engage): require `validate`, allow force-push none, require linear history. Direct-push stays for solo phase; protection flips on at first external collaborator.
4. **CI badge + local parity** — every CI check runnable locally with one command. `python scripts/validate_repo.py` already is; the rest should follow.
5. **Dependabot** — today only on actions (weekly); when app code lands, extend to pip/npm ecosystem groups.
6. **Release flow** (Phase 1+): tag → changelog gate → dependency-audit gate, advisory in CI and blocking on release.

## 3. 📦 Storage & data architecture

**Principle: git holds code and small config; the data store holds the data; git carries pointers.**

| Data class | Today | Target |
|---|---|---|
| OSS catalogs (static research) | git JSON | git — fine (one-off) |
| Data snapshots (append-daily) | git JSON dated | **price-history database** (nightly ETL from `latest.json`) + git keeps only `latest.json` |
| Bundle spine / registry (reference) | git CSV | git CSV (SSOT) + DB mirror at deploy |
| Lead-gen contacts (GDPR) | private workspace | **never git** — encrypted store + access log |
| Images / assets | none yet | Object storage — git-free |
| Backups | none | Nightly encrypted off-site copy, 30-day retention, **with a scheduled monthly restore test** |

> ⚠ **A backup nobody has restored is a hope, not a control.** The monthly restore job pulls
> a snapshot back into a scratch directory, verifies integrity and row counts, and records
> the result. It is part of the deliverable, not an optional extra — if we cannot prove a
> restore works, we do not claim you can recover.

**The database plan (Phase 1):** one Postgres for this engagement — products / offers / prices / orders-cache / reviews. SQLite for local development, Postgres in production, **same schema in both**. Numbered migrations in a `migrations/` directory, with an up/down smoke test in CI so a migration that breaks is caught before it runs. Nightly ETL moves snapshots into the `prices` table; the repository then carries the schema and the docs, not the history.

**Analytics layer:** the Monday reports (drift, dispersion, margin) query DuckDB over exported parquet/CSV — no new infrastructure, and an agent can run the SQL itself. It also keeps Postgres transactional-only.

**Asset storage:** product images go to object storage with public URLs; git keeps the manifest only.

## 4. 🧱 Pipeline evolutions

**WiseQ repo → deployable deliverables.** Phase 1 makes this repo produce artifacts: the bundle-spine importer (SQL + CSV), the drift-report generator (Python script + scheduled run), the competitor-watch configs (changedetection JSON). CI gains a job per artifact: `make spine` / `make drift-report` — outputs to `dist/` (git-ignored) + attaches to workflow run. Later: a published, versioned container image for the connector wrappers, signed — the polish item.

**Scheduled data jobs (Phase 1+).** One chain, cron-driven, each step writing an explicit status row:

```
02:17  supplier & competitor crawl      → dated snapshot
06:00  ETL snapshots → price DB         → prices table
06:15  diff & alerts (>5% moves)        → digest
07:00  monday: drift report             → repository data/reports/ + message
```

Alerting rides one rail for both digests and failure notices, so there is a single thing to watch rather than five.

## 5. 🗺️ Observability & SLOs

- **Heartbeats**: every scheduled or agent run writes a heartbeat row (timestamp, job, status, duration), and a monitor alerts on silence. Silence is the failure mode that matters — a job that stops is invisible without it.
- **Uptime**: shop and landing URLs on a public status page — a trust signal for B2B buyers, and cheap to keep current because the data is generated rather than written by hand.
- **Agent observability**: the same observability library we run internally — scheduled-job health plus alert routing — wired in at profile setup rather than later. Observability is a day-1 setting, not a phase-3 setting.
- **SLO draft**: nightly snapshot pipeline ≥95% success/30d; validator <5 min; drift report delivered by 07:10 ≥98%; WhatsApp agent eval pass-rate ≥90% (when live).
- **Runbooks**: per workflow — what healthy looks like, what silence means, the three-step restart (specialist review, §9).

## 6. 🔍 The build checklist (phased)

**Phase 0 — now (no infrastructure required):**
- [ ] Workflow-security and secret-scanning gates — already live; keep them green
- [ ] Keep-alive workflow + heartbeat monitor on every scheduled job (trap 1)
- [ ] Dependency updates for actions + CI badges in the README
- [ ] `make audit` docs + `dist/` gitignore

**Phase 1 — app code lands (shop, wrappers, spine importer):**
- [ ] Postgres schemas + migration smoke test in CI
- [ ] Price-history database + nightly ETL (snapshots → prices table); git keeps `latest.json` only
- [ ] Artefact jobs (spine importer, drift report) + a published container image for the connector wrappers
- [ ] Branch protection + PR flow at the first external collaborator
- [ ] Encrypted off-site backups, 30-day retention

**Phase 2 — scale:**
- [ ] DuckDB analytics + Monday report automation
- [ ] cosign signing + provenance attestations on images
- [ ] Multi-env (dev/prod) with GitHub Environments + approvals on prod
- [ ] Load-test the wrapper APIs (endpoint smoke test under realistic volume)

## 7. ⚙️ What we deliberately avoid

- **Kubernetes** — this is one small operation. A single host plus managed Postgres and object storage; cluster orchestration would be resume-driven busywork.
- **Infrastructure-as-code** for three cloud resources — a compose file and the provider dashboards cover it; revisit at ten or more resources.
- **A monorepo merge** — client-facing and internal material serve different audiences and different confidentiality levels; cross-references beat a shared tree.
- **Self-hosted CI** — managed Actions on a public repository costs nothing, and that is the entire reason the infrastructure budget is €0.

---

## 📌 In short

Production-readiness, decided in advance: CI hardening, **storage & database architecture**, observability and explicit SLOs, plus the two platform traps worth avoiding. The point of writing it before the build is that **operability is a design input, not an afterthought** — and the phased build checklist that falls out of it is what each phase is measured against.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Tooling Mcp Installs](13-TOOLING-MCP-INSTALLS.md)** | What gets installed |
| **[Dev Team Hats](16-DEV-TEAM-HATS.md)** | The build team's ranked improvements |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | The stack this plan hardens |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
