<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 16* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# The Full Dev Team Hat Pass — Both Projects Audited by Role

*2026-10-22. A complete software team reviews this repo as it exists NOW (15-16 docs, 5 workflows green, no app code yet). Each role: what they'd flag, what they'd praise, and the fix. Synthesis at the end ranks the top-10 improvements.*

---

## 1. 🧭 Product Manager

**Flags:** Phase 0 checklists exist but no acceptance criteria ("how do we know Phase 0 is DONE?"); the WiseQ pilot has no agreed success metrics (what makes Rob renew?); PY niche decision has no date-owner.
**Praise:** The one-paragraph pitches are crisp; the ask-lists are concrete.
**Fix:** One `MILESTONES.md` per repo — 3 milestones max, each with measurable exit criteria (e.g. "pilot: drift report delivered 4 consecutive Mondays + EAN fix live").

## 2. 🕰️ Business Analyst

**Flags:** Unit economics are documented but not *parameterized* — assumptions (margin %, CPM, courier $/kg) are scattered across docs 02/09/10 with no single source; no sensitivity analysis artifact.
**Praise:** Every number carries a source.
**Fix:** `data/assumptions.json` — one register: value, source, confidence, review-date. The simulator (T12) reads from it.

## 3. 💬 Software Architect

**Flags:** The canonical spine exists as concept + CSVs but no DDL/migration; MCP wrapper API contracts undefined (no OpenAPI/tool schemas yet); decisions live in prose docs, not ADRs — nothing numbered to cite later.
**Praise:** The layered architecture (git=code, Neon=data, R2=assets, DuckDB=analytics) is stated and consistent.
**Fix:** Start `docs/adr/` — ADR-001 (two repos), ADR-002 (ghcr for wrappers), ADR-003 (Neon per op)... retro-write 10 ADRs from existing docs in one pass; define spine DDL as the first migration file (even before the DB exists — it becomes the schema contract).

## 4. 📦 Tech Lead

