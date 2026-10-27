# Test lab architecture

## Goal

Reproduce WiseQ workflows **without** production credentials. Compare incumbent simulation vs extensions vs bounded OSS later.

## Layout

See [`lab/README.md`](../../lab/README.md).

## Adapter pattern

```text
Scenario → Provider Protocol → FixtureAdapter (default)
                            → OssAdapter (optional later)
                            → VendorAdapter (after approval)
```

Every response includes `simulated: bool` and `source: str`.

## Providers

`InventoryProvider`, `OrderProvider`, `AccountingProvider`, `ShippingProvider`, `MarketplaceProvider`, `ReviewProvider`, `MailboxProvider`.

## Determinism

Golden JSON under `lab/scenarios/expected/`. Pytest asserts exact business fields. AI probabilistic paths (if any) use separate eval thresholds — Milestone 1 scenarios are **rule-based**, not model-scored.

## CI

`pytest lab/` on PRs + existing `validate_repo.py`.
