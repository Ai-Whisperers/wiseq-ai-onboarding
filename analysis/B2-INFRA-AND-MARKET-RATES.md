# B2 · Infrastructure & Market Rates — VERIFIED 2026-10-22

> **⚠ INTERNAL — AI Whisperers only. NOT a client-facing document.**
> Written 2026-10-22. Companion to `A-COST-BASELINE-AUDIT.md`,
> `B1-COMPLIANCE-COSTS-VERIFIED.md`, `C-DEAL-STRUCTURE.md`.
> Visibility: `internal` · **All AIW fee figures TBD.**

---

## 0. Headline: the repo's "€0 – €20/mo infrastructure" is **directionally wrong**, not just stale

The correct figure for a real production agent layer is **€21–55/mo, not €0–20** —
and that excludes the AI token tier entirely. The €0 option depends on running on
WiseQ's office PC, which the repo itself calls a dependency, not a plan.

---

## 1. Compute — Hetzner (best fit: German/EU, GDPR-compliant, 20TB traffic included)

**Verified 2026-10-22 from hetzner.com, all prices excl. VAT:**

| Plan | vCPU | RAM | Storage | **€/mo** | Hourly | Traffic |
|:--|:--:|:--:|:--:|--:|--:|:--|
| CX23 | 2 | 4 GB | 40 GB NVMe | **€5.99** | €0.0096 | 20 TB |
| CX33 | 4 | 8 GB | 40 GB NVMe | **€8.99** | — | 20 TB |
| CX43 | 8 | 16 GB | 80 GB NVMe | **€16.49** | — | 20 TB |
| CX53 | 16 | 32 GB | 160 GB NVMe | **€29.99** | — | 20 TB |
| CAX11 | 2 (Ampere) | 4 GB | 40 GB NVMe | **€6.49** | €0.0104 | 20 TB |
| CAX21 | 4 (Ampere) | 8 GB | 80 GB NVMe | **€10.99** | — | 20 TB |
| CAX31 | 8 (Ampere) | 16 GB | 160 GB NVMe | **€21.49** | — | 20 TB |
| CAX41 | 16 (Ampere) | 32 GB | 320 GB NVMe | **€41.49** | — | 20 TB |
| CPX22 (regular, dedicated) | 3 | 8 GB | 80 GB | **€19.99** | — | 20 TB |
| CPX32 | 4 | 16 GB | 160 GB | **€35.99** | — | 20 TB |

- EU locations (Falkenstein/Nuremberg/Helsinki) include **at least 20 TB traffic**;
  extra TB **€1.00/hour**.
- **⚠ Availability caveat:** several plans rendered as *"not available"* /
  *"This product is currently unavailable"* at scrape time. **Verify the plan is
  orderable before quoting it to a client.**
- **GDPR:** Hetzner is German, GDPR-compliant, ISO/IEC 27001 — this matters
  because WiseQ is an EU client with EU customer data.

**→ Recommended production config for WiseQ: CAX31 (8 vCPU / 16 GB) at €21.49/mo**
for Phase 1–2 (Postgres + agent runtime + backups + R2 sync), or **CX43 at €16.49**
on shared vCPU if load is light. The repo's €20 figure happens to land near CAX11,
but CAX11's 4 GB is **too small** for Postgres + agent runtime + observability.

## 2. Database — Neon (verified)

| Plan | Price | Included | Notes |
|:--|:--|:--|:--|
| **Free** | **$0** | 100 projects, **100 CU-hrs/mo per project**, **1 GB storage**, sizes up to **2 CU (8 GB RAM)**, scales to zero after 5 min idle, 5 GB object storage | ✅ genuinely free |
| Launch | usage-based | $0.002/branch-hr, **$0.106 per CU-hour**, $0.35/GB-mo | up to 16 CU |
| Scale | usage-based | $0.222 per CU-hour | up to 56 CU |

