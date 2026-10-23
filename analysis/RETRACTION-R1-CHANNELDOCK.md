# ⚠ RETRACTION — R1 (ChannelDock / 5X "no API") was WRONG

> **INTERNAL — AI Whisperers only.** Written 2026-10-22, same day as `C-DEAL-STRUCTURE.md`.
> This document **retracts a claim made earlier today in this same analysis set.**
> It is kept as a permanent record rather than quietly edited out, because
> *how* the error happened matters more than the error.

---

## 1. What I claimed

In `C-DEAL-STRUCTURE.md` I listed as **R1, severity "Critical"**:

> *"ChannelDock/5X have no API. Phase 1's flagship needs to write to ChannelDock."*

and in the same document:

> *"**Phase 0 risk:** the stack map may reveal that **ChannelDock and 5X cannot be
> automated at all**… Nothing in the repo flags this."*

I also told Ivan directly, in chat:

> *"ChannelDock and 5X have no public API, and Phase 1's flagship pipeline must
> write back into ChannelDock. If that's true, we're selling a pipeline that
> can't complete."*

**It is not true. Both systems have APIs.** The claim is retracted in full.

---

## 2. What the evidence actually shows

### 2.1 ChannelDock — REST API + webhooks exist, and are plan-gated

Verified 2026-10-22 from `channeldock.com/nl/prijzen` (primary source, their own
pricing page):

| Plan | Price/mo (excl. VAT) | **REST API** | B2B portal | PIM | Unlimited SKUs |
|:--|--:|:--:|:--:|:--:|:--:|
| **Freemium / Gratis** | **€0** | ❌ **NOT included** | ❌ | ❌ | ❌ (100 products) |
| **Voorraad** | from **€45** | ✅ *"Prioriteitschat, **REST API** en webhooks"* | ✅ included €0 extra | — | ✅ |
| **Volledig WMS** | from **€135** | ✅ | ✅ | — | ✅ |
| **PIM** (separate module) | **€200** self-service | — | — | ✅ | — |

Other verified facts:
- **213+ integrations** live and maintained (Shopify, bol.com, Amazon, WooCommerce,
  Kaufland, Zalando, Mirakl, PostNL, DHL, **FiveX**, Returnless, xentral, …).
- ChannelDock is a **bol.com Bronze Partner** (verified on bol's partner platform).
- **REST API and webhooks are explicitly excluded from the free plan** and
  included from **Voorraad (€45/mo)** upward.
- **Inventory sync runs every 15 minutes**; B2B wholesale portal supported.

### 2.2 FiveX — has a documented direct bol.com API connection

Verified 2026-10-22 from FiveX's own help centre
(`intercom.help/fivex/en/articles/6474821`):

- FiveX has a **first-party "API koppelingen" (API links)** section:
  `Settings > API Links > Add Sales Channel`.
- It takes **bol.com Client ID + Client Secret**, retrieved from
  `partner.bol.com/sdd/preferences/services/api`.
- Purpose per FiveX: *"marketplace profit analytics, orders, ads, repricing,
  voorraad, LVB-economie, retouren en finance-ready exports."*
- And **FiveX is itself listed as a ChannelDock integration** (`channeldock.com/nl/fivex/`).

So the two systems are not isolated islands — they are connected to each other.

---

## 3. How the error happened (the part that actually matters)

`docs/08-OSS-INTEGRATIONS.md:36` says, verbatim:

> *"**ChannelDock & 5X** — no public API docs found in searches; both are SaaS
> dashboards. Approach: agent via browser-automation (computer-use) initially,
> request API access from vendor."*

**I read that line, repeated it, and escalated it to "Critical."** I never opened
`channeldock.com` or FiveX's help centre. I treated a *search failure recorded by a
previous session* as an established fact.

This is the precise failure the anti-laziness protocol names: **grep-and-inherit.**
The repo's own hedge — *"no public API docs **found in searches**"* — describes an
absence of evidence, and I converted it into evidence of absence.

> **The repo was more careful than I was.** It said "not found in searches."
> I wrote "cannot be automated at all."

**Correction to the record:** the original repo statement is *incomplete* (the
API exists and is documented) but its *caution* was sound. My amplification was the
defect.

---

## 4. What the verified position actually is (and the real remaining risk)

The API exists. The real constraint is **commercial, not technical**:

| Finding | Consequence |
|:--|:--|
| REST API/webhooks are **excluded from ChannelDock's free plan** | If WiseQ is on Freemium, the agent layer **cannot** use the API without an upgrade |
| Voorraad = **from €45/mo** excl. VAT | The upgrade is **cheap** — but it is **new spend we did not budget** |
| PIM = **€200/mo**, separate, 3-month or annual contract | Directly relevant: **PIM has "Bundels samenstellen" (bundle composition)** — the exact thing we planned to build ourselves! |
| Free plan caps at **100 products** | WiseQ has **230 products** → **they cannot be on the free plan.** They must be on ≥Voorraad. ✅ API therefore almost certainly available to them already. |
| Free plan caps at **500 orders/mo** | Useful for sizing |

### ⚠ The genuine finding underneath my wrong one

**WiseQ has 230 products, so they cannot be on ChannelDock's free tier (100-product
limit). They are therefore already on a paid plan — which from €45/mo includes the
REST API and webhooks.**

