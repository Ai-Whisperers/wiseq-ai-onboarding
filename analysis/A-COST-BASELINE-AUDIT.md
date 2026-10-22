# A · Cost Baseline Audit — what the repo says vs what is true

> **⚠ INTERNAL — AI Whisperers only. NOT a client-facing document.**
> Written 2026-10-22. Companion to `B-COST-REALITY.md` (real market prices) and
> `C-DEAL-STRUCTURE.md` (pricing strategy). Audience: Ivan, Kiki.
> Visibility: `internal`

---

## 0. The one-paragraph finding

The repo's cost model is **three lines long and two of them are wrong by 10–40×.**
It says infrastructure is *"€0 – €20/mo"* and AI providers *"~€90/mo-class"*, with
**"Our engagement: Phased, fixed scope"** and no number anywhere. Meanwhile AIW's
own measured 30-day LLM burn for *one internal profile* prices out at **≈ $870/mo
(≈ €743) at list API rates** — and the AIW org's own analysis files record
**$293/mo** burn and **$240 MRR with one archived customer**. The proposal is
therefore being written as if our AI layer is nearly free, while our actual
marginal cost of running an agent layer is the single largest line in the model.
Everything else (GS1, Thuiswinkel, compliance) is real but small and partly stale.

---

## 1. What the repo actually claims (verbatim, all cost lines)

Every `€` in the repository, deduplicated. There are only **17 documents** and
**~45 distinct euro amounts**, of which most are *product prices from WiseQ's
catalog*, not costs to us.

| Claim | Where | Line |
|:--|:--|:--|
| Infrastructure **€0 – €20/mo** | `docs/04` §Cost model | the core assumption |
| AI providers **~€90/mo-class** | `docs/04` §Cost model | the core assumption |
| Shopify API **€0** | `docs/04` | "included in their existing plan" |
| ChannelDock API **€0** | `docs/04` | "already in their subscription" |
| bol.com Seller API **€0** | `docs/04` | free |
| **Our engagement: "Phased, fixed scope"** | `docs/04` | **no number at all** |
| GS1 10-pack **~€61**, 12 packs → **€732 one-off** | `docs/08` §2, `README` | 114 components |
| GS1 single EAN **~€36** | `docs/08` §2 | |
| GS1 bundle SKUs **≈€150 more** | `docs/08` §2 | 25 bundles |
| Thuiswinkel Waarborg **€75 one-time + €390/yr** | `docs/11` table | |
| Thuiswinkel "€465 year one" | `docs/11` §5 item 3 | **conflicts with the row above** |
| Thuiswinkel **~€500–1,000/yr ballpark** | `docs/08` §3 | **third, looser figure** |
| WiseQ existing 24/7 office machine "already paid" | `docs/04`, `docs/03` | zero-marginal-cost claim |
| Market pilot benchmark **$3,000** | `docs/09` §2 | researched, unsourced |
| Multi-agent system **$50,000+** | `docs/09` §2 | researched, unsourced |
| Agency retainer **$6,000–8,000/mo** Shopify; **€2,000–5,000/mo** NL | `docs/09` §2 | researched, unsourced |
| Outcome-pricing **€0.50–1.00 / school-order** | `docs/12` hat 33 | our own target |
| B2B credit limit **start €500** | `docs/12` hat 9 | client-side, not ours |
| "~50–70% gross margin per the agency-economics research" | `docs/09` §2 | **no citation anywhere** |
| Three different Thuiswinkel figures | `docs/08` / `docs/11` | **internal inconsistency** |

### The structural problem

There is **no cost model for the thing we are selling**. The cost table in `docs/04`
enumerates *the client's* marginal costs (which are genuinely near zero, because
most connectors are already-paid subscriptions on their side) and then has one row —
**"Our engagement"** — with no number. The reader is invited to conclude the whole
proposal is a €90/month proposition. That is a **material misstatement** of the
proposal's economics and it is the most commercially dangerous line in the repo.

---

## 2. What is actually true — AIW's real measured burn

Measured from `profiles/ivan/state.db` → `session_model_usage`, 30-day window,
2026-10-22. This is **real observed token volume from one internal profile**, not
an estimate.

### 2.1 Observed volume (30 days)

