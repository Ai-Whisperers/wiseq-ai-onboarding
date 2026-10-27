# Data flow and systems of record

*Which system owns which fact. Conflicts are bugs until resolved.*

## Systems of record

| Domain | Authoritative system | Secondary / derived | Notes |
| :--- | :--- | :--- | :--- |
| Inventory qty / location | **ChannelDock** | FiveX exports, bol offers | Do not invent stock in Shopify alone |
| Bundle composition (ops) | **ChannelDock** native bundles | AIW `wiseq-bundle-spine.csv` (research) | Spine CI ≠ physical truth (Gate 3) |
| Product listing on bol | **bol Seller API** per account | FiveX | Three account identities |
| Own-shop catalog | **Shopify** | Feeds | 0/230 EAN in Oct 21 snapshot |
| School financial docs | **e-Boekhouden** | Email templates | Not Exact |
| Carrier tariffs (decision aid) | **Mastersheet** (dated exports) | Live carrier portals | Typed lab fixtures in `lab/fixtures/shipping/` |
| Shipping rule templates | **ChannelDock** (live) | Mastersheet clone table | Refuse `NEEDS_CONFIRMATION` |
| CE / conformity | **Google Drive library** | Manual | Missing → escalate |
| Customer mailbox | **Mailbox provider** (unnamed) | — | Read-only drafts first |
| Ops keywords / packaging URLs | Mastersheet | — | Public CSVs only |

## Multi-account bol identity

```text
order/listing → account_id ∈ {wiseq_nl, wiseq_electronics, wiseq_belgie}
```

Stock, offers, reviews, and credentials must never cross accounts without an explicit migration job (België phase-out).

## Happy-path school order data flow

```text
Mailbox (request)
  → draft relation + offer (e-Boekhouden) [human approve]
  → invoice [human approve]
  → MyParcel/DHL label prep [human approve]
  → ChannelDock / warehouse handoff
```

Every step needs an **idempotency key** (e.g. `school_order_id`) so retries do not duplicate invoices or labels.

## Conflict rules

| Conflict | Prefer | Escalate when |
| :--- | :--- | :--- |
| Shopify stock vs ChannelDock | ChannelDock | Drift > threshold |
| Mastersheet tariff vs live carrier | Live carrier (dated) | Sheet older than effective date |
| Manual 80% vs sheet 178% BE LVB | Neither for forecasts | Rob measurement note |
| AIW spine vs ChannelDock bundle | ChannelDock for ops | Physical reconcile Gate 3 |

## Lab vs production

| Mode | Adapters | Tag |
| :--- | :--- | :--- |
| Milestone 1 | `lab/adapters/fixture` | `simulated=true` |
| Future sandbox | vendor sandbox | `sandbox=true` |
| Production | vendor adapters | `simulated=false` + audit log |

---

*See also [stack-map](../../data/stack-map.md) capability matrix.*
