<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 12* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Specialist Review — 31 Hats on the WiseQ Engagement

*2026-10-22. An independent review of the WiseQ engagement from 30 specialist perspectives — operations, procurement, compliance, finance, engineering, and delivery. Each hat raises 2–3 concrete findings. Together they are the stress test behind every phase in the blueprint: what could break the plan, what could cost money, and what a reviewer would ask before signing. New regulatory finding integrated: the revised EU Product Liability Directive, which brings software and AI into scope for products — and kids' products face the highest scrutiny.*

---

## 🎯 Domain A — The WiseQ Engagement (hats 1-15)

### 1. Knowledge-transfer engineer
Rob IS the system today — the 30-page manual is the only doc. (a) Manual → structured runbooks: every process as checklist the agent can execute; (b) record a "day with Rob" screen-share session → transcript → task inventory; (c) bus-factor metric: % of processes documented vs in-head — the engagement's real deliverable is dropping that number.

### 2. Data-migration surgeon
Phase 0 moves data into the canonical spine. (a) Rehearse on a COPY (Shopify dev store + ChannelDock sandbox) — never live; (b) migration runbook with rollback point at every step (AIW rule: backup before migration, always); (c) post-migration diff report: SKU count, EAN count, bundle resolution rate before/after.

### 3. Contract lawyer (NL services)
(a) DPA (verwerkersovereenkomst) mandatory before touching any personal data — GDPR Art. 28; (b) outcome-priced components need precise unit definitions (what counts as a "processed order"?); (c) IP: agent-built scripts — who owns what; pilot-priced work should grant WiseQ usage rights, AIW keeps the reusable components.

### 4. Product-liability underwriter
Revised EU Product Liability Directive (2026 transposition): software/AI in products now liability-relevant; kids' products = highest scrutiny. (a) Verify WiseQ's aansprakelijkheidsverzekering covers e-commerce channel sales (not just B2B); (b) our automation touching safety-comms (volume-limiting claims) must never overstate — cert-evidence library (doc 11) is the guard; (c) GPS-tracker data incidents → liability + GDPR double exposure: incident runbook required.

### 5. School procurement officer (the buyer persona)
What actually triggers a school order: (a) budget windows (Q1 planning, June year-end spend-down) — outreach calendar synced to them; (b) process: bestelnummer/inkoopcoördinator needs an invoice line that maps to their administration — our order-parser must emit THEIR format; (c) reorders are habit: if first delivery lands clean, the school reorders in August forever — SLA on first order is the whole game.

### 6. Bol account-health watcher
Bol suspends sellers for performance dips. (a) Monitor late-shipment %, cancellation %, response-time metrics nightly — alert before bol does; (b) the drift cleanup (312→230) must be staged — mass-delisting triggers review; 10/day; (c) a bol policy-change RSS/watch on partnerplatform.bol.com — terms changes hit thin-margin sellers first.

### 7. Seasonality actuary (NL calendar)
(a) Back-to-school (Aug) = 40%+ of annual school-channel revenue — stock + content + ad budget pre-positioned in July; (b) Sinterklaas (Dec 5) + Christmas = consumer peak — gift-bundle SKUs (the 25 bundles!) merchandised from Oct 15; (c) summer dip = maintenance window: listings cleanup, cert audits, A/B tests.

### 8. Amazon.nl category analyst
(a) iClever wins on review count; WiseQ's counter is review velocity (D+1 engine) + A+ content on the 2020 ASINs; (b) FBM-vs-FBA decision per SKU: class sets = FBA (Prime badge converts schools' parents); (c) win the buy box on their own brand ASINs — currently resellers may hold it.

### 9. B2B credit controller
"Bestel op factuur" = WiseQ extends credit to schools. (a) Credit limit per school (start €500, grow with payment history); (b) automated payment-reminder ladder (day 14 polite, day 30 firm, day 45 stop-ship) — schools pay slowly, not never; (c) aging report weekly — the agent flags, Rob decides.

### 10. Returns/logistics optimizer
(a) NL returns culture (~10% fashion, less for electronics): return-reason taxonomy auto-tagged — feeds product improvement; (b) bol returns: auto-accept + restock to correct SKU via EAN (the spine pays off again); (c) damaged-in-transit claims to carrier automated with photo evidence.