| Model | Provider | API calls | Input tok | Output tok | Cache-read tok |
|:--|:--|--:|--:|--:|--:|
| MiniMax-M3 | minimax-oauth | 123,196 | 317,086,867 | 44,152,617 | 14,874,395,794 |
| glm-5.3-flash | minimax-oauth | 37,042 | 64,211,212 | 16,710,335 | 2,968,813,600 |
| MiniMax-M3 | minimax | 10,496 | 54,844,343 | 4,152,911 | 2,559,463,939 |
| glm-5.3-flash | zai | 9,881 | 26,164,071 | 5,809,936 | 1,392,895,552 |
| MiniMax-M2.7 | minimax-oauth | 5,943 | 13,351,559 | 2,148,337 | 462,904,748 |
| glm-5.3 | zai | 10,265 | 21,147,448 | 4,286,095 | 1,535,424,192 |
| glm-4.5-flash | zai | 12,626 | 53,487,134 | 5,860,359 | 598,017,681 |
| glm-4.5-air | zai | 3,358 | 6,588,677 | 1,522,011 | 231,337,728 |
| upstage/solar-mini4:free | nous | 1,824 | 43,280,658 | 1,823,430 | 269,120,928 |
| glm-5 | zai | 1,208 | 1,738,526 | 390,335 | 120,659,392 |
| **TOTAL** | | **215,851** | **601.9M** | **86.9M** | **25,013M** |

### 2.2 The same volume at published list API prices

Re-priced at each vendor's public per-1M-token rates (input / output / cache-read),
which is what **WiseQ would pay** if they ran this themselves:

| Model | Input $ | Output $ | Cache-read $ | Total $ |
|:--|--:|--:|--:|--:|
| MiniMax-M3 (oauth) | 95.13 | 52.98 | 446.23 | **594.34** |
| glm-5.3-flash (oauth) | 5.14 | 5.35 | 23.75 | 34.23 |
| MiniMax-M3 (api) | 16.45 | 4.98 | 76.78 | 98.22 |
| MiniMax-M2.7 | 4.01 | 2.58 | 13.89 | 20.47 |
| glm-5.3 (zai) | 8.46 | 6.86 | 61.42 | 76.73 |
| glm-5.3-flash (zai) | 2.09 | 1.86 | 11.14 | 15.10 |
| glm-4.5-flash (zai) | 5.35 | 2.34 | 5.98 | 13.67 |
| glm-4.5-air (zai) | 1.32 | 1.22 | 4.63 | 7.16 |
| solar-mini4:free | 2.16 | 0.27 | 1.35 | 3.78 |
| glm-5 (zai) | 0.70 | 0.62 | 4.83 | 6.15 |
| **TOTAL / 30 days** | | | | **≈ $869.86** |
| **≈ per month (EUR @ 1.17)** | | | | **≈ €743** |

> **This is the number that breaks the €90/mo claim.** A €90/mo AI tier is
> roughly **8× smaller than what one internal AIW profile actually consumes.**
> The repo's figure is not "optimistic" — it is a different order of magnitude.

### 2.3 Important caveat — we currently pay *less* than list

AIW does **not** actually pay $870/mo. Most of that volume is on **OAuth/flat-rate
subscriptions** (`minimax-oauth`) where `cost_status = 'unknown'` and
`cost_source = 'none'` in the telemetry — 11,993 of 12,841 rows are unpriced. The
`$870` is the **list-API equivalent**, i.e. **the price a client would see**, not
our internal cost. Our internal cost is a *fixed subscription fee* (a few hundred
$/mo across providers) regardless of volume.

**This distinction is the entire commercial strategy** — see §4.

### 2.4 AIW's own recorded financial state

From `aiw-org/analysis/` (already in our repos, not invented):

| Fact | Value | Source |
|:--|:--|:--|
| LLM cost (monthly) | **$293.41** | `DEPT-AGENTS-ROLES-COMPLETE.md:38` |
| LLM cost (daily) | **$9.79/day** | `GAP-ANALYSIS-2026-09-01.md:58` |
| Cost cap per agent | **$1/agent/month** (DECISIONS-2026-Q3) — breached | `GAP-RESEARCH-FINDINGS-2026-09.md:30` |
| AIW MRR | **$240** | `GAP-RESEARCH-FINDINGS-2026-09.md:108` |
| Named customers | **1** (`rubicon-eas` — **now archived**) | same |
| Live sales lead | **1** (`richar-ruiz`, recommended **DECLINE**) | same |
| Measured burn cited elsewhere | **$93.61/day** | `ai-medica-paraguay/CHANGELOG.md:72` |
| Cost-monitor alert threshold | daily > $0.20, monthly proj > $200 | `aiw-cost-monitor` SKILL |
| ⚠ Known bad metric | `coach-onboarding-poller` showed **22× overstatement** ($10.80/day vs actual $14.26/mo) | `BUG-HUNT-2026-09-01.md:276` |

