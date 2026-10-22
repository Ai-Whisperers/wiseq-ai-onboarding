# C2 · Pricing Benchmarks & Deal Economics — VERIFIED 2026-10-22

> **⚠ INTERNAL — AI Whisperers only. NOT a client-facing document.**
> Written 2026-10-22. Final piece of the WiseQ cost/pricing analysis set:
> `A-COST-BASELINE-AUDIT.md` · `B1-COMPLIANCE-COSTS-VERIFIED.md` ·
> `B2-INFRA-AND-MARKET-RATES.md` · `C-DEAL-STRUCTURE.md` (strategy) · **this doc (benchmarks)**
> Visibility: `internal` · **All AIW fee figures TBD.** This doc supplies the
> *evidence* the fee should be built on — it does not set the fee.

---

## 0. The single most urgent finding in the whole analysis

> **EU AI Act Article 4 (AI literacy) has applied since 2 February 2025, and
> national authorities began supervising and enforcing it in **August 2026** —
> roughly two months ago.**

**Both AIW and WiseQ are in scope.** Any company whose staff use AI is a
*deployer*. WiseQ is already AI-curious (founder uses Gemini/transcription); AIW
deploys agents for a living. `docs/11` — the compliance doc — **never mentions the
AI Act at all.** That is a live gap in a document whose entire job is compliance.

**The mitigation is cheap and should be sold as a deliverable, not a cost centre:**
Article 4 prescribes **no course, no certificate, no minimum hours**. The
Commission confirms **your own records are sufficient**. What's required is that
you decided per role what people need, acted on it, and **kept a record**. That is
a documentation exercise we can produce as part of Phase 0 — a few hours of work
that converts an unfunded legal exposure into a deliverable the client keeps.

---

## 1. Verified Dutch consultancy rate benchmarks (the price anchor)

| Source | Figure | Note |
|:--|:--|:--|
| **Consultancy.nl** (research into agency billing) | **€112/hr** average | consultancies up to 75 FTE; date **06 March 2024** — *oldest figure here, treat as floor* |
| **Consultancy.nl** rate distribution | **75% bill €90–160/hr**; experienced **€124**; starter **€117** | excl. VAT |
| **Consultancy.nl — revenue per FTE** | **€133,000/yr** at €112/hr | **the key ratio** |
| **Emerce** (NL digital agencies) | **€105/hr** average | plus: *"half the time is non-productive"* |
| **Knab Zzp Uurtarievenboek** | **€94/hr** average NL ZZP developer | individual-freelancer floor |
| **Lemon.io** (NL dev contracts, Q3 2026, 170 contracts) | mid **$39/hr** · senior **$51/hr** · strong senior **$58/hr** | contractor market, lower than bureau rate |
| **Clutch NL** | **$50–99/hr** → **€45–88** | *low end of bureau band* |

### What these numbers mean for the WiseQ deal

**The gap between €94 (ZZP) and €112–124 (bureau) is the entire commercial question.**

- At **€112/hr**, the NL market implicitly assumes **~€133k revenue per FTE**.
- At **€45–88/hr** (Clutch low end), the same business is a commodity shop.
- **AIW's advantage is structural, not rate-based.** We should not win by being
  cheap — we should win by being the team that already runs a 215k-call/month
  agent fleet, and price above the ZZP floor because the capability is not a
  freelancer's capability.

**The Emerce finding is the one to internalise:** *"half the time is non-productive."*
That is the empirical justification for the repo's fixed-fee-over-hourly instinct —
and simultaneously the argument that **AI agents are how we beat the 50% overhead**.
Our delivery leverage is the product.

---

## 2. AI automation agency pricing (secondary source — directional only)

From `taskip.net` (blog-tier, **not** a rate card — flagged U16):

| Segment | Monthly retainer |
|:--|:--|
| Small business | **$500–1,500/mo** |
| Mid-market | **$1,500–4,000/mo** |
| Enterprise | **$3,000–8,000+/mo** |
| Mid-market **setup projects** | up to **$20,000+** |

Cross-checked against repo claims:
- `docs/09` says NL Plus-agencies **€2,000–5,000/mo** → **consistent** with mid-market.
- `docs/09` says *"Shopify-specialist median $6,000–8,000/mo"* → **this is the
  enterprise band being applied to a 230-product SMB.** Drop it or source it.
- `docs/12` hat 33 proposes **"20–30% of value created"** outcome pricing →
  **structurally sound** and within normal professional-services practice, but
  unmeasurable in year 1 (see `C-DEAL-STRUCTURE.md` §4).