Neon Object Storage: **$0.023/GB-mo**, no per-operation charge.
**→ For a 139-SKU registry + orders cache, the Free tier is likely sufficient in
Phase 0–1.** The repo assumed Neon free tier; **that's correct**, but for a *reason
the repo never states* — not "it's free" but "100 CU-hr/mo covers 2 CU (8 GB),
which is oversized for this workload."

## 3. Object storage — Cloudflare R2 (verified)

| Component | Free | Paid |
|:--|:--|:--|
| Standard storage | **10 GB-month** | **$0.015/GB-mo** |
| Class A ops | 1M | $4.50/M |
| Class B ops | 10M | $0.36/M |
| **Egress** | — | **$0 (no egress charge)** |

**→ Egress-free is the whole reason R2 is the right pick** for product images +
backups (restic → R2), matching the repo's DevOps plan. ✅ The repo's instinct is
correct; only the per-GB figure was missing.

## 4. Backups — restic → R2

restic is free/open-source; storage lands in R2 at $0.015/GB-mo. **30-day retention
of a small agent instance ≈ a few GB ≈ effectively €0/mo.** ✅ Repo plan is sound.

## 5. Domain + DNS (verified)

| Provider | .nl price | Note |
|:--|:--|:--|
| **Cloudflare Registrar** | **at cost** — "never pay more than we do" | ✅ cheapest, no markup |
| **Porkbun** | **$7.64** on sale ($7.80 regular) | per year |

**→ Cloudflare Registrar at cost.** DNS is free. The repo doesn't cost the domain
at all, but WiseQ already owns wiseq.nl — this is **our** cost if we host anything.

## 6. Transactional email — Resend (verified)

- **Free plan** exists; every plan includes **3 inboxes** free.
- Pay-as-you-go: each additional inbox **$1/mo**; all sends count against the
  transactional quota.
- Open/click tracking included **on the Free plan**.
**→ Free tier is adequate for Phase 0–1.** ⚠ *Per-1k rate not captured in scrape —
UNVERIFIED, not quoted.*

## 7. Review platforms — **this is a real, unquoted cost for the Phase 2 flagship**

`docs/05` row 🔥14 and `docs/04` Phase 2 both promise a **review engine (25 → 250+
reviews)** with **no platform cost anywhere in the repo**. Verified Trustpilot
pricing (per domain, billed annually, 12-month commitment):

| Plan | Price/mo | Invitations/mo | Widgets | Users | Domains |
|:--|--:|--:|--:|--:|:--|
| **Free** | **$0** | — | — | — | 1 |
| **Starter** | **$99** | 100 | 2 | 1 | 1 |
| Plus | **$319** | 300 | 10 | 3 | up to 3 |
| Premium | **$799** | 1,000 | 21 | 10 | unlimited |

> **⚠ Critical for the proposal:** WiseQ's stated target is **250+ reviews**.
> On **Starter ($99/mo = $1,188/yr)** the cap is **100 invitations/month** — which
> can *never* produce 250 reviews/month. **Plus ($319/mo)** gives 300/mo — still
> under target. **Premium ($799/mo)** is the only tier that reaches 1,000.
>
> **The "25 → 250+ reviews" promise is arithmetically inconsistent with a $99 plan.**
> Either the target is cumulative-over-time (plausible) or the plan must be Premium.
> **This must be resolved before the number is shown to the client.** Neither the
> repo nor `docs/09`'s "low risk" framing accounts for it.
>
> Also note: **12-month commitment.** For a first client with a stop-gate
> philosophy, that lock-in is a real commitment and belongs in the AIW cost model.

**Kiyoh (the NL-standard, and what Thuiswinkel buyers expect): ⚠ UNVERIFIED** —
the page is JS-rendered and yielded no figures. Must be checked manually; it is the
*other* half of the Phase-2 review engine decision in `docs/06` question #3.

