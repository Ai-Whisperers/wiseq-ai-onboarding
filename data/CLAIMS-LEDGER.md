# Claim ledger — WiseQ onboarding repo

*Generated 2026-10-23. One row per material claim. This is the evidence-model upgrade the external audit asked for (audit §8.2): every material claim carries its source, observation date, scope, reproduction path, and honest status. Statuses: **VERIFIED** (reproducible from an inspectable artifact), **INFERRED** (plausible reading of evidence, not independently established), **HYPOTHESIS** (testable proposal — no evidence yet), **STALE** (snapshot older than 30 days; re-verify before quoting).*

| # | Claim | Status | Source & date | Scope / limits | Reproduce |
|---|---|---|---|---|---|
| 1 | 0/230 Shopify products have a barcode field populated | **VERIFIED** | `data/research-lanes/RESEARCH_CATALOG.md`, catalog snapshot Oct 21 | Snapshot of the captured export only; a missing field ≠ no GTIN exists elsewhere (audit §1.5) | `python3 scripts/validate_repo.py` → catalog checks; re-run against fresh export |
| 2 | 0/230 products carry a weight; 0/230 track inventory in Shopify | **VERIFIED** (as snapshot) | Same snapshot, Oct 21 | Same caveat: describes the export, not the full shipping/inventory architecture (audit table §2) | Same as above |
| 3 | Bundle spine: 114 components + 25 bundles, zero unresolved references | **VERIFIED** (structural) | `data/wiseq-bundle-spine.csv` + CI, Oct 22 | Referential integrity only. Semantic correctness (quantities, variants, physical reality) is Gate 3.1, untested (audit §1.4) | CI check 5 runs on every push |
| 4 | bol listing count 312 vs 230 own-shop SKUs | **STALE** | `RESEARCH_MARKETPLACES.md`, Oct 21 | bol seller page was bot-walled on re-check Oct 23; treat as unverified until browser pull | Browser pull of bol seller page; log in ledger |
| 5 | Trustpilot: 25 reviews, 4.4/5, "not recently invited" warning shown | **STALE→REFRESHED** | Trustpilot profile, Oct 21 → re-pulled Oct 23 | Fresh pull Oct 23 shows organic reviews continuing (latest Sep 2026, uninvited); total count needs the on-page counter (not in markdown extract) — re-verify | `web_extract` on `nl.trustpilot.com/review/wiseq.nl` |
| 6 | Scamadviser TrustScore 0 flag on the domain | **STALE** | `RESEARCH_MARKETPLACES.md`, Oct 21 | Third-party risk score; conversion impact unmeasured (audit §2 row 4) | Scamadviser lookup |
| 7 | GS1 cost for 139 GTINs = €854/yr (14 packs × €61) | **VERIFIED** (arithmetic) | gs1.nl pricing via `docs/08` §GS1, Oct 23 | Assumes all 139 need own GTINs (they do, selling on bol+Amazon); excludes VAT | 139/10 → 14 packs × €61 |
| 8 | Thuiswinkel Waarborg cost €983–1,759/yr | **INFERRED** | thuiswinkel.org fee schedule via doc 04 TCO, Oct 22 | Turnover-class dependent; exact class needs WiseQ's figures | thuiswinkel.org current tariff |
| 9 | School-order mornings take ~4 hours (founder, one session) | **HYPOTHESIS** (baseline) | Working session Oct 21, doc 03 | Single-observation estimate; touch vs elapsed not separated (audit §1.1) | Gate 0.3: ≥10 timed orders |
| 10 | Pipeline target: <15 min human involvement per morning | **HYPOTHESIS** | Doc 04 proposal | Target, not a measurement; depends on 9 | Gate 5.1 |
| 11 | Payback ~2–3 months on mid TCO ~€20k | **HYPOTHESIS** | Doc 04 TCO §payback | Requires 9+10 to land as modeled; deliberately caveated in doc 04 | Gate 5.1–5.3 |
| 12 | 25 → 250+ Trustpilot reviews in a quarter | **HYPOTHESIS** (retired as a promise) | Doc 04, re-labeled Oct 23 | No conversion model; platform-policy compliant invitations only (audit §1.3) | Gate 5.4 |
| 13 | DUO open data yielded 8,673 orgs / 857 verified emails (method only; no raw PII in repo) | **VERIFIED** (method) | `RESEARCH_LEADS-DUO.md`, Oct 21 | Raw data stays out of the public repo by policy | Re-run the documented query |
| 14 | 116-agent fleet / 79 cron jobs run AIW's own operations | **VERIFIED** (internal) | AIW internal state, Oct 23 | Internal infrastructure; client can't independently inspect — offered as context, not proof | Live demo on request |
| 15 | 5X (bookkeeping) has a public API | **UNRESOLVED** | Retraction note, Oct 22 | Existence unverified; billing step depends on it (audit §6) | Read-only test in Gate 1.2 |
| 16 | ChannelDock REST API exists, from €45/mo | **VERIFIED** (existence) | channeldock.com/nl/prijzen, Oct 22 | Plan-tier permissions untested — that's Gate 1.2 | Re-fetch pricing page |
| 17 | "NL e-commerce tooling thin at the edges, absent in the middle" | **INFERRED** | Doc 08 survey of 100 repos | Qualitative synthesis; not a market census (audit §2) | — (framing, not a count) |
| 18 | Site demos render clean (0 console errors, hero cutouts fixed) | **VERIFIED** | CI + this session's visual audit, Oct 23 | Visual QA on desktop Chromium; mobile re-check pending | Visit the three demo URLs |

*Ledger maintained alongside the repo. When a claim's status changes, the row changes with a dated note — history preserved in git.*

**Re-check policy:** rows marked STALE are re-verified before being quoted to the client (audit §4 "historical snapshots as current"). Next scheduled re-check: bol seller count + Trustpilot totals, on first client contact or Nov 21, whichever first.
