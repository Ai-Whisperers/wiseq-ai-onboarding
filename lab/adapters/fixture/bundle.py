from __future__ import annotations

import csv

from contracts.providers import SimulatedResult

from ._paths import REGISTRY_CSV, SPINE_CSV


class FixtureInventory:
    """Loads the repo bundle spine as synthetic inventory truth for the lab."""

    def __init__(self) -> None:
        spine = SPINE_CSV
        reg = REGISTRY_CSV
        self._components = {
            r["component_sku"].strip(): r
            for r in csv.DictReader(reg.open(encoding="utf-8"))
        }
        self._bundles: dict[str, list[str]] = {}
        for row in csv.DictReader(spine.open(encoding="utf-8")):
            b = row["bundle_sku"].strip()
            comps = []
            for key in ("component_1", "component_2", "component_3"):
                val = (row.get(key) or "").strip()
                if val:
                    comps.append(val)
            self._bundles[b] = comps
        self._stock = {sku: 25 for sku in self._components}
        for b in self._bundles:
            self._stock[b] = 10

    def get_stock(self, sku: str, account_id: str) -> SimulatedResult:
        if sku not in self._stock:
            return SimulatedResult(ok=False, data={}, error=f"unknown sku {sku}")
        return SimulatedResult(
            ok=True,
            data={"sku": sku, "account_id": account_id, "qty": self._stock[sku]},
        )

    def get_bundle_components(self, bundle_sku: str) -> SimulatedResult:
        comps = self._bundles.get(bundle_sku)
        if comps is None:
            return SimulatedResult(ok=False, data={}, error="not a known bundle")
        missing = [c for c in comps if c not in self._components]
        return SimulatedResult(
            ok=True,
            data={
                "bundle_sku": bundle_sku,
                "components": comps,
                "unresolved": missing,
                "ok": not missing,
            },
        )

    def missing_eans(self) -> SimulatedResult:
        """Registry has no EAN column today — all components count as missing EAN in lab."""
        gaps = list(self._components.keys())
        return SimulatedResult(
            ok=True,
            data={
                "missing_ean_count": len(gaps),
                "sample": gaps[:10],
                "note": "component registry has no ean column — catalog integrity gap",
            },
        )

    def all_bundles_resolve(self) -> SimulatedResult:
        bad = []
        for b, comps in self._bundles.items():
            missing = [c for c in comps if c not in self._components]
            if missing:
                bad.append({"bundle": b, "missing": missing})
        return SimulatedResult(
            ok=True,
            data={"bundle_count": len(self._bundles), "unresolved_bundles": bad},
        )
