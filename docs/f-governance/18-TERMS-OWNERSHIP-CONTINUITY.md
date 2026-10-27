<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track C · Document 18* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

# Working Together — Terms, Ownership & Continuity

*One page covering the questions a serious buyer asks before signing, and that we
would rather answer up front than be asked in week three. Nothing here is binding —
these are the positions we propose to work from.*

---

## 1. 🤝 Who owns what

**Short version: you own everything we build for you.**

| Asset | Owner | Notes |
| :--- | :--- | :--- |
| Your data — orders, products, customers, contacts | **WiseQ** | Always was. Never leaves your control. |
| Your credentials (Shopify, bol.com, ChannelDock, Amazon) | **WiseQ** | We use them under your grant; you revoke at any time. |
| The repository we build in | **WiseQ** | We work *inside your estate*, not a private repo of ours. |
| Code, scripts, ETL jobs, connectors written for you | **WiseQ** | Yours from the moment they exist. |
| Documentation and runbooks | **WiseQ** | So you are not dependent on us to operate it. |
| Generic know-how (how we approach EAN registries, ETL, review flows) | **AI Whisperers** | Ours. You get the *results*, we keep the *method*. |

**The line we draw:** you own **what runs in your business**. We retain ownership of
**general techniques** so that we can apply them elsewhere. Nothing we build for you
is held hostage to keep paying us — that would defeat the purpose of the handover.

---

## 2. 📄 Data protection — we are a processor, not a controller

Before we touch a single customer record, both sides sign a
**verwerkersovereenkomst (data processing agreement)** under **GDPR Art. 28**.

| Our obligation | Your right |
| :--- | :--- |
| Process personal data **only on your documented instructions** | Know exactly what we process and why |
| Ensure our sub-processors meet the same bar | See who they are |
| Assist with data-subject requests (DSAR) within statutory time | Exercise your rights directly |
| **Notify you of a data breach without undue delay** | Be informed, not discover it |
| Delete or return your data when the engagement ends | Get it all back |
| Never use your data to train anything | Your data stays yours |

**We are explicitly not a controller of your customer data.** We also sit outside the
consumer-product supply chain: for GPSR purposes WiseQ B.V. is the manufacturer and its
own EU Responsible Person, and we are a **software provider** — we do not place any
product on the market. That stays true in the contract language.

**AI literacy (EU AI Act Art. 4, in force since Feb 2025):** we maintain an internal
register of who uses which AI tooling, for what, and what training they received.
This costs us a few hours of record-keeping, not a training budget. We can help you
build the equivalent register for your team as part of Phase 0.

---

## 3. 🔒 How we keep your systems safe

| Control | What we actually do |
| :--- | :--- |
| **Read-only by default** | Phase 0 writes **nothing**. Any write requires approval gates you can see and switch off. |
| **Least privilege** | Separate credentials per connector, scoped to what that connector needs. |
| **Reversibility** | Every migration rehearses on a copy first, with a rollback point before each step. |
| **Backups you can verify** | Nightly encrypted backup, 30-day retention — **and we test a restore**, and show you the result. An untested backup is a hope, not a control. |
| **Secrets** | Never in the repo, never in a prompt. Managed secret store, rotated. |
| **Audit trail** | What the agent did, when, and what it was based on. |
| **Kill switch** | One action to stop all automated writes. |
| **No training on your data** | Stated in the DPA, and true. |

---

## 4. 🔄 If you decide to stop — the exit plan

This should be written down **before** anyone is depending on it, which is why it is
here.

**You can leave at any phase boundary.** Our own plan is built that way: Phase 0 writes
nothing, so stopping after Phase 0 leaves you with a full picture and no exposure.

| What you get on exit | Detail |
| :--- | :--- |
| **Everything built for you** | Full repository, full history, transferred to your org |
| **All documentation** | Architecture, runbooks, credentials map |
| **All credentials** | Rotated and handed over; we remove every copy |
| **A working handover session** | Walk through the system with whoever will operate it |
| **A knowledge-transfer period** | Agreed length, so it is not a cliff |
| **Data export** | Full export in open formats (SQL/CSV/JSON), on request |

**What we would ask for in return:** reasonable notice so we can hand over properly, and
payment for work completed to that date. **What we will not do:** hold your data, your
code, or your credentials hostage to a renewal.

**Portability is the test:** if you took everything we built and ran it with a different
consultant — or with nobody — would it work? We design for that answer being yes.

---

## 5. 🧑‍💻 Continuity — the honest answer to "what if you're unavailable?"

We should not pretend a one-person consultancy is a staffed helpdesk. Here is the real
position.

