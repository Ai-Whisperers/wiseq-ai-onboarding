# C · Deal Structure & Leverage — what we'd be doing, and what it's worth

> **⚠ INTERNAL — AI Whisperers only. NOT a client-facing document.**
> Written 2026-10-22. Companion to `A-COST-BASELINE-AUDIT.md` and
> `B-COST-REALITY.md`.
> Visibility: `internal` · **All AIW fee figures are TBD** per Ivan's instruction.
> This doc analyses *structure, leverage and value*; it does **not** set a price.

---

## 0. Executive frame

**What we are actually offering:** a 24/7 agent-operations layer over an estate
WiseQ already pays for. The *client's* marginal cost is genuinely near zero
(Shopify API €0, bol API €0, ChannelDock €0 — all already-paid subscriptions).
**Our** marginal cost is labour + AI tokens. Therefore:

> **The leverage is real, but it is almost entirely unpriced in the current repo.**
> That is the opportunity and the risk in one sentence.

---

## 1. What we would actually be doing — work decomposition

Mapped to the repo's four phases, with the **hidden labour** made explicit. These
effort estimates are the substance of the deal and were absent from every doc.

### Phase 0 — Foundation (repo says "week 1–2")

| Deliverable | Hidden work nobody costed | Dependency |
|:--|:--|:--|
| `data/stack-map.md` | Read a 30-page manual, identify every tool, test each for API/MCP availability. ~~ChannelDock + 5X have no public API~~ **RETRACTED — see `RETRACTION-R1-CHANNELDOCK.md`.** ChannelDock has REST API + webhooks (plan-gated, from Voorraad €45/mo); FiveX has a documented bol.com API link. | Blocks everything |
| EAN registry v1 | Parse Shopify + ChannelDock + supplier invoices; reconcile; design the canonical schema. **This is the keystone — 3 of 4 🔥 items depend on it.** | Blocks Phase 1 |
| Shadow school-order demo | The "visually, ah, nice" moment. Requires anonymised order samples + the offer→invoice flow. **Highest-risk demo: it must work on data we don't control.** | Needs client data |
| Read-only dashboard | 4 connectors × read paths. | Needs tokens |

**Phase 0 risk — CORRECTED 2026-10-22.** An earlier version of this document
claimed ChannelDock and 5X had no API and that Phase 1 might be blocked. **That was
wrong and is retracted** — see `RETRACTION-R1-CHANNELDOCK.md`. Both have APIs.
The real Phase 0 questions are commercial, not technical: **which ChannelDock plan
is WiseQ on, and do they already pay for the PIM module?** See §5a.

### Phase 1 — Kill the 4-hour mornings (repo says "week 3–6")

| Deliverable | Hidden work | Commercial note |
|:--|:--|:--|
| School-order pipeline | Email parse → relation match → offer w/ staffelprijzen → **human approval** → invoice → ChannelDock booking → shipment tracking. 8 stages, 2 of which need browser automation. | The flagship. The single clearest "before/after". |
| Bundle recombination engine | Component↔bundle graph; automatic component movements on combo sellout. Needs clean EAN base first. | Kills the "data gets polly" problem |
| Purchase-intelligence nightly job | Replace 6-month-per-EAN Excel. Straightforward ETL once EAN exists. | Lowest effort, highest client relief |
| Mailbox triage | Classification + draft replies, human sends. | Founder explicitly asked for this |

### Phase 2 — Revenue engines (repo says "week 7–12")

Review engine (25 → 250+ reviews), B2B outreach on the 857-org list, content
cadence (1 → 4+/mo), marketplace relaunch + Amazon EU expansion.

### Phase 3 — Compounding (quarter 2)

Agentic-commerce ops on their live UCP endpoint, supplier intelligence, new
segments, EU expansion activation.

### Effort reality check

Repo allocates **~14 weeks** to Phases 0–1 and **~6 weeks** to Phase 2. For a
build that includes: 6+ connector integrations, 2 browser-automation adapters for
APIs that don't exist, a canonical data registry, an approval-gated pipeline, a
nightly ETL, a shadow demo, and a dashboard — **14 weeks is optimistic for one
senior person with AI assistance.** This matters because the price anchors to
effort; underestimating effort at a fixed price destroys the margin that the
"50–70% gross margin" claim depends on.

### 5a. ⚠ CORRECTED — the browser-automation adapters are not needed

The paragraph above originally said *"2 browser-automation adapters for APIs that
don't exist."* **That was wrong.** Verified 2026-10-22:

- **ChannelDock ships a REST API + webhooks**, included from the **Voorraad plan
  (from €45/mo excl. VAT)**; excluded from the free tier.
- **FiveX has a first-party "API koppelingen" section** consuming bol.com
  Client ID/Secret, covering analytics, orders, ads, repricing, inventory and
  finance exports.
- ChannelDock additionally lists **FiveX as its own integration**, and has
  **213+ live integrations** including Shopify and bol.com.

