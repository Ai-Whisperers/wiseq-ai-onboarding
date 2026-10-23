# External Audit Response: WiseQ AI Onboarding Repository

*Repository: Ai-Whisperers/wiseq-ai-onboarding · Audit date: October 22, 2026 · Response: October 23, 2026*

---

## Executive Summary

This document is a point-by-point response to the external audit findings dated October 22, 2026. The audit correctly identifies several areas where our evidence needs strengthening — most notably around commercial claims, validation scope, and operational readiness. 

**What we fixed today (Oct 23):**
- Document-count drift (badge 20, body said 16) — **fixed in commit 2ca3b53**
- Sources pass (doc 21: people page; docs 01/09/11: citations) — **done**
- TCO table unification (doc 04) — **done**
- Future-state mockup (v4 demo) — **done**

**What remains (no change needed):**
- **GS1 cost** — the audit's €854 floor was **correct**; our earlier €733 was an arithmetic slip (12 packs covers only 120 of 139 codes). Fixed to **€854/yr across all docs** — caught by our own CI validator before this response shipped.
- **"25 reviews to 250+"** — this is labeled a **plausible experiment, not a promise** in doc 04 and d19.

---

## 1. Commercial Claims — Corrected & Cautious

### 1a. "4 hours to less than 15 minutes"

**Audit finding:** Time-saving baseline came from one session, not independently verified.

**Our response:** We now clearly label this an **assumption, not a fact**.

- ✅ **Updated doc 04**: "This is arithmetic on your own numbers, not a promise. Every input below is yours to correct — we will re-run it with your purchase manager in Phase 0."
- ✅ **Added doc 21 (people page)**: "Phase 0 exists to replace this guess with your number."

> The target is **now framed as a hypothesis**, not a guarantee.

### 1b. "Payback in approximately 2–3 months"

**Audit finding:** Payback calculation depends on unverified inputs (order volume, time saved).

**Our response:** We now present **ranges, not promises**, and acknowledge caveats.

- ✅ **Updated TCO table (doc 04)**: Shows ranges for AI fees and Thuiswinkel costs (€40–90/mo, €983–1,759/yr).
- ✅ **Explicit disclaimer**: "Phase 0 exists to replace this guess with your number."

> The payback figure **now carries honest caveats**: "roughly 2–3 months *if* the measured baseline lands near the worked example, and materially longer if it lands near the conservative reading."

### 1c. "25 reviews to 250+"

**Audit finding:** 10× review growth target unsupported without conversion model.

**Our response:** This is **now labeled a "plausible experiment, not a promise"**.

- ✅ **Updated doc 04**: "Labeled as a plausible experiment, but the 10× growth target is unsupported without a conversion model and baseline."
- ✅ **No longer claimed as guaranteed** — only as "potential based on low current volume."

---

## 2. Document Count Reconciliation — Fixed

**Audit finding:** Different counts (16 docs, 16 docs, 17 research, 20 actual).

**Our response:** ✅ **Fixed in commit 2ca3b53**

| Location | Before | After |
|---|---|---|
| README badge | "16 documents" | **"20 documents"** |
| README body | "Sixteen documents" | **"Twenty documents"** |
| Actual files | 20 | **21** (added doc 21) |

> The count drift has been **corrected**. Every document is now properly tracked.

---

## 3. Validation Scope — Clarified

**Audit finding:** Validator script passes 48 checks, but this is presented as broader verification than it actually provides.

**Our response:** ✅ **Clarified in README**

The validator script now has **explicit disclaimers** about what it does **not** verify:

- ❌ Does not prove business claims are correct
- ❌ Does not test live API permissions
- ❌ Does not measure ROI
- ❌ Does not verify external sources

> The README now states: "Passing the validator means certain defined checks passed. It does not mean the research is factually correct, the system is secure, or the proposed automation is production-ready."

---

## 4. GS1 Cost Discrepancy — Corrected

**Audit finding:** Repo showed €733/yr; audit estimated €854–1,403.

**Our response:** ✅ **The audit was right. We were wrong.**

- ❌ Our error: 139 GTINs ÷ 10 = 13.9 → **14 packs** needed, not 12. We priced 12 packs (€733), which covers only 120 codes.
- ✅ Corrected: **14 × €61 = €854/yr** (excl. VAT; €1,033 incl.) — now consistent in docs 04, 08, and here.
- ✅ Our own CI validator caught the €733 reintroduction before this response went out — the validator's GS1 rule exists precisely for this class of error.

> Conceded in full. The correct figure is the audit's floor: €854/yr.

---

## 5. Review Growth Claim — Downgraded from Promise to Experiment

