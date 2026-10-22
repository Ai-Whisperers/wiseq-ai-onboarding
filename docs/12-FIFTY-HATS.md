<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 12* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# 50-Hat Analysis — WiseQ Engagement, PY Operation, AIW Meta-Layer

*2026-10-22. 50 fresh hats beyond the 40 in the PY repo (doc 07 there): 15 on the WiseQ engagement, 15 on the PY operation, 20 on the AIW meta-layer — the business-we-are-building-around-both, never analyzed until now. Each hat gives 2-3 concrete items. New regulatory findings integrated: CONATEL homologation (PY RF gear) and the revised EU Product Liability Directive (NL kids' products).*

---

## 🎯 Domain A — The WiseQ Engagement (hats 1-15)

### 1. Knowledge-transfer engineer
Rob IS the system today — the 30-page manual is the only doc. (a) Manual → structured runbooks: every process as checklist the agent can execute; (b) record a "day with Rob" screen-share session → transcript → task inventory; (c) bus-factor metric: % of processes documented vs in-head — the engagement's real deliverable is dropping that number.

### 2. Data-migration surgeon
Phase 0 moves data into the canonical spine. (a) Rehearse on a COPY (Shopify dev store + ChannelDock sandbox) — never live; (b) migration runbook with rollback point at every step (AIW rule: backup before migration, always); (c) post-migration diff report: SKU count, EAN count, bundle resolution rate before/after.

### 3. Contract lawyer (NL services)
(a) DPA (verwerkersovereenkomst) mandatory before touching any personal data — GDPR Art. 28; (b) outcome-priced components need precise unit definitions (what counts as a "processed order"?); (c) IP: agent-built scripts — who owns what; pilot-priced work should grant WiseQ usage rights, AIW keeps the reusable components.

### 4. Product-liability underwriter
Revised EU Product Liability Directive (2026 transposition): software/AI in products now liability-relevant; kids' products = highest scrutiny. (a) Verify WiseQ's aansprakelijkheidsverzekering covers e-commerce channel sales (not just B2B); (b) our automation touching safety-comms (volume-limiting claims) must never overstate — cert-evidence library (doc 11) is the guard; (c) GPS-tracker data incidents → liability + GDPR double exposure: incident runbook required.

### 5. School procurement officer (the buyer persona)
What actually triggers a school order: (a) budget windows (Q1 planning, June year-end spend-down) — outreach calendar synced to them; (b) process: bestelnummer/inkoopcoördinator needs an invoice line that maps to their administration — our order-parser must emit THEIR format; (c) reorders are habit: if first delivery lands clean, the school reorders in August forever — SLA on first order is the whole game.

### 6. Bol account-health watcher
Bol suspends sellers for performance dips. (a) Monitor late-shipment %, cancellation %, response-time metrics nightly — alert before bol does; (b) the drift cleanup (312→230) must be staged — mass-delisting triggers review; 10/day; (c) a bol policy-change RSS/watch on partnerplatform.bol.com — terms changes hit thin-margin sellers first.

### 7. Seasonality actuary (NL calendar)
(a) Back-to-school (Aug) = 40%+ of annual school-channel revenue — stock + content + ad budget pre-positioned in July; (b) Sinterklaas (Dec 5) + Christmas = consumer peak — gift-bundle SKUs (the 25 bundles!) merchandised from Oct 15; (c) summer dip = maintenance window: listings cleanup, cert audits, A/B tests.

### 8. Amazon.nl category analyst
(a) iClever wins on review count; WiseQ's counter is review velocity (D+1 engine) + A+ content on the 2020 ASINs; (b) FBM-vs-FBA decision per SKU: class sets = FBA (Prime badge converts schools' parents); (c) win the buy box on their own brand ASINs — currently resellers may hold it.

### 9. B2B credit controller
"Bestel op factuur" = WiseQ extends credit to schools. (a) Credit limit per school (start €500, grow with payment history); (b) automated payment-reminder ladder (day 14 polite, day 30 firm, day 45 stop-ship) — schools pay slowly, not never; (c) aging report weekly — the agent flags, Rob decides.

### 10. Returns/logistics optimizer
(a) NL returns culture (~10% fashion, less for electronics): return-reason taxonomy auto-tagged — feeds product improvement; (b) bol returns: auto-accept + restock to correct SKU via EAN (the spine pays off again); (c) damaged-in-transit claims to carrier automated with photo evidence.

### 11. Content localization editor
(a) NL copy is native; EN store copy exists — DE store (Amazon.de) needs real German, not machine: ever-traduora + native review; (b) product manuals as PDFs per SKU family — support ticket reducer; (c) the 20 empty descriptions (doc: catalog lane) = first content-agent batch job.

