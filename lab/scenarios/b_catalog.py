"""Experiment B — SKU / EAN / bundle integrity."""

from __future__ import annotations

from adapters.fixture import FixtureInventory, FixtureShipping


def run_catalog_integrity() -> dict:
    inv = FixtureInventory()
    ship = FixtureShipping()

    bundles = inv.all_bundles_resolve()
    eans = inv.missing_eans()
    ok_clone = ship.clone_template("Lichte kabels")
    bad_clone = ship.clone_template("2x Adapter ?")
    case_clone = ship.clone_template("Koptelefooncase")

    sample_bundle = next(iter(inv._bundles.keys()))
    comps = inv.get_bundle_components(sample_bundle)

    return {
        "bundle_count": bundles.data["bundle_count"],
        "unresolved_bundles": bundles.data["unresolved_bundles"],
        "missing_ean_count": eans.data["missing_ean_count"],
        "sample_bundle": comps.data,
        "clone_ok_class": ok_clone.to_dict(),
        "clone_needs_confirmation": bad_clone.to_dict(),
        "clone_headphone_case": case_clone.to_dict(),
        "simulated": True,
    }
