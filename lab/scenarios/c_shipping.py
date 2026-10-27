"""Experiment C — shipping / unit economics (typed tariffs)."""

from __future__ import annotations

from adapters.fixture import FixtureShipping


CASES = [
    ("NL", "school_parcel", 1, "QLS_EUROPLUS", 10.54),
    ("BE", "school_parcel", 1, "QLS_EUROPLUS", 10.54),
    ("NL", "chargers_3xs", 1, "LVB", 2.78),
    ("BE", "chargers_3xs", 1, "LVB", 5.11),
    ("NL", "headphones_s", 1, "LVB", 6.27),
    ("NL", "light_cable", 5, "POSTNL", 1.85),
    ("BE", "light_cable", 10, "POSTNL", 4.42),
]


def run_shipping_quotes() -> dict:
    ship = FixtureShipping()
    results = []
    for country, pclass, qty, method, expected_unit in CASES:
        q = ship.quote(country=country, product_class=pclass, qty=qty, method=method)
        results.append(
            {
                "case": f"{method}:{country}:{pclass}:qty{qty}",
                "ok": q.ok,
                "unit_eur": q.data.get("unit_eur"),
                "total_eur": q.data.get("total_eur"),
                "expected_unit": expected_unit,
                "match": q.ok and q.data.get("unit_eur") == expected_unit,
            }
        )
    uplift = ship.quote(country="BE", product_class="lvb_uplift", qty=1, method="NOTE")
    return {
        "quotes": results,
        "all_match": all(r["match"] for r in results),
        "uplift_blocked": not uplift.ok and uplift.data.get("kind") == "UNVALIDATED_CLIENT_NOTE",
        "simulated": True,
    }
