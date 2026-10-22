<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track A · Document 04* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# WiseQ AI Stack — Blueprint

*The proposal: one orchestrated AI-operations layer across WiseQ's existing tools. Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) (open-source, provider-agnostic) + MCP connectors. Nothing rips-and-replaces; every phase is additive and measurable.*

## 📐 Architecture (target state)

```
┌───────────────────────────────────────────────────────────────────────┐
│                      THE AI OPERATIONS LAYER                          │
│         24/7 · reversible · audited · WiseQ-owned data                │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  orchestrator · memory · cron · kanban · skills · subagents    │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────┬───────────────────────────────────┘
                                    │
        ┌───────────┬───────────┬───┴─────┬───────────┬───────────┐
        ▼           ▼           ▼         ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌────────┐ ┌────────┐ ┌─────────┐ ┌────────┐
   │ Mailbox │ │ Book-   │ │Channel │ │ Shopify│ │ bol.com │ │ Web &  │
   │ IMAP/   │ │ keeping │ │ Dock   │ │ Admin  │ │ + 5X    │ │ market │
   │ SMTP    │ │ offers  │ │ stock &│ │ orders │ │ seller  │ │ intel  │
   │ (email) │ │ invoice │ │ pur-   │ │ UCP    │ │ APIs    │ │ scrape │
   │         │ │ relation│ │ chase  │ │        │ │ ads     │ │ leadgen│
   └────┬────┘ └────┬────┘ └───┬────┘ └────────┘ └─────────┘ └────────┘
        │           │          │
        └───────────┴──────────┴───► every action logged · money steps gated
```

| Layer | What it does | Reversal path |
| :--- | :--- | :--- |
| **Orchestrator** | Routes work, holds memory, schedules recurring jobs | Pause the cron job |
| **Connectors** | Read/write access to tools that already exist | Revoke the API token |
| **Approval gates** | Human sign-off on invoices, POs, campaigns | Flip a config flag |
| **Audit log** | Who / what / when / why, permanently recorded | — (append-only) |

> **Runs on WiseQ's existing 24/7 office machine or a €20/mo VPS.** Credentials live in a vault — never in chat, never in this repo. Every automated action is logged to an audit trail, and **money-touching steps keep human approval** until trust is earned.

---

## 🗓️ The plan at a glance

| | Phase 0 | Phase 1 | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- | :--- |
| **When** | Week 1–2 | Week 3–6 | Week 7–12 | Quarter 2 |
| **Name** | Foundation | Kill the 4-hour mornings | Revenue engines | Compounding advantages |
| **Goal** | Connect, read, shadow | Automate the painful path | Grow | Defend & extend |
| **Writes?** | **No — read-only** | Yes, gated | Yes, gated | Yes, gated |
| **Success test** | Dashboard live, EAN registry v1 | Cycle time 4h → <15min | Invitation engine live + TrustScore held ≥4.4 | UCP traffic + new segments |

**Every phase is additive.** Phase 0 writes nothing. Phase 1 adds one pipeline. If a phase underperforms, you stop — and keep everything that already works.

---

## 🧱 Phase 0 — Foundation *(week 1–2)*

**Goal: connect, read, and shadow. No writes.**

1. **Stack inventory from the 30-page company manual** → map every tool to MCP/API availability (research deliverable: `data/stack-map.md`)
2. **Connectors online**:
   - Shopify Admin API (orders, products, inventory — official API; complements their UCP endpoint)
   - ChannelDock API (inventory, purchase orders — REST, documented)
   - Mailbox (IMAP/SMTP or Gmail MCP) — read-only triage first
   - Bookkeeping (depends on vendor — Exact Online/nl.: API or browser-automation MCP fallback)
   - bol.com Seller API + 5X exports
3. **Canonical product registry (the EAN spine)**: EAN ↔ SKU ↔ bundle-components mapping table — the single source of truth that fixes the "long human trail" problem. Seeded from ChannelDock + Shopify + supplier invoices.
4. **Shadow demo**: school-order pipeline running on dummy data, visualized — as promised in the meeting.

| Phase-0 deliverable | What it proves |
| :--- | :--- |
| **Live read-only dashboard** | The data is real and readable — orders, stock, reviews, channel drift |
| **Stack map** (`data/stack-map.md`) | Every tool in the manual, mapped to its connector availability |
| **EAN registry v1** | The canonical EAN ↔ SKU ↔ component spine exists and validates |
| **Shadow demo** | The school-order pipeline running on dummy data, as promised in the meeting |

## ⚡ Phase 1 — Kill the 4-hour mornings *(week 3–6)*

**School-order pipeline (the flagship automation):**

```
email arrives → agent extracts order (school, products, qty)
  → checks/matches relation in bookkeeping (creates draft if new)
  → generates offer from price rules (staffelprijzen auto-applied)
  → sends for human review (one click) → on approve: invoice + booking
  → books correct component EANs into ChannelDock
  → tracks shipment → follows up
```