| Situation | What happens |
| :--- | :--- |
| **Normal operation** | Documented, yours to operate. You should not *need* us for daily running. |
| **Short absence (a week)** | Announced in advance where possible. Documented runbook; nothing breaks. |
| **Planned holiday** | Agreed dates, a handover note, and a named contact for anything genuinely urgent. |
| **Illness / emergency** | We commit to telling you **within one business day**. We do not promise same-day cover we cannot guarantee. |
| **Longer unavailability** | Honest conversation about scope and dates. No silent stalling — you hear from us either way. |
| **If AI Whisperers ceases entirely** | See §4. The exit plan *is* the continuity plan: everything you need is already yours and documented. |

**The design principle behind all of this:** we automate your repetitive work so that
your team is less dependent on any single vendor — **including us.** The most valuable
thing we can leave you with is a business that runs without us.

We will agree response expectations in writing for the support that is actually in
scope, rather than implying a 24/7 service we don't staff.

---

## 6. 📅 What we propose to agree before any work starts

Short list, in plain language. Each is a line in a contract, not a negotiation surprise.

1. Scope per phase, with a named stop/go decision at each boundary
2. A processing agreement (Art. 28) before any personal data is touched
3. Ownership: everything we build is yours (per §1)
4. Exit terms agreed up front (per §4); liability cap and invoicing mechanics (per §8–9)
5. Support expectations stated honestly (per §5)
6. Written record of every price before it becomes an invoice
7. **If we get something wrong, we tell you** — including in our own documents. This repo
   has a documented example of exactly that, in the backlog doc's review-target note.

---

## 8. ⚖️ Liability — the position we propose

*Drafted from published NL market terms and the NRF global benchmark; your counsel reviews the final wording before signature.*

| Element | Proposed position |
| :--- | :--- |
| **Cap** | Our total liability is limited to the fees invoiced in the **12 months before the claim first arose** |
| **Exclusions** | Indirect damage is excluded: gevolgschade, gederfde winst, goodwill, bedrijfsstagnatie, dataverlies |
| **Carve-outs** | Nothing in this cap limits liability for intent or gross negligence (opzet / bewuste roekeloosheid), and nothing caps GDPR liability below the statutory minimum (Art. 82) |
| **Claim window** | Claims expire 12 months after discovery |
| **Why so short a list** | The bigger protection is architectural: nothing writes to your systems or touches money before Gate 4 (see `23-ACCEPTANCE-CRITERIA.md`). The cap covers the residual, not the exposure. |

---

## 9. 🧾 Invoicing — how the money mechanically works

| Element | Position |
| :--- | :--- |
| **VAT** | Services to a NL bv are **reverse-charged** ("btw verlegd"): we invoice without VAT, citing your btw-identificatienummer; you self-account in your return (cash-flow neutral for you) |
| **Currency** | EUR |
| **Terms** | 14 days, NL-standard late-fee clause |
| **Timing** | First invoice at pilot start, not after it — the fee schedule in `../a-proposal/04-AI-STACK-BLUEPRINT.md` sequences pilot payment before the heavy build hours |
| **Care-plan step-up (agreed now, never sprung)** | Year 1 care plan at the quoted monthly rate. At renewal — or when a third engine (marketplace, integration, or workflow beyond the original scope) goes live, whichever comes first — the rate steps to **€395/month**, the bottom of the NL market band. It is in this contract so it is never a surprise negotiation later. |
| **Case study & references** | We may ask to publish a case study after Gate 2. It uses only anonymized metrics, and only with your written sign-off per item. Saying no costs you nothing and is never held against the engagement. |

---

## 10. 🗂️ Where to find the detail

| Topic | Document |
| :--- | :--- |
| Phased plan, architecture, guardrails | `../a-proposal/04-AI-STACK-BLUEPRINT.md` |
| The full opportunity list, scored | `../a-proposal/05-AUTOMATION-BACKLOG.md` |
| Integrations and the systems we connect | `../c-market/08-OSS-INTEGRATIONS.md` |
| Compliance map, incl. AI Act and GPSR | `../c-market/11-COMPLIANCE-REGULATORY.md` |
| Hosting, backups, monitoring | `../d-delivery/15-DEVOPS-MASTERPLAN.md` |
| What we need from you, and open decisions | `../a-proposal/06-NEXT-STEPS.md` |

---

<sub>*Prepared by AI Whisperers · Grootebroek engagement · 2026-10-22.*
*These are proposed working positions, not legal advice. Your counsel reviews the final wording — that is the right order of operations.</sub>