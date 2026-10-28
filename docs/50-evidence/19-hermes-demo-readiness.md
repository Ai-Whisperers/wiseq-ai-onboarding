<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Evidence · 19* · [← Prep catalog](01-preparation-catalog.md) · [Submissions](18-rob-submissions-status.md)</sub>

---

# Hermes demo readiness — what we can prep before Rob’s data

*Answer to: what has Rob given us, and what can we have ready so that when Wave-1 data/keys arrive we immediately show Hermes working on WiseQ — not a generic AI chat.*

## 1. What Rob has passed so far (complete inventory)

| Source | Content we can use offline |
| :--- | :--- |
| **File 1 — Handleiding** | Full ops cadences; ChannelDock bundles; e-Boekhouden school path; multi bol accounts; FiveX reports; ungefrankeerd / strikes / LVB / reviews playbooks |
| **File 2 — Mastersheet** | Shipping tariffs; ChannelDock clone-from-EAN templates; packaging links; keyword samples (safe CSVs) |
| **Meeting Oct 21** | 4h school mornings; bundle recombination pain; EAN as purchase key; “AI in my mailbox” ask |
| **Meeting Oct 28** | ~€1.5M revenue; ~€8k/mo own shop; 7k school emails; ~300 bol listings quality debt; wants ops **+** growth; ≥€2k fee signal |

**Not passed yet (blocks live Hermes):** ChannelDock/bol/e-Boekhouden/mailbox read keys · anonymized school packs · FiveX export samples · bol listing-quality dump.

---

## 2. What we can already show Rob *today* (no keys)

This is the **Milestone-1 Desktop demo** — synthetic, YOLO off, profile `wiseq-lab`:

| Demo beat | Proof artifact | What Rob sees |
| :--- | :--- | :--- |
| Lab green | `cd lab && pytest -q` | School / catalog / shipping shapes already coded |
| School pipeline | skill `school-pipeline` + mailbox fixtures (32 goldens) | Mail → offer/invoice **draft** → waits `APPROVE` |
| Shipping / ungefrankeerd | skill `shipping-econ` + Mastersheet fixtures | Template clone logic; refuses `NEEDS_CONFIRMATION` |
| Catalog / spine | skill `catalog-integrity` + spine CSVs | 114+25 bundle graph as agent memory |
| Ops briefing | skill `ops-briefing` + seeded memory | Multi-account bol + daily cadence in one digest |
| Next ask | [read-only guide](../start/rob/read-only-access.md) | “Keys = live digests; still read-only” |

Script: [`lab/hermes/DEMO-SCRIPT.md`](../../lab/hermes/DEMO-SCRIPT.md).

> This demo answers “can Hermes run WiseQ workflows?” with **fixtures shaped like his manual**. It does **not** yet answer “is this my live stock / my live inbox?”

---

## 3. Prep we can finish *before* data arrives 🔧

Ordered by demo impact. None need production access.

### A. Make the offline demo feel like *his* company (high)

| Prep | Why it matters when keys land |
| :--- | :--- |
| **Memory seed v2** from dossier + Oct-28 numbers (revenue band, 7k emails, €8k/mo shop) | Hermes answers “who is WiseQ?” without hallucinating Exact / single bol |
| **School golden set → 40–50** labeled mails (NL, staffel, new relation, cancel, sample request) | Drop-in replace with his anonymized packs; same eval harness |
| **Fixture “day in the life” digests** — Monday ungefrankeerd, Wed strike, Fri invoice-request, monthly school blast | Same digest *shape* later filled by live reads |
| **Dry-run Desktop on a clean `wiseq-lab` profile** on the machine you’ll demo from | Zero fumble when Rob is watching |
| **One-screen before/after story** — 4h morning → digest + APPROVE gate | Ties demo to his Oct-21 pain |

### B. Adapters & contracts ready to swap fixtures → live (high)

| Prep | Why |
| :--- | :--- |
| Keep **Provider Protocols** stable; fixture adapters stay default | Vendor adapters plug in without rewriting scenarios |
| Stub vendor adapters remain **fail-closed** until smoke | Safe default if someone toggles live too early |
| Document **field maps**: manual vocabulary → fixture JSON → expected live API fields | When first JSON from ChannelDock/bol arrives, mapping is already written |
| Capability-matrix template rows pre-filled with *vendor doc URLs* only | Phase-0 fill-in becomes checkboxes, not research |

### C. Growth demos he asked for Oct 28 (medium — still offline)

| Prep | Uses what he said |
| :--- | :--- |
| **Bol listing QA checklist** against public wiseq.nl / bol pages (sample 20 SKUs) | Previews the “300 listings not optimal” job |
| **School email personalization mock** — 5 synthetic orgs from methodology (no real PII) | Shows “not one blast to 7k” without his CRM export |
| **Influencer / affiliate outreach draft skill** (NL templates, human-send only) | Matches growth ask; no auto-send |
| Competitor watch URL pack (already started in checklists) | changedetection later |

### D. Commercial / trust packing (medium)

| Prep | Why |
| :--- | :--- |
| Phase-0 **read-only SOW** one-pager (“keys buy digests, not writes”) | Closes fee conversation against his €2k signal without over-scoping |
| Update Thuiswinkel quote card for **€1.5M band** (pending online confirm) | Stops quoting wrong contribution tier |
| Keep Handleiding **extract-only** in decks | Privacy |

### E. Explicitly do **not** prep yet 🚫

- Write scopes, auto review-deletion, price writes, CE sticker hacks  
- Always-on VPS before Desktop demo earns trust  
- ROI using 80%/178% BE LVB  
- Replacing ChannelDock / FiveX / e-Boekhouden  
- Loading full Mastersheet (COGS/PII) into public Hermes memory  

---

## 4. When Wave-1 data lands — plug-in sequence (same day)

```text
T+0h   Vault keys (Bitwarden) · never chat/repo
T+1h   Read smoke: ChannelDock stock/rules · bol assortment · e-Boekhouden relations · mailbox headers
T+3h   Fill capability matrix · note shape deltas vs fixtures
T+1d   Swap one digest to LIVE READ (ungefrankeerd or assortment drift) · still APPROVE-gated
T+2d   Drop 5 anonymized school packs into eval/ · re-run goldens · show Rob side-by-side fixture vs real
```

**Demo sentence after load:**  
“Same Hermes, same skills, same APPROVE gate — yesterday fixtures, today *your* ChannelDock queue.”

---

## 5. Scoreboard

| Layer | Ready now? | Blocked on Rob? |
| :--- | :---: | :---: |
| Proposal / costs / terms | ✅ | — |
| Ops understanding (manual + sheet) | ✅ | Confirm plan tier / 2× Adapter / België |
| Synthetic Hermes Desktop demo | ✅ | — |
| Live digests on his data | ❌ | Wave-1 keys |
| Shadow school on real packs | ❌ | Anonymized samples |
| Growth agents (ads/influencers) | 🔧 stubs only | Exports / brand assets later |

## 📌 Bottom line

We already have enough from Rob’s **two files + two meetings** to run a credible Hermes Desktop demo on **WiseQ-shaped synthetic data**, and to finish every offline artifact (goldens, digests, field maps, growth stubs, SOW) so live keys become a **swap**, not a rebuild. The only things we cannot fake for him are **his** live stock, inbox, and bookkeeping shapes — those wait on Wave 1.

---

<sub>[Open asks](../start/rob/open-asks.md) · [Demo script](../../lab/hermes/DEMO-SCRIPT.md) · [Lab](../../lab/README.md)</sub>