### 12. Financial controller (engagement-side)
(a) Track OUR hours per component — the reusable-component inventory needs real cost data for AIW pricing; (b) WiseQ ROI dashboard: hours saved (school orders), revenue added (reviews→conversion), errors avoided (EAN) — updated monthly, shown to Rob; (c) pilot → retainer decision gate: pre-agree the metrics that trigger continuation.

### 13. Scenario strategist (WiseQ futures)
(a) If bol adds agentic ordering (UCP momentum), WiseQ is early — the MCP endpoint becomes a sales channel; (b) if Heutink copies the B2B layer, WiseQ's moat = agentic reordering + niche depth; (c) exit optionality: the cleaned data + automation makes WiseQ acquirable at a different multiple — worth naming in the pitch's final slide.

### 14. Change-management coach
Rob's the user AND the owner. (a) Ship one automation he feels weekly (drift report Monday email) — trust compounds; (b) agent suggestions arrive as proposals, not actions, for the first 60 days (approval-mode default); (c) a "what did the agents do" daily digest — visibility kills fear of the black box.

### 15. Incident-response planner
(a) WhatsApp/channel outage → fallback order form on the shop; (b) agent gone rogue (wrong price live) → kill switch + 15-min rollback runbook + pricing-change freeze rule; (c) data incident → 72h GDPR notification runbook with pre-drafted templates (avanzialegal-style clock starts immediately).

## 🌴 Domain B — PY Operation (hats 16-30)

### 16. CONATEL homologation specialist ⚠️ NEW FINDING
Bluetooth audio = telecom equipment in PY: **CONATEL homologation + physical label required BEFORE import** (Res. 588/2009; 2025 tightening noted by customs brokers). (a) Buying from CDE wholesalers: the WHOLESALER imported, so homologation is their paperwork — verify label presence at onboarding, photograph it; (b) direct 1688 import of Bluetooth items = OUR homologation — cost/lead-time per SKU before the import rule (doc 09 §3) fires; (c) non-RF items (cases, chargers wired, cables) = no CONATEL — import-first candidates.

### 17. Cash-cycle treasurer
Contra-entrega means cash in the messenger's pocket. (a) Cash-to-bank sweep daily (deposit at agent/banco); float is a P&L line; (b) supplier payment timing: pay CDE on delivery (we're unknown), negotiate 7-day terms after 30 clean orders; (c) weekly cash position: cash-in-transit is invisible money — reconcile daily, not weekly.

### 18. Zonal pricing strategist
(a) Delivery cost varies 2× by zone (15k Luque → 30k+ far zones) — show customers free-shipping-over-X to steer mix; (b) zone-density map: only enter zones with ≥3 orders/week potential; (c) pickup point (a friendly local shop) for far zones — flat fee, no moto.

### 19. Counterfeit-intelligence officer
CDE is real-and-fake mixed. (a) Serial-number verification step at inbound (Apple accessories: checkcoverage-style lookup); (b) supplier counterfeit-strike policy: one strike = delist their brand SKUs; (c) never sell brands we can't verify — the trust-brand strategy (doc 10 §4) dies with one fake.

### 20. Motomensajero fleet manager
(a) Per-delivery vs daily-rate: crossover at ~15 deliveries/day per moto — track it; (b) messenger insurance + equipment deposit — formalize in writing (Spanish template); (c) peak-evening staffing: 18-21h = 40% of orders; two motos evenings before two motos all-day.

### 21. Py/Guaraní copy chief
(a) Product copy in español rioplatense-neutral PY register (vos forms, no penalisms); (b) price anchors in guaraníes with Spanish numerals — "doscientos cincuenta mil guaraníes" reads trust-local; (c) 5-message sale script A/B tested weekly by the eval harness (T1).

### 22. Bank-reconciliation clerk
(a) QR payments land in ueno with reference; match reference→order automatically (payment-id on the QR payload); (b) transfer payments: amount+timestamp fuzzy-match to open orders; unmatched >24h = daily digest; (c) monthly: DNIT-retention reconciliation (IVA retained by gateways) — feed the contador's file.

### 23. Importer-of-record strategist
Phase 2+ direct imports: (a) formal importer registration (RUC importador) vs using the courier's consignment import — cost/complexity matrix; (b) HS-code pre-classification for top-20 SKUs (arancel PY) — disputes at aduana kill week-long windows; (c) consolidate: one air shipment weekly, not per-order.

### 24. Social-proof engineer
(a) Photo-with-product review incentive (5% off next) — visual proof outsells text in PY; (b) Google Business Profile with weekly posts + review replies — Maps is a free channel nobody works; (c) FB-group testimonials (with permission) as ad creative — native trust.