**Full retraction and evidence: `RETRACTION-R1-CHANNELDOCK.md`.**

**Revised effort view:** the two hardest connectors are *easier* than assumed —
native APIs, not browser automation. That **reduces** Phase 0–1 effort and risk.
The genuine open questions are now commercial (R1b, R1c), not technical.

**New commercial line item:** if WiseQ is not already on Voorraad+, a plan upgrade
is **new spend** (from €45/mo excl. VAT) that appears nowhere in any of the 17
documents.

---

## 2. Value to WiseQ — what it is actually worth to them

The repo never quantifies the client's savings. It has to, because outcome-based
pricing needs it.

| Source | Repo evidence | Quantification |
|:--|:--|:--|
| **School-order mornings** | "4 hours in a single morning" + "~4h/week booking time historically" (founder-confirmed, `docs/03`) | **~8–17 hrs/week** recovered. At NL loaded staff cost, material. |
| **Purchase manager Excel** | 6-month rolling average per EAN, by hand, **one costly error/year** (`docs/03`) | Hours/week + error avoidance |
| **EAN backfill** | 0/230 SKUs carry EAN; **77 bundles (33%) have no component map** | **€732 one-off** to unblock every marketplace + purchasing workflow |
| **Review engine** | Trustpilot 4.4/5 but **25 reviews**; target 250+ | Conversion + marketplace ranking |
| **Scamadviser Trust Score 0** | Conversion suppressor on their own storefront | Direct revenue effect |
| **Bundle data pollution** | Founder's words: *"data gets polly"* | Purchasing decisions made on bad data |
| **B2B outreach** | 857 verified-org list already built | New pipeline, hard to value ex-ante |
| **Amazon EU expansion** | Account already carries .de/.fr/.it/.es listings | Activation of a sunk asset |

**The strongest single number: ~8–17 hours/week of founder/purchase-manager time.**
That is the honest anchor. Everything else is either already-paid or speculative.

---

## 3. Our leverage — the assets nobody else has