### 11. Content localization editor
(a) NL copy is native; EN store copy exists — DE store (Amazon.de) needs real German, not machine: ever-traduora + native review; (b) product manuals as PDFs per SKU family — support ticket reducer; (c) the 20 empty descriptions (doc: catalog lane) = first content-agent batch job.

### 12. Financial controller (engagement-side)
(a) Track OUR hours per component — the reusable-component inventory needs real cost data for AIW pricing; (b) WiseQ ROI dashboard: hours saved (school orders), revenue added (reviews→conversion), errors avoided (EAN) — updated monthly, shown to Rob; (c) pilot → retainer decision gate: pre-agree the metrics that trigger continuation.

### 13. Scenario strategist (WiseQ futures)
(a) If bol adds agentic ordering (UCP momentum), WiseQ is early — the MCP endpoint becomes a sales channel; (b) if Heutink copies the B2B layer, WiseQ's moat = agentic reordering + niche depth; (c) exit optionality: the cleaned data + automation makes WiseQ acquirable at a different multiple — worth naming in the pitch's final slide.

### 14. Change-management coach
Rob's the user AND the owner. (a) Ship one automation he feels weekly (drift report Monday email) — trust compounds; (b) agent suggestions arrive as proposals, not actions, for the first 60 days (approval-mode default); (c) a "what did the agents do" daily digest — visibility kills fear of the black box.

### 15. Incident-response planner
(a) WhatsApp/channel outage → fallback order form on the shop; (b) agent gone rogue (wrong price live) → kill switch + 15-min rollback runbook + pricing-change freeze rule; (c) data incident → 72h GDPR notification runbook with pre-drafted templates (avanzialegal-style clock starts immediately).

---

## 🏛️ Domain B — The commercial, channel & compliance bench

*Ten further passes, each on a question the first fifteen do not answer. These are the ones that
change a decision, not the ones that confirm one.*

### 16. Marketplace-fee analyst (bol + Amazon)
The margin conversation nobody in the repo has had. (a) bol.com charges selling fees per order plus
advertising costs that are billed separately — the true take-rate on a €19 child headphone can
exceed 20% once ads are counted; (b) Amazon EU referral fees on the same basket are close to
WiseQ's own margin at the €18.95–34 band; (c) therefore "price harmonization from one rule sheet"
(doc 04) is a margin exercise, not a tidiness exercise, and must be modelled per channel *net of
fees* before a single price moves. **Flag:** we have never seen WiseQ's actual margin per SKU.

### 17. NL tax and VAT specialist
(a) WiseQ ships NL→BE and holds an Amazon EU seller account; OSS/IOSS thresholds and the
one-stop-shop position determine whether EU expansion needs VAT registrations per country — that is
a compliance cost, not a marketing decision; (b) the German/Dutch dual inventory model changes
when Amazon logistics takes over cross-border fulfilment; (c) the €225/yr GS1 spend is trivial next
to a wrong VAT position. **Fix:** one question in Phase 0 — current VAT registrations and turnover
per country. We are not qualified to answer this for them; we are qualified to ask it.

### 18. Returns-abuse and chargeback investigator
The Trustpilot corpus concentrates two complaints: charger durability and slow support. (a) A
chargeback pattern on a low-value item is a margin leak that no dashboard currently shows;
(b) "defective on arrival" claims against bundles where the bundle was split (doc 07) are almost
certainly a *data* problem masquerading as a quality problem — the component the customer actually
received may not be the component that sold; (c) the fix is a reason-code discipline on every
return, fed back into the spine. **Flag:** untested, and it is a cheap test.

### 19. Accessibility auditor (EN 301 549 / European Accessibility Act)
WiseQ sells to schools and to parents of autistic and ADHD children — the exact population the
European Accessibility Act (applying from June 2025) is written for. (a) If any part of the B2B
ordering flow is a PDF invoice attachment rather than an accessible HTML document, that is an
exposure; (b) the site demos in doc 17 are the right place to prove accessibility rather than
assert it; (c) "inclusive design" is a genuine differentiator against Heutink (doc 09) and costs
nothing to demonstrate. **Flag:** we have never audited their accessibility posture.

