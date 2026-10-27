<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Internal review record* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Critical Review — the adversarial pass

*Independent adversarial review · 2026-10-22 · scope: all 16 docs (125k chars), 40 data files, live site + Trustpilot verification*

**Verdict:** This is unusually strong discovery work attached to a commercially incomplete proposal.
The research would survive scrutiny from Rob's CFO. The *deal* would not.

> **Status update (post-review).** The five blocking items below have been fixed and are enforced
> by CI:
> 1. **Our price** → published in [04 · Cost model](../a-proposal/04-AI-STACK-BLUEPRINT.md) (pilot €3.5–5k,
>    Phase 1 €8–12k, care plans €175/€250/mo) and priced per hosting option in
>    [06 · Hosting options](../a-proposal/06-NEXT-STEPS.md#hosting-options).
> 2. **ROI/payback** → [04 · What the time saving is worth](../a-proposal/04-AI-STACK-BLUEPRINT.md#-what-the-time-saving-is-worth),
>    with a worked example (134 h / ~€6,000 per month → payback in ~2–3 months). ⚠ *Corrected 2026-10-23: the earlier "167 h / €7,500 → inside two months" was wrong — the per-order time premise was unsourced and the range did not clear two months at the top of the investment range. See [04](../a-proposal/04-AI-STACK-BLUEPRINT.md#-what-the-time-saving-is-worth).*
> 3. **README `€20/mo` contradiction** → fixed; CI now fails if it reappears.
> 4. **Duplicate hats** → doc 12 rewritten to 31 genuinely distinct hats; CI now fails on
>    duplicate titles or a title/body count mismatch.
> 5. **ChannelDock / 5X verification** → ChannelDock's REST API confirmed to exist from its public
>    settings menu ("API-sleutels & webhooks"); **5X could not be verified publicly** and is now
>    flagged as an export-dependent risk in doc 04 with a question added to doc 06.
>
> The moat claim (#6) was also rewritten: we no longer sell a technical moat, we sell the
> decomposed data asset.
>
> This document is retained as the record of what the review found and what remains open.

---

# PART 1 — THE SIX THINGS THAT MATTER

## 1. The proposal never states our price. *(blocking)*

Doc 04's cost table has a row `Our engagement | Phased, fixed scope` — and nothing else.
Doc 09 says the *market* charges `$3-5k` pilot / `€2-4k/mo` retainer, and recommends that shape
**for us**. But no document ever says "this engagement costs X."

Consequence: Rob cannot evaluate this. Every real buyer computes payback, and there is no number
to compute it against. We have documented everyone else's prices and hidden ours — which reads
either as evasive or as "we haven't decided", and both cost the sale.

**Fix:** one line in doc 04 and one in doc 06. Pilot price, Phase 0–3 phase pricing, monthly
care-plan price per hosting option (a)/(c)/(d) need separate rates, not one blended number.

## 2. No ROI, no payback period, anywhere. *(blocking)*

We never convert "4-hour mornings" into money. The chain is:

```
4h per school order → N orders/week → loaded hourly rate → hours/year → € saved
```

None of those numbers exist in any document. The only adjacent figure is "one costly error/year"
— unquantified. Meanwhile doc 12 hat 12 says *"WiseQ ROI dashboard"* as if it were a *later*
deliverable, when it is the thing that sells the engagement.

**Fix:** a single table in doc 05 — baseline hours, automated hours, saving, cost, payback in
months. Three numbers. Its absence is the single largest gap in the repo.

## 3. Doc 12 contains 9 duplicate hats — self-inflicted. *(quality)*

My own rewrite collided. "50 hats" is 31 headings with **22 unique titles**; hats 16–25 repeat
4–15 nearly verbatim ("(revisited)" in one case). Bodies differ only by markdown bolding.

A reviewer who spots this concludes the padding was manufactured. That is precisely the
impression the doc is trying to avoid.

**Fix:** either genuinely replace 16–25 with new hats (marketplace-fee analyst, NL tax/VAT
specialist, returns-abuse investigator, accessibility auditor, wholesale-channel partner
manager, logistics/customs specialist, school-DPO privacy officer, peak-season staff planner)
or cut the doc to 22 and stop calling it fifty.

## 4. An unrelated credential incident is still open. *(external, not in this repo)*

A credential in a **different** AIW public repo's git history is still valid against a live host.
It is being rotated separately. It is noted here only because the review found it while sweeping
the org, and because an unresolved credential should never be left unwritten in a planning
document. Details stay in the private incident record, not in a client-facing repository.

## 5. The README still says "€20/mo VPS" — contradicting the hosting options we just shipped. *(regression)*

The README architecture block still reads *"Runs on WiseQ's existing 24/7 office machine or a
€20/mo VPS."* Docs 04 and 06 now offer four named options with (b) recommended and (c)
discounted. **The README contradicts both.** This is my merge from PR #4 — I updated 04 and 06
and missed the summary.

**Fix:** README must carry the four options, or drop the cost claim entirely and link to doc 06.

## 6. The "moat" claim is the weakest thing in the repo. *(credibility)*

Doc 09: *"every layer WiseQ needs either doesn't exist as OSS → we build it thin and own it, or
exists as official API → we integrate it... precisely the moat we're selling."*

This is not a moat. "We integrate APIs and write thin connectors" describes every competent
agency. Absence of OSS in a GitHub topic search is weak evidence — commercial tools (Picqer,
EffectConnect, ChannelDock's own suite) fill exactly those gaps, and we ourselves cite Picqer in
doc 08. A buyer with a technical cofounder will spot this in one read.

**Fix:** stop selling the moat. Sell the compounding asset — the EAN spine and the order
history that make *next year's* decisions better than a competitor's. That is defensible and
true.

---

# PART 2 — WHAT SOUNDS LIKE BULLSHIT

| Claim | Where | Why it is weak |
| :--- | :--- | :--- |
| "Cycle time 4h → <15min" | 04, 05 | Never defined: touch-time or elapsed? 15 min of *human* time is a different promise. |
| "25 → 250+ reviews" | 04, 05 | 10x in one quarter with zero automation today. No conversion assumption, no seasonality. Trustpilot explicitly flags "no recent invitations → reviews may not be representative." |
| "Revenue engines" for reviews | 04 | A review is a *permission to be found*, not revenue. Named as revenue with no conversion attached. |
| "4-hour mornings" | throughout | We measured it once, in one meeting. No baseline distribution. "Sometimes 4 hours" ≠ a mean of 4. |
| An asserted gross-margin figure | 09 | Our own cost model stated with nothing behind it — and it was the number that made us look expensive. *(already removed)* |
| "most NL retailers have nothing here" (UCP) | 04, 05 | Unquantified. One counter-example dissolves it. |
| "the reusable-component inventory needs real cost data for AIW pricing" | 12 hat 25 | Leaks that we price components from client work. Internal. |
| "Our privacy-agent design… ships in EU flavor" | 11 §4 | "EU flavor" is not a GDPR position. Vague compliance-as-product. |
| Cert library as marketing asset | 11 §1 | Genuine idea, but stated as settled. We don't know if WiseQ *has* current EN 71 files — that's the open question. |

---

# PART 3 — WHAT WE FOUND THAT'S ACTUALLY EXCELLENT

Do not lose these in a rewrite. They are what makes the repo credible.

- **The bundle spine.** 114 component SKUs + 25 composite bundles, zero unresolved, from public
  catalog data, referentially validated in CI. This is a genuine artifact. It proves we did the
  work *before* being paid, and it directly models their founder's own "long human trail" problem.
- **The catalog audit.** `0/230 EAN`, `0/230 weights`, `0/230 inventory`, 77 combinatorial
  bundles, a real SKU bug (10.9" case carrying 10.2" SKU). Specific, checkable, humble.
- **Lead-gen method.** 8,673 orgs from official DUO open data, 857 with verified emails, whale
  networks named (Auris 12 — hearing/language education, a genuinely sharp insight). Counts
  reconcile to the artifact.
- **Guardrails + reversibility.** Phase 0 writes nothing. Kill switch. Vault. Human gates on
  money. This is what separates a real proposal from a demo reel, and it's well done.
- **The hosting options (doc 06).** Four genuine choices, recommended default stated, and the
  discount's assumption written down so it can't quietly stop applying. Strongest commercial page.
- **Compliance breadth.** RED Aug-2025 cybersecurity layer, GPSR, Thuiswinkel, per-SKU cert
  evidence — mapped, not hand-waved.
- **Engineering CI.** validate_repo.py (37 checks), gitleaks, zizmor. Most client repos have none.

---

# PART 4 — GAPS A COMPLETE PROPOSAL NEEDS

## Commercial (all missing)
1. **Our price** — see #1.
2. **Payback / ROI** — see #2.
3. **Contract shape** — fixed-scope vs retainer, term, exit, IP assignment. Doc 04 says "WiseQ
   owns the repo and all data" — good — but nothing on liability, SLA, or what happens if they
   stop paying.
4. **Pricing per hosting option** — (a)/(d) carry care-plan costs that never appear.
5. **Total cost of ownership at 12 months** — infra + AI + our fee + Thuiswinkel + GS1 + bolt
   hardware, in one table. Currently scattered across four docs.

## Technical
6. ~~**ChannelDock API is assumed, not verified.**~~ **RESOLVED 2026-10-22 — this finding was
   correct and is now closed.** Doc 04 called it "REST, documented"; verification shows ChannelDock
   **does** ship a **REST API + webhooks**, plan-gated from **Voorraad (€45/mo)** and excluded from the
   free tier (which caps at 100 products — WiseQ has 230, so they are almost certainly on a paid plan).
   Doc 08 previously asserted "no public API docs found in searches", which was a search failure, not a
   fact; both docs now agree. **Residual question:** *which* plan, and do they hold the €200/mo PIM?
7. **5X** — **still open.** Its API could not be verified from public sources, so doc 04 carries it
   as an export-dependent risk and doc 06 asks for export access. Do not claim 5X has an API until
   someone confirms it with the vendor or from the account.
8. **Bookkeeping vendor unknown** — the flagship pipeline's billing step depends on a product we
   haven't named. Doc 06 asks for it; nothing works around not knowing.
9. **No rollback/DR plan.** "Reversal path" per layer exists; no backup, restore, or RTO for
   the agent layer itself.
10. **Data model for the registry** — schema, ownership, migration path off Shopify's export.

## Commercial-technical
11. **Dependency risk unstated.** UCP, MCP connectors, and the agent runtime are all
    open-source with shifting maintainers. Doc 04 names Hermes as the foundation and doesn't
    discuss what happens if it stalls. A client who adopts it is making a dependency bet.
12. **No security section at the client boundary** — what the agent can reach, blast radius of a
    compromised connector, who holds admin.

## Credibility
13. **Sources are thin.** Doc 01 cites "Creditsafe, footer, LinkedIn" with no URLs. Doc 11's
    regulatory claims have no article references. Doc 09's Euromonitor/iClever claim is
    paywalled and unverifiable by the client. For a repo whose whole pitch is *we did the
    research*, most findings aren't traceable.
14. **The 30-page manual is still the gate.** Two weeks of Phase 0 blocked on one document.
    Worth flagging as a risk to the client, with a fallback path that starts from the public
    Shopify export.

## Product
15. **Site demos (doc 17)** are strong but run on the *existing* catalog. No mock showing what
    their site looks like with the recommended changes (EAN/weight backfill, review counts,
    cert badges, Thuiswinkel seal). That's the single highest-converting artifact we could add.
16. **No customer-facing proof of *outcomes*.** We show artifacts from a sister project but never
    state a result. Even one anonymized before/after number ("cycle time 4h → 12m") would
    transform the credibility of every phase.

---

# PART 5 — WHAT THE CLIENT WILL ACTUALLY ASK

**Rob, at the next meeting:**
1. "What does this cost, and when does it pay back?" — **we currently cannot answer.**
2. "What happens to my data and my systems if we stop?" — doc 04 answers partially.
3. "Can it work with ChannelDock? Really?" — **unverified.**
4. "Who exactly is doing this?" — doc 06 says "we will introduce the people"; no names, no
   bios, no Dutch-language capability evidence. For an NL founder-led SME this matters.
5. "What if it gets it wrong and books 200 wrong invoices?" — guardrails exist; the *blast
   radius* and the rollback drill do not.
6. "Why you? You did this for a restaurant and a dental practice." — strong question, currently
   unanswered in the repo. The honest answer (transferable patterns, different domains) is
   better than pretending.

**A skeptical technical reader** will check: the 230/189 product counts, the 312-vs-230 drift,
the GS1 arithmetic, and the 4.4/25 Trustpilot figure. I verified the last one live —
**it is correct.** The others are internally consistent across six documents. That consistency
is an asset; keep it.

---

# PART 6 — RANKED FIX LIST

**Do before the next conversation**
1. State our price. (blocking)
2. Add ROI/payback arithmetic. (blocking)
3. Fix the README `€20/mo` contradiction — it's live and it's ours.
4. Rotate the exposed credential. (external, urgent — tracked privately)
5. ~~Verify ChannelDock + 5X API existence.~~ → **ChannelDock done** (finding 6, above). **5X still open** — confirm from the account or the vendor, not from a search.

**Do before sending the repo to Rob**
6. Fix doc 12's 9 duplicate hats.
7. Drop or substantiate the "moat" claim in doc 09.
8. Add sources/URLs to docs 01, 09, 11.
9. Add a contract-shape section.
10. Soften or quantify the three unreferenced targets (15min, 250 reviews, 4h baseline).

**Do when there's time**
11. Add people/credentials section.
12. Add a 12-month TCO table.
13. Build the "future-state mock" of their site.
14. Dependency-risk paragraph in doc 04.