| # | Leverage | Why it's real | Defensibility |
|:--|:--|:--|:--|
| **L1** | **We already did the research, unpaid.** 17 docs, 5 research lanes, 230-product audit, 1,277 images, 114-component bundle spine, 25 bundles decoded, 857-org lead list, 100-repo OSS catalog, 68 hat passes, 3 built site demos. | This is weeks of work, already spent. | Low — a competitor can re-research, but not before we finish |
| **L2** | **We run a real 24/7 fleet.** 177 skills, 35 MCPs, kanban orchestration, multi-machine dispatch, backups. We didn't read about agent ops — we operate them at 215k API calls/mo. | Proof that survives any technical evaluation | **High** — this is the moat |
| **L3** | **Sibling operating systems.** Bakery RMS (price tracking, forecasts, WhatsApp ordering, XML invoice parsing), Paraguay retail ops. Patterns transfer directly. | The invoice-XML and price-intelligence patterns are *proven in production*, not designed | Medium-high |
| **L4** | **Cost structure arbitrage.** Our marginal token cost ≈ €0 (flat subscription). WiseQ's marginal token cost ≈ $870/mo at list for equivalent volume. | We can run an agent layer they economically could not | **High, and it is the quiet killer advantage** |
| **L5** | **Structural/tax edge.** Paraguay-domiciled operation (per our own NEXA material: 10% IRE, territorial system) invoicing EUR to NL. | Real margin lever **if the VAT/withholding structure is legal** | **Conditional — see risk R3** |
| **L6** | **Geographic complementarity.** Paraguay build capacity + NL/EU market presence + a European family/company network. | A pure-Paraguay shop can't serve an NL client credibly; a pure-NL shop can't build this stack cheaply | Medium |
| **L7** | **Family/equity angle.** WPG (father's company), Sonia administers it, both are investors in AIW with equity. | Potential anchor-reference arrangement rather than pure cash revenue | **Sensitive — requires explicit decision, not an assumption** |

---

## 4. Deal structures available (all fee values TBD)

| Structure | Shape | When to use | Risk to us |
|:--|:--|:--|:--|
| **A. Paid pilot** | Fixed fee, 4–6 weeks, Phase 0 only, narrow scope | Repo already proposes this (`docs/09`); hat 33 says *"pilot priced at-cost deliberately"* — i.e. **free** | Highest if unpaid. Lowest if priced. |
| **B. Fixed scope per phase** | Fee locked per phase; stop between phases | The repo's stated model. Best for trust-building with a first client | Medium — fixed fee + effort overrun = margin loss |
| **C. Monthly retainer** | Monthly fee for ongoing ops | After build. Matches "agency retainer" market norms | Lowest. Predictable. Recurring. |
| **D. Outcome / per-unit** | Per school-order processed; per review captured; % of recovered time | `docs/12` hat 33: *"€0.50–1.00/processed order"*, *"20–30% of value created"* | Requires **trusted** measurement first — impossible in year 1 |
| **E. Hybrid (recommended)** | C small base + D upside on a *named* metric | Aligns both sides without making us bet on unmeasurable value | Medium-low |
| **F. Equity / deferred** | Fee deferred contingent on outcomes, or AIW equity | Only if the family/equity angle (L7) is deliberately chosen | Highest; changes the relationship |

### The structural recommendation

**A → B → E** is the sequence the repo already gestures at, and it is correct:
1. **Paid pilot** (not free) — de-risks both sides, proves we can write to their stack.
2. **Fixed scope per phase** with explicit stop gates — matches their "if a phase
   underperforms, you stop and keep what works" guardrail, which is a genuine
   trust asset.
3. **Hybrid retainer** with one measurable outcome component — but only on a metric
   **they already trust** (e.g. school orders processed per week, which they'll
   feel immediately). Never on reviews or revenue attribution in year 1.

**Do not** lead with outcome pricing. Their measurement systems are Excel and
a founder's memory. Per-order pricing requires *their* data to be trustworthy,
and the whole proposal exists because their data **is not** trustworthy yet. That's
a contradiction in the current docs.

---

## 5. Risks, ranked

| # | Risk | Severity | Mitigation |
|:--|:--|:--|:--|
| **R1** | ~~ChannelDock/5X have no API~~ **RETRACTED 2026-10-22 — false. Both have APIs. See `RETRACTION-R1-CHANNELDOCK.md`.** | ~~Critical~~ **n/a** | Replaced by R1b. |
| **R1b** | **ChannelDock REST API is plan-gated** (excluded from the free tier; included from Voorraad €45/mo). WiseQ has 230 products vs the free tier's 100-product cap, so they are almost certainly already on a paid plan — but **this must be confirmed**, and an upgrade would be new unbudgeted spend. | **Medium** | Ask which plan (`docs/06`). |
| **R1c** | **ChannelDock PIM (€200/mo) advertises "Bundels samenstellen"** — it may already cover backlog #2 / the bundle spine. We could be proposing to build a purchasable feature. | **High** | Verify in Phase 0 before scoping the bundle work. |
| **R2** | **Pilot is unpaid.** Real unbilled senior labour, and AIW has $240 MRR and one archived customer. | **Critical** | Price the pilot. A free pilot from a cash-constrained studio is a business risk, not generosity. |
| **R3** | **VAT / withholding / entity structure on EUR invoices from a non-EU operation.** | **High** | Tax advice before invoicing. Can erase the margin entirely. |
| **R4** | **Cost attribution is broken** (93.4% of rows unpriced). | **High** | Fix telemetry before quoting per-phase margins. |
| **R5** | **Effort underestimate** — 14 weeks is tight for 6 connectors + 2 browser adapters. | **High** | Re-estimate in Phase 0; use stop gates |
| **R6** | **Liability on automated money-touching.** One bad PO/invoice. | **High** | Approval gates (already promised), insurance, liability cap in contract |
| **R7** | **GDPR processor role + possible DPIA** on mailbox/bookkeeping/B2B data. | Medium | DPA before Phase 1; minimise data held |
| **R8** | **EU AI Act obligations** for both parties (deployer + literacy). | Medium | Budget it; doc 11 doesn't mention AI Act at all |
| **R9** | **Single-client concentration.** First real client = 100% of revenue. | Medium | Do not over-invest in bespoke; keep it generic enough to sell again |
| **R10** | **Reference value vs. confidentiality.** WiseQ is a named case study; do they know? | Medium | Get explicit written permission before publishing anything |

---

## 6. Expectations to set — explicitly

**With WiseQ, before any number:**
1. The first phase is a **discovery** phase. It may conclude that the school-order
   pipeline needs a ChannelDock plan upgrade (R1b), or that their PIM already
   covers part of the bundle work (R1c). Both are legitimate outcomes and should be
   contracted for. **Corrected:** it can no longer conclude "ChannelDock can't be
   automated" — that question is already answered.
2. The €90/mo AI figure in the current doc is **wrong** — we'll replace it with a
   real tiered model. Better they learn that from us now.
3. Their data is currently not trustworthy. **Outcome pricing is impossible until
   that's fixed** — so year 1 is fixed-fee, not outcome-based.
4. **They own the repo and the data.** We're building inside their estate. This is
   a genuine differentiator and should be priced as one (no lock-in for us = trust
   for them = faster close).

**With ourselves:**
1. **Do not repeat the free-pilot mistake.** AIW has no revenue cushion.
2. **Anything not committed to the repo does not exist.** There is no pricing
   decision on record anywhere — the next session would re-derive it.
3. **The €90/mo claim, the €20/mo VPS, the 50–70% margin, and three conflicting
   Thuiswinkel figures** must be corrected before this goes back to the client.
   A client who spots one wrong number stops trusting all the research.

---

*Prepared by AI Whisperers internal analysis · 2026-10-22.*
*All AIW fee figures intentionally TBD. Client-side cost figures pending `B-COST-REALITY.md`.*