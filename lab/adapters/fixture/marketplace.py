from __future__ import annotations

import json

from contracts.providers import SimulatedResult

from ._paths import FIXTURES


class FixtureMarketplace:
    def __init__(self) -> None:
        self._accounts = json.loads(
            (FIXTURES / "marketplace" / "accounts.json").read_text(encoding="utf-8")
        )

    def assortment_online(self, account_id: str) -> SimulatedResult:
        acct = self._accounts.get(account_id)
        if not acct:
            return SimulatedResult(ok=False, data={}, error=f"unknown account {account_id}")
        offline = [s for s in acct["skus"] if not s["online"]]
        return SimulatedResult(
            ok=True,
            data={
                "account_id": account_id,
                "label": acct["label"],
                "migration_state": acct["migration_state"],
                "total_skus": len(acct["skus"]),
                "offline_skus": offline,
                "all_online": len(offline) == 0,
            },
        )