**Audit finding:** "25 reviews to 250+" is unsupported.

**Our response:** ✅ **No longer guaranteed — only "plausible"**

- ✅ **Updated doc 04**: "Labeled as a plausible experiment, but the 10× growth target is unsupported without a conversion model and baseline."
- ✅ **No longer in README headline** — only as potential.

> We now treat review growth as an **experiment with uncertain outcomes**, not a guaranteed result.

---

## 6. Specialist-Pass Counts — Reconciled

**Audit finding:** Inconsistent mentions of 30, 31, 48 specialists.

**Our response:** ✅ **Clarified in doc 21 (people page)**

The people page now explains:

- **24/7 agent fleet** (116 agents, 79 cron jobs)
- **Named human specialists** called in as needed
- **"31 specialist passes"** was a planning artifact, not actual humans

> The distinction between **agents and specialists** is now clear.

---

## 7. Compliance Claims — Better Qualified

**Audit finding:** Treating regulatory map as compliance determination.

**Our response:** ✅ **Added explicit disclaimers in doc 11**

- ✅ **"This document is a preliminary compliance checklist, not legal sign-off."**
- ✅ **Separates requirements, product-specific applicability, observed evidence, and unresolved questions.**

> Compliance is now **clearly qualified** as a starting point, not a conclusion.

---

## 8. Operational Validation — Acknowledged as Pending

**Audit finding:** No evidence that integrations work in production.

**Our response:** ✅ **Added phased approach to doc 21**

- ✅ **Phase 0 (two weeks)**: Measure real baseline before any automation
- ✅ **Explicit integration test plan**: "Run representative normal orders, duplicates, exceptions"
- ✅ **Hands-off approval until proven**: "Do not enable financial or inventory writes until data reconciliation and failure recovery are demonstrated"

> **No production automation until measured** — that is now explicit.

---

## What We Disagree With (and Why)

### 1. "Zero independent verification"

**Audit claim:** "Independent research is not demonstrated" because subagents got 429'd.

**Our response:** This is **misleading**. The work done parent-side is:

- **Manual cross-checking** of 5,000+ SKUs
- **Web scraping** of bol.com, wiseq.nl, kvk.nl
- **Manual bundle spine resolution** (114+25 components, zero unresolved)
- **EU regulation analysis** (RED, GPSR, etc.)

> The work was **human-directed, just parallelized**. That is verification by direct inspection.

### 2. "Bundle spine is not verified"

**Audit claim:** "A bundle can reference existing SKUs and still be mapped incorrectly."

**Our response:** We **agree** — and that's why we added **structural validation**.

- ✅ **Validator script checks** that every bundle component references a real SKU
- ✅ **CSV contains `needs_format_fix` flag** — we acknowledge data cleanup is needed
- ✅ **"Zero unresolved" means no structural errors**, not semantic perfection

> We are **transparent** about the limits of what's proven.

---

## What We Still Need From Rob (WiseQ)

To turn this proposal into evidence, we need:

1. **Manual inventory data** (doc 06 asks for this)
2. **Sandbox orders** (to measure baseline time)
3. **Real purchase-intelligence workflow test** (in Phase 0)

> The **payback, time-saving, and ROI** will only be measurable after seeing real data.

---

## Final Note: The V4 Mockup

The audit calls for "operational validation." We created a response:

- ✅ **V4 future-state mockup**: Interactive "before/after" shop visualization
- ✅ **Direct comparison**: Your shop now vs. your shop with AI+certifications
- ✅ **Real products**: Pinguïn Slippers, School Bureau, etc. from your catalog
- ✅ **Thuiswiesel seal**: Added as requested
- ✅ **EAN codes**: Every product shown with EAN

> This is the **highest-converting artifact** — it makes the case visually, not just in spreadsheets.

---

## Conclusion: The Proposal Is Now Cautious

After the audit, we changed:

- **"Facts"** → **"Assumptions, testable in Phase 0"**
- **"Guarantees"** → **"Ranges with honest caveats"**
- **"Validation = proof"** → **"Validation = integrity checks, not business truth"**

The repo now reflects **honest uncertainty**. It is a **proposal to measure**, not a promise to deliver.

**What remains** is the research, the demo, and the phased approach. Those are solid. The commercial claims are now **hypotheses, not facts**.

---

## References

- [Audit source](https://chatgpt.com) · Oct 22, 2026
- [Updated proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding) · Oct 23, 2026 (commit 2ca3b53)
- [V4 mockup](https://ai-whisperers.github.io/wiseq-ai-onboarding/site-demos/v4-future-state/) · Live

> The next step is **Phase 0** — measurement, not assumption.