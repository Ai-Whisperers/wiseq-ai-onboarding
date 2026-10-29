# Preparation catalog — what we should and could prepare

*Docs-only planning map. Distinguishes **already done**, **prepare offline (no Rob keys)**, **needs Rob input/keys**, and **do not prepare yet**. Aligns with dossier [doc 30](../10-client/01-complete-dossier.md), lab Milestone 1, and [read-only guide](../start/rob/read-only-access.md). For the Hermes show-when-data-lands plan see [19 · Demo readiness](19-hermes-demo-readiness.md).*

## Legend

| Tag | Meaning |
| :--- | :--- |
| ✅ Done | In repo now |
| 🔧 Offline | Can finish without production access |
| 🔑 Rob | Needs Rob (file, answer, or read-only key) |
| ⏸ Later | After Milestone 1 / Gates |
| 🚫 Don't | Policy, waste, or premature |

---

## A. Already prepared ✅

| Item | Where |
| :--- | :--- |
| Company / market / compliance research | docs 01, 08–11, research-lanes |
| Bundle spine + component registry + CI | `data/wiseq-*.csv`, validate_repo |
| Operating manual + Mastersheet extracts | `data/client/` |
| Critical audit + evidence dimensions | doc 29, claims 48–60 |
| Synthetic lab scenarios A–C | `lab/` |
| Hermes Desktop notes + skills pack | `docs/50-evidence/HERMES…`, `lab/hermes/` |
| Read-only credential how-to for Rob | `docs/start/rob/read-only-access.md` |
| Workflow / SoR / bad practices / opportunity maps | `docs/50-evidence/` |
| Internal reuse + implement backlog | `INTERNAL-REUSE-AND-BEST-PRACTICES.md` |
| Keep/extend/replace for A–C | experiment register |

---

## B. Prepare offline now 🔧 (highest value)

### B1 — Client understanding & Rob UX (docs)

| Deliverable | Why | Owner note |
| :--- | :--- | :--- |
| Keep [doc 30 dossier](../10-client/01-complete-dossier.md) current | Single client truth | Update when Rob answers |
| Refresh Rob pitch for post-manual facts | Avoid stale “CD can’t do bundles” / Exact / Trustpilot-first | for-rob + THE-CASE |
| NL one-pager for Rob (optional) | Decision maker skims Dutch | extend 00-nl |
| ADR Desktop-first + e-Boekhouden | Stop 06 vs 24 drift | `docs/adr/` |
| Runbook stubs (ungefrankeerd, school escalate, strike Wed) | Ops handoff | docs/audits or lab/hermes |
| ESCALATION one-pager already started | Approval UX | APPROVAL-AND-ESCALATION |

### B2 — Data & knowledge packs (no secrets)

| Deliverable | Why |
| :--- | :--- |
| Expand school-mail golden set toward 30–50 labeled cases | Parser regression (doc 07) |
| Typed tariff fixture completeness + qty 1/5/10 matrix doc | Exp C expansion |
| Competitor watch URL list (BuddyPhones, Puro, Educatheek, …) | changedetection config |
| Shop↔bol **public** drift method note | Monday digest without tokens |
| Amazon ASIN cleanup checklist | Hero vs Unbreakable |
| Scamadviser remediation checklist | Trust Score 0 |
| CE/DoC **metadata** schema (no cert binaries in public repo) | Compliance triage |
| Reseller rule card (EDG / ITS / Onderwijsmagazijn) | Invoice kenmerk |
| NL school calendar / promo moments | Seasonality |
| GS1 enrolment checklist (€225/yr path) | EAN program |

### B3 — Agent / Hermes (still offline)

| Deliverable | Why |
| :--- | :--- |
| Remaining skill **stubs** (bol-retailer-ops, reputation, incident, compliance, oss-vat, shopify-admin) | Match doc 24 |
| Seeded memory v2 from dossier §1–8 | Desktop answers |
| Demo script for Rob (3 scenarios + digest) | Meeting artifact |
| Guardrail policy table as Markdown (margins, contact limits, NEEDS_CONFIRMATION refuse) | Before code |

### B4 — Commercial / governance docs

