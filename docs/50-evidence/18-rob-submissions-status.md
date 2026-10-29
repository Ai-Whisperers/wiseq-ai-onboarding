<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Evidence · 18* · [← Evidence index](17-evidence-index.md)</sub>

---

# Rob submissions vs repo — status (2026-10-28)

*What WiseQ has already given us, what the repo already contains, and what still blocks Phase 0. Synthesizes Oct-21 meeting, Oct-27 file ingest, and Oct-28 follow-up transcript.*

## 1. The two files Rob sent ✅

| # | What Rob sent | In repo as | Status |
| ---: | :--- | :--- | :--- |
| **1** | **Werkwijze / Operationele Handleiding** (~30p ops manual) | Raw: [`data/client/Handleiding_opzet.txt`](../../data/client/Handleiding_opzet.txt) · Extract: [`OPERATING-MANUAL-EXTRACT.md`](../../data/client/OPERATING-MANUAL-EXTRACT.md) · Summary: [doc 03](../10-client/03-operating-manual.md) | **Received 2026-10-27.** Raw still under publication gate (cite extracts publicly). |
| **2** | **Mastersheet.xlsx** (ops workbook) | Public CSVs: [`data/client/mastersheet/`](../../data/client/mastersheet/) · Extract: [`MASTERSHEET-EXTRACT.md`](../../data/client/MASTERSHEET-EXTRACT.md) | **Received 2026-10-27.** Full xlsx **not** committed (COGS / PII / promo codes). |

Those two files closed the original “send the manual + software inventory” ask for **ops design**. They did **not** include API tokens or school-order samples.

### What the two files unlocked

| Unlocked | Evidence |
| :--- | :--- |
| Bookkeeping vendor = **e-Boekhouden** (not Exact) | Manual → [ADR 002](../adr/002-e-boekhouden-not-exact.md) |
| ChannelDock **native bundles** | Manual → spine thesis reconciled in [dossier](../10-client/01-complete-dossier.md) |
| Multi bol accounts (NL / Electronics / België phase-out) | Manual |
| Shipping tariffs + ChannelDock rule templates | Mastersheet CSVs |
| Daily/weekly/monthly cadences for backlog | Manual § daily ops |
| Draft stack map | [`data/stack-map.md`](../../data/stack-map.md) |

### What they still leave open

| Gap | Why it matters |
| :--- | :--- |
| ChannelDock **plan tier** + API key | Connector build vs browser-only |
| e-Boekhouden / bol / mailbox **read tokens** | Live read-only smoke |
| Anonymized school order packs | Shadow demo realism |
| Mastersheet **2× Adapter** template conflict | Auto-clone unsafe until confirmed |
| BE LVB **+80% vs +178%** definition | Do not forecast on either |
| Raw Handleiding **publish OK?** | Privacy gate |

## 2. Meetings on record

| Date | Artifact | Net-new for us |
| :--- | :--- | :--- |
| **2026-10-21** | [Meeting notes](../10-client/04-meeting-2026-10-21.md) | 4h school mornings; bundle recombination pain; EAN as key; agreed to share manual |
| **2026-10-28** | [Notes](../10-client/07-meeting-2026-10-28.md) + [raw transcript](../../data/client/meetings/2026-10-28-transcript-turboscribe.txt) | **~€1.5M revenue**; profit band; webshop ~€8k/mo; 7k school emails; ~300 bol listings quality debt; Rob’s **≥€2k base-fee** signal; wants ops **+** growth package |

## 3. Scorecard — ask list vs reality

| Ask (doc 06 / open-asks) | Status 2026-10-28 |
| :--- | :--- |
| Company manual | ✅ Received (file 1) |
| Software inventory | ✅ Mostly answered *inside* the manual |
| Sandbox / anonymized school orders | ❌ Not received |
| Read-only API access (CD / bol / e-Boekhouden / mailbox) | ❌ Not received |
| Purchase-manager walkthrough | ❌ Not scheduled |
| Annual online turnover | 🟡 **Verbal ~€1.5M** — confirm “online” vs total |
| ChannelDock plan + PIM? | ❌ Plan name still unknown; native bundles confirmed |
| Hosting / review / bookkeeping / first-engine **decisions** | ❌ Still open (our defaults stand) |

Full tick list: [open-asks](../start/rob/open-asks.md).

## 4. What *we* already built (repo side) — independent of Rob’s keys

| Track | Where | Ready without tokens? |
| :--- | :--- | :--- |
| Proposal + cost model | [`20-offer/`](../20-offer/) | ✅ |
| Bundle spine 114+25 | [`data/wiseq-*.csv`](../../data/) | ✅ |
| Research / claims / compliance | [`data/`](../../data/) · [`30-market/`](../30-market/) | ✅ |
| Lab scenarios A–C (school / catalog / shipping) | [`lab/`](../../lab/) | ✅ fixtures only |
| Hermes Desktop-first profile | [`40-build/01`](../40-build/01-agent-infrastructure.md) · [`lab/hermes/`](../../lab/hermes/) | ✅ design |
| Evidence / gates / terms | [`50-evidence/`](../50-evidence/) · [`60-governance/`](../60-governance/) | ✅ |
| Live vendor smoke | needs Wave-1 secrets | ❌ blocked |

## 5. Recommended next moves (ordered)

1. **WhatsApp Rob** with [cred template](../start/rob/whatsapp-cred-template.md) — Wave 1 read-only keys only.  
2. **Confirm €1.5M** = online turnover for Thuiswinkel tier.  
3. Ask for the **bol listing-quality export** mentioned 28 Oct.  
4. Ask for **5–10 anonymized school packs** for Gate 0.3.  
5. Commercial align: scoped Phase 0–1 (ops) vs his “full growth package” — don’t silently expand SOW.  
6. Keep citing **extracts**, not raw Handleiding, until publish OK.

## 📌 Verdict

**Rob’s two files are ingested and already reshaped the proposal** (e-Boekhouden, native bundles, multi-account bol, shipping templates). The **Oct-28 meeting adds money and growth context** (€1.5M, €2k fee signal, three income pillars) but **does not unblock live Phase 0** — that still waits on read-only credentials and sample school orders.

---

<sub>[Preparation catalog](01-preparation-catalog.md) · [Complete dossier](../10-client/01-complete-dossier.md) · [Progress log](15-progress-log.md)</sub>