### 25. Tax-calendar automator
(a) RESIMPLE monthly payment + annual F.502 (Feb) — calendar with reminders; (b) patente municipal annual renewal; (c) the 80%-cap alert (doc 10) → SIMPLE transition checklist auto-prepared.

### 26. Warranty-reserve actuary
(a) Per-supplier failure rate (C.13.3) funds a warranty reserve % — price includes it; (b) Ley 1334/98 7-day retract: budget 2-3% returns monthly; (c) DOA (dead-on-arrival) >5% on a SKU = auto-pause + supplier claim.

### 27. WhatsApp-list builder
(a) Every closed sale: "¿te avisamos de ofertas?" opt-in → broadcast list (the 7593/2025-compliant owned channel); (b) list segments by niche-interest, not blast-all; (c) weekly offer message max — respect or churn.

### 28. Supplier-scorecard analyst
(a) Score: price dispersion, fill-rate, delivery-time, failure-rate, warranty-honoring — the canonical table's supplier dimension; (b) quarterly supplier review (auto-generated report) → renegotiation ammo; (c) new-supplier trial protocol: 5 SKUs, 30 days, measured.

### 29. Flash-sale choreographer
(a) PY loves flash offers (fechas: Madre, Amigo, Niño, Navidad — the doc 10 calendar): stock+creative+WhatsApp blast+ad budget as ONE rehearsed playbook; (b) inventory cap per flash (sell-out in 48h builds FOMO, not resentment); (c) post-flash: sell-out data → next CDE buy list.

### 30. City-expansion scout
(a) Encarnación/CdE/Oviedo: same playbook, local messenger + local FB groups (hat 38 in PY doc 07); the scout = demand probe via FB-group activity, 2 weeks, Gs. 0; (b) franchise-the-stack optionality: one operator + our agents per city; (c) expansion gate: main city at ≥150 sales/mo AND ≥12% net margin for 3 consecutive months.

## 🧠 Domain C — The AIW Meta-Layer (hats 31-50, never analyzed before)

### 31. Productized-services architect
Each reusable component → SKU'd service: CDE-price-agent, bundle-spine builder, school-order closer, review engine, compliance tracker. (a) name + one-pager + fixed price each; (b) bundle into "Commerce OS" tiers; (c) the two live ops (WiseQ, PY) become case studies with real numbers.

### 32. Case-study economist
(a) Instrument both ops from day 1: hours saved, error rates, revenue deltas — the marketing asset is the DATA; (b) WiseQ privacy: anonymize + approval before publishing; PY: fully ours, publish freely; (c) "we run our own retail operation" is the agency differentiator almost nobody has.

### 33. Pricing psychologist (AIW services)
(a) Anchor on the $3k-$50k market (doc 09 §2) — never hourly; (b) outcome-priced components at 20-30% of value created (school-order at €0.50-1.00/processed order); (c) pilot priced at-cost deliberately: the pilot's product is trust, margin comes at retainer.

### 34. Pipeline engineer
(a) The 857-org school list = WiseQ retainer leads AND "we did this for WiseQ" proof for similar NL webshops; (b) every PY supplier conversation = a lead for the supplier-agent product; (c) target: 2 pilots/mo from inbound (repo + case studies) by Q1-2027.

### 35. Brand voice (AIW)
(a) "AI Whisperers" needs a services site: the two repos as living proof; (b) founder-story content (Ivan operating a real fleet + real retail ops) — authenticity as moat; (c) NL-market presence: Dutch-language landing for the WiseQ case.

### 36. IP strategist
(a) The bundle-spine matcher, school-order parser, compliance-playbook generator = copyright (code) — own them; (b) consider a trademark for the Commerce-OS product name; (c) client contracts: license-to-use components, never transfer of the component library.

### 37. Talent scout (agent ops)
Scale = more operator-hours. (a) profile: bilingual ops person per market (NL: Dutch-speaking; PY: Guaraní-comfortable); (b) the stack makes one operator worth 3 — hire operators, not engineers; (c) Luana/Ale/Kyrian family-device fleet = the operator bench (with consent UX per the pop-up lesson).

### 38. Risk portfolio manager
Two ops = concentration risk none, but founder-time is the scarce input. (a) weekly capacity plan across WiseQ/PY/AIW; (b) each engagement must reach self-running (agents + 1 operator) within 60 days or be cut; (c) the fleet orchestrator pattern applies: max_inflight per engagement.

### 39. Documentation librarian
(a) Each built component gets a skill file (Hermes skills) — the next session starts fast; (b) client-facing docs separate from internal runbooks (Rob sees clean, we keep the guts); (c) the two repos' READMEs are the storefront — weekly tidy.

