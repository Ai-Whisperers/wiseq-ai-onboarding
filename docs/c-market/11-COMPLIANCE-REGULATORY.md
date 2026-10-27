<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track C · Document 11* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# WiseQ Compliance & Regulatory Map — 2026-10-22

*The certifications, marks, and bodies that govern WiseQ's product categories — and the gaps to check. Researched from public sources; every item is a conversation-opener with Rob, not an accusation.*

## 1. 🧭 Product-safety certifications (the electronics)

| Requirement | Scope | Status question for WiseQ |
|---|---|---|
| **EN 71-1/-2/-3** (Toy Safety Directive 2009/48/EC) | Products aimed at/usable by children <14 — WiseQ's entire catalog by positioning | Are class sets marketed as "voor kinderen" tested & documented per EN 71? |
| **EN IEC 62115** | Electric/electronic toys — harmonized with the Toy Safety Directive; covers electrical safety for kids' electronic products | Headphones/tablets/trackers with child positioning fall here |
| **Radio Equipment Directive (RED) 2014/53/EU** | Bluetooth headphones, GPS watches, wireless chargers — **legally mandatory CE**; since **Aug 2025 includes cybersecurity requirements** (RED Delegated Act 2022/30: secure updates, no vulnerabilities, personal-data protection) | The 2025 RED cybersecurity layer is NEW — products certified before it may need file updates. GPS trackers (child location data!) are squarely in scope |
| **85 dB volume limiting** | Not a formal EN standard by itself, but the de-facto market norm (every competitor markets "85 dB"); WiseQ already claims it — keep test evidence per SKU family |
| [GPSR (EU) 2023/988](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R0988) | General Product Safety Regulation (applies since Dec 2024): EU responsible-person contact on product/listings, traceability, recall readiness | Check: is the responsible-person info on all Amazon/bol listings? |

**Why this matters for the pitch:** certification evidence per SKU family (EN 71 / 62115 / RED files) is ALSO a content asset — "getest volgens EN 62115" on product pages converts parent-trust into listings. An agent maintaining a cert-evidence library per SKU = compliance + marketing in one table.

## 2. 🕰️ Trust marks & organizations (the shop)

| Body | Cost | Value |
|---|---|---|
| **Thuiswinkel Waarborg** | **€75 one-time + €390/yr certification + contribution** | 92-96% consumer recognition; the direct counter to the Scamadviser-0 trust suppressor; also requires the disputes-committee (Geschillencommissie) process |
| **bol CPOP certified partner** | Application-based | Post-integration credibility; bol lists certified integrators/service providers |
| **GS1 Nederland** | 10 EAN-pack ~€61 + annual licence | The 0/230 EAN fix (see doc 08) |
| **Trustpilot** | Free tier + paid plans | Review engine target (13 reviews → automated D+1 flow) |
| **KvK / ILT / NVWA** | — | Market-surveillance bodies for toy-safety/e-com compliance; low risk but the cert files above are their ask |

## 3. 💬 Regional & channel organizations (the network)

- **Stichting Westelijke Tuinsteden** (Amsterdam-West public primary education) and the other **640+ school boards** in our lead-gen dataset — the board layer is the volume B2B channel (doc 02-WHAT-WE-DID).
- **School inkoopcollectieven** (Onderwijs Inkoop Groep, Contractables) — collective catalogs; listing = many schools at contract prices (doc 08 §3).
- **Beverwijk/Grootebroek region**: 7 nearby schools in the contact set — the local-walk-in pilot list for WiseQ's own backyard.
- **Educatheek** (wholesaler already stocking WiseQ products) — deepen or compete; either way, monitor.

## 4. 📦 Data-protection layer

