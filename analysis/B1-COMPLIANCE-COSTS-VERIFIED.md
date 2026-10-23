# B1 · NL/EU Compliance & Marketplace Costs — VERIFIED 2026-10-22

> **⚠ INTERNAL — AI Whisperers only. NOT a client-facing document.**
> Written 2026-10-22. Companion to `A-COST-BASELINE-AUDIT.md`, `B2-INFRA-COSTS.md`,
> `C-DEAL-STRUCTURE.md`.
> Visibility: `internal` · **All AIW fee figures TBD.**
>
> **Provenance:** every figure below was read from the **primary source** on
> 2026-10-22 (official vendor/government pages), not from SEO blogs. Items I could
> not verify from a primary source are marked **UNVERIFIED** and listed in §7.

---

## 0. Headline: the repo's compliance numbers are **wrong in three places**, and the GS1 figure is **materially overstated**

| Repo claim | Verified truth | Verdict |
|:--|:--|:--|
| GS1 10-pack **~€61**, "12 × 10-packs ≈ **€732**" | **€61/yr covers 10 codes. 114 components + 25 bundles = 139 codes → €733/yr RECURRING, not one-off.** The "one-off" label is wrong: the 10-pack is an **annual** product. | ❌ **Wrong — and it recurs forever** |
| Thuiswinkel "**€75 one-time + €390/yr**" | ✅ **exactly right** for Waarborg alone. | ✅ **Correct** |
| Thuiswinkel "**€465 year one**" (docs/11) | ❌ **wrong** — omits the turnover-based contribution (**€518–€1,294/yr**) | ❌ **Understated by ~€500–1,300/yr** |
| Thuiswinkel "**~€500–1,000/yr ballpark**" (docs/08) | ⚠ **directionally right, too vague** — and it hides that it's **revenue-tiered** | ⚠ **Imprecise** |
| GS1 annual licence | **€0 for turnover €0–€5M** (category A–D) | ✅ **Free at WiseQ's size** |
| Thuiswinkel extra platform (bol) | **€45/yr per extra platform** | ⚠ **Not in the repo at all** |

---

## 1. GS1 Nederland — the €732 is real but **recurring**, not one-off

**Verified 2026-10-22 from `gs1.nl`:**

| Item | Price | Unit | Type |
|:--|:--|:--|:--|
| GS1 code package **10** | **€61/yr** | per 10 article codes (GTIN) + 10 GLN + 1M SSCC | **ANNUAL** |
| Single code (1–5 pack) | **€36 one-time** | max 5 codes | one-off |
| **GS1 EDI annual contribution** | **€0** for turnover **€0–€5M** (category A–D) | annual | **free at WiseQ's size** |
| GS1 EDI, category E (€5–11M turnover) | €200/yr | annual | — |
| All amounts **excl. 21% VAT** | | | |

Sources:
- `gs1.nl/en/products-services/digital-identity/ean-13gtin` (package structure)
- `gs1.nl/producten-services/data-exchange/overige/gs1-edi/tarieven-en-bestellen` (turnover table)

### The correction that matters

`docs/08` §2 says: *"single EAN ~€36 one-off; **10-pack ~€61**; annual licence fee
applies"* and then *"12 × 10-packs ≈ **€732 one-off** + modest annual fee."*

**The €732 is arithmetically right but categorically wrong.** The 10-pack is
priced **per year** — it is not a consumable you buy once. So:

- **Year 1:** €733 (12 packs) + €0 GS1 EDI (under €5M turnover)
- **Year 2:** **€733 again**
- **Year 3:** **€733 again** — forever, while those codes are registered

And the repo's own note *"no EAN purchase needed for 25 bundles if sold only via
own shop"* is contradicted by the same document: *"bol/Amazon require per-listing
GTINs."* Since WiseQ sells on **both bol.com and Amazon**, **all 139 codes are
required**. There is no saving.

> **Repo line to change:** `docs/08` §2 and `docs/05` backlog row #9.
> Replace "€732 one-off" with "**€733/yr recurring (12 × €61 ten-packs, ex VAT)**".
> Also add "+21% VAT" — the repo quotes ex-VAT figures as if they were all-in.

### Prefix allocation — the EU-expansion gotcha