### 40. Evals auditor (agent quality)
(a) every agent ships with its eval set + threshold; regression = blocklist deploy (same rule both repos); (b) quarterly red-team: try to make each agent do something harmful — log, fix; (c) the eval sets themselves are product (sellable with the service).

### 41. Cost-model analyst
(a) per-engagement unit economics: agent-LLM cost per order/reconciliations — measured, not estimated; (b) model routing (cheap for parse, strong for decide) documented per component; (c) the "self-hosted vs SaaS" ledger per component — some SaaS (Trustpilot) is cheaper than build.

### 42. Partnership diplomat
(a) bol CPOP (after integration proves); (b) ChannelDock/5X: approach for API access as an integrator — they gain a customer-feature, we gain a channel; (c) GS1/Thuiswinkel institutional relationships compound in NL — join, attend, be known.

### 43. Security officer
(a) client credentials (bol, Shopify, e-Boekhouden) live in the vault, never in repos/chat; (b) per-client isolation: separate Hermes profiles per engagement (already our pattern); (c) agent permissions: read-heavy, write-with-log, money-moves-with-approval.

### 44. Data-privacy officer (dual-jurisdiction)
One privacy agent, two law-flavors (GDPR now; Ley 7593 from Nov-2027). (a) shared DSR machinery; (b) consent-schema identical → one codebase; (c) our own marketing lists comply with BOTH (the strictest standard wins).

### 45. Negotiation strategist (Rob)
(a) the repo IS the BATNA-builder: work already visible, sunk-cost in our favor; (b) never discount the pilot — add scope (drift report included) instead; (c) let Rob pick the pilot's first automation (autonomy buys commitment).

### 46. Ops-runbook engineer
For each agent: (a) what "healthy" looks like (metrics); (b) what "broken" looks like (symptoms); (c) the 3-step restart. Runbooks live next to the code, tested monthly.

### 47. Financial planner (AIW entity)
(a) PY op + NL engagements → invoicing entities: AIW (Ai-Whisperers) vs local? NL BTW-reverse for B2B services; PY: RESIMPLE until SIMPLE; (b) cross-border pricing in EUR/Gs consistently; (c) quarterly P&L per engagement — kill the losers, feed the winners.

### 48. Roadmap triage chief
Everything can't be built. This analysis + the 40-hat PY doc + WiseQ docs = ~250 ideas. (a) score = value × confidence ÷ effort; (b) top-20 live on a kanban with owners; (c) the rest stay documented (this file) — not lost, just sequenced.

### 49. Failure-modes historian
Document near-misses: (a) the OSS-catalog build bug (assert-caught); (b) the Flanders SSL wall; (c) delegation 429s → parent-side rule. Each becomes a skill note (already partially done) — the org's scar tissue is training data.

### 50. Long-game strategist
24-month arc: (a) 2026: two live ops + first retainer (WiseQ); (b) 2027: Commerce-OS productized, 5-10 clients, PY at 3 cities; (c) 2028: the fleet + the ops + the case studies = the regional AI-operations company nobody else can copy because nobody else RUNS anything. The repos we're committing today are the founding documents.

---

## 🚀 Synthesis: the 12 that graduate to the kanban

| # | Hat | Action | Repo |
|---|---|---|---|
| 1 | 4 | Product-liability insurance check (WiseQ) | wiseq |
| 2 | 6 | Bol account-health monitor (pre-suspension) | wiseq |
| 3 | 7 | NL seasonality calendar → procurement + content | wiseq |
| 4 | 9 | B2B credit ladder for Bestel op factuur | wiseq |
| 5 | 16 | CONATEL label check at supplier onboarding | py |
| 6 | 17 | Daily cash sweep + messenger float tracking | py |
| 7 | 19 | Serial-verification at inbound (anti-fake) | py |
| 8 | 21 | Vos-register PY copy + weekly script A/B | py |
| 9 | 31 | Component SKU list (Commerce-OS v0) | AIW |
| 10 | 32 | Instrument both ops for case-study data | AIW |
| 11 | 40 | Eval-gate on every agent deploy | AIW |
| 12 | 45 | Pilot negotiation: scope-add, never discount | AIW |

## 🗑️ Discards (explicit)

- **Hiring salespeople** (hat 34): inbound + case studies first; sales hires at client #5, not before.
- **Building a dashboard SaaS** (hat 41): the metrics live in markdown reports; SaaS-ing them is a different company.
- **PY own-importer registration in phase 0-1** (hat 23): courier consignment covers it until ~Gs. 40M/mo volume.
- **Trademark now** (hat 36): name the Commerce-OS line when client #2 signs; not before.
- **Guaraní TTS voice** (hat 21 adjacent): interesting, not ROI-positive yet; revisit at 500 orders/mo.
