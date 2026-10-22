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

## 🏗️ Hosting options

There is no single right answer here, and we would rather you choose than have us pick for you. All four options include remote access for us to install, update, monitor, and fix things — that part is the same in every case.

| Option | Where it runs | Who owns the server | What you pay |
| :--- | :--- | :--- | :--- |
| **(a) Yours, managed by us** | A server on your own hosting account, connected to your devices | You own it; we run everything on it | Your hosting cost + a small monthly care plan |
| **(b) Ours, dedicated** | Our infrastructure, a server set up for WiseQ only | We own and operate it | One monthly fee, everything included |
| **(c) Ours, shared capacity** | Our infrastructure, running your jobs — and our own work when yours are idle | We own and operate it | **Reduced rate** — see below |
| **(d) Yours, we set it up** | You open the account; we do all the technical work | You own it after handover | One-off setup fee, then optional care plan |

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