**Flags:** No CONTRIBUTING.md, no CODEOWNERS, no branch strategy doc (direct-push now, PR-flow at first collaborator — currently only stated in a chat-level note); the commerce-os-repo decision (doc 14 §C2) is still open and wrapper #1 is approaching.
**Praise:** Commit hygiene is good; validators runnable locally = local/CI parity (our house rule) already in place.
**Fix:** Decide commerce-os repo NOW (before wrapper #1 lands in a client repo); 20-line CONTRIBUTING per repo.

## 5. 🧱 Backend Engineer

**Flags:** Crawler has no retry/backoff (single fetch fails → category skipped silently), no structured logging, no tests; scripts lack type hints; no dead-letter concept for a category that fails N nights straight.
**Praise:** stdlib-only dependency posture; polite 1.2s delays; graceful per-category continue.
**Fix:** v2 crawler: 3-retry with exponential backoff, JSONL run-log (`ts, category, n, status`), one pytest with a fixture HTML asserting the regex parses 113-ish cards (golden-file test against today's snapshot).

## 6. 🗺️ Frontend Engineer

**Flags:** Zero FE code (fine — Tiendli phase 0), but the report/dashboard surface is undecided: Monday report as markdown vs web page; the ops TUI widget is specced nowhere.
**Praise:** The ai-whisperers-packages tokens exist for reuse when FE lands.
**Fix:** Decide: reports stay markdown (agent-authored) until 10 readers exist; the TUI widget gets a 1-paragraph spec (what 4 numbers, refresh rate) so it can be built in a day.

## 7. 🔍 UX Designer

**Flags:** The WhatsApp conversation is the real product UI and its scripts are referenced everywhere but never written; the Monday report is a product with no template; the WiseQ school-order flow has states (new → parsed → quoted → confirmed → shipped) but no state diagram.
**Praise:** Customer-persona thinking (procurement officer hat, PY conversational selling) is already deep.
**Fix:** Write `docs/16-CONVERSATION-FLOWS.md` (PY): greeting → qualify → offer → close → pay → confirm, with fallbacks; WiseQ: order-state diagram (mermaid) in the backlog doc.

## 8. ⚙️ QA Engineer

**Flags:** Validators are smoke-tier; no property tests (price always int>0, dates monotonic); eval sets for agents designed (T1) but zero conversations labeled; no test for the validator itself.
**Praise:** CI caught two real bugs on day one (bad SHA, _index schema) — the gates work.
**Fix:** Golden-file test per snapshot day-1 (catch silent parser drift); validator self-test (inject a bad file, expect exit 1); start the 50-conversation WhatsApp eval set now, before the agent exists — from PY seller FAQ pages.

## 9. 💰 SRE

**Flags:** Keepalive shipped but the Better Stack monitor on "no Actions run in 48h" is planned, not built; no runbooks for the 5 workflows; the commit-bot failing (bad push) would be silent; SLOs drafted but not measured anywhere.
**Praise:** Concurrency-cancel, timeouts, min-perms everywhere; nightly pipeline verified end-to-end.
**Fix:** `docs/runbooks.md` — one block per workflow (healthy/symptom/3-step restart); wire the Better Stack heartbeat this week; a `status` badge row in both READMEs.

## 10. 🌱 Security Engineer (AppSec)

**Flags:** Branch protection off on both repos (accept for solo, but the snapshot workflow has contents:write — a compromised PR could alter it if protection flips on late); crawler content will flow into agent context (prompt-injection surface — snapshot JSON contains arbitrary titles from an external site); no dependency scanning (no deps yet — add pip-audit at first requirements.txt).
**Praise:** zizmor+gitleaks green; dedicated vault for secrets; no tokens in tree.
**Fix:** Add `gitleaks.toml` allowlist doc-note (none needed yet); at wrapper-repo creation: branch protection from commit #1; sanitize crawler output at ingestion (strip markdown/control chars from titles before they reach any LLM context).

## 11. 🛡️ Data Engineer

**Flags:** Snapshot JSONs have no `schema_version` field (breaking parser changes later = ambiguity); cross-source product identity unresolved (the matcher is a planned build, not started); no data-quality checks beyond price sanity (category drift, empty titles).
**Praise:** Dated files, dedupe on (title, price), captured-date integrity checked.
**Fix:** Add `"schema_version": 1` to crawler output + validator; draft the identity key (brand+model+color normalization sketch) as a doc so the matcher starts from a spec; add title-length anomaly check.

## 12. 📋 DBA

**Flags:** No migration tooling chosen; Neon projects not created; no retention policy (snapshots forever? 24 months?); indexing plan unstated.
**Praise:** The "git=latest, DB=history" split is the right call.
**Fix:** At phase-1 kickoff: alembic-style numbered migrations in-repo, `price_history(product_key, source, captured, price)` with composite index stated in the DDL doc now; retention = 24 months raw, aggregates forever.

## 13. 🎯 ML / Data Science Engineer

**Flags:** The eval harness is the make-or-break component and exists only as a bullet (T1); no cost telemetry on any lane yet; forecasting is rules (fine) but rules need backtesting data — which starts accumulating tonight.
**Praise:** Model-routing per task documented; Jev audit trail already logging 40k decisions.
**Fix:** Define the eval-set schema (input, expected, grader) this week so conversations get labeled from day one; add token-cost log line to every agent run (the P&L-line rule needs the line).

## 14. 📊 Technical Writer

**Flags:** The master/extraction pattern (PY docs 12/15 duplicating WiseQ masters) = translation-drift risk with no lint; no glossary (jopara, contrapedido, staffelprijzen, RESIMPLE mix freely); no AGENTS.md in either repo — future agent sessions won't inherit conventions automatically.
**Praise:** Docs are source-cited, dated, and versioned in git — better than most startups.
**Fix:** AGENTS.md per repo (10 lines: language policy, SSOT rule, validate-before-commit); a `GLOSSARY.md`; extraction docs get "generated-from master@SHA" headers so staleness is detectable.

## 15. 🔬 Scrum Master / Delivery

**Flags:** ~250 ideas across three hat-docs with no board — the 12 kanban graduates (doc 12) aren't in GitHub Issues/Projects; no WIP limit; no weekly review ritual defined.
**Praise:** The phase discipline (research → blueprint → tooling → data) has been unusually sequential and complete.
**Fix:** Convert the 12 graduates + top-10 below into GitHub Issues with labels (wiseq/py/aiw) this week; WIP limit 3; the "Status" section of each README becomes the weekly review artifact.

## 16. 🧪 Release Manager

**Flags:** No versioning policy for anything (docs or future components); changelog discipline starts "when app code lands" but the habit should start with the repos themselves; tag conventions undefined.
**Praise:** [skip ci] conventions already correct on bot commits.
**Fix:** v0.1.0 tags on both repos at Phase-0 completion (milestone marker); CHANGELOG.md starts then, not later.

## 17. 🧩 Performance Engineer

**Flags:** Crawler is serial (10 categories × ~2s = fine today, 584 categories × 2s = 20min — still fine nightly, but multi-source ×10 will need async with per-host politeness); nothing measured.
**Praise:** Workload is small enough that this is genuinely not a problem yet.
**Fix:** One number in the run-log: wall-clock per crawl — start the series now, optimize when it crosses 30min.

## 18. 🔗 Support Engineer

**Flags:** Escalation paths undefined for both ops: what happens when the WhatsApp agent can't close, or a school email is ambiguous? No SLA templates, no "human takeover" runbook.
**Praise:** UVdesk-as-inbox and approval-mode defaults already specced.
**Fix:** `docs/ESCALATION.md` per op: triggers for human takeover, response-time promise, template replies (ES for PY, NL/EN for WiseQ).

---

## Synthesis — top 10 improvements (ranked by risk-removed ÷ effort)

| # | Improvement | Owner role | Repo | Effort |
|---|---|---|---|---|
| 1 | `schema_version` in snapshots + golden-file test | DataEng/QA | py | 30m |
| 2 | MILESTONES.md with exit criteria (both) | PM | both | 1h |
| 3 | GitHub Issues for the 12+10 backlog | Scrum | both | 1h |
| 4 | AGENTS.md + glossary + extraction-SSOT headers | TechWriter | both | 1h |
| 5 | Crawler v2: retry/backoff + JSONL run-log + 1 test | Backend | py | 2h |
| 6 | Better Stack heartbeat on Actions + runbooks.md | SRE | both | 1.5h |
| 7 | ADR folder (10 retro ADRs) + spine DDL doc | Architect | wiseq | 2h |
| 8 | commerce-os repo decision + CONTRIBUTING | TechLead | aiw | 45m |
| 9 | Eval-set schema + first 50 labeled conversations | ML | py | 3h |
| 10 | Snapshot-title sanitization before LLM context | Security | py | 30m |

## What the team would keep (no action)

- Evidence-first culture: every claim has a source; every number a date.
- CI that caught its own bugs on day one.
- The reuse-first stack (doc 14) — no rebuild of what AIW owns.
- Bilingual discipline: Spanish for PY operations, English for the client-facing WiseQ repo.
- €0 infra, all pipelines verified live, not described.

---

## 📌 In short

**18 roles, each giving a verdict** — PM to Support Engineer — with flags, praise and fixes, ranked into a **top 10**. It reads as candid because it is: several hats disagree with the current plan. That disagreement is the value; a build team that only agrees is a build team that has not been asked.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Fifty Hats](../60-governance/04-specialist-31-hats.md)** | The 50-hat cross-view |
| **[Devops Masterplan](04-devops.md)** | The top-ranked fixes, scheduled |
| **[Next Steps](../20-offer/03-next-steps.md)** | What we need to act on the findings |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