**Shopify review apps** (Judge.me/Loox/Stamped): industry average **$58–67/mo**
(Shopify App Store stats) — a valid cheaper alternative for own-shop reviews only.

## 8. Shopify — API limits verified, prices partially captured

**GraphQL Admin API rate limits (verified):**

| Plan | Rate limit |
|:--|--:|
| Standard | **100 points/second** |
| Advanced | **200 points/second** |
| Shopify Plus | 1,000 points/second |

⚠ **This is a real engineering constraint the repo never mentions.** 100 pts/sec on
Standard is **fine** for a nightly ETL and low-frequency order sync, but a
high-frequency bundle-recombination engine or a review-invitation blast could hit
it. **Design note:** batch queries, use bulk operations. The repo's DevOps doc
says "load test the wrapper APIs" in Phase 2 — this is the specific reason why.

**Shopify NL plan prices:** ⚠ **the NL pricing page served CAD despite the EUR
locale** (showed C$37 / C$99 / C$389 for Basic/Grow/Advanced). **UNVERIFIED in EUR.**
WiseQ is *already paying* this — it's their cost, not ours, and `docs/04`'s "Shopify
API €0 — included in their existing plan" is **correct**: the API itself is
included in whatever plan they hold. No change needed, but **don't quote a plan
price to them — ask which plan they're on**, it determines our API budget.

## 9. Agency / market rates (from the second research pass — partially verified)

| Benchmark | Figure | Source quality |
|:--|:--|:--|
| **NL digital agency average hourly rate** | **€105/hr** | Emerce — credible industry figure |
| **NL ZZP software developer average** | **€94/hr** | Knab Zzp Uurtarievenboek via TMM |
| **AI automation agency retainers** | **$500–1,500/mo** SMB · **$1,500–4,000/mo** mid-market · **$3,000–8,000+/mo** enterprise | taskip.net (secondary/blog-tier) |
| AI automation **setup projects** | up to **$20,000+** mid-market | same |
| **Shopify App Store revenue share** | register **one-time $19**; keep **100% of first $1M USD** lifetime gross, above that a % kicks in | Shopify partner docs |
| Average Shopify app price | **$58–67/mo** | craftberry app-store stats |

> **Repo check:** `docs/09` claims *"Agency retainer (ecommerce): $6,000–8,000/mo
> (Shopify-specialist median); NL Plus-agencies €2,000–5,000/mo."*
> **The $6–8k figure is anchored on the Shopify-specialist median and is too high
> for a 230-product Dutch SMB.** The realistic NL band is **€2,000–5,000/mo** —
> which the repo does state. **The $6–8k "median" is doing anchoring work it hasn't
> earned; drop it or cite it properly.**

### EU AI Act — obligations and penalties (relevant to both parties)

- **Article 4 (AI literacy)** is a real, dated obligation applying to providers
  **and deployers** — i.e. **both AIW and WiseQ**. Confirmed on
  `digital-strategy.ec.europa.eu/en/ai-act/article-4`.
- **Article 99 penalties** are public and include the **€35M / 7% of turnover**
  tier for prohibited practices. **⚠ UNVERIFIED in exact 2026 form** — I confirmed
  the article exists and the headline tier, but **not** the current consolidated
  schedule. Do not quote figures to the client without re-checking the official
  text.

**Cost implication:** AI-literacy training is unbudgeted in every one of the 17
docs. For an SMB it's modest (internal training sessions), but **it must be
acknowledged**, because it's an obligation we impose on the client by deploying
AI. It is a trust signal: name it, budget it, and it stops being a liability.

---

## 10. Corrected infrastructure cost model (the thing to put in `docs/04`)

