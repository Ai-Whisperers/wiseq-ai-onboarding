from __future__ import annotations

from contracts.providers import MailboxProvider, SimulatedResult

from .base import VendorNotConfigured


class MailboxReadStub(VendorNotConfigured, MailboxProvider):
    system = "mailbox"

    def list_messages(self, folder: str = "inbox") -> SimulatedResult:
        return self._blocked("list_messages")

    def get_message(self, message_id: str) -> SimulatedResult:
        return self._blocked("get_message")
