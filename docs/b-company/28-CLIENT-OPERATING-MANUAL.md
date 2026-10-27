<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track B · Document 28* · [← Docs map](../README.md)</sub>

---

# Client operating manual — what we learned

*WiseQ shared their internal **Werkwijze Operationele Handleiding** on 2026-10-27. Raw + structured extract: [`data/client/`](../../data/client/OPERATING-MANUAL-EXTRACT.md). This page is the client-facing summary for the proposal.*

## Why this unblocks Phase 0

Doc 06 asked for the ~30-page company manual before the stack map. **Received.** Draft stack map: [`data/stack-map.md`](../../data/stack-map.md).

## Headline corrections to our earlier assumptions

| We thought / left open | Manual says |
| :--- | :--- |
| Bookkeeping vendor unknown (Exact?) | **e-Boekhouden** — offers → invoices → relations for schools |
| 5X API unverified | FiveX used weekly for **EAN/stock/sales reports**, LVB replenishment, review export, auto price brake |
| Bundle graph only in our CSV spine | ChannelDock already has **bundle products**; sea freight must book 300-series as bundles |
| One bol seller mental model | **Three accounts:** WiseQ NL, WiseQ Electronics, WiseQ België (holding — phasing out) |
| Trustpilot as first review engine | Ops manual prioritises **bol.com reviews / seller score ≥9** |
| Brand colours inferred | Official: light `#26b5b7` · dark `#1648ad` |

## How the company actually runs (compressed)

1. **Sales org rule:** 100% of assortment online 100% of the time (multi-account).  
2. **NL:** WiseQ NL · before 15:00 → next day · LVB heavy.  
3. **BE:** WiseQ Electronics · brievenbus 2–3 days · packages VVB · LVB for conversion (+~80% claim when switching to next-day).  
4. **Daily friction:** ungefrankeerde ChannelDock orders, cancellations, review triage, assortment/levertijd fixes.  
5. **School sales:** catalog/sample → e-Boekhouden offer → invoice → MyParcel/DHL — same path our Phase-1 pipeline targets.  
6. **Warehouse:** QLS / post / BE print waves; 100–200–300 SKU ranges; bundle “bijmaken” is treated as a failure mode.

## What we will automate first *(aligned to their checklist)*

| Their daily/weekly pain | Our Phase 0–1 mapping |
| :--- | :--- |
| Assortment online + levertijden | Read-only monitor → dashboard |
| Ungefrankeerde zendingen | ChannelDock queue digest |
| School offer→invoice | Shadow demo on dummy data → gated writes |
| FiveX→LVB replenishment | Report ingest + suggestion draft |
| Strike / on-time Wed review | Digest + escalation rail |
| Bol review follow-ups | **Draft-only**, human send (policy-sensitive) |

## Still needed from WiseQ

See [Next Steps](../a-proposal/06-NEXT-STEPS.md) — items 2–8 (plan tier, tokens, sandbox orders, turnover, etc.). Manual closed item 1 and largely item 2’s bookkeeping question.

## Source files

| File | Role |
| :--- | :--- |
| [`Handleiding_opzet.txt`](../../data/client/Handleiding_opzet.txt) | Client raw (promo code / phone redacted for public repo) |
| [`OPERATING-MANUAL-EXTRACT.md`](../../data/client/OPERATING-MANUAL-EXTRACT.md) | Structured SoT for builders |
| [`stack-map.md`](../../data/stack-map.md) | Phase-0 connector map draft |

---

## Continue reading

| Next | Why |
| :--- | :--- |
| [Company profile](01-COMPANY-PROFILE.md) | Public registry facts (now plus ops structure) |
| [Automation backlog](../a-proposal/05-AUTOMATION-BACKLOG.md) | Re-score against their daily checklist |
| [Next Steps](../a-proposal/06-NEXT-STEPS.md) | Remaining asks |
