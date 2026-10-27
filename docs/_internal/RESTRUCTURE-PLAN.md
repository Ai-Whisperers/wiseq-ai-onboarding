# Docs restructure plan — complete reorder, rename, rehome

*Status: **executed 2026-10-27** (defaults D1–D7).*  
*Scope: everything under `docs/` (not `data/`, `lab/`, or `site/` except link updates).*  
*Date: 2026-10-27 · supersedes Approach A letter-prefix layout as the long-term IA.*

---

## 1. Diagnosis (why reorder)

### 1.1 What Approach A fixed

- Role packs (`for-rob` / `for-kiki` / `for-ops`) as shallow entry.
- Numbered docs moved into letter tracks so the flat `docs/01…24.md` dump is gone.

### 1.2 What is still broken

| Problem | Evidence |
| :--- | :--- |
| **Global numbers lie** | Docs are `01…30` but **not** reading order: company has 01–03 then **07**, then **25/28/30**; delivery has 13–16 then **24**; governance skips 20–21 (those are showcase). Nobody can “read 01→30”. |
| **Two parallel systems** | Letter tracks (`a-proposal`…) **plus** unnumbered `audits/` SCREAMING_CASE (17 files). Audits are first-class work but second-class in `docs/README.md`. |
| **Opaque folder names** | `a-proposal` / `f-governance` / `g-reviews` mean nothing to Rob; letters are AIW internal taxonomy. |
| **Misleading filenames** | `07-PY-TRANSFER-WISEQ` (Paraguay codename), `12-FIFTY-HATS` (title is **31** hats), `14-HERMES-JEV-AIW-REUSE` (Jev noise). |
| **Overlapping SoT** | Client truth split across **28** (manual summary), **30** (dossier), `data/client/*` extracts, meeting notes + addendum. |
| **Overlapping “what to build”** | `05` backlog · audits opportunity map · `10` OSS catalog · INTERNAL-REUSE · `14` reuse · thin IMPLEMENTATION-ROADMAP · `06` next steps · `24` agent infra · `15` devops. |
| **Overlapping governance history** | `19` critical review · `22` audit response · `29` Oct-27 critical audit — three “adversarial” docs without clear primary. |
| **Thin / uneven tracks** | `g-reviews` = 1 doc; `00-nl` = 1 doc; `for-rob` has real content, other packs are indexes only. |
| **Internal meta in client tree** | `docs/superpowers/` plans sit beside client packs. |
| **Stale absolute GitHub links** | Some bodies still cite `blob/main/docs/24-…` (pre-move paths). Validator only checks README `docs/…` links — cross-doc relative rot is under-checked. |
| **Track labels in footers wrong** | e.g. hats doc says “Track D · Document 12” while living under `g-reviews`. |

### 1.3 Inventory snapshot (current)

| Area | Files (approx) | Role |
| :--- | ---: | :--- |
| Role packs | 3 indexes + 3 Rob content docs | Audience entry |
| `00-nl` | 1 | Dutch pitch |
| `a-proposal` | 3 | Sell / decide |
| `b-company` | 7 | Client |
| `c-market` | 5 | Market |
| `d-delivery` | 5 | Build |
| `e-showcase` | 3 | Proof |
| `f-governance` | 6 | Terms / evidence / audits |
| `g-reviews` | 1 | Specialist hats |
| `audits` | 17 | Lab / Desktop / prep / handoff |
| `superpowers` | 2+ | Internal reorg history |
| Hub | `docs/README.md` | Map |

~**55 content docs** + indexes. Too many surfaces for one SMB engagement unless IA is ruthless.

---

## 2. Design principles (locked for this plan)

1. **Audience first, domain second** — Rob/Kiki/ops/NL never dig through letter soup.
2. **Stable slugs, local order** — drop global `01–30`; use `NN-slug.md` **inside** a decade folder only.
3. **One primary SoT per question** — others become pointers or `archive/`.
4. **Client-facing vs builder-facing** — clear folder split; audits join “evidence”, not a side alley.
5. **Rename for truth** — filename matches H1 intent; no PY/Jev/Fifty mismatches.
6. **`git mv` only** — preserve history; then fix links in one validator pass.
7. **No content rewrite in move PR** — moves/renames/stubs/pointers only; copy edits are a follow-up PR.
8. **Keep claim IDs in ledger** — `data/CLAIMS-LEDGER.md` stays; docs cite claims by number, not by old doc numbers.

