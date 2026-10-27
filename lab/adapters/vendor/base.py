"""Vendor adapters stay inert until Gate 1.2 read keys land."""

from __future__ import annotations

from contracts.providers import SimulatedResult


class VendorNotConfigured:
    """Mixin: all calls fail closed with a clear next step."""

    system: str = "vendor"

    def _blocked(self, op: str) -> SimulatedResult:
        return SimulatedResult(
            ok=False,
            data={},
            simulated=True,
            source="vendor-stub",
            error=(
                f"{self.system}.{op} blocked: no read credentials. "
                "Send Wave 1 keys via docs/start/rob/read-only-access.md"
            ),
        )