This means:
1. `docs/04`'s "ChannelDock API — €0, already in their subscription" is **correct**,
   and B1's "€0 incremental" is **correct**. My R1 undercut both.
2. **The Phase 1 flagship is not blocked.** It was never blocked.
3. **We must still ask which plan they're on** (`docs/06`) — because if they're on
   Volledig WMS vs Voorraad vs +PIM, that determines what we can automate and
   whether their PIM already does bundle composition (which would shrink our
   scope — or reveal that their €200/mo PIM is underused).

### 🔴 New finding the retracted claim obscured

**ChannelDock's PIM module advertises "Bundels samenstellen" (compose bundles),
variant management, per-channel translation, and content quality scores.**

`docs/05` backlog item #2 ("Bundle recombination engine") and the entire
**bundle-spine** deliverable may be **partially solvable with a feature WiseQ can
already buy for €200/mo**. We may be proposing to build what they can switch on.

**This is a genuine scoping risk and it is the opposite of R1**: not "we can't do
it" but "**they may already be able to do it, and we should say so**." Proposing to
build a €200/mo feature as bespoke consulting is the fastest way to lose the room.

---

## 5. Corrections to apply

| # | Doc | Correction |
|:--|:--|:--|
| **X1** | `C-DEAL-STRUCTURE.md` **R1** | **DELETE the risk row.** It is false. |
| **X2** | `C-DEAL-STRUCTURE.md` §Phase 0 risk paragraph | **DELETE.** Superseded by this document. |
| **X3** | `C-DEAL-STRUCTURE.md` §stack-map row ("ChannelDock + 5X have no public API") | **REWRITE:** both have APIs; ChannelDock REST API + webhooks are plan-gated (Voorraad €45+); FiveX has a documented bol.com API link. |
| **X4** | `C-DEAL-STRUCTURE.md` §effort ("2 browser-automation adapters for APIs that don't exist") | **REWRITE:** no browser automation needed for these two; effort drops. |
| **X5** | `C-DEAL-STRUCTURE.md` §expectations ("Phase 0 may conclude ChannelDock can't be automated") | **DELETE.** It cannot conclude that; it's already answered. |
| **X6** | new | **Add to `docs/06-NEXT-STEPS.md`:** "Which ChannelDock plan are you on (Gratis / Voorraad / Volledig WMS), and do you have the PIM module?" |
| **X7** | new | **Add to Phase 0 scope:** verify whether PIM's "Bundels samenstellen" already covers backlog #2. If so, scope shifts from *building* to *using + extending*. |
| **X8** | `docs/08:36` | **FIX IN REPO:** replace "no public API docs found in searches" with the verified API status + plan gating. The repo's error is the seed of mine. |
| **X9** | `B1` §6 / `A` §1 | **No change needed** — "ChannelDock API €0 incremental" is now *confirmed* correct, not merely assumed. |

---

## 6. The lesson, recorded

**Inherited "not found in searches" is not "does not exist."**

Before repeating a predecessor's negative finding as a critical risk:
1. Open the vendor's own site.
2. Open their developer/help documentation.
3. Check whether the limitation is **technical** or **commercial** — this one is
   purely commercial (a €45/mo plan tier).

Three minutes of primary-source reading would have prevented a fabricated
"Critical" risk in a client-facing strategy document — and, worse, would have
**prevented the PIM discovery that could genuinely reshape the proposal.**

---

*Prepared by AI Whisperers internal analysis · 2026-10-22.*
*Primary sources: channeldock.com/nl/prijzen, channeldock.com/nl/kanalen,
partnerplatform.bol.com/nl/cpdp/channeldock, intercom.help/fivex article 6474821.*
*This retraction supersedes the R1 risk in `C-DEAL-STRUCTURE.md`.*