---

## 3. Target tree

```text
docs/
  README.md                          # hub: audiences → decades → archive
  RESTRUCTURE-PLAN.md                # this file (move to _internal after done)

  start/                             # was for-* + 00-nl (+ Rob content)
    README.md                        # “who are you?” switchboard
    rob/
      README.md
      the-case.md                    # was THE-CASE-IN-ONE-BREATH
      open-asks.md
      read-only-access.md
    kiki/
      README.md
    ops/
      README.md
    nl/
      README.md
      samenvatting.md                # was 00-NL-SAMENVATTING

  10-client/                         # who WiseQ is (primary SoT)
    README.md
    01-complete-dossier.md           # was 30 (PRIMARY)
    02-company-profile.md            # was 01
    03-operating-manual.md           # was 28 (summary; points at data/client)
    04-meeting-2026-10-21.md         # was 03
    05-catalog-scorecard.md          # was 25
    06-bundle-spine-reuse.md         # was 07-PY-TRANSFER-WISEQ
    07-research-log.md               # was 02-WHAT-WE-DID (or archive — see §4)

  20-offer/                          # what we recommend
    README.md
    01-blueprint.md                  # was 04
    02-automation-backlog.md         # was 05
    03-next-steps.md                 # was 06

  30-market/
    README.md
    01-oss-integrations.md           # was 08
    02-competitors-deals.md          # was 09
    03-oss-catalog.md                # was 10 (rename away from “100” if stale)
    04-compliance.md                 # was 11
    05-unit-economics.md             # was 26

  40-build/                          # how we deliver
    README.md
    01-agent-infrastructure.md       # was 24 (PRIMARY for runtime)
    02-tooling-mcp.md                # was 13
    03-aiw-reuse.md                  # was 14; absorb pointer to audits reuse
    04-devops.md                     # was 15
    05-dev-team-hats.md              # was 16

  50-evidence/                       # was audits/ + living evidence indexes
    README.md
    01-preparation-catalog.md
    02-workflow-audit.md             # CURRENT-STATE-AND-WORKFLOW-AUDIT
    03-data-flow-sor.md
    04-bad-practices.md
    05-opportunity-map.md            # AI-AND-OSS-OPPORTUNITY-MAP
    06-hermes-desktop.md
    07-approval-escalation.md
    08-test-lab.md                   # TEST-LAB-ARCHITECTURE
    09-experiment-register.md
    10-keep-extend-replace.md
    11-oss-evaluations.md
    12-risk-register.md
    13-internal-reuse.md             # INTERNAL-REUSE (current implement backlog)
    14-roadmap.md                    # IMPLEMENTATION-ROADMAP (keep thin or merge → handoff)
    15-progress-log.md
    16-handoff.md
    17-evidence-index.md             # moved from f-governance/27

  60-governance/
    README.md
    01-terms.md                      # was 18
    02-acceptance-criteria.md        # was 23
    03-critical-audit-2026-10-27.md  # was 29 (PRIMARY living audit)
    04-specialist-31-hats.md         # was g-reviews/12-FIFTY-HATS

  70-showcase/
    README.md
    01-site-concepts.md              # was 17
    02-send-to-rob.md                # was 20
    03-who-we-are.md                 # was 21

  archive/                           # dated / superseded — keep for evidence, not nav
    README.md                        # “do not cite as current”
    2026-10-critical-review.md       # was 19
    2026-10-external-audit-response.md  # was 22
    # optional: 02-what-we-did if not kept as 10-client/07

  _internal/                         # AIW only
    README.md
    superpowers/                     # move docs/superpowers here
      specs/…
      plans/…
```

**Root README** (`/README.md`) keeps the one-paragraph pitch + short map pointing at `docs/start/rob/` and `docs/10-client/01-complete-dossier.md`.

---

## 4. Merge / demote / keep matrix

