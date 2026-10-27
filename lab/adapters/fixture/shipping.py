from __future__ import annotations

import csv
import json
from pathlib import Path

from contracts.providers import SimulatedResult

from ._paths import FIXTURES


class FixtureShipping:
    def __init__(self) -> None:
        self._tariffs = json.loads(
            (FIXTURES / "shipping" / "tariffs_typed.json").read_text(encoding="utf-8")
        )
        self._templates = list(
            csv.DictReader((FIXTURES / "shipping" / "templates.csv").open(encoding="utf-8"))
        )

    def quote(self, *, country: str, product_class: str, qty: int, method: str) -> SimulatedResult:
        key = f"{method}:{country}:{product_class}"
        row = self._tariffs.get(key)
        if not row:
            return SimulatedResult(
                ok=False,
                data={},
                error=f"no tariff for {key}",
            )
        note = row.get("note")
        if note and row.get("kind") == "UNVALIDATED_CLIENT_NOTE":
            return SimulatedResult(
                ok=False,
                data={"note": note, "kind": row["kind"]},
                error="unvalidated client observation — not a tariff quote",
            )
        unit = float(row["eur"])
        return SimulatedResult(
            ok=True,
            data={
                "country": country,
                "product_class": product_class,
                "qty": qty,
                "method": method,
                "unit_eur": unit,
                "total_eur": round(unit * max(qty, 1), 2),
                "currency": "EUR",
                "source_effective": row.get("source_effective"),
            },
        )

    def clone_template(self, product_class: str) -> SimulatedResult:
        match = next((r for r in self._templates if r["category"] == product_class), None)
        if not match:
            return SimulatedResult(ok=False, data={}, error=f"unknown class {product_class}")
        status = (match.get("validation_status") or "").strip()
        if status != "OK":
            return SimulatedResult(
                ok=False,
                data={"validation_status": status, "row": match},
                error=f"refuse auto-clone: validation_status={status}",
            )
        return SimulatedResult(
            ok=True,
            data={
                "template_ean": match["template_ean"],
                "category": product_class,
                "validation_status": status,
            },
            needs_approval=True,
        )

    def prepare_shipment(self, invoice_id: str, approved: bool) -> SimulatedResult:
        if not approved:
            return SimulatedResult(
                ok=True,
                data={"invoice_id": invoice_id, "status": "awaiting_approval"},
                needs_approval=True,
            )
        if not invoice_id.startswith("inv_"):
            return SimulatedResult(ok=False, data={}, error="invoice_id required")
        return SimulatedResult(
            ok=True,
            data={
                "shipment_id": f"ship_{invoice_id}",
                "carrier": "DHL_MYPARCEL_SIM",
                "status": "label_prepared_simulated",
            },
        )