### 20. Wholesale and purchasing-cooperative specialist
The *inkoopcollectieven* route (doc 08, doc 11) is named but never scoped. (a) Listing costs a
one-off and reaches hundreds of schools through a single contract — the highest leverage per euro
in the entire backlog; (b) but collectives impose their own payment terms, price ceilings, and
annual re-tender cycles that a €7–34 long-tail catalog may not clear; (c) **we do not know which
collectives WiseQ is already in.** That is the first question of any Phase-0 commercial call.

### 21. Customs, EPR and logistics specialist
(a) Cross-border children's electronics into Germany and France implicates **EPR packaging
registration** (LUCID in DE) and battery registration — per-country, per-category, non-negotiable,
and entirely absent from the repo; (b) the current model appears to be Netherlands-stock shipped
cross-border, which is the *worst* option for EPR and duty; (c) a DACH Amazon push without EPR
registration is a takedown risk on day one. **Flag:** this is the compliance item most likely to
cost WiseQ money we have not mentioned.

### 22. School DPO / privacy officer
Doc 11 says outreach needs "a lawful basis" and doc 18 assumes a processor relationship — but a
school board is a *public body* under a different regime than an SME. (a) Dutch school boards
process personal data of children under APV, and contracting with them has its own paperwork;
(b) harvest-based B2B contact lists (857 orgs, doc 02) need the legitimate-interest assessment
written down, not asserted; (c) a one-page AV + APV position before the first outreach wave is
cheap and prevents a complaint. **Flag:** unasked, and it is a question Rob will appreciate us
raising first.

### 23. Peak-season capacity planner
Back-to-school is a step change, not a ramp (hat 19). (a) If the school-order pipeline goes
live in June it hits the exact month WiseQ is busiest — sequencing matters more than speed;
(b) the automation's value is highest in August and near zero in January, so an annual
commitment should be phase-weighted, not flat; (c) the honest recommendation may be *launch in
February, not July*, and we should say so before it becomes obvious.

### 24. Energy, hardware and TCO challenger
A 24/7 office machine running agent workloads is a line item nobody costs. (a) Always-on compute
has a power cost that lands on WiseQ's electricity bill with no attribution; (b) hosting option
(b) — our dedicated server — moves that cost into the care plan where it is visible; (c) this
slightly favours the hosting decision we already recommended, which is worth being honest about
rather than hiding.

### 25. Reference-check and proof-of-outcome challenger
*(This hat replaces the internal-economics pass from earlier drafts. The finding is uncomfortable
and belongs in the client-facing document.)* (a) The repo demonstrates *artefacts* — a bundle
spine, an audit, a lead list — but states no **outcome from a previous client engagement**;
(b) a completed engagement with a named, anonymised result ("cycle time 4h → 12m") would settle
the credibility question that no amount of research substitutes for; (c) until one exists, the
honest pitch is "here is what we can build and here is exactly what it costs" — which doc 04's
new pricing now supports, and which is a legitimate position. **Flag:** still the weakest link in
the commercial story.

## 🔧 Domain C — Engineering & delivery passes

*The build-side review: what the team would fix before writing the first line of production code.*

### 26. Software architect
**Flags:** the canonical spine exists as a concept plus CSVs but has no DDL or migration; wrapper API contracts are undefined; decisions live in prose rather than numbered ADRs. **Praise:** the layered architecture (git = code, managed Postgres = data, object storage = assets, DuckDB = analytics) is stated and consistent. **Fix:** start `docs/adr/` — ADR-001 (repository split), ADR-002 (image registry for wrappers), ADR-003 (one database per operation); retro-write ten ADRs from the existing docs in one pass, and define the spine DDL as the first migration file even before the database exists — it becomes the schema contract.

### 27. Data engineer
**Flags:** snapshots carry no `schema_version`, so a breaking parser change later is ambiguous; cross-source product identity is unresolved; data-quality checks stop at price sanity. **Praise:** dated files, dedupe on (title, price), captured-date integrity checked. **Fix:** add `"schema_version": 1` to crawler output plus a validator rule; draft the identity key (brand + model + colour normalisation) as a spec so the matcher starts from a document rather than from scratch; add a title-length anomaly check.