| Current | Action | Rationale |
| :--- | :--- | :--- |
| `30-CLIENT-COMPLETE-DOSSIER` | **Keep → primary** `10-client/01` | Single client map |
| `28-CLIENT-OPERATING-MANUAL` | **Keep thin** `10-client/03` | Manual-ingest narrative; dossier links here + `data/client` |
| `01-COMPANY-PROFILE` | Keep | Registry / public facts |
| `03-MEETING-NOTES` | Keep | Founder words + addendum |
| `02-WHAT-WE-DID` | **Demote → archive** *or* `10-client/07` research log | Overlaps dossier + research-lanes |
| `07-PY-TRANSFER` | **Rename** spine/reuse | Drop PY brand |
| `25-CATALOG-SCORECARD` | Keep | Ops one-pager |
| `04/05/06` proposal | Keep as `20-offer/01–03` | Core sell path |
| `08–11, 26` market | Keep as `30-market/*` | |
| `24` agent infra | **Primary** in `40-build` | Desktop-first truth |
| `13–16` delivery | Keep; rename | |
| `14` vs `INTERNAL-REUSE` | Keep both: `40-build/03` = narrative inventory; `50-evidence/13` = implement backlog (cross-link) | Different jobs |
| `05` backlog vs opportunity map | Keep both: offer vs evidence detail | |
| `27-EVIDENCE-INDEX` | Move into `50-evidence` | Belongs with audits |
| `29` Oct-27 audit | **Primary** governance living doc | |
| `19` critical review | **Archive** | Historical adversarial pass |
| `22` audit response | **Archive** | Partly superseded (GS1 etc.); cite from 29 |
| `12-FIFTY-HATS` | Move + rename `60-governance/04` | Kill empty `g-reviews` |
| Audits pack | Move → `50-evidence` with short slugs | End dual taxonomy |
| `IMPLEMENTATION-ROADMAP` | Keep thin **or** fold into `16-handoff` | Prefer fold if still 20 lines |
| `for-rob` content | Move under `start/rob/` | Audience tree |
| `superpowers/` | Move → `_internal/superpowers/` | Out of client nav |
| Letter folders `a–g`, `00-nl`, `audits`, `for-*` | **Delete after empty** | |

**Do not merge in the move PR:** blueprint ↔ backlog, terms ↔ acceptance, showcase trio.

---

## 5. Full rename map (old → new)

### 5.1 Start / audiences

| Old | New |
| :--- | :--- |
| `for-rob/README.md` | `start/rob/README.md` |
| `for-rob/THE-CASE-IN-ONE-BREATH.md` | `start/rob/the-case.md` |
| `for-rob/OPEN-ASKS-CHECKLIST.md` | `start/rob/open-asks.md` |
| `for-rob/READ-ONLY-ACCESS-GUIDE.md` | `start/rob/read-only-access.md` |
| `for-kiki/README.md` | `start/kiki/README.md` |
| `for-ops/README.md` | `start/ops/README.md` |
| `00-nl/00-NL-SAMENVATTING.md` | `start/nl/samenvatting.md` |
| `00-nl/README.md` | `start/nl/README.md` |

### 5.2 Client

| Old | New |
| :--- | :--- |
| `b-company/01-complete-dossier.md` | `10-client/01-complete-dossier.md` |
| `b-company/02-company-profile.md` | `10-client/02-company-profile.md` |
| `b-company/03-operating-manual.md` | `10-client/03-operating-manual.md` |
| `b-company/04-meeting-2026-10-21.md` | `10-client/04-meeting-2026-10-21.md` |
| `b-company/05-catalog-scorecard.md` | `10-client/05-catalog-scorecard.md` |
| `b-company/06-bundle-spine-reuse.md` | `10-client/06-bundle-spine-reuse.md` |
| `b-company/../archive/2026-10-research-log.md` | `archive/2026-10-research-log.md` *(preferred)* **or** `10-client/07-research-log.md` |

### 5.3 Offer / market / build / showcase

| Old | New |
| :--- | :--- |
| `a-proposal/01-blueprint.md` | `20-offer/01-blueprint.md` |
| `a-proposal/02-automation-backlog.md` | `20-offer/02-automation-backlog.md` |
| `a-proposal/03-next-steps.md` | `20-offer/03-next-steps.md` |
| `c-market/01-oss-integrations.md` | `30-market/01-oss-integrations.md` |
| `c-market/02-competitors-deals.md` | `30-market/02-competitors-deals.md` |
| `c-market/03-oss-catalog.md` | `30-market/03-oss-catalog.md` |
| `c-market/04-compliance.md` | `30-market/04-compliance.md` |
| `c-market/05-unit-economics.md` | `30-market/05-unit-economics.md` |
| `d-delivery/01-agent-infrastructure.md` | `40-build/01-agent-infrastructure.md` |
| `d-delivery/02-tooling-mcp.md` | `40-build/02-tooling-mcp.md` |
| `d-delivery/03-aiw-reuse.md` | `40-build/03-aiw-reuse.md` |
| `d-delivery/04-devops.md` | `40-build/04-devops.md` |
| `d-delivery/05-dev-team-hats.md` | `40-build/05-dev-team-hats.md` |
| `e-showcase/01-site-concepts.md` | `70-showcase/01-site-concepts.md` |
| `e-showcase/02-send-to-rob.md` | `70-showcase/02-send-to-rob.md` |
| `e-showcase/03-who-we-are.md` | `70-showcase/03-who-we-are.md` |

