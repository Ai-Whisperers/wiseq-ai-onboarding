<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 16* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Delivery Review — How We Build

*2026-10-22. A full engineering team reviewed this proposal and the repository as they stand today, role by role: what each discipline would flag, what it would keep, and what it would build first. This is how the work gets done — the quality bar is set before Phase 0 starts, not discovered during it.*

---

## 1. 🧭 Product Manager

**Would flag:** Phase 0 has a checklist but no acceptance criteria — how do we know Phase 0 is *done*? And the pilot has no agreed success metric, which is really the same question asked of the future.
**Would keep:** the ask-list is concrete, and the pitch is one page a director can read in ninety seconds.
**Would build first:** a `MILESTONES.md` with three milestones maximum, each with a measurable exit test — for example *"pilot: drift report delivered four consecutive Mondays and the EAN fix live."*

## 2. 🕰️ Business Analyst

**Would flag:** unit economics are documented but not *parameterised* — margin, ad cost, and courier assumptions are scattered across several documents with no single source.
**Would keep:** every number carries a source.
**Would build first:** `data/assumptions.json` — one register with value, source, confidence, and review date.

## 3. 💬 Software Architect

**Would flag:** the canonical spine exists as a concept and a pair of CSVs, but has no schema definition; the connector API contracts are undefined; decisions live in prose rather than numbered records.
**Would keep:** the layered architecture — code in git, transactional data in Postgres, assets in object storage, analytics in DuckDB — is stated and consistent.
**Would build first:** numbered architecture records, and the spine schema as the first migration file *before* the database exists. Defining the contract early is what makes it a contract.

## 4. 📦 Tech Lead

**Would flag:** no written contribution guide or branch strategy; the wrapper-code ownership decision is still open and the first wrapper is approaching.
**Would keep:** commit hygiene is good, and every CI check is runnable locally — local/CI parity already in place.
**Would build first:** a twenty-line contribution guide, and settle where reusable connector wrappers live before the first one lands in a client repository.

## 5. 🧱 Backend Engineer

**Would flag:** the crawler has no retry or backoff — a single failed fetch skips a category silently; no structured logging; no tests; scripts lack type hints.
**Would keep:** a stdlib-only dependency posture, polite crawl delays, and graceful per-category continue.
**Would build first:** crawler v2 — three retries with exponential backoff, a structured run log (`ts, source, count, status`), and one test that asserts the parser handles a known-good snapshot.

## 6. 🗺️ Frontend Engineer

**Would flag:** no interface code yet (correct for Phase 0), but the reporting surface is undecided — is the Monday report markdown or a page?
**Would keep:** design tokens already exist for reuse when interface work lands.
**Would build first:** decide the answer. Reports stay markdown, agent-authored, until there are ten readers. Decide it now rather than at the point it blocks someone.

## 7. 🔍 UX Designer

**Would flag:** the customer conversation is the real user interface and its scripts are referenced everywhere but never written; the school-order flow has states — new → parsed → quoted → confirmed → shipped — but no state diagram.
**Would keep:** buyer-persona thinking is already deep. The procurement-officer view is the right lens.
**Would build first:** write the conversation flows (greeting → qualify → offer → close → confirm) with fallbacks, and a state diagram for the school-order path.

## 8. ⚙️ QA Engineer

**Would flag:** validators are smoke-tier; no property tests (price always a positive integer, dates monotonic); the agent evaluation sets are designed but nothing is labelled yet.
**Would keep:** CI caught two real bugs on day one — the gates work.
**Would build first:** a golden-file test per snapshot to catch silent parser drift, a validator self-test that injects a bad file and expects a non-zero exit, and the first 50 labelled conversations *before* the agent exists.

## 9. 💰 SRE

**Would flag:** no runbooks for the scheduled workflows; an automated-commit failure would be silent; service levels are drafted but not measured anywhere.
**Would keep:** concurrency cancellation, job timeouts, and minimum permissions throughout; the scheduled pipeline verified end-to-end.
**Would build first:** `docs/runbooks.md` — one block per workflow covering what healthy looks like, what the symptom is, and the three-step restart. Then wire the heartbeat monitor.

## 10. 🌱 Security Engineer

**Would flag:** branch protection is off, which is fine while solo but not before the first external collaborator — one workflow holds write access and needs protection at the moment collaboration starts. Crawled content flows into agent context, which is a prompt-injection surface: a snapshot carries arbitrary titles from an external site. No dependency scanning yet.
**Would keep:** workflow-security linting and secret scanning are green; credentials live in a vault; no tokens in the tree.
**Would build first:** branch protection from the first commit of any new repository, and **sanitise external content at ingestion** — strip markup and control characters from titles before they reach a model context.

## 11. 🛡️ Data Engineer