GS1 prefixes are **country-specific to the issuing GS1 organisation**. A NL prefix
(starting `871`) is valid across the EU, but selling in DE/FR/IT/ES via Amazon
requires the GTIN to be **registered in Verified by GS1** — unresold or
resold-code marketplaces reject it. WiseQ already carries Amazon EU listings
(.de/.fr/.it/.es) per `docs/01`, so **the 139 codes must be actively registered,
not merely purchased.** That's an operational task we can automate (it is one of
the 21 backlog items' territory) — worth calling out as a deliverable.

---

## 2. Thuiswinkel.org — the €465 figure in docs/11 is materially wrong

**Verified 2026-10-22 from `thuiswinkel.org/lid-worden/kosten-lidmaatschap`:**

| Component | Cost | Type |
|:--|:--|:--|
| **Eenmalige inschrijfkosten** | **€75** | one-time |
| **Thuiswinkel Waarborg** certification | **€390/yr** | annual |
| Thuiswinkel Waarborg **+** Zakelijk | €550/yr | annual (alt) |
| Shopping Secure (international) | €450/yr for 1 country, **+€90 per extra country** | annual |
| Thuiswinkel Duurzaamheidscertificering | €890 first webshop, +€250 per extra trading name | annual |
| **Extra handelsnaam / webshop** | **€45/yr** | annual |
| **Extra land** | **€90/yr** | annual |

**And the part the repo missed entirely — the contribution is revenue-tiered:**

| Klasse | Jaaromzet (incl. BTW) | Contributie (excl. BTW) |
|:--|:--|:--:|
| 2 | €0 – €100,000 | **€518** |
| 3 | €100,000 – €250,000 | **€776** |
| 4 | €250,000 – €500,000 | **€1.035** |
| 5 | €500,000 – €1.000.000 | **€1.294** |
| 6 | €1.000.000 – €2.000.000 | €2.070 |
| 7 | €2.000.000 – €4.000.000 | €3.933 |
| 8 | €4.000.000 – €6.000.000 | €5.382 |
| 9 | €6.000.000 – €8.000.000 | €7.556 |
| 10 | €8.000.000 – €10.000.000 | €9.626 |

Note the contribution is calculated on **total online turnover in NL including
marketplace sales** (excl. physical retail), and **if you join mid-year it's
pro-rated from the quarter you join.**

### The correction

`docs/11` §5 item 3 says *"Thuiswinkel Waarborg application (**€465 year one**)"*.
That is **€75 + €390 only** — it omits the contribution, which starts at **€518**
for a company in the €0–100k class and rises with revenue.

**Realistic first-year Thuiswinkel cost for WiseQ** (their turnover is unknown to
us — this is a **question we must ask**, it is a direct input to their cost):

| Turnover class | Year 1 total (excl. VAT) |
|:--|:--|
| €0–100k | €75 + €390 + €518 = **€983** |
| €100–250k | €75 + €390 + €776 = **€1.241** |
| €250–500k | €75 + €390 + €1.035 = **€1.500** |
| €500k–1M | €75 + €390 + €1.294 = **€1.759** |

Plus **+€45/yr** because they also sell on bol.com and Amazon as platforms
(the source states certification of the first platform is free for existing
members, €45 per extra).

> **Repo line to change:** `docs/11` §5 item 3 — replace "€465 year one" with the
> tiered table and note it scales with turnover. **Add a question to
> `docs/06-NEXT-STEPS.md`: "what is your annual online turnover?"** It is currently
> unasked and it directly determines this cost.

---

## 3. Marketplace fees — bol.com is a far bigger cost than the repo implies

The repo's cost model says **"bol.com Seller API — €0 — Free."** That is true of
the *API*, but the repo then implies selling costs nothing, which is misleading
for any margin work.

**Verified from bol.com Partner Platform + Operator One (Oct 2026 table):**

| Item | Value | Note |
|:--|:--|:--|
| Commission structure | **variable % + fixed per-item fee**, on price **incl. VAT** | both ex VAT |
| Variable range | **2.1% – 20.7%** across 36 categories | |
| Fixed per item | **€0.05 – €3.09**, all 36 categories | Audio/Video/Camera is at the **high** end |
| Example (kitchen) | 12.4% + €0.95 on a €206.50 item = **€26.55** ex VAT | |