| Deliverable | Why |
| :--- | :--- |
| Phase-0 read-only SOW one-pager | What keys buy |
| DPA outline pointer (doc 18) before mailbox PII | AVG |
| Publication ask: raw Handleiding yes/no | Privacy |
| Turnover question card (Thuiswinkel bands) | Quote accuracy |

---

## C. Needs Rob 🔑 (block live reads / calibration)

| Ask | Use | Guide |
| :--- | :--- | :--- |
| ChannelDock plan + API key/secret | Stock, rules, ungefrankeerd | Read-only guide §1 |
| bol credentials × accounts | Assortment, promises, reviews read | §2 |
| e-Boekhouden REST token | School doc shapes | §3 |
| Mailbox provider + read access | Triage drafts | §4 |
| FiveX CSVs (stock/sales/reviews) | LVB + review baselines | §6 |
| ≥5–10 anonymized school order packs | Eval realism + Gate 0.3 timing | Doc 06 item 3 |
| Confirm 2× Adapter template + BE uplift definition | Data quality / ROI hygiene | Mastersheet flags |
| België migration date/intent | Account matrix | Dossier §3 |
| Shopify collaborator / skip | Own-shop spine | Guide §5 |
| Annual turnover band | Thuiswinkel | Doc 06 |
| Raw manual public OK? | Repo hygiene | client/README |

**How to ask:** send [READ-ONLY-ACCESS-GUIDE](../start/rob/read-only-access.md) + checklist at bottom; secrets via Bitwarden Send — never GitHub issue.

---

## D. Prepare after read-only works ⏸

| Item | Depends on |
| :--- | :--- |
| Fill stack-map capability matrix with real R tests | Wave 1 keys |
| Vendor adapters in lab (still read) | Smoke success |
| Live ungefrankeerd / assortment digests in Desktop | CD + bol read |
| School shadow vs real anonymized examples | Sample packs |
| Purchase-intel prototype on FiveX export | CSV |
| Thin bol / e-Boekhouden MCP (telescope pattern) | commerce-os decision |
| Langfuse / cron-health | Companion profile later |
| B2B outreach pack (outreach-engine patterns) | AVG templates + 857-org rules |

---

## E. Do not prepare yet 🚫

| Item | Why |
| :--- | :--- |
| Write scopes on any API | Gates 1–2 not passed |
| Auto review-deletion / rating change mailers | Policy |
| CE sticker workarounds | Unsafe |
| ChannelDock / FiveX / e-Boekhouden replacements | No measured gap |
| Exact Online MCP | Wrong vendor |
| Full Mastersheet / COGS / gift cards in public repo | Secrets/PII |
| ROI model using 80% or 178% | Conflict / unvalidated |
| Always-on VPS build before Desktop demo | Premature infra |
| n8n sprawl before Hermes skills used daily | Complexity |

---

## F. Suggested prep sequence (docs + offline artifacts)

```text
Week now
  1. Keep dossier 30 + this catalog accurate
  2. Fix Rob-facing pitch inconsistencies (bundles, bol-first, Desktop, e-Boekhouden)
  3. Send Rob: read-only guide + open-asks checklist + Handleiding publication question
  4. Offline: competitor URLs, Amazon/Scamadviser checklists, reseller card, GS1 checklist
  5. Offline: skill stubs + demo script + ADR

When wave-1 keys arrive
  6. Capability matrix + read smoke notes (still docs + private vault)
  7. Compare live shapes to lab fixtures; expand goldens
```

---

## G. Traceability

| Theme | Deep dive |
| :--- | :--- |
| Who / stack / pain | [Doc 30](../10-client/01-complete-dossier.md) |
| Workflows | [CURRENT-STATE…](02-workflow-audit.md) |
| Data ownership | [DATA-FLOW…](03-data-flow-sor.md) |
| What to build/test | [AI-AND-OSS…](05-opportunity-map.md) · [lab](../../lab/README.md) |
| AIW reuse | [INTERNAL-REUSE…](13-internal-reuse.md) |
| Safety | [doc 29](../60-governance/03-critical-audit-2026-10-27.md) · [RISK…](12-risk-register.md) |
