"""Provider contracts for WiseQ lab adapters."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Protocol


@dataclass
class SimulatedResult:
    ok: bool
    data: dict[str, Any]
    simulated: bool = True
    source: str = "fixture"
    error: str | None = None
    needs_approval: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class InventoryProvider(Protocol):
    def get_stock(self, sku: str, account_id: str) -> SimulatedResult: ...

    def get_bundle_components(self, bundle_sku: str) -> SimulatedResult: ...


class OrderProvider(Protocol):
    def list_open_orders(self, account_id: str) -> SimulatedResult: ...


class AccountingProvider(Protocol):
    def draft_offer(self, school_order_id: str, lines: list[dict[str, Any]]) -> SimulatedResult: ...

    def draft_invoice(self, offer_id: str) -> SimulatedResult: ...

    def commit_invoice(self, draft_id: str, approved: bool) -> SimulatedResult: ...


class ShippingProvider(Protocol):
    def quote(self, *, country: str, product_class: str, qty: int, method: str) -> SimulatedResult: ...

    def clone_template(self, product_class: str) -> SimulatedResult: ...

    def prepare_shipment(self, invoice_id: str, approved: bool) -> SimulatedResult: ...


class MarketplaceProvider(Protocol):
    def assortment_online(self, account_id: str) -> SimulatedResult: ...


class ReviewProvider(Protocol):
    def triage(self, account_id: str) -> SimulatedResult: ...


class MailboxProvider(Protocol):
    def list_messages(self, folder: str = "inbox") -> SimulatedResult: ...

    def get_message(self, message_id: str) -> SimulatedResult: ...