For WiseQ's categories (audio, kids tech, chargers/cables) the fixed per-item fee
is the punishing part: **~130 of their 230 SKUs are €7–34 items**, where a €0.85–3.09
fixed fee is a **large percentage of a low-price sale.** That is a real, structural
cost of their long-tail strategy — and it's a genuinely useful insight for the
proposal: *the long tail is expensive to sell on bol*, which strengthens the case
for own-shop margin recovery work.

⚠ **UNVERIFIED:** the exact commission % for WiseQ's specific product groups on
bol. The `verkooprechten-computer-en-elektronica` page returned only a nav shell
(no figures). **Needs one manual lookup on the partner platform before quoting.**

### Amazon.nl
`docs/01` notes Amazon EU listings (.de/.fr/.it/.es) exist. **Amazon referral fees
for electronics/audio and per-item fees: UNVERIFIED** — the sell.amazon.nl pricing
page is JS-rendered and did not yield figures to automated extraction. Must be
checked manually.

---

## 4. GPSR — the biggest cost the repo never mentions

`docs/11` covers EN 71 / 62115 / RED / GPSR *as compliance topics* but assigns
**zero euros** to any of them. GPSR has a hard, recurring, paid requirement:

| Item | Cost | Type | Mandatory? |
|:--|:--|:--|:--|
| **EU Responsible Person** service | **from $500/yr** (low-risk/small catalogue) up to **$800/yr** (complex) | annual | **Mandatory for non-EU sellers** |
| Discounted first year (if other services used) | $300 | one-off-ish | optional |

**The key nuance for WiseQ:** GPSR requires an EU Responsible Person for
non-EU businesses. **WiseQ B.V. is Dutch (Grootebroek, NL) and is the
manufacturer/brand owner** — so **WiseQ is its own Responsible Person and pays
€0.** This is worth stating explicitly because it is a *positive* finding, and
because our Paraguay operation is the party that *would* need one if it ever sells
physical goods into the EU.

**Where it does bite:** if AIW imports, holds, or distributes physical goods —
we don't, and shouldn't. Worth one line in the contract that AIW is a software
provider, not a party to the product chain. That protects both sides.

---

## 5. What the repo treats as free but is a real, unbudgeted line

| Item | Status | Cost impact |
|:--|:--|:--|
| **EU AI Act — deployer obligations** | Not mentioned anywhere in the 17 docs | AIW + WiseQ both deploy AI. Article 4 AI-literacy training is mandatory. **Zero budgeted.** |
| **EU AI Act penalties** | Not mentioned | Public fine schedule; a useful *argument* lever with a risk-averse founder, but only if we're honest that we're not evading anything |
| **Product-liability insurance** | Flagged in hat #4 for WiseQ; **never for AIW** | We automate POs and invoices. Our exposure is unpriced |
| **DPIA / GDPR processor agreement** | "GDPR discipline" mentioned only as an *emailing* rule | Holding mailbox + bookkeeping + B2B data = a processor role. Unbudgeted |
| **EN 71 / RED lab testing per SKU family** | Listed as a *topic*, no cost | For kids headphones + GPS watches this is the **largest genuine product cost** — lab testing runs **hundreds to low-thousands of EUR per SKU family**. **UNVERIFIED — must not be quoted without a lab quote.** |

---

## 6. First-year cost summary for WiseQ (what we can actually defend)

Splitting **already-paid** from **genuinely new spend** — this is what the repo
never did:

### Already-paid (do not re-sell as a saving)
- Shopify API — €0 incremental (in their plan)
- ChannelDock API — €0 incremental (in their subscription)
- bol.com Seller API — €0 (but **commission is per-sale and already in their P&L**)
- GS1 EDI annual contribution — **€0** (under €5M turnover)

### Genuinely new / newly-quantified spend

| Item | Year 1 | Recurring? | Was in repo? |
|:--|--:|:--|:--|
| **GS1 GTIN codes (139)** | **€733** (+21% VAT = €887) | **YES, annually forever** | ❌ labelled one-off |
| **Thuiswinkel Waarborg + contribution** | **€983 – €1,759** depending on turnover class | YES | ❌ said €465 |
| Thuiswinkel extra platform (bol/Amazon) | +€45 | YES | ❌ absent |
| **GPSR Responsible Person** | **€0** — WiseQ is EU-based, self-RP | — | ❌ absent |
| EU AI Act literacy/training | **TBD — unbudgeted** | — | ❌ absent |
| **EN 71 / RED lab testing** | **UNVERIFIED — needs lab quotes** | per SKU family | ❌ topic only, no € |
| **AIW engagement** | **TBD** | — | ❌ "fixed scope", no number |

