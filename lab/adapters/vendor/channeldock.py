from __future__ import annotations

from contracts.providers import InventoryProvider, OrderProvider, SimulatedResult

from .base import VendorNotConfigured


class ChannelDockReadStub(VendorNotConfigured, InventoryProvider, OrderProvider):
    system = "channeldock"

    def get_stock(self, sku: str, account_id: str) -> SimulatedResult:
        return self._blocked("get_stock")

    def get_bundle_components(self, bundle_sku: str) -> SimulatedResult:
        return self._blocked("get_bundle_components")

    def list_open_orders(self, account_id: str) -> SimulatedResult:
        return self._blocked("list_open_orders")
