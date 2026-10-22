# WiseQ × AI Whisperers — AI Transformation Onboarding

**Public working repo for WiseQ** ([wiseq.nl](https://www.wiseq.nl)) — the Dutch kids-technology brand from Grootebroek — and its AI/automation transformation program with [AI Whisperers](https://github.com/Ai-Whisperers).

**Purpose:** everything we know about WiseQ, everything we've already researched and built, and the complete blueprint for the AI stack we propose to build together. Built for **Rob Nyari** and the WiseQ team to review.

> 🔒 **Data note:** this repo deliberately contains **no personal contact data**. Our lead-generation research produced large B2B contact datasets (school boards, special-education networks, EU education registers). Those stay private and are handed over directly under GDPR-compliant terms — see `data/leadgen-summary.md` for counts, sources, and methodology only.

## Quick links

| Doc | What's in it |
|---|---|
| [Company profile](docs/01-COMPANY-PROFILE.md) | Who WiseQ is — verified registry, timeline, channels, catalog, tech stack |
| [Meeting notes 2026-10-21](docs/03-MEETING-NOTES-2026-10-21.md) | Business intel from our first working session |
| [AI stack blueprint](docs/04-AI-STACK-BLUEPRINT.md) | **The main proposal** — the full stack, phase by phase |
| [Automation backlog](docs/05-AUTOMATION-BACKLOG.md) | Every automation opportunity we found, scored by ROI |
| [What we've done so far](docs/02-WHAT-WE-DID.md) | Research dossier, market scan, lead-gen — with artifacts |
| [PY → WiseQ transfer](docs/07-PY-TRANSFER-WISEQ.md) | Capabilities from our Paraguay build that solve WiseQ problems — incl. the decoded **bundle spine** |
| [Next steps](docs/06-NEXT-STEPS.md) | What we need from WiseQ to start Phase 0 |
| [OSS & integrations](docs/08-OSS-INTEGRATIONS.md) | Bol/Shopify/GS1/feeds OSS landscape, EAN fix costs (€732), NL trust marks, school collectives |
| [Competitors & deals](docs/09-COMPETITORS-DEALS.md) | Real competitor map (iClever/Puro/Alpine/Heutink), deal pricing benchmarks, new opportunities |
| [OSS catalog — 100 repos](docs/10-OSS-CATALOG-100.md) | 31 topics · 420 found · **100 curated** by stack layer, adopted additions (UVdesk, Umami, BillionMail, QuestPDF) |
| [Compliance & regulatory](docs/11-COMPLIANCE-REGULATORY.md) | EN 71/62115/RED (2025 cyber layer), GPSR, Thuiswinkel €465/yr, cert-evidence library plan |
| [50-hat analysis](docs/12-FIFTY-HATS.md) | 15 WiseQ + 15 PY + **20 AIW meta-layer hats** — liability, bol health, CONATEL, Commerce-OS productization, 24-month arc |
| [Tooling & MCP installs](docs/13-TOOLING-MCP-INSTALLS.md) | Verified Hermes catalog inventory, per-op MCP install lists (Shopify/bol/e-Boekhouden/Trustpilot wrappers), PY docker-compose, week-1 checklist |
| [Hermes/Jev + AIW reuse](docs/14-HERMES-JEV-AIW-REUSE.md) | **Jev verdict** (keep, route the ops lanes), Hermes optimization checklist, **full AIW asset inventory** (7 org + 81 personal repos), reuse-first stack |
| [DevOps masterplan](docs/15-DEVOPS-MASTERPLAN.md) | CI/CD upgrades (zizmor/gitleaks/branch-protection), storage & DB architecture (Neon + DuckDB + R2), SLOs, phased masterpiece checklist |

## The one-paragraph pitch

WiseQ already runs a remarkably modern stack (Shopify with a custom B2B layer, ChannelDock + 5X, agentic-commerce endpoints). The gap isn't tools — it's **orchestration**: school orders eat 4-hour mornings, bundle stock is re-tracked by hand in Excel, review volume is thin, and marketing runs below the site's potential. We propose a single 24/7 AI-operations layer (Hermes Agent) that connects the mailbox, bookkeeping, ChannelDock, and the webshop — cutting the school-order process from ~4 hours to minutes, making EAN-based purchasing automatic, and running reputation/content/outreach continuously. Most pieces exist as MCP-connectable services already.

## Status

- 2026-10-21: repo created. Research phase complete (company, catalog, marketplaces, marketing, EU market, B2B lead-gen). Awaiting WiseQ's company manual + stack inventory to start Phase 0.
- 2026-10-22: **bundle spine decoded** from public catalog data — 114 component SKUs + 25 composite bundles fully decomposed (0 unresolved); artifacts in `data/wiseq-bundle-spine.csv` + `data/wiseq-component-registry.csv`. PY→WiseQ transfer doc added (docs/07).
- 2026-10-22: Hermes/Jev + AIW reuse inventory — Jev verified live (enabled, zai-lane inert by design, grid documented), fallback-add flagged as top fix; AIW assets mapped: saskia-app (SIFEN backend), gaby-client-engine (outreach), ops-toolkit (VPS), hermes observability lib, telescope-ai (MCP pattern); reuse-first stack defined.
- 2026-10-22: tooling & MCP plan — live catalog audit (27 enabled / square+paypal+n8n-official available), MCP install lists both ops (P0: Shopify Admin custom app + Evolution API MCP), PY docker-compose defined, 3 thin wrapper builds queued (e-Boekhouden, bol, Trustpilot).
- 2026-10-22: 50-hat analysis — 3 domains incl. first-ever AIW meta-layer analysis (Commerce-OS productization, case-study economics, dual-jurisdiction privacy); new grounded findings: EU Product Liability Directive (kids products), CONATEL homologation for PY Bluetooth imports; 12 actions graduate to kanban.
- 2026-10-22: compliance map — EN 71/EN 62115/RED (incl. Aug-2025 cybersecurity act, GPS trackers in scope), GPSR responsible-person check, Thuiswinkel Waarborg costs verified (€75 + €390/yr), cert-evidence library per SKU family. Original 5 research-lane reports added under data/research-lanes/.
- 2026-10-22: OSS catalog expanded to 31 topics / 100 curated repos by layer — adopted additions: UVdesk 19.6k★ (school-order inbox as tickets), Umami 39.5k★ (cookieless analytics), BillionMail 15.9k★ (self-hosted ESP), QuestPDF 14.2k★ (slips/labels), open-seo-mcp 6.4k★.
- 2026-10-22: competitors & deals research — iClever = #1 US kids-audio (Euromonitor), Alpine = NL school-oorkap A-brand, Heutink ICT = totaalleverancier incumbent; deal benchmarks (pilot $3-5k / retainer €2-4k / outcome-priced per order); OSS wave 2 confirms gaps = moat; 6 new opportunities incl. bol CPOP track.
- 2026-10-22: OSS & integrations research — 10 GitHub topics (~115 repos) proving the NL e-com tooling layer is thin (orchestration IS the moat); GS1 EAN fix quantified (~€732 one-off for 114 components + 25 bundles); bol Retailer API surface mapped; Thuiswinkel Waarborg + Trustpilot trust plan; school inkoopcollectieven identified as B2B channel 2.0.
