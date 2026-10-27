# AI and OSS opportunity map

*Ranked by offline testability × business impact. Prefer keep/extend incumbents unless lab proves otherwise.*

## Scoring (1–5)

Impact · Frequency · Error cost · Effort↓ · Offline testability · Confidence

## Priority queue (Milestone 1 → next)

| Rank | Opportunity | Approach bias | Offline? | Score notes |
| ---: | :--- | :--- | :---: | :--- |
| 1 | Canonical EAN / bundle integrity | **Extend** (registry + CD) | Yes | Unblocks school + purchase |
| 2 | School-order draft pipeline | **Extend** e-Boekhouden + Hermes | Yes (synthetic) | Flagship time save |
| 3 | Shipping template + tariff validation | **Extend** Mastersheet→engine | Yes | Stops ungefrankeerd |
| 4 | Assortment / promise monitor | **Extend** bol+CD read | Partial | Needs tokens later |
| 5 | Mailbox triage drafts | **Extend** IMAP + Hermes | Yes (fixtures) | Draft-only |
| 6 | Purchase / LVB suggestions | **Extend** FiveX exports | Partial | SQL baselines first |
| 7 | Review triage (bol) | **Extend** carefully | Yes | Policy-constrained |
| 8 | PDF offer/invoice render | **OSS** QuestPDF | Yes | Complement e-Boekhouden |
| 9 | Helpdesk tickets | **OSS** UVdesk *or* keep mailbox | Later | Only if ticket model wins |
| 10 | Flow sidecar | **OSS** n8n | Later | After Hermes skills prove value |
| 11 | Analytics | **OSS** Umami | Later | Privacy fit |
| 12 | Replace ChannelDock | **Reject for now** | — | No measured gap vs native bundles |
| 13 | Replace e-Boekhouden | **Reject for now** | — | Wrong problem; API first |
| 14 | Autonomouse review deletion | **Reject** | — | Policy + AVG |

## Incumbent default

| System | Default decision until lab says otherwise |
| :--- | :--- |
| ChannelDock | **Keep** + extend with monitors |
| FiveX | **Keep** exports; investigate price rule; no blind auto-write |
| e-Boekhouden | **Keep**; prove API |
| bol ×3 | **Keep**; multi-account wrappers |
| Mastersheet | **Improve** → typed tariffs in lab; retire as calc engine |
| Shopify | **Keep**; EAN backfill |

## Empty OSS stubs (do not pretend coverage)

`inventory-sync`, `invoice-parse`, `review-automation`, `product-matching`, `content-generation`, `edtech` under [`data/oss/`](../../data/oss/) — refill only when an experiment needs them.

---

*Experiments A–C register: [EXPERIMENT-REGISTER](09-experiment-register.md)*
