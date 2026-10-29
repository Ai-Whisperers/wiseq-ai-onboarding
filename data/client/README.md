# Client source-of-truth materials

## Publication gate

| Artifact | Public repo? | Notes |
| :--- | :--- | :--- |
| [`OPERATING-MANUAL-EXTRACT.md`](OPERATING-MANUAL-EXTRACT.md) | ✅ | Sanitized structured extract — preferred citation |
| [`MASTERSHEET-EXTRACT.md`](MASTERSHEET-EXTRACT.md) | ✅ | Shipping / templates / packaging / keywords |
| [`mastersheet/*.csv`](mastersheet/) | ✅ | Public-safe exports only |
| `Handleiding_opzet.txt` (raw ops manual) | ❌ **Not in the public tree** | Held in the private AIW handover folder. Promo's + phone redacted, but it still contains internal procedures, review tactics and named examples, and Rob's publication approval has not been collected. |
| Full `Mastersheet.xlsx` | ❌ Never | COGS, contacts, gift cards, promo codes |
| `meetings/*.txt` (raw transcripts) | ❌ **Not in the public tree** | Held in the private AIW handover folder. Cite the [structured notes](../../docs/10-client/07-meeting-2026-10-28.md) instead. |

**Cite the extracts, not the raw dumps.** The raw manual and the raw transcripts are untracked in this repo by design — a CI guard fails the build if either is ever tracked again. If a future reader needs the raw source, it is released to the private handover folder, never committed here.

## Related

- [Doc 28](../../docs/10-client/03-operating-manual.md) — proposal summary  
- [Doc 30](../../docs/10-client/01-complete-dossier.md) — complete client dossier  
- [Meeting 2026-10-28](../../docs/10-client/07-meeting-2026-10-28.md) — revenue / growth follow-up  
- [18 · Submissions status](../../docs/50-evidence/18-rob-submissions-status.md) — files vs open asks  
- [Doc 29](../../docs/60-governance/03-critical-audit-2026-10-27.md) — Oct 27 critical audit response  
- [Preparation catalog](../../docs/50-evidence/01-preparation-catalog.md) — offline vs needs-Rob  
- [`../stack-map.md`](../stack-map.md) — connector capability draft  