- **GDPR/AVG** (already law, unlike PY's 7593/2025): shop customers + school-contact outreach both in scope. Our privacy-agent design (consent registry, DSR handling, 72h breach protocol) ships in EU flavor.
- **RED cybersecurity clause** overlaps: kids' GPS/location data = sensitive-adjacent; evidence of secure handling strengthens both RED and GDPR posture.

## 4b. ⚠ EU AI Act — applies to **us** as deployers (added 2026-10-22, verified)

**This section was missing from the original map. It is the most time-sensitive item in this document.**

| Fact | Status |
|---|---|
| **Article 4 — AI literacy obligation** | **Applies since 2 February 2025.** Providers and deployers must ensure sufficient AI literacy of staff. |
| **National supervision began** | **August 2026** — i.e. this is **already being enforced now**, not a future requirement. |

**Scope for WiseQ:** they are a **deployer** (they use our agent layer internally).
We — AI Whisperers — are also a **deployer** of the same systems. Both are in scope.

**What Article 4 actually requires (important, because it is cheap):**
- It prescribes **no specific course, no certificate, and no minimum number of hours.**
- The obligation is to ensure staff have sufficient AI literacy, taking into account
  their knowledge, experience, education, training and context.
- **An organisation's own records suffice** as evidence — no accredited training
  provider is required.

**Consequence:** this is a **few hours of Phase 0 work, not a budget line.** It becomes
a deliverable: an AI-literacy register (who uses AI tools, for what, what training
was given) that satisfies a Dutch supervisor. Turn a compliance exposure into
evidence of rigour.

**What we deliberately do NOT claim:** high-risk AI Act obligations (and their
penalty tiers) apply to systems placed on the market as safety components of
products, and to certain named use cases. WiseQ's internal ops layer triggers
**none** of that. Do not use high-risk framing to sell fear to the client — it
would collapse on inspection.

## 4c. 🧾 Cost corrections in this document (2026-10-22)

| Item | Stated here before | **Verified now** |
|---|---|---|
| Thuiswinkel Waarborg | "€75 one-time + €390/yr certification + contribution"; "€465 year one" (§5.3) | **€75 once + €390/yr + revenue-tiered contribution €518–€1,294/yr** (thuiswinkel.org, excl. VAT). Year 1 realistically **€983–€1,759** depending on turnover class, plus **€45/yr per extra platform** (bol.com/Amazon). **We have never asked WiseQ their annual online turnover — it sets the tier.** |
| GS1 10-pack | "€61 + annual licence"; called a one-off in doc 08 | **€61 is PER YEAR**, not one-off. EDI licence is **€0** below €5M turnover. 139 GTINs needed (114 components + 25 bundles) = **€733/yr recurring (€887 w/ VAT)**. |
| GPSR responsible person | listed only as a "field check" | A third-party EU Responsible Person costs from **~$500/yr**, but **WiseQ B.V. is an NL-established manufacturer and is its own Responsible Person → €0.** Keep AIW explicitly out of the product chain (contract language: software provider, not goods supplier). |
| EN 71 / RED testing | not costed anywhere | **Still uncosted and still unknown.** Lab testing per SKU family is typically **hundreds to low-thousands of EUR**. **Get real lab quotes before any total is presented to the client.** |

## 5. 🧱 Actions this adds to the backlog

1. Cert-evidence library per SKU family (EN 71 / 62115 / RED) — agent-maintained, marketing-usable
2. RED-2025 file audit on the GPS-tracker line (child location data = highest scrutiny)
3. Thuiswinkel Waarborg application (**€983–€1,759 year 1 excl. VAT, depending on turnover class** — see §4c; needs their turnover figure) — paired with review engine
4. Responsible-person field check across Amazon/bol listings (GPSR) — WiseQ is its own RP, so this is a *listing-hygiene* task, not a purchase
5. **EU AI Act Article 4 AI-literacy register** — applies now, costs hours not euros (§4b)
6. **EN 71 / EN IEC 62115 / RED lab quotes** — obtain real figures; currently the single largest uncosted item in the whole proposal
7. Outreach wave to 3 regional boards (West Friesland backyard first)

---

## 📌 In short

Compliance here is **cheap if done early and expensive if discovered late**. The corrections that matter: **GS1 is €225/yr for the whole catalog** (1,000-pack + contribution), and **Thuiswinkel is €983–€1,759 in year 1** depending on turnover tier, not the €465 previously quoted — WiseQ's own turnover band settles it. The most time-sensitive item is **EU AI Act Article 4**: it has applied since February 2025 and supervision began in **August 2026**, making it *now*, not future. It prescribes no course or certificate — an internal literacy register satisfies it in a few hours.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Oss Integrations](08-OSS-INTEGRATIONS.md)** | NL trust marks and feed compliance |
| **[Company Profile](../b-company/01-COMPANY-PROFILE.md)** | The product certifications already held |
| **[Ai Stack Blueprint](../a-proposal/04-AI-STACK-BLUEPRINT.md)** | Compliance gates built into the phases |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.


---
**Primary sources:** all five instruments above link to their EUR-Lex consolidated texts. Thuiswinkel Waarborg requirements: [thuiswinkel.org](https://www.thuiswinkel.org). GS1 NL code pricing: [gs1.nl](https://www.gs1.nl). This document is a **preliminary compliance checklist, not legal sign-off** — product-specific applicability is assessed per SKU in Phase 0.
