# WiseQ AI Stack — Blueprint

*The proposal: one orchestrated AI-operations layer across WiseQ's existing tools. Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) (open-source, provider-agnostic) + MCP connectors. Nothing rips-and-replaces; every phase is additive and measurable.*

## Architecture (target state)

```
                         ┌──────────────────────────────────────┐
                         │        HERMES AGENT (24/7)           │
                         │  orchestrator + memory + cron +      │
                         │  kanban + skills + subagents         │
                         └───────────────┬──────────────────────┘
         ┌──────────┬──────────┬─────────┼──────────┬───────────┐
         ▼          ▼          ▼         ▼          ▼           ▼
   Mailbox/SMTP  Bookkeeping ChannelDock  Shopify    bol.com/5X   Web/Research
   (email MCP)   (offers/    (stock,     (Admin     (seller      (scraping,
                  invoices,  purchase,   API/UCP)   APIs, ads)   monitoring,
                  relations) recomb.)                            leadgen)
```

Runs on their existing 24/7 office machine or a €20/mo VPS. Credentials in a vault (Bitwarden Secrets), never in chat. Every automated action logged to an audit trail; money-touching steps (invoices, purchase orders) keep human approval until trust is earned.

## Phase 0 — Foundation (week 1–2)

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

**Deliverables:** live dashboard (read-only), stack map, EAN registry v1, shadow demo.

## Phase 1 — Kill the 4-hour mornings (week 3–6)

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

## Phase 2 — Revenue engines (week 7–12)

1. **Reputation engine**: post-delivery review invitations (Trustpilot/Kiyoh), Amazon listing refresh (salvage Hero's 4.4★×45 equity; fix Unbreakable's 2.5★ listing), Scamadviser/Webshopchecker remediation. Target: 25 → 250+ reviews.
2. **B2B outreach on the lead-gen data**: the 857-org NL contact list + whale networks; event-aware personalized email campaigns (school anniversaries, jubileums — exactly what was sketched in the meeting), with unsubscribe/AVG compliance.
3. **Content cadence**: knowledge-hub pages + blog at scale (they do ~1/month manually; the architecture supports 1/week), listicle/PR outreach to the review sites that own head terms, newsletter flows (no ESP today — pick one, wire abandoned-cart + B2B nurture).
4. **Marketplace relaunch**: Amazon EU expansion via existing seller account; price harmonization across bol/shop/Amazon from one rule sheet.

## Phase 3 — Compounding advantages (quarter 2)

- **Agentic-commerce operations**: UCP traffic analytics (who's querying their MCP endpoint), agents.md freshness automation, structured-data QA — extend the lead they already have
- **Supplier intelligence**: price monitoring across Chinese providers (the "which is cheapest right now" question from the meeting), quote comparison, MOQ tracking
- **New segments (from the meeting)**: screen-time-control service layer on tablets (with the manufacturer preinstall path), elderly hearing-assist line evaluation
- **EU expansion**: Flanders register pull, DACH via Amazon.de, FR datasets already banked

## Cost model (honest)

- **Infra**: their 24/7 machine (already paid) or €20/mo VPS
- **AI**: €90/mo-class provider plan(s) — the same tier discussed in the meeting; batch jobs on cheap models, reasoning on strong models, `--deliver-only` hooks for zero-LLM alerts
- **Connectors**: Shopify API (included in plan), ChannelDock API (in their subscription), bookkeeping API (vendor-dependent), bol Seller API (free) — mostly already-paid surfaces
- **Our engagement**: phased build with fixed deliverables per phase; WiseQ owns the repo and all data

## Guardrails

- Human approval gates: invoices, purchase orders, outbound campaigns (first 90 days)
- Full audit log of every agent action (who/what/when/why) — their own agents.md philosophy applied internally
- Secrets in vault, never in chat or repo
- GDPR: B2B role-address outreach under legitimate interest; named-person emails need lawful basis; unsubscribe in every send
- Kill switch: every automation is a cron job or webhook that can be paused in one command