### 28. QA engineer
**Flags:** validators are smoke-tier only; no property tests (price always int > 0, dates monotonic); the agent eval sets are designed but no conversations are labelled yet. **Praise:** CI caught two real bugs on day one — the gates demonstrably work. **Fix:** a golden-file test per snapshot day to catch silent parser drift; a validator self-test (inject a bad file, expect exit 1); start the 50-conversation eval set now, before the agent exists, from supplier FAQ pages.

### 29. SRE
**Flags:** no runbooks for the workflows; a failing automated commit would be silent; SLOs are drafted but not measured anywhere. **Praise:** concurrency cancellation, timeouts, and minimum permissions everywhere; the nightly pipeline verified end-to-end. **Fix:** `docs/runbooks.md` — one block per workflow (what healthy looks like, what the symptom is, the 3-step restart); wire the heartbeat monitor; add a status badge row to both READMEs.

### 30. Security engineer (AppSec)
**Flags:** branch protection is off (acceptable while solo, but the snapshot workflow has `contents:write`, so protection must be on before the first external collaborator); crawler content flows into agent context, which is a prompt-injection surface — a snapshot JSON carries arbitrary titles from an external site; no dependency scanning yet. **Praise:** workflow-security linting and secret scanning are green; credentials live in a vault; no tokens in the tree. **Fix:** branch protection from the first commit of the wrapper repository; **sanitise crawler output at ingestion** — strip markdown and control characters from titles before they reach any model context.

### 31. Support engineer
**Flags:** escalation paths are undefined — what happens when the school-order agent cannot complete, or an email is genuinely ambiguous? No SLA templates, no human-takeover runbook. **Praise:** the approval-mode default is already specced. **Fix:** `docs/ESCALATION.md` per operation: triggers for human takeover, a response-time promise, and template replies (NL/EN for WiseQ).

---

## 🚀 Synthesis — the actions that graduate to delivery

| # | Hat | Action | Track |
|---|---|---|---|
| 1 | 16 | Product-liability insurance check — confirm channel-sales cover | wiseq |
| 2 | 17 | Bol account-health monitor, alert before suspension | wiseq |
| 3 | 18 | NL seasonality calendar feeding procurement and content | wiseq |
| 4 | 19 | B2B credit ladder for invoice orders | wiseq |
| 5 | 20 | Bundle-purchase-driver insight replacing the hand-built Excel | wiseq |
| 6 | 24 | Monday drift report as the first trust-building automation | wiseq |
| 7 | 25 | Incident-response runbook + pre-drafted GDPR templates | wiseq |
| 8 | 26 | `schema_version` in snapshots + golden-file test | build |
| 9 | 27 | Validator self-test — inject a bad file, expect exit 1 | build |
| 10 | 28 | Heartbeat monitoring on every scheduled workflow | build |
| 11 | 30 | Sanitise external content before it reaches model context | build |
| 12 | 31 | `docs/ESCALATION.md` — takeover triggers and SLA promises | build |

## 🗑️ Discards (explicit)

- **Hiring salespeople** (hat 21): inbound and case studies first; a sales hire at client #5, not before.
- **Building a dashboard SaaS** (hat 30): the metrics belong in markdown reports; productising them is a different company.
- **Voice-based ordering in a second language** (hat 21 adjacent): interesting, not ROI-positive yet; revisit when volume justifies it.
- **Trademarking a product name now** (hat 26): name it when the second client signs, not before.
- **Rewriting the ERP** (from the tooling pass): nothing gets replaced. Every phase is additive and reversible.

---

## 📌 In short

**30 structured passes** across the WiseQ engagement, compliance and risk, and engineering and delivery. They change the plan in specific, checkable ways — bundle scope, the 24-month arc, B2B credit handling, incident response. Discards are listed explicitly so the argument has a floor, not just a ceiling, and the synthesis section says which findings actually graduate into delivery work.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Dev Team Hats](../d-delivery/16-DEV-TEAM-HATS.md)** | The same treatment from the build team's side |
| **[Ai Stack Blueprint](../a-proposal/04-AI-STACK-BLUEPRINT.md)** | What the review changes about the plan |
| **[Next Steps](../a-proposal/06-NEXT-STEPS.md)** | The decisions the review actually moves |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