Also in this phase:
- **Bundle recombination engine**: component↔bundle graph in the EAN registry; when combos sell out, the agent books "regular charger + regular cable" movements automatically, keeping ChannelDock clean and purchase data true
- **Purchase-intelligence reports**: replace the manual 6-month-per-EAN Excel with a nightly job (actual-product sales basis, per the founder's own framing)
- **Mailbox triage**: classification + draft replies for common streams (order requests, school questions, reviews, spam) — human sends

**Measure:** school-order cycle time (target: 4h → <15min human touch), purchase-report freshness (weekly-manual → daily-auto), booking errors.

## 💰 Phase 2 — Revenue engines *(week 7–12)*

| # | Engine | What it does | Target |
| :--- | :--- | :--- | :--- |
| 1 | **Reputation engine** | Post-delivery review invitations (Trustpilot / Kiyoh); Amazon listing refresh — salvage Hero's 4.4★×45 equity, fix Unbreakable's 2.5★ listing; Scamadviser / Webshopchecker remediation | **25 → 250+ reviews** |
| 2 | **B2B outreach** | Campaigns on the 857-org NL contact list + whale networks; event-aware personalization (school anniversaries, jubileums — as sketched in the meeting); unsubscribe / AVG compliant | A working B2B pipeline |
| 3 | **Content cadence** | Knowledge-hub pages + blog at scale (today ~1/month manually; architecture supports 1/week); listicle/PR outreach to the review sites owning head terms; newsletter flows (no ESP today — pick one, wire abandoned-cart + B2B nurture) | 1 → 4+ per month |
| 4 | **Marketplace relaunch** | Amazon EU expansion via the existing seller account; price harmonization across bol / shop / Amazon from one rule sheet | One price rule sheet |

## 🌱 Phase 3 — Compounding advantages *(quarter 2)*

| Advantage | Detail | Why it compounds |
| :--- | :--- | :--- |
| **Agentic-commerce operations** | UCP traffic analytics (who's querying their MCP endpoint), `agents.md` freshness automation, structured-data QA | Extends a lead WiseQ already has — most NL retailers have nothing here |
| **Supplier intelligence** | Price monitoring across Chinese providers ("which is cheapest right now" — from the meeting), quote comparison, MOQ tracking | Margin defense becomes continuous, not quarterly |
| **New segments** *(from the meeting)* | Screen-time-control service layer on tablets (manufacturer preinstall path); elderly hearing-assist line evaluation | Opens product lines that don't compete on price |
| **EU expansion** | Flanders register pull, DACH via Amazon.de, FR datasets already banked | Data already collected — this is activation, not research |

## 💶 Cost model (honest)

| Line | Cost | Notes |
| :--- | :--- | :--- |
| **Infrastructure** | **€0 – €20/mo** | Their existing 24/7 office machine (already paid) **or** a €20/mo VPS |
| **AI providers** | **~€90/mo-class** | The same tier discussed in the meeting. Batch jobs on cheap models, reasoning on strong models, `--deliver-only` hooks for zero-LLM alerts |
| **Shopify API** | €0 | Included in their existing plan |
| **ChannelDock API** | €0 | Already in their subscription |
| **Bookkeeping API** | Vendor-dependent | Exact Online / nl. — API or browser-automation fallback |
| **bol.com Seller API** | €0 | Free |
| **Our engagement** | Phased, fixed scope | Fixed deliverables per phase. **WiseQ owns the repo and all data.** |

> Most connector surfaces are **already-paid** — the marginal cost of the orchestration layer is the AI tier plus a small amount of infrastructure.

## 🛡️ Guardrails

| Guardrail | Commitment |
| :--- | :--- |
| **Human approval gates** | Invoices, purchase orders, and outbound campaigns require human approval for the first 90 days |
| **Full audit log** | Every agent action records who / what / when / why — WiseQ's own `agents.md` philosophy, applied internally |
| **Secrets in a vault** | Never in chat, never in this repository |
| **GDPR discipline** | B2B role-address outreach under legitimate interest; named-person emails need a lawful basis; unsubscribe in every send |
| **Kill switch** | Every automation is a cron job or webhook that can be paused in one command |
| **Ownership** | WiseQ owns the repository, the data, and the credentials. We build inside your estate, not ours. |

---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Automation Backlog](05-AUTOMATION-BACKLOG.md)** | The scored backlog this blueprint is built from |
| **[Devops Masterplan](15-DEVOPS-MASTERPLAN.md)** | CI/CD, storage and SLOs behind the stack |
| **[Tooling Mcp Installs](13-TOOLING-MCP-INSTALLS.md)** | The concrete MCP installs, per operation |
| **[Site Concepts](17-SITE-CONCEPTS.md)** | Three working site concepts built against the real catalog |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