**Would flag:** snapshots carry no schema version, so a breaking parser change later becomes ambiguous; cross-source product identity is unresolved; quality checks stop at price sanity.
**Would keep:** dated files, dedupe on title and price, captured-date integrity verified.
**Would build first:** a `schema_version` field on every snapshot plus a validator rule, a written spec for the product-identity key so the matcher starts from a document, and a title-length anomaly check.

## 12. 📋 Database Engineer

**Would flag:** no migration tooling chosen; databases not provisioned; no retention policy; indexing unstated.
**Would keep:** the "git carries the latest, the database carries the history" split is the right call.
**Would build first:** numbered migrations in-repo, the price-history table and its composite index written down before implementation, and an explicit retention policy — raw data for a defined window, aggregates kept indefinitely.

## 13. 🎯 ML / Data Science Engineer

**Would flag:** the evaluation harness is the component the whole plan depends on, and it exists today only as a design note; there is no cost telemetry on any lane yet.
**Would keep:** model routing is documented per task type — cheap models for parsing, strong models for decisions.
**Would build first:** define the evaluation schema (input, expected outcome, grader) so conversations get labelled from day one, and log a cost line on every agent run, so per-order unit economics are measured rather than estimated.

## 14. 📊 Technical Writer

**Would flag:** documentation that summarises a master document can drift from it with nothing to catch it; the vocabulary mixes Dutch, German, and English trade terms without a glossary.
**Would keep:** documents are source-cited, dated, and versioned in git — better than most companies at any size.
**Would build first:** a glossary, and "generated from master@revision" headers on derived documents so staleness becomes detectable rather than invisible.

## 15. 🔬 Delivery / Scrum

**Would flag:** the analysis across this repository produced on the order of 250 ideas with no board; no work-in-progress limit; no weekly review ritual defined.
**Would keep:** the phase discipline — research, blueprint, tooling, data — has been unusually sequential and complete.
**Would build first:** convert the twelve graduating actions into tracked issues with labels, set a WIP limit of three, and make each README's status section the weekly review artefact.

## 16. 🧪 Release Manager

**Would flag:** no versioning policy for anything yet; change discipline starts when application code lands, but the habit should start with the repository itself.
**Would keep:** commit-message conventions are already correct, including `[skip ci]` handling.
**Would build first:** a `v0.1.0` tag at Phase-0 completion as a milestone marker, and a changelog that starts then.

## 17. 🧩 Performance Engineer

**Would flag:** the crawler is serial — fine at today's volume, and still fine nightly at ten times it, but it becomes a problem when sources multiply.
**Would keep:** the workload is small enough that this is genuinely not urgent.
**Would build first:** record one number — wall-clock per crawl — and start the series. Optimise when it crosses thirty minutes, not before.

## 18. 🔗 Support Engineer

**Would flag:** escalation paths are undefined for both operations — what happens when an agent cannot complete, or a school email is genuinely ambiguous? No SLA templates, no human-takeover runbook.
**Would keep:** approval-mode defaults are already specified.
**Would build first:** `docs/ESCALATION.md` — the triggers that require a human, the response-time promise, and template replies.

---

## Synthesis — first ten build items

| # | Item | Owner | Effort |
|---|---|---|---|
| 1 | Schema version on every snapshot + golden-file test | Data / QA | 30 min |
| 2 | `MILESTONES.md` with measurable exit criteria | Product | 1 h |
| 3 | Track the twelve graduating actions as labelled issues | Delivery | 1 h |
| 4 | Glossary + "generated from master@revision" headers | Writing | 1 h |
| 5 | Validator self-test — inject a bad file, expect non-zero exit | QA | 30 min |
| 6 | Sanitise external content before it reaches a model context | Security | 30 min |
| 7 | Heartbeat monitoring on every scheduled workflow | SRE | 1 h |
| 8 | `docs/runbooks.md` — healthy / symptom / 3-step restart | SRE | 1.5 h |
| 9 | Spine schema document + architecture records | Architecture | 2 h |
| 10 | Evaluation schema + first 50 labelled conversations | ML | 3 h |

## What the team would deliberately keep

- **Evidence-first culture.** Every claim has a source; every number has a date. This is the reason the proposal can be checked in minutes instead of trusted.
- **Gates that catch their own bugs.** The validation suite found two real defects on day one.
- **Reuse before rebuild.** Existing components are adapted rather than reimplemented — the discipline that makes the phase estimates credible.
- **Additive by design.** Nothing is replaced; every phase can be stopped without losing what already works.
- **Clear per-audience language.** Client-facing material in one language, operational material in another, with no ambiguity about which is which.

<div align="center">
<sub>Review conducted 2026-10-22 · 18 disciplines · every finding above is already reflected in the phase plan or the backlog.</sub>
</div>