| Line | Repo says | **Verified correct** | Note |
|:--|:--|:--|:--|
| VPS | €0–20/mo | **€16.49–21.49/mo** (CX43 or CAX31) | EU, GDPR, 20TB incl. |
| Postgres | "Neon free tier" | **$0** — 100 CU-hr/mo, 1 GB, up to 8 GB RAM | ✅ correct, now justified |
| Object storage | "R2" | **$0.015/GB-mo, free to 10 GB, egress $0** | ✅ correct, now priced |
| Backups | "restic → R2, 30d" | **≈€0/mo** at this size | ✅ correct |
| Domain | not mentioned | **at cost** (Cloudflare Registrar) | ours if we host |
| Transactional email | not mentioned | **$0** (Resend free, 3 inboxes) | Phase 0–1 adequate |
| **Review platform** | **not mentioned** | **$99–799/mo** ⚠ | **new line — see §7** |
| Observability | "Better Stack" | Free tier exists; **$29–34/mo** paid | budget the paid tier for SLOs |
| **AI tokens** | "~€90/mo-class" | **see Doc A §2** — ~$870/mo list for our volume | **❌ the big one** |
| **AIW engagement** | "fixed scope" | **TBD** | per Ivan |

**Infra subtotal (excl. AI tokens): €17–25/mo realistic, not €0–20.**
**The material miss is not the VPS — it's the review platform and the AI tier.**

---

## 11. Corrections to add to the repo (extends Doc A / B1)

| # | File | Change |
|:--|:--|:--|
| C11 | `docs/04` cost model | Infra → "**€16.49–21.49/mo** (Hetzner CX43/CAX31, EU, 20TB incl., excl. VAT)" — delete "€0–20" |
| C12 | `docs/04` cost model | Add **review platform €99–799/mo** line, tied to the 250-review target |
| C13 | `docs/04` Phase 2 / `docs/05` row 14 | **Resolve the review math**: 100 invitations/mo (Starter) cannot reach 250. State cumulative-vs-monthly and the plan implied |
| C14 | `docs/09` §2 | Drop or properly source the "$6,000–8,000/mo" Shopify-specialist median; keep **€2,000–5,000/mo** NL band |
| C15 | `docs/15` §5 | Add **Shopify API rate limits** (100 pts/s Standard) as a design constraint; batch queries + bulk ops |
| C16 | `docs/04` / `docs/15` | Add **EU AI Act Article 4 (AI literacy)** line — both parties; cost TBD |
| C17 | `docs/15` §3 | Add verified R2 ($0.015/GB-mo, egress $0), Neon Free (100 CU-hr, 1GB, 8GB RAM), restic→R2 ≈ €0 |
| C18 | `docs/06` ask-list | Add **"which Shopify plan are you on?"** — determines our API budget |

---

## 12. UNVERIFIED — do not quote these yet

| # | Item | Why | How to fix |
|:--|:--|:--|:--|
| U10 | **Kiyoh** plan prices | JS-rendered, no figures captured | Manual check — needed for `docs/06` Q3 |
| U11 | **Resend** per-1k email rate | Only free-tier details captured | Pricing page |
| U12 | **Shopify NL plan prices in EUR** | Page served CAD despite EUR locale | Check out in EUR |
| U13 | **EU AI Act Article 99** exact 2026 penalty schedule | Confirmed article + headline tier only | Official consolidated text |
| U14 | **Hetzner plan availability** | Several plans showed "not available" | Order page check |
| U15 | **Sentry / Better Stack** exact tier boundaries | Better Stack verified ($0 free, $29–34 paid); Sentry not captured | Sentry pricing page |
| U16 | **taskip.net retainer bands** | Blog-tier source, not a primary rate card | Treat as directional only |
| U17 | **Amazon EU seller fees** | Still JS-rendered | Manual (carried from B1 U2) |

---

*Prepared by AI Whisperers internal analysis · 2026-10-22.*
*Primary sources: hetzner.com, neon.com, cloudflare.com, resend.com,
business.trustpilot.com, porkbun.com, shopify.dev, emerce.nl, EC AI Act text.*
*AIW fee figures intentionally TBD.*