### 5.4 Evidence (audits)

| Old | New |
| :--- | :--- |
| `audits/PREPARATION-CATALOG.md` | `50-evidence/01-preparation-catalog.md` |
| `audits/CURRENT-STATE-AND-WORKFLOW-AUDIT.md` | `50-evidence/02-workflow-audit.md` |
| `audits/DATA-FLOW-AND-SYSTEM-OF-RECORDS.md` | `50-evidence/03-data-flow-sor.md` |
| `audits/BAD-PRACTICES-AND-ROOT-CAUSES.md` | `50-evidence/04-bad-practices.md` |
| `audits/AI-AND-OSS-OPPORTUNITY-MAP.md` | `50-evidence/05-opportunity-map.md` |
| `audits/HERMES-DESKTOP-CAPABILITY-NOTES.md` | `50-evidence/06-hermes-desktop.md` |
| `audits/APPROVAL-AND-ESCALATION.md` | `50-evidence/07-approval-escalation.md` |
| `audits/TEST-LAB-ARCHITECTURE.md` | `50-evidence/08-test-lab.md` |
| `audits/EXPERIMENT-REGISTER.md` | `50-evidence/09-experiment-register.md` |
| `audits/SOFTWARE-KEEP-EXTEND-REPLACE-DECISIONS.md` | `50-evidence/10-keep-extend-replace.md` |
| `audits/OSS-CANDIDATE-EVALUATIONS.md` | `50-evidence/11-oss-evaluations.md` |
| `audits/RISK-AND-SECURITY-REGISTER.md` | `50-evidence/12-risk-register.md` |
| `audits/INTERNAL-REUSE-AND-BEST-PRACTICES.md` | `50-evidence/13-internal-reuse.md` |
| `audits/IMPLEMENTATION-ROADMAP.md` | `50-evidence/14-roadmap.md` *(or fold)* |
| `audits/PROGRESS-LOG.md` | `50-evidence/15-progress-log.md` |
| `audits/HANDOFF.md` | `50-evidence/16-handoff.md` |
| `f-governance/17-evidence-index.md` | `50-evidence/17-evidence-index.md` |
| `audits/README.md` | rewrite as `50-evidence/README.md` |

### 5.5 Governance / archive / internal

| Old | New |
| :--- | :--- |
| `f-governance/01-terms.md` | `60-governance/01-terms.md` |
| `f-governance/02-acceptance-criteria.md` | `60-governance/02-acceptance-criteria.md` |
| `f-governance/03-critical-audit-2026-10-27.md` | `60-governance/03-critical-audit-2026-10-27.md` |
| `g-reviews/04-specialist-31-hats.md` | `60-governance/04-specialist-31-hats.md` |
| `f-governance/19-CRITICAL-REVIEW.md` | `archive/2026-10-critical-review.md` |
| `f-governance/22-AUDIT-RESPONSE.md` | `archive/2026-10-external-audit-response.md` |
| `superpowers/**` | `_internal/superpowers/**` |
| `RESTRUCTURE-PLAN.md` | `_internal/RESTRUCTURE-PLAN.md` after execution |

---

## 6. Citation / compatibility rules

### 6.1 Stop saying “doc 04 / doc 30”

| Old habit | New habit |
| :--- | :--- |
| “see doc 30” | “see [client dossier](10-client/01-complete-dossier.md)” |
| “doc 29” | “Oct-27 critical audit” or path |
| “Track B · Document 07” footers | `10-client · bundle spine` or drop track letters |

### 6.2 Compatibility redirects (optional, one release)

Add `docs/_redirects.md` table old-path → new-path for humans. Do **not** leave stub files at old paths unless GitHub Pages needs them (this repo mostly uses GH blob links — update those).

