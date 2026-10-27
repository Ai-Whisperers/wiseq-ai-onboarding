<div align="center">

<img src="assets/brand/hero-banner.png" alt="WiseQ × AI Whisperers — AI Transformation Work Proposal" width="100%">

</div>

<br>

<div align="center">

[![Documents](https://img.shields.io/badge/documents-28-blue?style=for-the-badge)](#document-map)
[![SKUs%20audited](https://img.shields.io/badge/SKUs%20audited-230-blue?style=for-the-badge)](#the-case-in-one-page)
[![Bundle%20spine](https://img.shields.io/badge/bundle%20spine-114%20SKUs%20%2B%2025%20bundles-success?style=for-the-badge)](#the-case-in-one-page)
[![OSS%20catalog](https://img.shields.io/badge/OSS-31%20topics%20·%20curated%20menu-blueviolet?style=for-the-badge)](#track-c)
[![Research](https://img.shields.io/badge/research-5%20lanes%20+%207%20addenda-orange?style=for-the-badge)](#evidence-base)
[![Specialist%20passes](https://img.shields.io/badge/specialist%20passes-31%20+%2018%20hats-pink?style=for-the-badge)](#evidence-base)
[![validate](https://img.shields.io/github/actions/workflow/status/Ai-Whisperers/wiseq-ai-onboarding/validate.yml?branch=main&style=for-the-badge)](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/actions/workflows/validate.yml)

[WiseQ](https://www.wiseq.nl) — the Dutch kids-technology brand from Grootebroek, Netherlands ·
prepared by [AI Whisperers](https://github.com/Ai-Whisperers)

</div>

---

<a id="if-you-are"></a>

## 👋 If you are…

| You are… | Read this first | Then |
| :--- | :--- | :--- |
| **Rob Nyari** — E-Commerce CEO, decision-maker | [for-rob pack](docs/for-rob/README.md) → [04 · Blueprint](docs/a-proposal/04-AI-STACK-BLUEPRINT.md) | [06 · Next Steps](docs/a-proposal/06-NEXT-STEPS.md) for the four decisions |
| **AIW co-founder (Kiki)** | [for-kiki pack](docs/for-kiki/README.md) | [Terms](docs/f-governance/18-TERMS-OWNERSHIP-CONTINUITY.md) · [Evidence](docs/f-governance/27-EVIDENCE-INDEX.md) |
| **A founder or director** deciding whether to commission this | [The case in one page](#the-case-in-one-page) → [Cost model](docs/a-proposal/04-AI-STACK-BLUEPRINT.md#cost-model-honest) | [09 · Competitors & Deals](docs/c-market/09-COMPETITORS-DEALS.md) |
| **An operations / purchase lead** | [for-ops pack](docs/for-ops/README.md) → [05 · Backlog](docs/a-proposal/05-AUTOMATION-BACKLOG.md) | [25 · Catalog scorecard](docs/b-company/25-CATALOG-SCORECARD.md) |
| **A technical evaluator or IT reviewer** | [04 · Architecture](docs/a-proposal/04-AI-STACK-BLUEPRINT.md) + [15 · Delivery](docs/d-delivery/15-DEVOPS-MASTERPLAN.md) | [13 · Tooling](docs/d-delivery/13-TOOLING-MCP-INSTALLS.md) |
| **New to this repository** | [Docs folder map](docs/README.md) | [Document map](#document-map) below |

---

<a id="the-one-paragraph-pitch"></a>

## 🎯 The one-paragraph pitch

> WiseQ already runs a remarkably modern stack — **Shopify with a custom B2B layer, ChannelDock, 5X, and live agentic-commerce endpoints.** The gap isn't tools; it's **orchestration**. School orders eat four-hour mornings. Bundle stock is re-tracked by hand in Excel. Review volume is thin and marketing runs below the site's potential.
>
> We propose **one 24/7 AI-operations layer** — an orchestrated agent runtime that connects the mailbox, bookkeeping, ChannelDock, and the webshop — cutting the school-order process from **~4 hours to minutes**, making EAN-based purchasing automatic, and running reputation, content, and outreach continuously. **Most pieces already exist as connectable services.** Nothing is ripped out and replaced: every phase is additive and measurable.

---

<a id="the-case-in-one-page"></a>

## 📊 The case in one page

| The gap we found | The evidence | What we build | The measurable target |
| :--- | :--- | :--- | :--- |
| **School orders eat 4-hour mornings** | Founder-confirmed in working session | School-order pipeline: email → offer → invoice → ChannelDock booking | **4h → <15 min** human touch |
| **Bundle recombination pollutes purchase data** | A cable sells inside 4 adapter combinations; ChannelDock can't model it | Component↔bundle graph in a canonical EAN registry | Clean, true purchase data |
| **0 of 230 SKUs carry an EAN barcode** | Programmatic Shopify audit | EAN/GTIN backfill + GS1 registry — **€225/yr** for the whole catalog (1,000-pack + contribution; covers 139 critical codes and all 230) | 230/230 registered |
| **77 bundle-products (33%) have no component map** | Same audit — component→bundle mapping lives in human memory | Decoded **bundle spine**: 114 component SKUs + 25 bundles, 0 unresolved | Fully decomposed |
| **Purchase data assembled by hand in Excel** | 6-month rolling average per EAN, one costly error/year | Nightly purchase-intelligence job | Daily, automatic, correct |
| **13 reviews, no automated invitations** | Trustpilot 4.5/5 but only 13 reviews (Oct 23; all organic) | Post-delivery review engine | Every order invited; TrustScore defended |
| **Scamadviser "Trust Score 0" flag** | Algorithmic remediation pending | Trust-profile remediation | Flag cleared |

---

<a id="document-map"></a>

## 🗺️ Document map

Twenty-eight documents (00 NL + 01–27) in [Approach A folders](docs/README.md) — proposal, company, market, delivery, showcase, governance, reviews — plus shallow role packs for Rob, Kiki, and ops.

**Role packs:** [for-rob](docs/for-rob/README.md) · [for-kiki](docs/for-kiki/README.md) · [for-ops](docs/for-ops/README.md) · [NL](docs/00-nl/00-NL-SAMENVATTING.md) · [full docs map](docs/README.md) · [data attic](data/README.md)

### Track A — The proposal *(what we recommend)* · [`docs/a-proposal/`](docs/a-proposal/README.md)

| # | Doc | What's in it | Read if |
| :--- | :--- | :--- | :--- |
| **04** | [AI Stack Blueprint](docs/a-proposal/04-AI-STACK-BLUEPRINT.md) | **The main proposal** — architecture, phase-by-phase plan, honest cost model, guardrails | You want the sell. Start here. |
| **05** | [Automation Backlog](docs/a-proposal/05-AUTOMATION-BACKLOG.md) | 21 automations scored by impact and effort, 🔥 flags on do-first | You want the option list, ranked |
| **06** | [Next Steps](docs/a-proposal/06-NEXT-STEPS.md) | The ask-list, our Phase-0 commitments, **four decisions for WiseQ**, and the four hosting options | You need to unblock us this week |

### Track B — The company *(who WiseQ is)* · [`docs/b-company/`](docs/b-company/README.md)

| # | Doc | What's in it |
| :--- | :--- | :--- |
| **01** | [Company Profile](docs/b-company/01-COMPANY-PROFILE.md) | Verified registry, timeline, channels, catalog, tech stack |
| **02** | [What We've Done](docs/b-company/02-WHAT-WE-DID.md) | Research dossier, market scan, lead-gen — with artifacts |
| **03** | [Meeting Notes 2026-10-21](docs/b-company/03-MEETING-NOTES-2026-10-21.md) | Business intel from our first working session |
| **07** | [Reuse-First](docs/b-company/07-PY-TRANSFER-WISEQ.md) | Existing capability mapped to WiseQ problems — incl. the decoded **bundle spine** |
| **25** | [Catalog scorecard](docs/b-company/25-CATALOG-SCORECARD.md) | One-page EAN / bundle / data-quality snapshot |

<a id="track-c"></a>

### Track C — The market & regulation *(what surrounds the plan)* · [`docs/c-market/`](docs/c-market/README.md)

| # | Doc | What's in it |
| :--- | :--- | :--- |
| **08** | [OSS & Integrations](docs/c-market/08-OSS-INTEGRATIONS.md) | Bol/Shopify/GS1/feed OSS landscape, EAN fix costs (€225/yr for the whole catalog via GS1 1,000-pack), NL trust marks, school collectives |
| **09** | [Competitors & Deals](docs/c-market/09-COMPETITORS-DEALS.md) | Real competitor map (iClever / Puro / Alpine / Heutink), deal pricing benchmarks, new opportunities |
| **10** | [OSS Catalog — 100 repos](docs/c-market/10-OSS-CATALOG-100.md) | 31 topics · ~100 listed by layer (6 topic JSON stubs still empty — see [data/README](data/README.md)) |
| **11** | [Compliance & Regulatory](docs/c-market/11-COMPLIANCE-REGULATORY.md) | EN 71 / 62115 / RED (2025 cyber layer), GPSR, Thuiswinkel €983–1,759/yr, cert-evidence library plan |
| **26** | [Unit economics](docs/c-market/26-UNIT-ECONOMICS.md) | PSP / PostNL / OSS VAT — Bancontact trap + €10k threshold |

### Tracks D–G — [`d-delivery`](docs/d-delivery/README.md) · [`e-showcase`](docs/e-showcase/README.md) · [`f-governance`](docs/f-governance/README.md) · [`g-reviews`](docs/g-reviews/README.md)

| # | Doc | Folder | What's in it |
| :--- | :--- | :--- | :--- |
| **12** | [Specialist Review — 31 Hats](docs/g-reviews/12-FIFTY-HATS.md) | [`g-reviews/`](docs/g-reviews/README.md) | 31 independent specialist passes |
| **13** | [Tooling & Integration Plan](docs/d-delivery/13-TOOLING-MCP-INSTALLS.md) | [`d-delivery/`](docs/d-delivery/README.md) | Connector install list + thin wrappers |
| **14** | [Hermes / AIW reuse](docs/d-delivery/14-HERMES-JEV-AIW-REUSE.md) | [`d-delivery/`](docs/d-delivery/README.md) | What ports from AIW |
| **15** | [Delivery Plan](docs/d-delivery/15-DEVOPS-MASTERPLAN.md) | [`d-delivery/`](docs/d-delivery/README.md) | CI/CD, storage, SLOs |
| **16** | [Delivery Review](docs/d-delivery/16-DEV-TEAM-HATS.md) | [`d-delivery/`](docs/d-delivery/README.md) | 18 build-discipline passes |
| **17** | [Site Concept Showcase](docs/e-showcase/17-SITE-CONCEPTS.md) | [`e-showcase/`](docs/e-showcase/README.md) | Three live scroll-driven concepts |
| **18** | [Terms & Ownership](docs/f-governance/18-TERMS-OWNERSHIP-CONTINUITY.md) | [`f-governance/`](docs/f-governance/README.md) | Ownership, GDPR, liability, exit |
| **19** | [Critical Review](docs/f-governance/19-CRITICAL-REVIEW.md) | [`f-governance/`](docs/f-governance/README.md) | Adversarial pass |
| **20** | [Send-to-Rob](docs/e-showcase/20-SEND-TO-ROB.md) | [`e-showcase/`](docs/e-showcase/README.md) | Outreach copy + demo links |
| **21** | [Who we are](docs/e-showcase/21-WHO-WE-ARE.md) | [`e-showcase/`](docs/e-showcase/README.md) | People + Dutch capability |
| **22** | [Audit response](docs/f-governance/22-AUDIT-RESPONSE.md) | [`f-governance/`](docs/f-governance/README.md) | Oct-22 external audit reply |
| **23** | [Acceptance criteria](docs/f-governance/23-ACCEPTANCE-CRITERIA.md) | [`f-governance/`](docs/f-governance/README.md) | Stage gates before pilot |
| **24** | [Agent infrastructure](docs/d-delivery/24-AGENT-INFRASTRUCTURE.md) | [`d-delivery/`](docs/d-delivery/README.md) | Hermes on WiseQ’s server |
| **27** | [Evidence index](docs/f-governance/27-EVIDENCE-INDEX.md) | [`f-governance/`](docs/f-governance/README.md) | Claim → artifact map |

---

## ⚙️ Target architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│  THE AI OPERATIONS LAYER — 24/7, reversible, audited                  │
│  orchestrator · memory · cron · kanban · skills · subagents          │
└───────────────────────────────────┬───────────────────────────────────┘
                                    │
        ┌───────────┬───────────┬───┴─────┬───────────┬───────────┐
        ▼           ▼           ▼         ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌────────┐ ┌────────┐ ┌─────────┐ ┌────────┐
   │ Mailbox │ │ Book-   │ │Channel │ │ Shopify│ │ bol.com │ │ Web &  │
   │ IMAP/   │ │ keeping │ │ Dock   │ │ Admin  │ │ + 5X    │ │ market │
   │ SMTP    │ │ offers  │ │ stock &│ │ orders │ │ seller  │ │ intel  │
   │ (email) │ │ invoice │ │ pur-   │ │        │ │ APIs    │ │ scrape │
   └─────────┘ └─────────┘ │ chase  │ └────────┘ └─────────┘ └────────┘
                          └────────┘
```

Runs wherever you choose — **four hosting options**, from your own server maintained by us to shared capacity at a reduced rate. See [06 · Hosting options](docs/a-proposal/06-NEXT-STEPS.md#hosting-options). Credentials live in a vault — never in chat, never in this repo. Every automated action is logged to an audit trail, and **money-touching steps keep human approval** until trust is earned.

Full detail, phase by phase: **[04 · AI Stack Blueprint](docs/a-proposal/04-AI-STACK-BLUEPRINT.md)**

---

## 🗓️ Delivery phases

```
Phase 0 ────────────► Phase 1 ────────────► Phase 2 ────────────► Phase 3
Foundation            Kill the 4-hour      Revenue engines        Compounding
Week 1–2              mornings              Week 7–12              advantages
                                                                  Q2

Connect, read,        School-order          Reputation engine     Agentic-commerce
shadow. No writes.     pipeline · Bundle     B2B outreach          operations
Read-only dashboard   recombination         Content cadence        Supplier
+ EAN registry v1     Purchase reports      Marketplace relaunch   intelligence
+ shadow demo         Mailbox triage        ESP + cart flows      New segments
                                                                        EU expansion
```

**Every phase is additive.** Phase 0 writes nothing. Phase 1 adds one pipeline. If a phase underperforms, you stop and keep what works.

---

## 🛡️ Guardrails we commit to

| Guardrail | How it works |
| :--- | :--- |
| **Human approval gates** | Invoices, purchase orders, and outbound campaigns require approval for the first 90 days |
| **Full audit log** | Every agent action records who / what / when / why — their own `agents.md` philosophy, applied internally |
| **Secrets in a vault** | Never in chat, never in this repository |
| **GDPR discipline** | B2B role-address outreach under legitimate interest; named-person emails need lawful basis; unsubscribe in every send |
| **Kill switch** | Every automation is a cron job or webhook that can be paused in one command |
| **Reversible by design** | Nothing replaces an existing system; every phase can be rolled back |

---

## 🎨 Built, not described

*[Site Concept Showcase](docs/e-showcase/17-SITE-CONCEPTS.md)* — three scroll-driven site concepts we built against WiseQ's **real 229-product catalog**. Proof that this team ships working software, not slideware.

<table>
<tr>
<td width="33%"><img src="assets/demos/v1-cinematic.png" alt="Cinematic concept — hero headphone render on black"></td>
<td width="33%"><img src="assets/demos/v2-editorial.png" alt="Editorial concept — serif masthead in WiseQ orange on warm paper"></td>
<td width="33%"><img src="assets/demos/v3-webgl.png" alt="Constellation concept — product objects as a museum catalogue with a WebGL component graph"></td>
</tr>
<tr>
<td align="center"><sub><b>01 · Cinematic</b><br>Immersive dark hero<br><a href="https://ai-whisperers.github.io/wiseq-ai-onboarding/site-demos/v1-cinematic/index.html" target="_blank" rel="noopener">run it →</a></sub></td>
<td align="center"><sub><b>02 · Editorial</b><br>Print-inspired whitepaper<br><a href="https://ai-whisperers.github.io/wiseq-ai-onboarding/site-demos/v2-editorial/index.html" target="_blank" rel="noopener">run it →</a></sub></td>
<td align="center"><sub><b>03 · Constellation</b><br>WebGL · bundle spine made visible<br><a href="https://ai-whisperers.github.io/wiseq-ai-onboarding/site-demos/v3-webgl/index.html" target="_blank" rel="noopener">run it →</a></sub></td>
</tr>
</table>

> **Concept 03 is the commercially interesting one.** WiseQ's audit found 77 combinatorial bundle-products (33% of the catalog) whose component mapping lived only in human memory. That concept makes the bundle graph the *visual language* of the storefront — turning the operational weakness into a brand asset, and reusing the same component registry that would drive purchasing.

---

<a id="evidence-base"></a>

## 🔬 Evidence base

This proposal is not built on assumptions. Every claim traces to a verified artifact in this repository.

| Evidence track | Contents | Where |
| :--- | :--- | :--- |
| **Catalog & data-quality audit** | All 230 products, 1,277 images, 228 SKUs audited programmatically | [`data/research-lanes/RESEARCH_CATALOG.md`](data/research-lanes/RESEARCH_CATALOG.md) |
| **Company, registry & history** | Verified entity, domain history, timeline | [`data/research-lanes/RESEARCH_COMPANY.md`](data/research-lanes/RESEARCH_COMPANY.md) |
| **Marketplace & reputation** | bol.com, Amazon.nl, Trustpilot, Scamadviser — verified vs. not-found | [`data/research-lanes/RESEARCH_MARKETPLACES.md`](data/research-lanes/RESEARCH_MARKETPLACES.md) |
| **Marketing, SEO & competition** | 45-page knowledge hub, 12 blog articles, agentic-readiness | [`data/research-lanes/RESEARCH_MARKETING_COMPETITION.md`](data/research-lanes/RESEARCH_MARKETING_COMPETITION.md) |
| **Consolidated dossier** | The one-page cross-cutting synthesis | [`data/research-lanes/WISEQ-DOSSIER.md`](data/research-lanes/WISEQ-DOSSIER.md) |
| **B2B lead-gen (NL)** | 8,673 organizations mapped · 857 with verified emails · methodology and counts only | [`data/leadgen-summary.md`](data/leadgen-summary.md) |
| **Bundle spine** | 114 component SKUs + 25 bundles, referentially validated | [`data/wiseq-bundle-spine.csv`](data/wiseq-bundle-spine.csv) · [`data/wiseq-component-registry.csv`](data/wiseq-component-registry.csv) |
| **OSS catalog** | 31 topics · curated menu by layer (6 JSON stubs empty) | [`docs/c-market/10-OSS-CATALOG-100.md`](docs/c-market/10-OSS-CATALOG-100.md) · [`data/oss/`](data/oss/) |
| **Oct-23 addenda (2–7)** | GS1 €225, certs, UCP, unit economics, engagement mechanics | [`data/README.md`](data/README.md) |
| **Claims ledger** | 47 material claims with status / source / reproduce path | [`data/CLAIMS-LEDGER.md`](data/CLAIMS-LEDGER.md) · [doc 27](docs/f-governance/27-EVIDENCE-INDEX.md) |
| **Data index** | How the attic is organized | [`data/README.md`](data/README.md) |

> 🔒 **Data note — by design, this repository contains no personal contact data.** Our lead-generation research produced large B2B contact datasets (school boards, special-education networks, EU education registers). Those stay private and are handed over directly under GDPR-compliant terms. See [`data/leadgen-summary.md`](data/leadgen-summary.md) for counts, sources, and methodology only.

---

## 📦 What else is in this repository

```
wiseq-ai-onboarding/
├── docs/                    Approach A — see docs/README.md
│   ├── for-rob/ for-kiki/ for-ops/   role packs
│   ├── a-proposal/ b-company/ c-market/
│   ├── d-delivery/ e-showcase/ f-governance/ g-reviews/
│   └── 00-nl/                       NL samenvatting
├── data/                    Evidence attic — see data/README.md
│   ├── CLAIMS-LEDGER.md · leadgen-summary.md · spine CSVs
│   ├── research-lanes/      5 lanes + dossier + 7 addenda
│   └── oss/                 31 topic JSON files (6 stubs)
├── assets/brand/            Logo variants, hero, OG
├── site-demos/              Live concepts — see site-demos/README.md
├── scripts/validate_repo.py CI integrity gate
└── .github/workflows/       validate · gitleaks · zizmor
```

**CI runs on every push** and enforces: every `docs/` link in this README resolves · every `data/oss/*.json` parses and carries the required schema · every bundle component resolves to the registry · no secret patterns anywhere. Reproduce locally with:

```bash
python3 scripts/validate_repo.py
```

---

## 📌 Status

- **2026-10-27** — docs Approach A reorg (role packs + track folders); claim sync (GS1 €225, Trustpilot 13/4.5); new docs 25–27 + `data/README.md`.
- **2026-10-21** — repo created. Research phase complete (company, catalog, marketplaces, marketing, EU market, B2B lead-gen). Awaiting WiseQ's company manual + stack inventory to start Phase 0.
- **2026-10-22** — **bundle spine decoded** from public catalog data — 114 component SKUs + 25 composite bundles fully decomposed (0 unresolved). Reuse-first mapping added (docs/07).
- **2026-10-22** — tooling & integration plan — connector install list, three thin wrappers queued, week-by-week checklist.
- **2026-10-22** — specialist review — 30 independent passes across compliance, risk, engineering and delivery; 12 actions graduate to the build plan.
- **2026-10-22** — compliance map — EN 71 / 62115 / RED (incl. Aug-2025 cybersecurity act), GPSR responsible-person check, Thuiswinkel costs verified.
- **2026-10-22** — OSS catalog expanded to 31 topics / 100 curated repos by layer.
- **2026-10-22** — competitors & deals research — competitor map, deal pricing benchmarks, 6 new opportunities.
- **2026-10-22** — OSS & integrations research — the NL e-com tooling layer is thin (orchestration IS the moat); GS1 EAN fix quantified (€225/yr via 1,000-pack; earlier €854 stacking figure retracted).

**Waiting on WiseQ:** the ~30-page company manual, software inventory, sandbox dataset, and read-only access. Full ask-list: **[06 · Next Steps](docs/a-proposal/06-NEXT-STEPS.md)**

---

## 💬 Response channel

This repository is the collaboration surface. **Open an issue or comment on any document** — we monitor it and respond there. Questions, corrections, and "we already solved this differently" are all welcome; the goal is a plan that fits your reality, not ours.

---

## 📎 Provenance

| | |
| :--- | :--- |
| **Prepared by** | [AI Whisperers](https://github.com/Ai-Whisperers) — AI systems & automation studio |
| **Prepared for** | Rob Nyari & the WiseQ team · [wiseq.nl](https://www.wiseq.nl) |
| **Revision** | 2026-10-27 |
| **Working session** | 2026-10-21 · Grootebroek, NL ([notes](docs/b-company/03-MEETING-NOTES-2026-10-21.md)) |
| **License** | See repository · client-proposal material, citation with attribution welcome |

---

<div align="center">
<sub>Built as a public proof-of-work proposal — every claim here is independently verifiable in minutes.</sub>
</div>

> **Evidence discipline:** every material claim is tracked in [data/CLAIMS-LEDGER.md](data/CLAIMS-LEDGER.md) with source, date, status (verified / inferred / hypothesis / stale), and reproduction path — implemented as the external audit requested (Oct 2026).
