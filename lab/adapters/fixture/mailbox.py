from __future__ import annotations

import json

from contracts.providers import SimulatedResult

from ._paths import FIXTURES


class FixtureMailbox:
    def __init__(self) -> None:
        self._messages = json.loads(
            (FIXTURES / "mailbox" / "school_inbox.json").read_text(encoding="utf-8")
        )

    def list_messages(self, folder: str = "inbox") -> SimulatedResult:
        msgs = [m for m in self._messages if m.get("folder", "inbox") == folder]
        return SimulatedResult(ok=True, data={"messages": msgs})

    def get_message(self, message_id: str) -> SimulatedResult:
        for m in self._messages:
            if m["id"] == message_id:
                return SimulatedResult(ok=True, data=m)
        return SimulatedResult(ok=False, data={}, error="message not found")
