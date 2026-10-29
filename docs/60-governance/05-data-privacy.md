# Data privacy & publication boundaries

*2026-10-29. This page states, in plain language, what is published in this repository, what is deliberately **not** published, and who decides.*

## 1. The short version

This is a **client-facing** repository. It publishes our research, our recommendations, and a synthetic test lab. It does **not** publish the raw material a client handed us, our internal cost analysis, or the names of the other engagements our capabilities came from.

## 2. What is published

| Category | Examples |
| :--- | :--- |
| Research & analysis | `docs/30-market/`, `docs/50-evidence/`, `data/research-lanes/` |
| Recommendations & commercial terms | `docs/20-offer/` |
| A sanitized extract of the client operations manual | `data/client/OPERATING-MANUAL-EXTRACT.md` |
| A sanitized extract of the mastersheet | `data/client/MASTERSHEET-EXTRACT.md` |
| The mastersheet working data (aggregated, no supplier pricing of third parties) | `data/client/mastersheet/` |
| A synthetic test lab — fake SKUs, fake orders, no live credentials | `lab/` |
| Our own public profile | `docs/70-showcase/03-who-we-are.md` |

## 3. What is NOT published, and why

### 3.1 Raw client source material

| File | Why it stays out | Where it lives |
| :--- | :--- | :--- |
| `data/client/Handleiding_opzet.txt` | The client's own operations manual, verbatim. Contains internal pricing, supplier terms, and staff detail. **Rob's explicit publication approval has not been collected.** | Private AIW handover folder, `700` permissions, outside any Git repository |
| `data/client/meetings/2026-10-28-transcript-turboscribe.txt` | A verbatim meeting transcript. Contains revenue, margin, and pricing discussion. | Same private handover folder |

The **sanitized extracts** of both are published and are the citable versions. If the client approves publication of the raw originals, we can add them deliberately — not by accident.

Enforcement is automated: `.github/workflows/validate.yml` fails the build if either file is ever tracked again, and `.gitignore` keeps them out of the tree.

### 3.2 Our internal working documents

`analysis/` holds our cost audits, margin models, and honest appraisals of our own weaknesses. Useful to us; not the client's business, and not public. Gitignored and CI-guarded.

### 3.3 Where our capabilities came from

We describe our previous work **by capability, not by client**.

We will say things like *"we built a catalog decomposition engine that decoded 25 bundles into 114 components"* or *"our house standard for CI is pinned action SHAs, minimum token permissions, and secret scanning on every push"*. We will not name the other engagements those capabilities were first built for, link to their repositories, or publish a transfer map that shows which client paid for which capability.

**Why:** a client should not be able to infer our commercial pipeline, our margins on other work, or the identity of other customers by reading a public repository. It is also simply not their business.

## 4. Who decides

| Change | Decision |
| :--- | :--- |
| Publishing a raw client file | **The client's written approval.** Not ours. |
| Publishing internal cost analysis | AIW internal — our call, our risk. |
| Naming another client or engagement | AIW internal — default is **no**. |
| Publishing a demo with synthetic data | AIW internal — allowed, and encouraged. |

## 5. Secrets

No credential of any kind appears in this repository. Read-only access tokens are requested privately, are labelled and revocable, and live in the client's own vault — never in Git. `scripts/validate_repo.py` scans every tracked text file for secret patterns on every push, and CI fails on a hit.

## 6. Related

- [Terms & confidentiality](01-terms.md) — the engagement-level confidentiality terms
- [Acceptance criteria](02-acceptance-criteria.md)
- [`data/client/README.md`](../../data/client/README.md) — the publication gate for client data
- [Rob pack](../start/rob/README.md) — the entry point we share with the client
