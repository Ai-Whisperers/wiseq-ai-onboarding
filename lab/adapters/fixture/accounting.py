from __future__ import annotations

from contracts.providers import SimulatedResult


class FixtureAccounting:
    """e-Boekhouden-like lifecycle on fixtures (simulated)."""

    def __init__(self) -> None:
        self._offers: dict[str, dict] = {}
        self._invoices: dict[str, dict] = {}

    def draft_offer(self, school_order_id: str, lines: list[dict]) -> SimulatedResult:
        offer_id = f"offer_{school_order_id}"
        if offer_id in self._offers:
            return SimulatedResult(
                ok=True,
                data={**self._offers[offer_id], "idempotent_replay": True},
            )
        draft = {
            "offer_id": offer_id,
            "school_order_id": school_order_id,
            "lines": lines,
            "status": "draft",
            "system": "e-boekhouden-sim",
        }
        self._offers[offer_id] = draft
        return SimulatedResult(ok=True, data=draft, needs_approval=True)

    def draft_invoice(self, offer_id: str) -> SimulatedResult:
        offer = self._offers.get(offer_id)
        if not offer:
            return SimulatedResult(ok=False, data={}, error="offer not found")
        inv_id = f"inv_{offer_id}"
        if inv_id in self._invoices:
            return SimulatedResult(
                ok=True,
                data={**self._invoices[inv_id], "idempotent_replay": True},
            )
        draft = {
            "invoice_id": inv_id,
            "offer_id": offer_id,
            "status": "draft",
            "system": "e-boekhouden-sim",
        }
        self._invoices[inv_id] = draft
        return SimulatedResult(ok=True, data=draft, needs_approval=True)

    def commit_invoice(self, draft_id: str, approved: bool) -> SimulatedResult:
        inv = self._invoices.get(draft_id)
        if not inv:
            return SimulatedResult(ok=False, data={}, error="invoice draft not found")
        if not approved:
            return SimulatedResult(
                ok=True,
                data={**inv, "status": "awaiting_approval"},
                needs_approval=True,
            )
        if inv.get("status") == "committed":
            return SimulatedResult(
                ok=True,
                data={**inv, "idempotent_replay": True},
            )
        inv = {**inv, "status": "committed"}
        self._invoices[draft_id] = inv
        return SimulatedResult(ok=True, data=inv)
