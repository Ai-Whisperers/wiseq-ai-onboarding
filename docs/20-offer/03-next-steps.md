<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track A · Document 06* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Next Steps

## 🚀 What we need from WiseQ

Everything here is **bounded, low-risk, and mostly already in your hands.** None of it requires a production change.

| # | What we need | Why | Effort on your side | Blocks |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **The ~30-page company manual** | Lets us map every tool to its MCP/API availability precisely — no guessing | ✅ **Received 2026-10-27** — [doc 28](../10-client/03-operating-manual.md) · [`data/client/`](../../data/client/OPERATING-MANUAL-EXTRACT.md) | Stack map draft live |
| 2 | **Software inventory** | ChannelDock plan + API access, mailbox provider, confirm FiveX export; **bookkeeping = e-Boekhouden** (from manual) | Confirm remaining gaps | Connectors |
| 3 | **Sandbox / dummy data** | A copy of a few anonymized school orders + the offer→invoice flow, so the shadow demo mirrors reality | 30 min to export | Shadow demo |
| 4 | **Read-only API access** *(when ready)* | Shopify · ChannelDock · bol (per account) · e-Boekhouden · mailbox — **step-by-step + links:** [Read-only access guide](../start/rob/read-only-access.md) | ~30–45 min wave 1 | Live read-only |
| 5 | **30 minutes with the purchase manager** | Walkthrough of the EAN/Excel workflow — so we design the replacement against reality, not assumptions | One meeting | Purchase intelligence |
| 6 | **Your annual online turnover (or a rough band)** | **Sets your Thuiswinkel contribution tier — the difference between €518 and €1,294/yr.** We've never asked, and it changes the number we quote. | One number | Trust-mark costing |
| 7 | **Which ChannelDock plan are you on?** (Gratis / Voorraad / Volledig WMS) **And do you have the PIM module?** | **Correcting an earlier note in our own docs:** ChannelDock *does* have a REST API + webhooks, included from Voorraad (€45/mo) upward and excluded from the free tier. Since you have 230 products and the free tier caps at 100, you should already be on a paid plan — we need to confirm, because it decides what we can automate. | Two answers | Connector build |
| 8 | **Do you already use ChannelDock PIM's "Bundels samenstellen"?** | Manual already shows **native ChannelDock bundles** (stock→0 → mark bundle → add mothers). PIM (€200/mo) may be redundant — confirm what you pay for vs what you already use. | One answer | Bundle-scope |

### 🎨 If you want a real storefront later

A shippable WiseQ storefront is **out of scope for Phase 0–1** (operations first).
If you later want a redesign, building something you would actually ship needs five things we don't have:

| # | What | Why it changes the design |
| :--- | :--- | :--- |
| 1 | **Brand assets** — logo files, typefaces, photography (exact colours now known: `#26b5b7` / `#1648ad` from manual) | Colours locked; still need logo files, typefaces, photography for a shippable site. |
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
| `data/stack-map.md` | Every tool from your manual, mapped to connector availability | 🟡 **Draft started** (manual ingested) — needs plan tier + tokens |
| [Doc 28 · Client manual](../10-client/03-operating-manual.md) | Manual translated into proposal corrections | ✅ Done |
| **EAN registry v1** | The canonical EAN ↔ SKU ↔ component spine, seeded from ChannelDock + Shopify exports — **no live access needed to start** | ⬜ Not started |
| **Shadow school-order demo** | The pipeline running on dummy data — the "visually, ah, nice" moment promised in the meeting | ⬜ Not started |
| **Read-only dashboard prototype** | Orders, stock, reviews, channel drift — visible without touching production | ⬜ Not started |

---

## 🧭 Decision points for Rob

Four open decisions. Each has a recommended default — if we don't hear otherwise, we proceed with the recommendation and tell you what we're doing.

