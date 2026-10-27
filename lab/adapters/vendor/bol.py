from __future__ import annotations

from contracts.providers import MarketplaceProvider, ReviewProvider, SimulatedResult

from .base import VendorNotConfigured


class BolRetailerReadStub(VendorNotConfigured, MarketplaceProvider, ReviewProvider):
    system = "bol"

    def assortment_online(self, account_id: str) -> SimulatedResult:
        return self._blocked("assortment_online")

    def triage(self, account_id: str) -> SimulatedResult:
        return self._blocked("triage")