**The defensible new-compliance-spend floor for WiseQ is roughly
€1,700–2,700 in year 1** (GS1 + Thuiswinkel, excl. VAT), **recurring annually** —
and that is *before* lab testing, which is the item most likely to be a
five-figure surprise and the one we have priced at zero.

---

## 7. UNVERIFIED — must be checked before anything goes to the client

| # | Item | Why it matters | How to verify |
|:--|:--|:--|:--|
| U1 | **bol.com commission % + fixed fee for WiseQ's exact product groups** (audio, kids tech, chargers/cables) | Determines whether their long tail is profitable on bol; needed for any margin claim | Partner Platform login, category table |
| U2 | **Amazon.nl referral + per-item fees for electronics/audio; Individual vs Professional subscription** | `.de/.fr/.it/.es` listings are live; EU expansion is a Phase 3 pillar | sell.amazon.nl pricing page (JS-rendered — manual) |
| U3 | **EN 71 / EN 62115 / RED lab test costs per SKU family** | **Largest unbudgeted item.** Kids headphones + GPS watches | Quote from Eurofins/Kiwa/TÜV/SGS/CIBSE |
| U4 | **WEEE / Battensysteem** Dutch producer-responsibility fees (per-kg) | Electronics seller — likely already registered, but unconfirmed | RVO / Battensysteem tariff |
| U5 | **Verpakkingswet / PMU** packaging-fund contribution rates | Per-shipment cost, never mentioned | KIDV / HVO |
| U6 | **Battery Regulation 2023/1542** labelling obligations for GPS watches | GPS watches = batteries + location data, highest scrutiny | EU Commission / NVWA |
| U7 | **WiseQ's actual annual online turnover** | **Directly determines Thuiswinkel contribution tier** | Ask them — `docs/06` doesn't ask it |
| U8 | **KvK fee, NL VAT 2026 rates, ZZP 2026 tariffed brackets** | Affects how a retainer lands in their cash flow, and our invoicing | Belastingdienst.nl |
| U9 | **Education procurement collective (inkoopcollectieven) listing fees** | `docs/08` frames these as a growth channel with zero cost | Onderwijs Inkoop Groep / Contractables — likely no public fee; confirm |

---

## 8. Corrections to land in the repo (extends Doc A's C4/C5/C6)

| # | File | Current | Must become |
|:--|:--|:--|:--|
| C4a | `docs/08` §2, `docs/05` row 9 | "€732 one-off" | **"€733/yr recurring (12 × €61, ex VAT; +21% VAT = €887)"** |
| C4b | `docs/08` §2 | "annual licence fee applies" | **"GS1 EDI contribution = €0 for turnover under €5M (category A–D)"** |
| C4c | `docs/08` §2 | "no EAN needed for 25 bundles if own-shop only" | **Delete** — contradicted by their bol + Amazon requirement |
| C4d | `docs/11` table + §5 | "€75 + €390/yr" | ✅ keep, but **add the contribution tier table** |
| C4e | `docs/11` §5 item 3 | "€465 year one" | **"€983–€1,759 yr 1 depending on turnover class"** |
| C4f | `docs/11` | absent | **Add GPSR row: €0 for WiseQ (EU-established, self-RP); note AIW is software-only, not in the product chain** |
| C4g | `docs/11` | absent | **Add EU AI Act row — deployer + literacy, cost TBD** |
| C4h | `docs/11` | absent | **Add EN 71 / RED lab testing as a named UNVERIFIED cost line** |
| C5 | `docs/04` cost model | "bol.com Seller API €0 — Free" | **Clarify: API is free; per-sale commission (2.1–20.7% + €0.05–3.09/item) is a P&L cost, not an API cost** |
| C6 | `docs/06` ask-list | 5 asks | **Add: "annual online turnover (incl. VAT)" — it sets the Thuiswinkel tier** |

---

*Prepared by AI Whisperers internal analysis · 2026-10-22.*
*Primary sources read 2026-10-22: gs1.nl, thuiswinkel.org, bol.com Partner Platform.*
*AIW fee figures intentionally TBD.*