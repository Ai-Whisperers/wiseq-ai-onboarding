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
| 6 | **Your fully-loaded hourly staff cost, and orders per week** | Turns the 4-hour mornings into money. Without it we can only show you the method, not your payback | Two numbers | ROI case |
| 7 | **5X export confirmation** | We could not verify a public 5X API from outside their login. Does your plan allow CSV/XML export? If not, profitability data stays manual | One yes/no | 5X connector |
| 8 | **Which purchasing cooperatives are you already in?** | The *inkoopcollectieven* route (doc 08, doc 11) is the highest-leverage channel per euro — and we do not know your existing position | One list | B2B strategy |

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
| 1 | **Where does the agent run?** | **(a)** your own server, we maintain it · **(b)** our server, dedicated · **(c)** our server, shared capacity · **(d)** you open the account, we do the setup | **(b)** — dedicated on our infrastructure, included in the monthly fee, and the easiest to change later. See [the hosting options](#hosting-options) below. |
| 2 | **Bookkeeping connection style?** | (a) native API if Exact/nl. supports it · (b) browser-automation MCP | **(a) first, (b) as fallback.** API is cleaner; automation is the safety net for vendors without an API. |
| 3 | **Review platform priority?** | Trustpilot (international) · Kiyoh (NL standard) · both | **Both.** Trustpilot for international traffic, Kiyoh for the NL school/B2B segment. |
| 4 | **First revenue engine?** | Review invitations (fastest) · B2B outreach (biggest data advantage) | **Reviews first** — fastest measurable win, and it compounds into every later phase. |

---

<a id="hosting-options"></a>

## 🏗️ Hosting options

There is no single right answer here, and we would rather you choose than have us pick for you. All four options include remote access for us to install, update, monitor, and fix things — that part is the same in every case.

| Option | Where it runs | Who owns the server | What you pay |
| :--- | :--- | :--- | :--- |
| **(a) Yours, managed by us** | A server on your own hosting account, connected to your devices | You own it; we run everything on it | Your hosting cost (€16–21/mo) **+ care plan from €250/mo** |
| **(b) Ours, dedicated** *(recommended)* | Our infrastructure, a server set up for WiseQ only | We own and operate it | **Included** in one monthly figure |
| **(c) Ours, shared capacity** | Our infrastructure, running your jobs — and our own work when yours are idle | We own and operate it | **€175/mo** — reduced, see below |
| **(d) Yours, we set it up** | You open the account; we do all the technical work | You own it after handover | **One-off setup fee**, then care plan from €250/mo (optional) |

**Why (c) is cheaper.** The host is already paid for. School orders arrive in morning batches, reports run weekly, and the nightly jobs are short — so between peaks there is real idle capacity. In option (c) that idle time carries our own work instead of sitting empty, and the saving comes back to you as a lower rate. The discount assumes genuinely bursty usage; if you later want something running continuously, we would move you to the standard rate rather than quietly overcharging you.

**Our recommendation is (b).** It is the lowest-friction start, everything is included in one number, and moving to (a) or (c) later is a configuration change rather than a migration.

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
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | What Phase 0 delivers |
| **[Competitors Deals](09-COMPETITORS-DEALS.md)** | Deal shape, benchmarked |
| **[Devops Masterplan](15-DEVOPS-MASTERPLAN.md)** | The production-readiness checklist |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
