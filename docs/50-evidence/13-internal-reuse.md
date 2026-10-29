# Internal reuse + external best practices — WiseQ implementation map

*Research pass 2026-10-27. Sources: our live infrastructure inventory, [doc 14](../40-build/03-aiw-reuse.md), [doc 07](../10-client/06-bundle-spine-reuse.md), [doc 13](../40-build/02-tooling-mcp.md), lab state, industry patterns (mcp-eval / golden-set pytest, Langfuse OSS, adapter contracts). The inventory is described by capability, not by repository or client name — see the naming rule in doc 14.*

**Principle:** reuse AIW production patterns; do not copy client-specific or Bucket-C personal skills. Prefer keep/extend WiseQ SaaS unless lab proves otherwise.

---

## 1. What WiseQ already has (baseline)

| Layer | Status |
| :--- | :--- |
| Evidence / claims | Strong (ledger, audits, doc 29) |
| Synthetic lab A–C | Working (`lab/` · 9 pytest) |
| Hermes Desktop path | Documented; skills pack ready |
| Read-only Rob guide | [`READ-ONLY-ACCESS-GUIDE`](../start/rob/read-only-access.md) |
| Lab Hermes skills | **6/9** — present: operations, school-pipeline, shipping-econ, catalog-integrity, ops-briefing, client-communication. **Missing stubs:** shopify-admin-ops, bol-retailer-ops, oss-vat-watchdog, compliance-triage, reputation-engine, incident-runbooks (doc 24 lists nine; some names differ) |
| Thin MCP wrappers | **Not built yet** (`adapters/vendor` empty) |
| `lab/eval/` harness | **Stub only** — need golden mailbox cases + audit log |
| Observability / cost P&L | **Missing** (Langfuse / hermes-agent health) |
| School-order labeled eval set | **Missing** (doc 07: 50+ emails) |
| `wiseq-ops` / `commerce-os` | **Missing** — decide before 2nd MCP |
| Secrets vault wiring | Policy only |
| Guardrails-as-code | Approval in scenarios only — no margin-floor / invite-cap tests yet |

---

## 2. AIW org repos — worth considering for WiseQ

Scored: **Port now** · **Adapt pattern** · **Later** · **Ignore for WiseQ**.

### Port / adapt soon (high leverage)

| Capability | Why it matters | WiseQ action |
| :--- | :--- | :--- |
| **Proven thin MCP server** | A working **thin MCP server** pattern | Template for `bol-mcp`, `eboekhouden-mcp`, later ChannelDock |
| **Production backend skeleton** | FastAPI+SQLite, pre-commit, Vale, AGENTS.md, Makefile, smoke, CI discipline | Copy **repo hygiene**: `AGENTS.md`, Makefile targets, pre-commit, CHANGELOG — not the source domain |
| **Outreach / cadence / lead-scoring engine** | Lead intake → scoring → outreach cadence | Phase 2 B2B on 857-org list — cadence design only |
| **Public sanitized run ledger** | Status + run history, auto-generated | Optional trust page for B2B later |
| **Audit-trail ledger discipline** | Immutable action log + cost lines | Pattern for agent action log + cost lines |
| **Commerce research stack** | The source of the doc 07 transfer map | Bundle spine (done), eval harness shape, competitor watch, margin floors |
| **Ops documentation set** | Hermes/MCP/cron runbooks (archived topics) | Read for Desktop+gateway ops runbooks; do not paste secrets |
| **Agent-definition corpus** | Agent defs / generic skills / research | Mine **generic** skills (research, prompt-injection); never engagement-specific or personal ones |
| **Py/TS boilerplate templates** | Standard project scaffolding | Scaffold `wiseq-ops` or MCP packages |
| **Multi-domain research corpus** | 14-domain research corpus | Spot-check Hermes client setup chapters when designing Desktop profile |
| **Decisions-extraction pipeline** | Meeting → structured decisions log | Optional: Rob meeting → decisions log for audits |
| **Stack configuration mirror** | Stacks mirror, secrets redacted | Pattern for companion VPS compose later |

### Mentioned in doc 14 but not in the capability list above

| Capability | Action |
| :--- | :--- |
| **Hermes observability library** | **Find & wire** cron-health + alert-router before any always-on cron |
| **Ops bootstrap toolkit** | Companion VPS bootstrap when hosting leaves Desktop-only |
| **Shared design-token package** / site templates | Only if building real storefront (out of M1) |
| **Multi-agent dispatch fleet** | Pattern for multi-agent dispatch — **do not** port internal auth tokens to the client |

### Ignore / do not leak into WiseQ

| Class | Reason |
| :--- | :--- |
| Internal org state, orchestration dashboards, versioned state stores | Internal PII/cost |
| Personal, family, and non-Dutch product sites | Wrong domain |
| Domain modules from other product lines | Wrong product; hygiene only |
| Growth coaching / wizard / occult | Irrelevant |

---

## 3. External projects & practices (industry)

