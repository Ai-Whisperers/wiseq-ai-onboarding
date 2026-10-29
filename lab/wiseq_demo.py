#!/usr/bin/env python3
"""Demo CLI for the WiseQ test lab.

Prints the three synthetic scenarios (A: school order, B: catalog integrity,
C: shipping economics) as readable text. Every value shown comes from
fixtures — there are no production credentials and no live calls.

Usage:
    python -m wiseq_demo            # all scenarios
    python -m wiseq_demo school     # one scenario
    python -m wiseq_demo --json     # machine-readable
"""

from __future__ import annotations

import json
import sys

from scenarios.a_school import run_school_order
from scenarios.b_catalog import run_catalog_integrity
from scenarios.c_shipping import run_shipping_quotes

SCENARIOS = {
    "school": ("A — School order pipeline (simulated)", run_school_order),
    "catalog": ("B — Catalog / EAN / bundle integrity", run_catalog_integrity),
    "shipping": ("C — Shipping & unit economics", run_shipping_quotes),
}

BANNER = "=" * 68


def _fmt(value) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, default=str)


def run_one(name: str) -> dict:
    title, fn = SCENARIOS[name]
    print(BANNER)
    print(title)
    print(BANNER)
    result = fn()
    print(_fmt(result))
    print()
    return result


def main(argv: list[str]) -> int:
    args = argv[1:]
    as_json = "--json" in args
    names = [a for a in args if not a.startswith("-")] or list(SCENARIOS)

    unknown = [n for n in names if n not in SCENARIOS]
    if unknown:
        print(f"unknown scenario(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(SCENARIOS)}", file=sys.stderr)
        return 2

    results = {}
    for name in names:
        results[name] = run_one(name) if not as_json else SCENARIOS[name][1]()

    if as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False, default=str))

    print(BANNER)
    print("All scenarios ran on synthetic fixtures. No live calls, no writes.")
    print("Production actions require an explicit APPROVE and live read-only keys.")
    print(BANNER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