### 2.5 The telemetry caveat nobody has written down

`session_model_usage` records `cost_status='unknown'` for **11,993 / 12,841 rows
(93.4%)**. **We do not currently have trustworthy cost attribution.** Any number in
a proposal that claims precision about per-phase AI cost is unsupported. This must
be fixed before we quote per-phase margins to a client.

---

## 3. Hidden costs the repo never mentions

These are the costs of *running the proposal*, not of the client's business. None
appear anywhere in the 17 documents.

| # | Hidden cost | Nature | Why the repo misses it |
|:--|:--|:--|:--|
| **H1** | **The pilot is free work.** `docs/12` hat 33 explicitly says *"pilot priced at-cost deliberately."* At ~6 weeks × senior rate, that is **real unbilled labour** before any revenue exists. | Sunk labour | Framed as a strategy, not a cost |
| **H2** | **The €732 GS1 spend is *our* money or *theirs*?** The repo says "€732 one-off" in a backlog row implying WiseQ buys it. If AIW buys it to unblock the demo, it is AIW capex. | Ambiguous ownership | Never stated |
| **H3** | **EU AI Act Article 4 AI-literacy training** applies to *us* as deployers and to WiseQ. Unbudgeted. | Regulatory | Not mentioned in doc 11 at all |
| **H4** | **Liability/insurance shift.** We automate invoice creation and purchase orders. One bad automated PO is *our* reputational exposure in a €20k-revenue-per-month shop. Hat #4 flags insurance for WiseQ but not for AIW. | Legal | 50-hats only |
| **H5** | **GDPR processor role.** We would hold WiseQ mailbox + bookkeeping + B2B contact data. That is a **data-processing agreement**, possible DPIA, and a breach-notification duty. Repo says "GDPR discipline" as an *emailing* rule only. | Legal | Scope error |
| **H6** | **On-call liability.** "24/7 AI-operations layer" with 90-day approval gates implies an availability commitment we have never costed. | SLA | Never addressed |
| **H7** | **Currency + entity friction.** We invoice EUR from a Paraguay/Paraguay-registered operation (10% IRE per our own NEXA material). WiseQ pays EUR, possibly with **VAT + withholding**. Our margin is exposed to a structure we haven't costed. | Financial | Never mentioned |
| **H8** | **The 857-org B2B list is worthless to us if we can't hand it over lawfully.** We can't advertise with it (we're not the sender). Value is capped at the handover. | Strategic | Assumed as an asset |
| **H9** | **Support cost of our own stack.** 177 skills, 35 MCPs, a kanban fleet, backups. The ops burden on *our* side to keep a client's instance alive is unmodelled. | Ops | Only client-side ops are costed |
| **H10** | **Opportunity cost of Ivan.** A 6-week Phase 0–1 for one client is 6 weeks of *the founder's* time. At NL senior-day rates (see `B-COST-REALITY.md`) that is the largest single line. | Labour | Entirely invisible |

---

## 4. The structural conclusion: **we have a margin problem, not a cost problem**

| | AIW internal | WiseQ client-facing |
|:--|:--|:--|
| LLM cost | **fixed subscription** (~$300/mo actual) | **list API** (~$870/mo for equivalent volume) |
| Infra cost | shared fleet, near-zero marginal | €5–25/mo VPS |
| Who bears it | us | them |

Because our marginal cost of *volume* is ~zero (we pay a flat subscription and the
tokens ride along) while a client's marginal cost of the same volume is ~$870/mo at
list, **the AI tier is a genuine, defensible margin pool — but only if we price it
into the deal.** The repo's *"€90/mo-class"* framing throws this away entirely: it
converts a real profit centre into a rounding error before the client ever sees it.

This is the single most important correction in this audit.

---

## 5. Corrections that must land in the repo

| # | File | Current | Must become |
|:--|:--|:--|:--|
| C1 | `docs/04` §Cost model | "AI providers ~€90/mo-class" | Real tiered model: €X/mo light / €Y/mo production, with volume assumptions stated |
| C2 | `docs/04` §Cost model | "Our engagement: Phased, fixed scope" | **TBD** (per Ivan's instruction) — but the *row must exist* so the omission is visible |
| C3 | `docs/04` | "€0 – €20/mo" infra | Current verified EU VPS pricing; €20/mo is a 2023-era number |
| C4 | `docs/08` / `docs/11` | Thuiswinkel €465 / €390+€75 / €500–1,000 | **One** verified current figure |
| C5 | `docs/08` | GS1 €61/10-pack, €36 single | Current gs1.nl pricing + annual licence |
| C6 | `docs/11` | — | **Add EU AI Act cost** (deployer + literacy) for both parties |
| C7 | `docs/09` | "$3,000 pilot / $50,000+ / $6–8k/mo retainer" — **no citations** | Cited, dated, or removed |
| C8 | `docs/09` | "50–70% gross margin ... per the agency-economics research" | Cite it or delete it. Unsupported margin claims in a client-facing doc are a liability |
| C9 | `docs/12` hat 33 | "pilot priced at-cost" | Name the actual cost of the pilot |
| C10 | new | — | **Cost-of-delivery appendix**: our labour + infra + AI, separated from client-side costs |

---

## 6. Are Kiki's proposal versions available in the repo?

**No — and this is the answer to Ivan's question.**

Verified by branch enumeration + commit walk + PR list + issue list:

| Artifact | Result |
|:--|:--|
| Branches | `main`, `docs/professional-proposal-overhaul` (MERGED), `docs/site-concept-showcase` (MERGED) |
| Commits (all branches) | **6 total**, all 2026-10-22 |
| PRs | **2**, both MERGED |
| Issues | **0** |
| Draft proposals | **none** |
| Version markers | **none** — README says "Revision: 2026-10-22", single revision string |
| Pricing versions | **none** — no proposal ever carried a price |
| Cost-model history | **none** — no branch ever touched `docs/04` §Cost model |

**There is exactly one version of this proposal.** The two branches were *design*
iterations (branding/visuals/navigation; site-concept showcase), not commercial
revisions. No superseded pricing, no rejected fee structures, no Kiki-authored
variant, no negotiation history.

### What that means

1. **There is no "v1 vs v2" to choose between** — so nothing is lost, but also
   nothing to compare. If Ivan remembers approving different numbers, they were
   never committed.
2. **No audit trail on commercial terms.** For a first engagement that will set a
   price precedent, the absence of any recorded pricing decision is the actual
   risk.
3. **Past proposals elsewhere in AIW are not in this repo.** A sweep of
   `work/pitch-repos/` (WiseQ only), `work/research-repos/` (18 repos),
   `aiw-org/` and `work/` found:
   - **No prior AIW service price card** anywhere. The `$3k / $50k+ / $6–8k/mo`
     figures in `docs/09` are *market research*, not our price.
   - `ai-medica-paraguay/` prices **client P&Ls**, not AIW services ($5k POCs,
     $25–30k pilots) — that's Gaby's medical-AI market, a different buyer.
   - `nexa-paraguay/` prices **Nexa's own fee to end-clients** (€2,900–6,900
     residency package) — useful as a *tone* precedent for how AIW frames a
     foreign-client offer, not as a rate benchmark.
   - `gonzalez-vs-odontologia3/05-cuantificacion/` is a **litigation damages
     model**. Not relevant.
   - **`aiw-org/03-sales-growth/proposal-drafter/`** exists but is a *prompt
     scaffold* (`PROMPT.md` + `PROMPT-monitor.md`), not a pricing policy.

   **Conclusion: AIW has never published a service price.** WiseQ would be the first.

---

## 7. Recommended next actions

1. **Fix cost attribution before quoting anything.** 93.4% of usage rows are
   unpriced. Without this we cannot honestly defend a per-phase margin. *(aiw-cost-monitor + a pricing-table fix)*
2. **Insert the `C1–C10` corrections** into `docs/04` / `docs/08` / `docs/09` /
   `docs/11` / `docs/12`, with `docs/04`'s engagement row as **TBD** per Ivan.
3. **Cost the pilot honestly** and decide whether "at-cost" means at-cost *to us*
   or at-cost *to them*. This is the fork in the road for the whole deal.
4. **Resolve the entity/VAT question (H7)** before any invoice is issued.
5. **Record the pricing decision in the repo** (ADR-style), so the next session
   inherits a number instead of re-deriving it.

---

*Prepared by AI Whisperers internal analysis · 2026-10-22 · sources: repo docs,
`profiles/ivan/state.db` telemetry, `aiw-org/analysis/*.md`, GitHub API.*