<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track B · Document 07* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# PY → WiseQ: Everything We Built for Paraguay That WiseQ Should Get

*2026-10-22. While building our Paraguay dropshipping operation's research stack, we produced capabilities that solve WiseQ problems directly. This document maps each one — and delivers the artifacts we already prepared from WiseQ's own public data.*

## 1. 🧭 The headline: we decoded the bundle spine

WiseQ's public catalog encodes Rob's exact bundle problem in its SKUs. Analysis of the 230-product Shopify export:

- **114 component SKUs** (pure numeric: 1xx chargers, 2xx cables, 3xx charge-sets, 4xx audio)
- **25 composite bundles** written as component sums — `119+207` = charger 119 + cable 207; `115+240`, `117 + 240`, `234+121`…
- **All 25 decompose cleanly, zero unresolved components.**
- **19 of 25 bundles have inconsistent formatting** (spacing around `+`) — a silent data-quality bug in the making: `119+207` vs `117 + 240` sort and match differently.

**Delivered artifacts (in `data/`):**
- `data/wiseq-bundle-spine.csv` — all 25 bundles decomposed into components, with a `needs_format_fix` flag
- `data/wiseq-component-registry.csv` — the 114-component registry

**What this enables on day one of a collaboration:** the EAN spine becomes mechanical. Assign EANs to the 114 components first (one-time), then every bundle's identity = ordered tuple of component EANs. When ChannelDock reports "component 207 out of stock," the agent propagates: 207 → 3 bundles containing it → pause those listings everywhere (shop + bol + Amazon) in minutes, not mornings. This is the exact "bundle goes out of stock, which cables do I still have" problem Rob described — solved at the SKU layer, before any AI.

## 2. 🕰️ The PY research stack, mapped to WiseQ

| PY capability (py-dropship-ai) | WiseQ application |
|---|---|
| **Agente CDE** — nightly hierarchical scraping (open sites first, stealth for bot-walled) + price-dispersion index | WiseQ's competitors (BuddyPhones, Puro, educatheek wholesale) scraped nightly → price-position dashboard per SKU; alert when a competitor undercuts a WiseQ listing |
| **Supplier price/stock monitoring** with changedetection.io pattern (35k★, no parser needed) | Watch ChannelDock feed + bol offer pages for stock events; watch supplier (China) price shifts on reorder SKUs |
| **Canonical product table + EAN discipline** (the anti-0/230 rule) | Already WiseQ's biggest gap — the bundle spine above is the concrete fix |
| **Evals for the WhatsApp/sales agent** (100 labeled conversations, regression-tested) | Same discipline for WiseQ's school-order inbox: a labeled set of real school emails/orders → the order-parsing agent is tested, not vibes-checked |
| **Observability (every agent decision logged with cost)** | Cost-per-order-processed visible; the "4-hour mornings" get a number attached before/after |
| **Dynamic pricing with margin floor** | bol repricing within floor/ceiling rules — vs. 312-article bol drift (shop 230 vs bol 312: 82 listings need audit) |
| **RAG policy engine** | School-order terms (Bestel op factuur, staffelprijzen tiers, proefexemplaar rules) answered consistently by an agent, not from Rob's head |
| **Review engine (post-sale D+1 ask)** | Trustpilot 4.5 but only 13 reviews (Oct 23), zero automated invitations — the engine we designed for PY plugs straight in |
| **MCP-server exposure of catalog** | WiseQ already runs UCP + MCP shopping server (we verified it live) — our stack speaks that protocol natively; agents can place/know orders machine-to-machine |
| **Privacy agent (consent registry, DSR handling)** | GDPR is already law for WiseQ (NL) — same agent, EU flavor |
| **Failure-mode finance rules** (kill criteria, CPA ≤ 50% margin, runway separation) | Per-SKU profitability floors from 5X data → auto-pause losers instead of silent margin bleed |
| **Seasonality calendar** | NL school calendar: back-to-school Aug, Sinterklaas Dec, Christmas — procurement timed to it |

## 3. 💬 New insights from the PY work that WiseQ should hear

1. **Bol drift is measurable now**: 312 bol articles vs 230 shop products — at least 82 listings live only on bol (or are stale ghosts). First automation: nightly shop↔bol reconciliation report. Zero risk, immediate clarity.
2. **The 5X + ChannelDock data stays where it is — we add the missing layer**: a canonical SQLite/Postgres spine joining Shopify SKUs ↔ bol offers ↔ ChannelDock stock ↔ 5X margin. Four systems, one table, one truth. (The PY repo's `data/` layer is the template.)
4. **Amazon cleanup is a batch job**: 2020-era ASINs (B08G/B08P) with 2.5★ dud listing — a one-week agent project: audit, merge or kill, refresh content, reclaim the 4.4★ store average.
5. **The agentic edge compounds**: WiseQ's UCP/MCP endpoints are ahead of the market — connecting them to an orchestration layer (Hermes) turns "machine-readable" into "machine-OPERATED": orders in, labels out, stock propagated, exceptions escalated.

## 4. 📦 Ready-to-run first week (what we can prepare before any access)

No credentials needed — all preparable now:

- [ ] **Bundle-spine import script** — reads the two CSVs, emits the canonical table DDL + seed rows (Shopify SKU ↔ components ↔ bundle membership)
- [ ] **Nightly competitor price watch** — BuddyPhones/Puro/educatheek product pages + changedetection.io config export
- [ ] **Shop↔bol drift report generator** — pulls public bol brand page + Shopify products.json, diffs, emails a Monday report
- [ ] **School-order eval set v0** — 50 labeled example orders (from the public order-flow docs) for testing the parsing agent
- [ ] **Review-invitation flow spec** — post-delivery D+1 email/WhatsApp ask (Trustpilot invite via public API)
- [ ] **Amazon audit checklist** — per-ASIN: title/images/bullets/price vs shop, flag mismatches

With read-only access (later): ChannelDock + 5X joins, live stock propagation, margin floors, and the WhatsApp school-order closer.

## 5. 🧱 Why this pattern works

The PY operation forced us to build retailer-grade automation with zero budget and zero legacy — the same constraints as WiseQ's home-office operation, one person, many channels. Everything was designed agent-first: every component speaks API/CLI, every decision is logged, every data leak (the 0/230 EAN lesson) becomes a structural rule instead of a cleanup project. WiseQ gets the benefit of that discipline without paying for the scar tissue.

---

## 📌 In short

We built these systems for a harder problem — a multi-branch retail operation in Paraguay with the same school-order and stock-truth table shape. **The bundle spine is the headline: 25 bundles decoded into 114 components**, which is precisely the mapping WiseQ does by hand today. Transfer is a capability, not a codebase dump; what moves is the pattern plus the connectors.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Automation Backlog](../a-proposal/05-AUTOMATION-BACKLOG.md)** | Where each transferred component lands |
| **[Hermes Jev Aiw Reuse](../d-delivery/14-HERMES-JEV-AIW-REUSE.md)** | The full asset inventory behind this transfer |
| **[Company Profile](01-COMPANY-PROFILE.md)** | The WiseQ problems these components solve |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
