"""Approved vendor sandbox adapters — stubs until Wave 1 read keys."""

from .bol import BolRetailerReadStub
from .channeldock import ChannelDockReadStub
from .eboekhouden import EBoekhoudenReadStub
from .mailbox import MailboxReadStub

__all__ = [
    "BolRetailerReadStub",
    "ChannelDockReadStub",
    "EBoekhoudenReadStub",
    "MailboxReadStub",
]
