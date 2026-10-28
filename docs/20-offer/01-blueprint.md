<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
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

> **Runs wherever you choose** — on a server you own, on a dedicated server we provide, or on shared capacity we already pay for. Every option includes remote installation, updates, monitoring, and fixes. Credentials live in a vault — never in chat, never in this repo. Every automated action is logged to an audit trail, and **money-touching steps keep human approval** until trust is earned. The four options are laid out in [06 · Next Steps](03-next-steps.md#hosting-options).

---

## 🗓️ The plan at a glance

| | Phase 0 | Phase 1 | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- | :--- |
| **When** | Week 1–2 | Week 3–6 | Week 7–12 | Quarter 2 |
| **Name** | Foundation | Kill the 4-hour mornings | Revenue engines | Compounding advantages |
| **Goal** | Connect, read, shadow | Automate the painful path | Grow | Defend & extend |
| **Writes?** | **No — read-only** | Yes, gated | Yes, gated | Yes, gated |
| **Success test** | Dashboard live, EAN registry v1 | Cycle time 4h → <15min | Invitation engine live + TrustScore defended | UCP traffic + new segments |

**Every phase is additive.** Phase 0 writes nothing. Phase 1 adds one pipeline. If a phase underperforms, you stop — and keep everything that already works.

---

## 🧱 Phase 0 — Foundation *(week 1–2)*

**Goal: connect, read, and shadow. No writes.**

1. **Stack inventory from the 30-page company manual** → map every tool to MCP/API availability (research deliverable: `data/stack-map.md`)
2. **Connectors online**:
   - Shopify Admin API (orders, products, inventory — official API; complements their UCP endpoint)
   - ChannelDock API (inventory, purchase orders — REST, documented)
   - Mailbox (IMAP/SMTP or Gmail MCP) — read-only triage first
   - Bookkeeping (**e-Boekhouden** — confirm API/permissions first; browser-automation MCP only as fallback)
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
| 1 | **Reputation engine** | Post-delivery review invitations (Trustpilot / Kiyoh); Amazon listing refresh — salvage Hero's 4.4★×45 equity, fix Unbreakable's 2.5★ listing; Scamadviser / Webshopchecker remediation | **Every order invited; TrustScore defended** |
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

## 💶 Cost model — split into *your running costs* and *our fee*

These are **two different budgets** and we have separated them deliberately, because
conflating them is how proposals end up misunderstood.

### A. What WiseQ pays — the running costs of the automation layer

| Line | Cost | Notes |
| :--- | :--- | :--- |
| **Infrastructure** | **€0 – €21/mo** | Depends on the hosting option you choose. A real VPS (8 vCPU / 16 GB) is **€16.49–21.49/mo** at Hetzner — EU-hosted, GDPR-friendly, 20 TB traffic included. Options detailed in [06](03-next-steps.md#hosting-options). |
| **AI providers** | **Tier-dependent** | Batch jobs on cheap models, reasoning on strong models. We size this to *your* actual order volume in Phase 0 — it is not a fixed guess. |
| **Shopify API** | €0 | Included in your existing plan |
| **ChannelDock API** | €0 incremental | **Already in your subscription** — the REST API is included from the Voorraad plan (from €45/mo). With 230 products you cannot be on the free tier (100-product cap), so you should already have access. ⚠ *To confirm — see question 7 in [06](03-next-steps.md).* |
| **Bookkeeping API** | €0 if native | **e-Boekhouden** (confirmed vendor) — API where feasible; automation as fallback |
| **bol.com Seller API** | €0 | Free |
| **5X** | €0 or per-plan | ⚠ **Unverified.** We could not find a public API or developer documentation for 5X from outside their login. Phase 0 assumes **CSV export**; if there is no export either, this becomes a browser-automation connector. One of the questions in [06 · Next Steps](03-next-steps.md). |

**And the recurring compliance costs, which are separate from the tech stack:**

| Line | Verified cost | Notes |
| :--- | :--- | :--- |
| **GS1 codes** | **€225/yr** (all SKUs) | Live GS1 NL tariff (until Dec 1 2026): **codepakket 1.000 = €196/yr** covers up to 1,000 GTINs — all 139 needed codes (114 components + 25 bundles), indeed the whole 230-SKU catalog, with headroom. + GS1 Contribution €29/yr (turnover <€1M band; scales with revenue). Earlier repo figures (stacked 10-packs) were both wrong — the 1,000-pack is cheaper. Full correction history in addendum 4. See [08](../30-market/01-oss-integrations.md) and [addendum 4](../../data/research-lanes/RESEARCH-ADDENDUM-4-GS1-AMAZON-COMPETITIVE.md). |
| **Thuiswinkel Waarborg** | **€983–1,759 year 1** | €75 once + €390/yr + revenue-tiered contribution (€518–1,294/yr) + €45/yr per extra platform. **Depends on your turnover — we have asked, not yet known.** |
| **Review platform** | **$0–799/mo** | Trustpilot's tiers cap the monthly *invitation allowance*; a review still only happens if a buyer writes one. Sized in Phase 0. |
| **Lab testing (EN 71 / 62115 / RED)** | **Unknown — get quotes** | ⚠ **The largest uncosted item in this proposal.** Typically hundreds to low-thousands per SKU family. We will not quote a total without real lab figures. |

### B. What AI Whisperers charges

| Line | Cost | Notes |
| :--- | :--- | :--- |
| **Pilot (Phase 0)** | **€3,500 – €5,000** fixed | Stack map, EAN registry v1, shadow demo, read-only dashboard. Two weeks. Credit the full pilot fee against Phase 1 if you continue. |
| **Phase 1** *(school-order pipeline)* | **€8,000 – €12,000** fixed | The flagship automation, bundled with bundle-recombination booking and purchase intelligence. |
| **Phase 2** *(revenue engines)* | **€6,000 – €9,000** fixed | Priced per engine, not as a block — take one, review, take the next. |
| **Phase 3** *(compounding)* | **Quoted per segment** | Each new market or product line is its own decision. |
| **Care plan** (hosting option *a* or *d*) | **From €250/mo** | Hosting is yours; this covers monitoring, updates, fixes, and the monthly ops review. Not charged on options *b* or *c*. |
| **Care plan** (option *b*) | **Included** | One monthly figure, everything included. |
| **Care plan** (option *c*) | **€175/mo** | Reduced rate; see the capacity note below. |

**What sets the number.** Our fee is driven by one variable: how much of the work we can do
against a connector that already exists. ChannelDock and Shopify both have real APIs, which is
why the flagship pipeline is a build rather than an integration. If your bookkeeping package has
no usable API, the browser-automation fallback adds roughly **€1,500 – €3,000** to Phase 1 — we
will tell you before it happens, not after.

**How to compare us.** Doc 09 benchmarks this work at a $3–5k focused pilot and €2–4k/mo
retainer. Our pilot sits inside that range. Our Phase 1 is a build, not a retainer month, so the
total Phase 0 + 1 figure is the honest comparison point — not the monthly rate.

> **On honesty about the AI tier:** the number is scoped to your order volume in Phase 0, not
> assumed. We would rather measure it than guess — and if the measured cost is lower than
> expected, that is information you should have.


<a id="12-month-tco"></a>

## 🧮 12-month total cost of ownership (TCO)

*Every cost in this proposal, in one table, for each hosting option. Year 1 assumes Pilot + Phase 1 + a care plan; Phase 2+ engines are priced per engine and excluded here (take one, review, take the next). Lab testing (EN 71 / 62115 / RED) is **excluded — uncosted until real quotes exist** ([11](../30-market/04-compliance.md)).*

| Cost line | (b) dedicated *(recommended)* | (a) your server + care plan | (c) shared capacity |
| :--- | :--- | :--- | :--- |
| Infrastructure | **€0** — included in option (b) | €198–259 (Hetzner VPS, 8 vCPU/16 GB) | **€0** — included in option (c) |
| AI providers | €480–1,080 (€40–90/mo, sized in Phase 0) | €480–1,080 | €480–1,080 |
| **Our fee — Pilot (Phase 0)** | €3,500–5,000 | €3,500–5,000 | €3,500–5,000 |
| **Our fee — Phase 1** | €8,000–12,000 | €8,000–12,000 | €8,000–12,000 |
| **Our fee — care plan** | **included** | €3,000 (€250/mo) | €2,100 (€175/mo) |
| **GS1 codes** (1,000-pack covers all SKUs + contribution) | €225/yr | €225/yr | €225/yr |
| **Thuiswinkel Waarborg** | €983–1,759 | €983–1,759 | €983–1,759 |
| **12-month TCO** | **€18,688 – €20,064** | **€21,886 – €23,323** | **€20,788 – €22,164** |

**How to read this table.** The ranges come from the fee ranges above and the two open
variables (your turnover class for Thuiswinkel, and your order volume for the AI tier). The
lowest-total option is also the one we recommend — (b) — which is a coincidence of design,
not of pricing.

**What is deliberately not in the number:** lab testing (now bounded: RED €2–8k/product standard, €8–18k notified-body, SAR €4–10k/config — [addendum 3](../../data/research-lanes/RESEARCH-ADDENDUM-3-CERTS-PRICING-MARKET.md); a triage exercise, not catalog-wide testing), Trustpilot (real tariff: $99/mo for 100 invitations ≈ €1,100/yr if the review engine runs — [addendum 3](../../data/research-lanes/RESEARCH-ADDENDUM-3-CERTS-PRICING-MARKET.md)), and any Phase 2 engine.
total materially), Trustpilot's invitation tier (sized in Phase 0, $0–799/mo), and any
Phase 2 engine. A TCO that hides a known-unknown is a sales document, not a decision tool.

**Payback context.** Against the [time-value arithmetic](#-what-the-time-saving-is-worth) —
which itself carries honest caveats — the mid TCO of ~€20k pays back in roughly 2–3 months
*if* the measured baseline lands near the worked example, and materially longer if it lands
near the conservative reading. Phase 0 exists to replace this guess with your number.

## 📈 What the time saving is worth

*This is arithmetic on your own numbers, not a promise. Every input below is yours to correct —
we will re-run it with your purchase manager in Phase 0.*

| Step | Assumption (to confirm) | Value |
| :--- | :--- | :--- |
| School orders per week | from your order book | `_n_` |
| Current human time per order | ~4h (your figure, "sometimes") | 4h |
| Automated share — extraction, stock check, offer, invoice draft | ~85% of the path | 3h 24m |
| **Human time released per order** | | **~2h 35m** |
| Orders per month | `_n_ × 4.3` | — |
| **Hours released per month** | | **~2h 35m × orders** |
| Loaded staff cost | your rate (fully-costed, incl. employer costs) | `€_r_` |
| **Value released per month** | | **hours × `€_r_`** |
| Plus the reported booking time | ~4h/week historic | ~17h/month |
| **Against** | Pilot €3,500–5,000 + Phase 1 €8,000–12,000 + care plan | |

**Worked example — the arithmetic is illustrative; the premise is ours, not yours.**
Taking **12 school orders a week** and **€45/hour fully-loaded**, at **2h35m of
admin time per order** that is ≈ **134 hours/month ≈ €6,000/month**, against a Phase 0+1
investment of €11,500–17,000 → **payback in roughly 2–3 months.**

> ⚠ **Two honest caveats about that example.**
> 1. **The 2h35m-per-order figure is our assumption, not a measured baseline.** The repo
>    separately records ~4h/**week** of school-order work, which over 52 orders/month is
>    ~20 min/order — *not* 2h35m. Those two numbers disagree by a factor of seven. We
>    flag the conflict rather than pick the flattering one. **Phase 0 measures the real
>    baseline**, and the payback is recalculated from it before anyone relies on it.
> 2. **The payback range is 2–3 months, not "inside two months."** At the top of the
>    investment range it takes 2.3 months. We would rather quote you the slower number.
>
> **The three numbers we need to firm this up:** orders per week, your fully-loaded hourly cost,
and the true average time per order (not the worst case). We are asking because the difference
between "sometimes 4 hours" and a measured average is the difference between a business case and
an anecdote.

**What we are not claiming:** none of the above counts revenue gained from reviews or content.
Those are upside we have not modelled, and we would rather show you a conservative payback we
can defend than a number we cannot.

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

## 📌 In short

One 24/7 AI-operations layer, built on open-source [Hermes Agent](https://github.com/NousResearch/hermes-agent) plus MCP connectors, sitting **across** WiseQ's existing tools rather than replacing any of them. Every phase is additive, reversible and measurable — nothing here is a rip-and-replace, and the cheapest entry point ([doc 06](03-next-steps.md)) costs WiseQ nothing but a few answers and a sandbox.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Automation Backlog](02-automation-backlog.md)** | The scored backlog this blueprint is built from |
| **[Devops Masterplan](../40-build/04-devops.md)** | CI/CD, storage and SLOs behind the stack |
| **[Tooling Mcp Installs](../40-build/02-tooling-mcp.md)** | The concrete connectors, per operation |
| **[Who we are](../70-showcase/03-who-we-are.md)** | People, roles, Dutch-language honesty |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