| # | Question | Options | Our recommendation |
| :--- | :--- | :--- | :--- |
| 1 | **Where does the agent run?** | **(e) Hermes Desktop on your Windows laptop** (Milestone 1) · **(a)** your own always-on server · **(b)** our server, dedicated · **(c)** our shared capacity · **(d)** you open the account, we set up | **(e) first for interactive assistant** — proven in the [test lab](../../lab/README.md). Always-on cron (assortment sweeps) later uses a **companion VPS** (doc 24), not the laptop alone. Resolves prior **06(b) vs 24 v2** tension: Desktop = Rob’s seat; VPS = scheduled ops when ready. |
| 2 | **Bookkeeping connection style?** | (a) native **e-Boekhouden** API if endpoints + permissions support offers/invoices/relations · (b) browser-automation MCP fallback | **(a) first, conditional on API feasibility check; (b) as fallback.** Package is e-Boekhouden (client manual) — not Exact. |
| 3 | **Review platform priority?** | Trustpilot (international) · Kiyoh (NL standard) · both | **Both.** Trustpilot for international traffic, Kiyoh for the NL school/B2B segment. |
| 4 | **First revenue engine?** | Review invitations (fastest) · B2B outreach (biggest data advantage) | **Reviews first — bol.com primary, Trustpilot/Kiyoh secondary** (manual’s daily ops already run bol review triage; Trustpilot alone would miss their scoreboard). |

---

<a id="hosting-options"></a>

## 🏗️ Hosting options

There is no single right answer here, and we would rather you choose than have us pick for you. All four options include remote access for us to install, update, monitor, and fix things — that part is the same in every case.

| Option | Where it runs | Who owns the server | What you pay |
| :--- | :--- | :--- | :--- |
| **(e) Hermes Desktop** *(Milestone 1)* | Your Windows laptop — [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) | You (profile backup required) | Model API cost only during pilot lab |
| **(a) Yours, managed by us** | Always-on companion VPS for cron | You own it; we run it | Hosting (€16–21/mo) **+ care plan from €250/mo** |
| **(b) Ours, dedicated** | Our infrastructure, WiseQ-only | We own and operate it | **Included** in one monthly figure |
| **(c) Ours, shared capacity** | Shared AIW capacity | We own and operate it | **€175/mo** — reduced, see below |
| **(d) Yours, we set it up** | You open the account; we do setup | You own it after handover | **One-off setup fee**, then care plan from €250/mo (optional) |

**Milestone 1 recommendation: (e).** Interactive assistant on Hermes Desktop against the synthetic [lab](../../lab/README.md) — no production credentials. **Always-on jobs** (06:30 sweeps) need (a)/(b)/(d) later because laptops sleep; that companion does not replace Desktop as Rob’s seat.

**Why (c) is cheaper (when used).** Burst school-order peaks leave idle capacity; shared rate assumes that. Continuous loads move to standard rates.

Whichever you choose: the agents never hold credentials that only they can reach, every action is logged, and you can pause any automation with one command.

## 📬 Response channel

- **This repository is the response channel.** Open an issue or comment on any document — we monitor it and reply there.
- Direct contact details for AI Whisperers are available on request — we will introduce the people who will actually do the work.

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

Everything on this list is **bounded, low-risk, and mostly already in WiseQ's hands** — a manual, a software inventory, some anonymised sample orders, and read-only tokens. None of it requires a production change, none of it commits WiseQ to anything, and all of it unblocks a priced Phase 0. **The single most valuable answer is annual online turnover** — it alone sets the Thuiswinkel contribution tier (**€983–1,759/yr**) and changes the compliance quote.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Ai Stack Blueprint](01-blueprint.md)** | What Phase 0 delivers |
| **[Competitors Deals](../30-market/02-competitors-deals.md)** | Deal shape, benchmarked |
| **[Devops Masterplan](../40-build/04-devops.md)** | The production-readiness checklist |

> **Not sure where to start?** [Role packs](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/README.md) (Rob / Kiki / ops) or the [document map](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map).
