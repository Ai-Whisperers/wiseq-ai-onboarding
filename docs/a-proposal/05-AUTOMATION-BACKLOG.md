<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track A · Document 05* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Automation Backlog — every opportunity found, scored

*Compiled from research + the 2026-10-21 session. Impact = time saved or revenue gained; Effort = build complexity. 🔥 = do first.*

## 🎯 How to read this backlog

| Signal | Meaning |
| :--- | :--- |
| 🔥 | **Do first** — founder-confirmed pain or the highest-leverage foundation item |
| **Impact** | Time saved or revenue gained, sized from the research |
| **Effort** | Build complexity — `Low` ships in days, `Med` needs a phase |
| **Order** | Items build on each other — #8 (EAN registry) unblocks #1, #2 and #3 |

> **The dependency is real:** three of the four 🔥 operations items need the canonical EAN registry (#8) to exist first. That is why the registry is the first thing we build.

---

## ⚙️ Operations

| # | Automation | Impact | Effort | Notes |
| :---: | :--- | :--- | :--- | :--- |
| 🔥 1 | **School-order pipeline** — email → offer → invoice → ChannelDock booking | **4h/morning → minutes** | Med | Flagship; founder-confirmed pain |
| 🔥 2 | **Bundle recombination booking** — component EAN movements when combos split | Ends purchase-data pollution | Med | Needs EAN registry (#8) first |
| 🔥 3 | **Purchase intelligence** — 6-mo per-EAN averages, actual-product basis | Replaces manual Excel; fewer errors | Low | Nightly job + report |
| 4 | **Mailbox triage + draft replies** | Hours/week | Low | Founder explicitly wished for this |
| 5 | **Invoice-XML parsing** — supplier QR→XML → inventory + price updates | Hours/week | Low | Pattern proven in sister project |
| 6 | **New-relation onboarding** — extract school details → bookkeeping draft | Minutes/order | Low | Part of #1 |
| 7 | **Return/review-driven automated emails** (5X rules) | Fewer returns | Low | Configure in 5X + trigger |

---

## 🗃️ Data & catalog

| # | Automation | Impact | Effort | Notes |
| :---: | :--- | :--- | :--- | :--- |
| 🔥 8 | **Canonical EAN registry** — EAN ↔ SKU ↔ components | **Foundation for #1, #2, #3** | Med | Build this first |
| 9 | **EAN/GTIN backfill into Shopify** (0/230 today) | Feed quality everywhere | Med | €225/yr (GS1 1,000-pack + contribution), 139 GTINs |
| 10 | **Weights + `inventory_policy` backfill** (0/230 today) | Correct shipping calculation | Low | |
| 11 | **Empty-description rewrite** (20 products) + structured copy for all | Conversion | Low | |
| 12 | **Variant consolidation** (6 colors → 1 product) A/B | Reviews concentrate, feeds cleaner | Med | Needs a test window |
| 13 | **Channel drift sync** (bol 312 vs shop 230) | One truth | Med | |

---

## 💰 Revenue

| # | Automation | Impact | Effort | Notes |
| :---: | :--- | :--- | :--- | :--- |
| 🔥 14 | **Review-invitation engine** — post-delivery, shop + bol | **100% of delivered orders invited; TrustScore held ≥4.4** | Low | Fastest measurable win — see the honesty note below |
| 15 | **Amazon listing refresh + compliance blocks** | Salvage 4.4★ equity | Low | Hero 4.4★×45 · Unbreakable 2.5★ |
| 16 | **Scamadviser / Webshopchecker remediation** | Conversion | Low | Clears the Trust Score 0 flag |
| 17 | **B2B campaign engine** on lead-gen data (event-aware personalization) | New pipeline | Med | 857 verified-org list |

| 18 | **Newsletter + abandoned-cart flows** (ESP setup) | Recovered revenue | Low | No ESP today — pick one |
| 19 | **Content cadence agent** (hub pages, listicle outreach) | Organic growth | Med | ~1/month → 1/week |
| 20 | **Competitor + supplier price monitoring** | Margin defense | Med | |
| 21 | **UCP / agent traffic analytics** | Extend the agentic lead | Low | Most NL retailers have nothing here |

### 📌 Why the review target is worded the way it is (read this before quoting a number)

An earlier draft of this repo promised **"25 → 250+ reviews."** We removed that number,
on purpose, because **we cannot deliver it.**

Three things had to be true for it to be honest, and none of them are:

1. **Reviews are not ours to produce — and invitations are capped.** We control *whether a
   buyer is invited*, not whether they reply. Trustpilot separates two allowances: the
   **API call allowance** (200k / 1M / unlimited per year, by module tier) and the
   **monthly invitation allowance** (plan-dependent). Invitations sent through the API
   **count towards the invitation allowance** — so invitations are bounded by the plan in
   force, not unlimited. And a review only exists if a **buyer chooses to write one.**
2. **Paid tiers buy allowance, not reviews.** Plans (Starter $99, Plus $319, Premium $799
   per domain/month, on a **12-month commitment**) raise the invitation ceiling and what
   we may display. None of them manufactures a review.
3. **A bad review costs more than good ones gain.** TrustScore weights recent reviews
   most heavily. On a 25-review base: 20 five-star + 5 four-star = **4.65** (comfortably
   4-star). But 23 five-star + **2 one-star = 4.40** — two angry reviews drop a whole
   band. For a brand selling GPS watches and headphones to children, one bad review is
   a realistic event.

**So we promise what we actually control:** *every delivered order is invited, and the
TrustScore is defended.* Invitation coverage is a hard number we can guarantee and audit.
TrustScore ≥4.4 is a number we can actively protect by routing complaints before they
become one-star reviews — which is the more valuable thing anyway.

> If anyone quotes "250+ reviews" from an earlier copy of this document, **that figure is
> withdrawn.** Ask us for the current target rather than the old one.


---

## 🧪 Later / exploratory

| Opportunity | Why it's on the list |
| :--- | :--- |
| **Screen-time-control service on tablets** | New product line — the manufacturer would preinstall it (from the meeting) |
| **Elderly hearing-assist line** | New market — big-corporation competition acknowledged |
| **Flanders + DACH expansion operations** | Registers already mapped; this is activation |
| **WhatsApp ordering loop for B2B reorders** | Pattern already proven in our sister project |

---

## 📊 The shape of it

| Bucket | Count | Build profile |
| :--- | :--- | :--- |
| 🔥 **Do first** | 4 | Two low-effort wins (#3, #14), two medium foundations (#1, #2), plus the registry (#8) |
| **Standard backlog** | 13 | Mixed low/medium — sequenced into Phases 1–2 |
| **Exploratory** | 4 | Evaluated in Phase 3 or as separate product lines |

**The lowest-hanging fruit is #14 (review invitations) and #3 (purchase intelligence) — both `Low` effort, both immediately measurable.** They're what we'd build in week 1 if you asked for a quick win before the bigger pipeline work lands.

---

## 📌 In short

**Nine opportunities, three that matter this quarter.** The order is not arbitrary: item 8 (EAN registry) unblocks items 1–3, so the €225/yr GS1 spend is both the highest-ROI line item *and* the dependency. School-order intake (from ~4 hours to minutes) is the headline; review generation and reputation monitoring run continuously behind it at near-zero marginal cost.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | The stack that delivers this backlog |
| **[Py Transfer Wiseq](../b-company/07-PY-TRANSFER-WISEQ.md)** | Proven components we can port from the Paraguay build |
| **[Next Steps](06-NEXT-STEPS.md)** | The questions that unblock the highest-ROI items |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