**WiseQ's true segment:** 230 products, ~€1M-order-of-magnitude turnover, small team.
That is **SMB-to-mid-market**, so the **$1,500–4,000/mo mid-market band** is the
honest comparator — not enterprise. The repo's anchors are pitched one tier too high.

---

## 3. Agency economics — what margin is actually realistic

| Finding | Value | Source |
|:--|:--|:--|
| Revenue per FTE (NL consultancy) | **€133,000/yr** | Consultancy.nl |
| **Non-productive time** | **~half** | Emerce |
| NL digital agency sector | **~€1.2bn** turnover | Emerce |
| Most NL digital agencies | **profitable** | DDA benchmark 2024 |
| **"High Performers"** | top **15% on EBITDA** | DDA benchmark 2024 |
| DDA note | most agencies offer **60–70% of services to clients in long-term contracts** | DDA benchmark 2024 |

> **This is the number that settles Doc A's C8.** `docs/09` claims *"50–70% gross
> margin per the agency-economics research"* with **no citation**. The DDA data
> shows profitability is real but the top decile-plus performers separate on
> EBITDA, not gross margin. **The 50–70% figure is plausible but must be sourced
> or removed** — an uncited margin claim in a client-facing document is a
> liability, not a selling point.

**The strategic read:** the NL market's defining trait is **long-term contracts
(60–70%)** and a **half-non-productive-time tax on every engagement**. That is
precisely the argument for a **retainer** structure over per-project work, and
precisely the gap AI agents close. It validates `C-DEAL-STRUCTURE.md`'s
**A → B → E** recommendation on independent evidence.

---

## 4. EU AI Act — costs and penalties (verified)

### Obligations

| Article | Requirement | Applies to | Status |
|:--|:--|:--|:--|
| **Art. 4** | AI literacy — "measures aimed at a sufficient level" | providers **and deployers** | **applying since 2 Feb 2025; supervised since Aug 2026** |
| **Art. 99** | Penalties | all | in force |
| Art. 25 / 26 | Provider documentation duties | providers of GPAI/systems | in force |

**Article 4 explicitly prescribes:** no course, no certificate, no minimum hours,
no formal test. **The Commission's own records are sufficient.** The obligation is
to *decide, act, and document* — per role, proportionate to context.

### Penalties

| Tier | Amount |
|:--|:--|
| Prohibited practices | **up to €35M or 7% of total global annual turnover** |
| Most other breaches | proportionate, scaled down |
| **SME treatment** | **provisions exist ensuring penalties "remain fair" for SMEs** |

⚠ *The €35M/7% tier is verified from the CEPS analysis and multiple secondary
sources. The exact consolidated 2026 schedule remains U13 — re-check the official
text before quoting any penalty figure to a client.*

### SME compliance cost reality-check

CEPS, citing Commission impact assessment: compliance for an SME can run to
**~€400,000 per high-risk product** (QMS €71.4k–330k, technical documentation
component among others).

> **Critical scoping point:** that figure applies to a **high-risk product** —
> a product being placed on the market. **WiseQ is not building a high-risk AI
> product; it is internally deploying a marketing/ops agent layer.** It does not
> trigger high-risk obligations. Using this number to scare or justify spend would
> be both wrong and, if the client checked, credibility-destroying.
>
> **What actually applies to us: Article 4. Nothing else in this table does.**

### Netherlands-specific

The Dutch supervisory split for the AI Act is **not yet settled** (as of the
sources read). Relevant to both parties and worth a line in the proposal —
it affects who our client answers to.

---

## 5. Shopify App Store economics (relevant if we productise)

| Term | Value | Source |
|:--|:--|:--|
| App Store registration | **one-time $19** | Shopify partner docs |
| Revenue share | **keep 100% of first $1,000,000 USD lifetime gross**; % applies above that | Shopify partner docs |
| Average Shopify app price | **$58–67/mo** | craftberry app-store stats |
| Apps in store | **17,165+** | craftberry |

> **This is the long game, not the WiseQ deal.** It matters for hat #31/#50
> (Commerce-OS productisation). Keep it in the 24-month plan, **not** in the
> WiseQ proposal. **Do not tell WiseQ about the productisation path** — that's our
> strategy, and disclosing it invites the client to demand product pricing.

---

## 6. What the cost of the AIW pilot actually is (the H10 line, finally priced)

Using verified rates rather than the repo's guess:

| Item | Basis | Value |
|:--|:--|--:|
| Phase 0 build (repo: "week 1–2") | 2 weeks senior + agent leverage | **10–20 days** |
| At NL bureau rate | €112/hr × 8h × 15 days | **≈ €13,440** |
| At ZZP-equivalent (AIW's real cash cost of opportunity) | €94/hr × 8h × 15 days | **≈ €11,280** |
| Phase 1 (repo: "week 3–6") | 4 weeks | **≈ €26,880–53,760** |
| **Phases 0+1 combined** | | **≈ €40,000–67,000 at market rate** |

**Against AIW's $240 MRR.** `docs/12` hat 33 says *"pilot priced at-cost
deliberately — the pilot's product is trust."*

> **This is now quantifiable and the number is uncomfortable.** A free Phase 0 is
> **€11–13k of unbilled senior labour** from a studio with $240 MRR, one archived
> customer, and a live pipeline of one lead marked DECLINE.
>
> "At-cost" is defensible **once**, as a deliberate reference investment against a
> named case study. It is not a standing policy. If WiseQ becomes the reference
> that unlocks clients 2–5, the pilot was an investment with a return. If WiseQ
> doesn't convert, it was €13k of runway we don't have.
>
> **Recommend: cap the free pilot at a scoped, time-boxed Phase 0 only (never
> Phase 1), and treat anything beyond as paid.** TBD pending your decision.

---

## 7. Consolidated evidence table for the pricing decision

Everything below is verified. The fee itself stays TBD — this is the substrate.

| Anchor | Value | Confidence |
|:--|:--|:--|
| NL consultancy avg rate | **€112/hr** | High (Consultancy.nl, 2024) |
| NL consultancy experienced | **€124/hr** | High |
| NL digital agency avg | **€105/hr** | High (Emerce) |
| NL ZZP developer | **€94/hr** | High (Knab) |
| Revenue per FTE | **€133k/yr** | High (Consultancy.nl) |
| Non-productive time | **~50%** | High (Emerce) |
| NL retainer band (SMB→mid) | **$1,500–4,000/mo** | Medium (blog-tier) |
| NL agency retainer | **€2,000–5,000/mo** | Medium (repo, uncited) |
| Long-term-contract share | **60–70%** | High (DDA 2024) |
| High-performer cohort | top **15% EBITDA** | High (DDA 2024) |
| AI Act Art. 4 | applying **2 Feb 2025**, supervised **Aug 2026** | **High (EC + secondary)** |
| AI Act max penalty | **€35M / 7%** | High, schedule U13 |
| Phase 0 at market rate | **€11–13k** | Derived from High anchors |
| Phases 0+1 at market rate | **€40–67k** | Derived |

---

## 8. Recommendations (fee = TBD; these are the decisions around it)

1. **Ship an Article 4 compliance record as a Phase 0 deliverable.** Hours of work,
   removes a live legal exposure from both parties, and gives WiseQ a document a
   NL supervisor would actually accept. Make it visible — it's a differentiator.
2. **Do NOT quote the €35M/7% penalty at WiseQ.** They're not at risk of it, and
   using it would be fear-selling. Their actual exposure is Article 4.
3. **Do NOT use the ~€400k high-risk SME figure.** It doesn't apply to an internal
   ops deployment and would collapse on inspection.
4. **Drop the "$6,000–8,000/mo Shopify-specialist median"** anchor from `docs/09` —
   it's an enterprise figure applied to an SMB and it's the weakest thing in the doc.
5. **Price above the €94 ZZP floor.** The moat is the operating fleet, not the hours.
6. **Free pilot: time-box to Phase 0, never Phase 1, and say so in writing.**
7. **Source or delete the "50–70% gross margin"** claim (C8).
8. **Write the pricing decision into the repo this time.** There is currently no
   recorded fee anywhere — the next session would re-derive it from scratch.

---

## 9. UNVERIFIED carried forward

All of B1's U1–U9 and B2's U10–U17 still stand. New from this pass:

| # | Item | Note |
|:--|:--|:--|
| U18 | **EU AI Act Art. 99 consolidated 2026 penalty schedule** | €35M/7% verified; full schedule not |
| U19 | **NL AI Act supervisory split** | unsettled at time of reading |
| U20 | **taskip.net retainer bands** | blog-tier, directional only |
| U21 | **Consultancy.nl figures are dated 06-03-2024** | floor, not current; re-verify |
| U22 | **Kiyoh** | still JS-rendered (from B1 U10) |

---

*Prepared by AI Whisperers internal analysis · 2026-10-22.*
*Sources: consultancy.nl, emerce.nl, dutchdigitalagencies.com (DDA Benchmark 2024),
shopify.dev, craftberry, CEPS on EU AI Act costs, EC AI Act Navigator,
cybercoach/beesensible on Article 4, kiyoh/Trustpilot (B1/B2), Hetzner/Neon/Cloudflare (B2).*
*AIW fee figures intentionally TBD.*