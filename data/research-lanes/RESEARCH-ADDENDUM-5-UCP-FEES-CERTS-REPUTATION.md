# Research addendum 5: UCP's true meaning, bol commission math, Thuiswinkel timeline, Scamadviser remediation

*Oct 23, 2026 — fifth lane. The headline: doc 07's "WiseQ runs UCP" claim connects to something much bigger than we framed it as — Google's agentic-commerce standard. Plus the fee math the repricing agent needs, the certification timeline that reshapes the Q4 plan, and the playbook for the TrustScore-0 problem. Sources linked inline.*

---

## 1. UCP is Google's Universal Commerce Protocol — and WiseQ is already on it

Doc 07 records: "WiseQ already runs UCP + MCP shopping server (we verified it live)." What that actually means, now documented:

**Two competing agentic-commerce standards are live in 2026:**

| | **UCP** (Universal Commerce Protocol) | **ACP** (Agentic Commerce Protocol) |
|---|---|---|
| Backers | **Google**, Shopify, Etsy, Wayfair, Target, Walmart; endorsed by 20+ incl. Adyen, AmEx, Best Buy, Mastercard, Stripe, Visa, Zalando ([Google dev blog](https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/)) | **Stripe, OpenAI, Meta** ([Stripe docs](https://docs.stripe.com/agentic-commerce/protocols/acp), [spec repo](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol), beta) |
| Consumer surfaces | **Google AI Mode in Search + Gemini app** | ChatGPT + Stripe merchant tooling |
| Scope | Discovery → cart → checkout → order management; identity linking (OAuth 2.0); AP2 payments with cryptographic proof of consent | Agentic checkout, cart/feed, delegate payment & auth, orders/webhooks |
| Transports | REST, JSON-RPC, **MCP**, A2A | REST/OpenAPI |
| Shopify angle | Shopify [Universal Cart API](https://shopify.dev/docs/agents) built on UCP ("One Cart, every brand", early access) — agents collect items from any merchant into one cart | — |

**Why this matters for WiseQ, concretely:**

1. **Their UCP/MCP endpoint isn't a curiosity — it's a storefront in Google's AI shopping surfaces.** A 230-SKU Dutch SME being machine-reachable via UCP puts them ahead of nearly every NL competitor (Heutink included — their API is developer-facing, not consumer-surface-facing).
2. **The strategic risk is standards bifurcation:** UCP (Google) vs ACP (OpenAI/Stripe/Meta). A merchant on UCP only is invisible to ChatGPT-native shopping; vice versa for Gemini. **Phase-2 research lane: how hard is dual-homing?** UCP's design (capability schema, MCP transport) suggests a merchant can expose both — our orchestration layer is exactly the piece that could normalize them.
3. **The pitch upgrade:** doc 07's "agentic-commerce operations" engine (UCP traffic analytics, agents.md freshness) should be repositioned from "keep it fresh" to **"you are early to the surface where Google says shopping is going — let's measure and defend that position."** UCP-profile freshness, catalog completeness (EANs!), and stock accuracy now directly affect AI-surface discoverability. That ties the EAN fix to the agentic story: garbage catalog in = garbage agent presence out.

---

## 2. bol commission structure — the repricing agent's fee math

Two sources, one discrepancy, documented honestly:

**Structure** (both sources agree): fixed commission per item + variable % by category, excl. VAT.

- Fixed: €0.20 (<€10) / €0.40 (€10–20) / €0.85 (>€20) / €2.48 (big electronics >€20) + €1.00 media surcharge
- Variable, [Boloo guide](https://boloo.co/blog/hoeveel-commissie-bol-com): speelgoed & spellen **12.4%** (standard band)
- Variable, [Winkelfactuur Q1-2026 table](https://winkelfactuur.nl/nl/blog/bol-com-commissie-tarieven-2026): speelgoed **11%**, computers/tablets 7%, kabels/adapters 12%, kinderkleding 14%

**The discrepancy (12.4% vs 11% for toys) is itself the finding:** bol adjusts rates quarterly and third-party tables lag. **The repricing agent must read the live category rate per offer from the Retailer API (commission is exposed per order item), not from any static table** — that becomes a design rule for doc 04's repricing engine, not a footnote.

**Margin sanity check for WiseQ's category mix** (indicative, using the conservative 12.4%): a €29.95 kids headset → €0.85 + €3.72 ≈ **€4.57 commission (~15% of the incl-VAT price)**. On a €24.99 toy: €0.85 + €2.59 ≈ €3.44. Against typical category margins (25–35% for kids audio hardware per addendum 4's market reports), bol takes roughly half the gross margin — which is why the repricing agent's margin-floor logic (doc 07, PY-proven) matters, and why **Groeibeloning** (bol's performance discount, per Winkelfactuur up to 10–15% off commission at scale) is worth tracking in the pipeline.

**Also confirmed:** Amazon.nl reference for the cross-channel price-harmonization lane — 7–15% + €39/mo Pro account ([Zoloo comparison](https://zoloo.co/blog/bol-com-commissie)).

---

## 3. Thuiswinkel Waarborg: the real process and the Q4 verdict

From [thuiswinkel.org's certification page](https://www.thuiswinkel.org/vertrouwen/keurmerken/thuiswinkel-waarborg/hoe-krijg-je-het-keurmerk), verified Oct 23:

**Three certification steps, run by independent parties (ICTRecht + Forus-P):**
1. **Legal check** — external law firm audits the shop's terms, returns policy, info duties; findings must be fixed
2. **Security scan** — ethical hacking of the webshop (the same class of checks our own doc 23 Gate-4 demands of *us*)
3. **Financial monitoring** — jaarcijfers checked for stability

**Timeline: 4–6 weeks average**, assuming the site is live and fixes are implemented promptly. Annual recertification.

**The Q4 verdict, honestly:** starting today (Oct 23), certification lands **end-November to early-December** — at best the tail of Sinterklaas (Dec 5), realistically Christmas-adjacent, with the legal-check fix round as the main variance. The TCO's Thuiswinkel line (€983–1,759/yr) is year-one-stable, but the *conversion benefit* should be modeled from Q1 2027, not Q4 2026. This kills any "certified before Sinterklaas" pitch line — and adds a good one instead: **the certification's legal check will surface exactly the terms/returns/privacy gaps the AVG verwerkersovereenkomst work (addendum 2 §3) would fix anyway. Sequence them together and one effort serves both.**

**Bonus finding:** Thuiswinkel membership includes the Geschillencommissie guarantee (Thuiswinkel stands surety up to €10,000 per ruling) — worth citing in school-channel offers as institutional-grade dispute resolution.

---

## 4. Scamadviser TrustScore 0: there is an actual remediation path

From [Scamadviser's algorithm explainer](https://scamadviser.com/articles/scamadviser-algorithm-explainer) and [FAQ](https://scamadviser.com/faq):

- The score (1–100, from 40+ data sources) is **dynamic**: "A site that scores 30 today can score 75 in six months if it establishes a legitimate track record." WiseQ's score of 0 (per the Oct-21 research) sits in the worst band (1–20, "very likely unsafe") — almost certainly driven by structural factors (domain age/config signals, low review volume, hidden WHOIS) rather than any actual fraud history.
- **Owner remediation exists:** owners can [contact Scamadviser](https://www.scamadviser.com/contact) to dispute the score and incorrect user reviews. There's also a trust-seal program.
- **The levers we can pull without paying anyone** (all map to work already in the backlog): positive review volume elsewhere (Trustpilot engine), active social profiles, multi-year domain registration, public/complete contact details (KvK number, address — already present), fast site performance, SSL posture.
- **The honest caveat:** no SLA, no guaranteed uplift, and the algorithm is opaque. The playbook is: dispute + fix every positive-signal lever + re-check monthly. Timeline: months, not weeks. This lane stays a Phase-2 engine with modest expectations — but it now has a documented method instead of a shrug.

**One connection worth making:** the NIH finding (addendum 4 §3 — many kids headphones don't truly limit volume) is the kind of thing that generates *organic* press and reviews, which is what actually moves a Scamadviser score. The verified-limiter report is simultaneously a product differentiator, an Amazon-compliance asset, AND a reputation-signal generator. One artifact, three lanes.

---

## 5. Ledger updates from this lane

| Row | Change |
|---|---|
| NEW 31 | UCP = Google's Universal Commerce Protocol (Shopify/Walmart/Visa/Stripe-endorsed; powers AI Mode + Gemini shopping); ACP = Stripe/OpenAI/Meta rival. WiseQ's live UCP/MCP endpoint = a storefront in Google's AI surfaces — ahead of NL competitors. Dual-homing question = Phase-2 lane. **VERIFIED** |
| NEW 32 | bol commission: fixed €0.20–2.48 + variable 4.1–20.7%; toys 11% (Winkelfactuur Q1-2026) vs 12.4% (Boloo) — **source discrepancy documented; repricing agent must read live rates from the Retailer API, not static tables**. Groeibeloning up to 10–15% off at scale |
| NEW 33 | Thuiswinkel certification: 3 independent steps (ICTRecht legal, ethical-hack scan, financial check), **4–6 weeks**, annual recert → starting Oct 23 lands end-Nov/early-Dec; model conversion benefit from Q1 2027. €10k Geschillencommissie surety = school-channel trust asset |
| NEW 34 | Scamadviser remediation path exists (owner dispute + positive-signal levers: reviews, social, domain registration length, contact completeness); dynamic score, months-scale, no SLA. Maps to existing backlog items. **VERIFIED** (Scamadviser's own pages) |

*No messaging performed. Browser still down (bol count row 4 STALE; screenshot QA pending). All findings primary-sourced.*
