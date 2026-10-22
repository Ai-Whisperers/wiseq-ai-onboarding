<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track A · Document 06* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Next Steps

## 🚀 What we need from WiseQ

Everything here is **bounded, low-risk, and mostly already in your hands.** None of it requires a production change.

| # | What we need | Why | Effort on your side | Blocks |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **The ~30-page company manual** | Lets us map every tool to its MCP/API availability precisely — no guessing | Send a file | Stack map |
| 2 | **Software inventory** | Which bookkeeping package (Exact? nl.? other?), ChannelDock plan + API access, 5X export access, mailbox provider | A list | Connectors |
| 3 | **Sandbox / dummy data** | A copy of a few anonymized school orders + the offer→invoice flow, so the shadow demo mirrors reality | 30 min to export | Shadow demo |
| 4 | **Read-only API access** *(when ready)* | Shopify (read-only collaborator) · ChannelDock (API token) · bol Seller (sandbox) · mailbox (app-password, read-only first) | Issue 4 tokens | Live read-only |
| 5 | **30 minutes with the purchase manager** | Walkthrough of the EAN/Excel workflow — so we design the replacement against reality, not assumptions | One meeting | Purchase intelligence |
| 6 | **Your annual online turnover (or a rough band)** | **Sets your Thuiswinkel contribution tier — the difference between €518 and €1,294/yr.** We've never asked, and it changes the number we quote. | One number | Trust-mark costing |
| 7 | **Which ChannelDock plan are you on?** (Gratis / Voorraad / Volledig WMS) **And do you have the PIM module?** | **Correcting an earlier note in our own docs:** ChannelDock *does* have a REST API + webhooks, included from Voorraad (€45/mo) upward and excluded from the free tier. Since you have 230 products and the free tier caps at 100, you should already be on a paid plan — we need to confirm, because it decides what we can automate. | Two answers | Connector build |
| 8 | **Do you already use ChannelDock PIM's "Bundels samenstellen"?** | If PIM (€200/mo) already composes bundles, part of what we planned to build is a configuration task, not a build. We'd rather tell you that up front than quote you for it. | One answer | Bundle-scope |

### 🎨 If you want a real storefront (not our 30-minute samples)

The three site concepts in [doc 17](17-SITE-CONCEPTS.md) were each built in about half
an hour as a **speed sample** — they show the quality floor and the pace, not a finished
design. Building something you would actually ship needs five things we don't have:

| # | What | Why it changes the design |
| :--- | :--- | :--- |
| 1 | **Brand assets** — logo files, typefaces, photography, exact colour values | Right now we inferred the brand. Guessing a brand is how you get a site that looks almost-right, which is worse than one that looks clearly different. |
| 2 | **Who it's for** — schools (B2B), parents, gift buyers, neurodivergent households? | Each segment needs its own front door. One site trying to serve all four serves none. |
| 3 | **Which products carry the business** | Which ~20 of the 230 decide the entire homepage. Everything else is browse. |
| 4 | **Language & voice** — NL, EN, both? How do you talk about hearing safety and children's location data? | Some of this is compliance content that has to be present, not marketing copy we invent. |
| 5 | **What must be visible on every page** — 85 dB limits, GPS/location, age ranges | Some of these are legally-required notices, not selling points. |

**None of this needs production access**, and none of it blocks the operations work in
Phase 0. It's only needed when you decide the storefront is worth doing — at which point
it's a scoped piece of work with its own price, not something bundled in.

> 🔁 **Items 1–3 need no production access at all.** We can start the stack map and the EAN registry the same day the manual arrives.

---

## ✅ What we commit to *(Phase 0, ~2 weeks)*

| Deliverable | What it proves | Status |
| :--- | :--- | :--- |
| `data/stack-map.md` | Every tool from your manual, mapped to connector availability | ⬜ Not started |
| **EAN registry v1** | The canonical EAN ↔ SKU ↔ component spine, seeded from ChannelDock + Shopify exports — **no live access needed to start** | ⬜ Not started |
| **Shadow school-order demo** | The pipeline running on dummy data — the "visually, ah, nice" moment promised in the meeting | ⬜ Not started |
| **Read-only dashboard prototype** | Orders, stock, reviews, channel drift — visible without touching production | ⬜ Not started |

---

## 🧭 Decision points for Rob

Four open decisions. Each has a recommended default — if we don't hear otherwise, we proceed with the recommendation and tell you what we're doing.

| # | Question | Options | Our recommendation |
| :--- | :--- | :--- | :--- |
| 1 | **Where does the agent run?** | (a) existing 24/7 office machine · (b) €20/mo VPS · (c) both | **(c)** — VPS as primary, office machine as worker. Survives a power cut at the office. |
| 2 | **Bookkeeping connection style?** | (a) native API if Exact/nl. supports it · (b) browser-automation MCP | **(a) first, (b) as fallback.** API is cleaner; automation is the safety net for vendors without an API. |
| 3 | **Review platform priority?** | Trustpilot (international) · Kiyoh (NL standard) · both | **Both.** Trustpilot for international traffic, Kiyoh for the NL school/B2B segment. |
| 4 | **First revenue engine?** | Review invitations (fastest) · B2B outreach (biggest data advantage) | **Reviews first** — fastest measurable win, and it compounds into every later phase. |

---

## 📬 Response channel

- **This repository is the response channel.** Open an issue or comment on any document — we monitor it and reply there.
- Direct contact details for AI Whisperers (operated through Iván Weiss Van Der Pol, AI/systems) are available on request.

---

## 🗓️ What happens next

```
1. You send the company manual + software inventory
        │
        ▼
2. We build the stack map + EAN registry v1  (week 1)
        │
        ▼
3. Shadow demo on your dummy data  (week 2)
        │
        ▼
4. You review the demo → we agree Phase 1 scope
        │
        ▼
5. Phase 1: the 4-hour mornings stop  (weeks 3–6)
```

---

## 📌 In short

Everything on this list is **bounded, low-risk, and mostly already in WiseQ's hands** — a manual, a software inventory, some anonymized sample orders, and read-only tokens. None of it requires a production change, none of it commits WiseQ to anything, and all of it unblocks a priced Phase 0. **The single most valuable answer is annual online turnover** — it alone determines which Thuiswinkel contribution tier applies and changes the compliance quote.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | What Phase 0 delivers |
| **[Competitors Deals](09-COMPETITORS-DEALS.md)** | Deal shape, benchmarked |
| **[Devops Masterplan](15-DEVOPS-MASTERPLAN.md)** | The production-readiness checklist |
| **[Terms, Ownership & Continuity](18-TERMS-OWNERSHIP-CONTINUITY.md)** | Ownership, the Art. 28 DPA, the exit plan, and what happens if we're unavailable — worth reading before you sign anything |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