### 6.3 Validator changes (`scripts/validate_repo.py`)

1. README link check (already path-based) — update root README.  
2. Replace `find_doc("30")` style helpers with **slug/path map** or folder+local-NN.  
3. Add check: every `docs/**/*.md` relative link target exists.  
4. Forbid new files matching `docs/[a-g]-*/` or global `NN-SCREAMING`.  
5. Ensure exactly one `01-complete-dossier.md` etc.

### 6.4 Site / demos

Update `site/index.html`, `index.html`, any hardcoded `docs/start/rob/…` paths in the same PR.

---

## 7. Hub UX after restructure

**`docs/README.md` (target shape):**

1. Who are you? → `start/rob|kiki|ops|nl`  
2. Know the client → `10-client/01-complete-dossier`  
3. Offer → `20-offer/01-blueprint`  
4. Evidence / lab → `50-evidence` + `../lab`  
5. Archive / internal collapsed at bottom  

**Rob pack read order (unchanged intent):**  
`the-case` → `20-offer/01` → `20-offer/03` → `open-asks` → `read-only-access` → `60-governance/01` → showcase.

---

## 8. Execution phases (when approved)

| Phase | Work | Risk |
| ---: | :--- | :--- |
| **0** | Approve this plan (especially §4 demotions + decade names) | Decision |
| **1** | Create target folders; `git mv` all files per §5; no content edits | Medium (link break window) |
| **2** | Rewrite all `docs/**/README.md` + root `README.md` + `docs/README.md` maps | Low |
| **3** | Bulk link rewrite (scripted: old path → new path table) | Medium |
| **4** | Fix footers / “doc NN” prose / absolute GitHub URLs | Low |
| **5** | Validator + CI update; `validate_repo.py` PASS | Gate |
| **6** | Delete empty old folders; move this plan to `_internal/` | Low |
| **7** *(follow-up PR)* | Content merges (fold roadmap into handoff; trim 28 vs 01 dossier duplication; H1 renames inside files) | Editorial |

**Do not** combine Phase 7 content rewriting with the mechanical move PR.

---

## 9. Open decisions (need your call before execute)

| # | Decision | Default if you say “go with defaults” |
| ---: | :--- | :--- |
| D1 | Decade folders (`10-client`) vs semantic only (`client/`)? | **Decades** (sortable, scannable) |
| D2 | `start/rob` vs keep `for-rob` name? | **`start/rob`** (clearer hierarchy) |
| D3 | Archive `02-WHAT-WE-DID`? | **Yes → archive** |
| D4 | Archive `19` + `22`? | **Yes** |
| D5 | Fold thin `IMPLEMENTATION-ROADMAP` into handoff? | **Yes** |
| D6 | Drop all global “doc NN” language in the same PR? | **Phase 4 yes** (mechanical replace via map) |
| D7 | Execute now on `feature/wiseq-test-lab-assistant`? | Wait for explicit “execute the restructure” |

---

## 10. Out of scope

- Renaming `data/client/`, research-lanes, claims ledger IDs  
- Rewriting blueprint commercial content  
- Lab package layout  
- Translating everything to NL  

---

## 11. Success criteria

- [ ] No `a-proposal`…`g-reviews`, `for-*`, `audits/`, `00-nl/` left  
- [ ] Rob path ≤ 4 clicks from repo root to dossier + open-asks  
- [ ] Filename matches purpose (no PY / Fifty / Jev)  
- [ ] One primary doc per question in §4  
- [ ] `python scripts/validate_repo.py` PASS  
- [ ] Root pitch links resolve  
- [ ] `50-evidence` listed as first-class in docs hub  

---

## 12. Quick “before → after” for Rob

| Before | After |
| :--- | :--- |
| `docs/start/rob/THE-CASE-…` | `docs/start/rob/the-case.md` |
| `docs/10-client/30-CLIENT-…` | `docs/10-client/01-complete-dossier.md` |
| `docs/20-offer/04-AI-STACK-…` | `docs/20-offer/01-blueprint.md` |
| `docs/50-evidence/PREPARATION-…` | `docs/50-evidence/01-preparation-catalog.md` |
| “see doc 29” | `docs/60-governance/03-critical-audit-2026-10-27.md` |

---

*Approve D1–D7 (or say “defaults + execute”) and the mechanical restructure can run as one PR.*