| Practice / project | Use for WiseQ |
| :--- | :--- |
| **Adapter + contract tests** (already started in `lab/`) | Keep; extend with JSON Schema on every `SimulatedResult` |
| **Golden sets** (intent/tools/fields, not full prose) | School-mail parser eval: 30–50 cases; CI on structure |
| **mcp-eval / MCP contract harness** | Gate publish of bol/e-Boekhouden MCP: `expect_tools`, schema fixtures, offline only |
| **Langfuse OSS core** or **Laminar** (doc 14) | Trace Desktop+cron decisions; cost per school-order |
| **OpenObserve / Better Stack** | Uptime + token spend as P&L line |
| **changedetection.io** | Competitor + public bol drift watch (doc 07) |
| **QuestPDF / zint** | Offer PDF + EAN labels when drafting leaves Markdown |
| **n8n** (sidecar) | Only after Hermes skills prove value — Hermes decides, n8n executes |
| **UVdesk / BillionMail / Umami** | Investigate if mailbox/ESP/analytics gaps appear in lab |
| **Bitwarden / 1Password Send** | Credential intake (already in Rob guide) |
| **ADR (Architecture Decision Records)** | Short `docs/adr/` for Desktop-first, e-Boekhouden, no Exact |
| **pre-commit + ruff/black + gitleaks** | Match our house engineering standard |
| **SemVer + CHANGELOG** | For `lab/` and future MCP packages |

**Do not adopt:** random “AI ecommerce OS” repos that replace ChannelDock without measured gap; Exact Online MCP; review-manipulation tools.

---

## 4. Professionalism gaps in *this* repo (honest)

| Gap | Impact | Fix |
| :--- | :--- | :--- |
| No `AGENTS.md` / CONTRIBUTING at root | New sessions re-derive norms | Add from our house pattern + HANDOFF |
| No Makefile | Ritual commands tribal | `make lab-test validate` |
| No school-order golden JSON set | Parser will be vibe-tested | `lab/fixtures/mailbox/eval_cases.json` |
| No action/audit SQLite | Can’t prove what agent did | `lab/eval/audit.db` schema |
| No cost telemetry | Can’t defend TCO | Log tokens/scenario stub → Langfuse later |
| Vendor adapters empty | Read-only keys unused | Implement after Rob wave 1 |
| Docs sprawl (legacy flat `docs/04-*`) | Confusion | Track-only links; deprecate duplicates in ADR |
| No `commerce-os` MCP monorepo | Wrappers will fork per client | Decide before 2nd MCP (doc 14 §C) |
| Desktop skills not hermes-trusted by default | Rob friction | PROFILE.md already; add install script |
| Observability day-1 skipped | Silent cron failures later | Port hermes-agent health before companion VPS |

---

## 5. Recommended implementation backlog (ordered)

### P0 — this week (professionalize lab)

1. **`AGENTS.md` + root Makefile** — validate, lab-test, list scenarios (our house hygiene standard).  
2. **School-order eval golden set** (30–50 cases in `lab/eval/` + mailbox fixtures).  
3. **Audit log** — every fixture commit → `lab/eval/audit.jsonl` / sqlite.  
4. **ADR-001 Desktop-first / ADR-002 e-Boekhouden**.  
5. **Skill stubs** for remaining doc-24 skills (bol-retailer-ops, reputation-engine, incident-runbooks at minimum).  
6. **Commit** read-only guide + this research doc on `feature/wiseq-test-lab-assistant`.

### P1 — after Rob wave 1 keys

6. **Thin-MCP-style stubs** for bol read + e-Boekhouden list (separate package or `lab/adapters/vendor/`).  
7. **MCP contract tests** (tool list + schemas) in CI — no live network.  
8. **Capability matrix fill** from smoke reads.  
9. **Secrets**: a dedicated vault (Bitwarden/1Password org) for WiseQ — never repo.  
10. **Monday shop↔bol drift report** from public sources first (doc 07).

### P2 — productize

11. Spin **`wiseq-ops`** (or private sibling) for connectors; keep onboarding as evidence attic.  
12. **Langfuse OSS** traces on Hermes profile.  
13. **cron-health** from hermes-agent before always-on VPS.  
14. **Outreach-engine** cadence for B2B only after AVG templates.  
15. **QuestPDF** offer draft render from school pipeline output.

### Explicitly defer

- Replace ChannelDock / FiveX / e-Boekhouden  
- n8n until 3+ Hermes skills are daily-used  
- Full storefront (`site-template`)  
- Internal orchestration dashboards  

---

## 6. Decision: one MCP monorepo?

**Recommendation:** create a private `commerce-os` MCP package **before** the second WiseQ MCP lands. The onboarding repo stays public evidence; the wrappers stay private, licensed to WiseQ per doc 18. Prevents copy-paste of the bol MCP into separate engagements.

---

## 7. Session checklist for implementers

```text
[ ] Read HANDOFF + this doc
[ ] Don’t port Bucket C skills
[ ] Prefer fixture → vendor sandbox → read → draft → write
[ ] Every new automation needs a golden or contract test
[ ] Cost/observability stub before “smart” model routing
[ ] Rob keys only via READ-ONLY-ACCESS-GUIDE
```

---

*Companion: [AI-AND-OSS-OPPORTUNITY-MAP](05-opportunity-map.md) · [EXPERIMENT-REGISTER](09-experiment-register.md) · [doc 14](../40-build/03-aiw-reuse.md)*
