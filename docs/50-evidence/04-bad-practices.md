# Bad practices and root causes

*Evidence-backed weaknesses only. Do not invent problems to justify AI.*

| ID | Finding | Type | Severity | Confidence | Evidence | Root cause | Recommended fix |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BP01 | Spreadsheet as tariff + shipping-rule brain | Confirmed (client SoT) | High | High | Mastersheet + ungefrankeerd pain | No typed engine; notes in numeric cells | Lab typed tariffs; CD validation; refuse bad templates |
| BP02 | Conflicting SoT (Shopify / CD / bol / sheet) | Inferred risk | High | Med | Catalog research + stack-map | No canonical registry | EAN registry (#8) + drift report |
| BP03 | 0/230 Shopify EANs (snapshot) | Confirmed defect (snapshot) | High | High | RESEARCH_CATALOG | Missing GTIN discipline | GS1 + backfill Gate |
| BP04 | Exact assumed; actual e-Boekhouden | Confirmed defect (docs) | Med | High | Manual Oct 27; doc 29 | Stale proposal assumption | Fixed in docs; API still untested |
| BP05 | BE LVB uplift used as if causal | Hypothesis misuse risk | Med | High | 80% vs 178% conflict | Client observation ≠ experiment | Exclude from ROI (claim 57) |
| BP06 | Shipping template EAN mismatch (2× Adapter) | Confirmed data defect | Med | High | CSV `NEEDS_CONFIRMATION` | Sheet error or intentional oddity | Confirm with Rob; CI blocks OK mismatch |
| BP07 | FiveX +10% @ ≤10 may overfire | Client-reported + risk | Med | Med | Manual; fast movers ~10/day | Rule without floors/ceilings documented | Detect+recommend only until tested |
| BP08 | Review deletion follow-ups | Policy risk | High | High | Raw manual; extract §8 | Score goal ≠ compliance | Draft-only; contact limits; no auto remove-ask |
| BP09 | CE sticker peel workaround | Unsafe practice | High | High | Manual | Expedience | Never automate; Drive library + human |
| BP10 | België account “phasing out” treated as done | Inferred | Med | Med | Manual | Incomplete migration | Explicit account state machine |
| BP11 | Production writes before capability matrix | Process risk | High | High | Empty stack-map matrix | Optimism | Lab first; Gates 0–2 |
| BP12 | Overloaded “verified” claim status | Process defect | Med | High | Audit Oct 27 | Single status column | Four-dimension model (claims 48+) |
| BP13 | School mornings ~4h unmeasured | Hypothesis | Med | Low | One session estimate | No time study | Gate 0.3 ≥10 timed orders |
| BP14 | Underused SaaS / plan uncertainty | Hypothesis | Low | Low | CD plan unknown | No inventory of entitlements | Rob software inventory |

### Legend

- **Confirmed defect** — reproducible from artifact  
- **Client-reported** — in WiseQ docs; not independently proven  
- **Inferred risk** — plausible from architecture  
- **Hypothesis** — needs experiment  

---

*Companion: [AI-AND-OSS-OPPORTUNITY-MAP](05-opportunity-map.md)*
