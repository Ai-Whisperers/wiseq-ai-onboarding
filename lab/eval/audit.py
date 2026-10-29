from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# The audit log is a local file, never secrets. Its location is overridable
# because the Docker image runs with a read-only filesystem — WISEQ_EVAL_OUT
# points it at the writable tmpfs there.
_OUT = Path(os.environ.get("WISEQ_EVAL_OUT") or (Path(__file__).resolve().parent / "out"))
_LOG = _OUT / "audit.jsonl"


def append_audit(action: str, *, simulated: bool = True, approved: bool | None = None, **payload: Any) -> dict:
    """Append one audit row (local file; never secrets)."""
    _OUT.mkdir(parents=True, exist_ok=True)
    row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "simulated": simulated,
        "approved": approved,
        **payload,
    }
    with _LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def read_audit(limit: int = 100) -> list[dict]:
    if not _LOG.is_file():
        return []
    lines = _LOG.read_text(encoding="utf-8").strip().splitlines()
    rows = [json.loads(line) for line in lines if line.strip()]
    return rows[-limit:]
