from __future__ import annotations

from typing import Any

from contracts.providers import AccountingProvider, SimulatedResult

from .base import VendorNotConfigured


class EBoekhoudenReadStub(VendorNotConfigured, AccountingProvider):
    system = "e-boekhouden"

    def draft_offer(self, school_order_id: str, lines: list[dict[str, Any]]) -> SimulatedResult:
        return self._blocked("draft_offer")

    def draft_invoice(self, offer_id: str) -> SimulatedResult:
        return self._blocked("draft_invoice")

    def commit_invoice(self, draft_id: str, approved: bool) -> SimulatedResult:
        return self._blocked("commit_invoice")
