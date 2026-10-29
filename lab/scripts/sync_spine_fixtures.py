#!/usr/bin/env python3
"""Refresh the vendored bundle-spine fixtures from the repo-root source of truth.

The lab vendors `wiseq-bundle-spine.csv` and `wiseq-component-registry.csv`
into `lab/fixtures/` so it stays self-contained (the Docker image contains
only `lab/`). The repo-root copies remain the source of truth.

Run this after changing either source CSV:

    python lab/scripts/sync_spine_fixtures.py

`--check` exits non-zero if the vendored copies are out of date — CI uses that
to fail the build on drift.
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parent
FIXTURES = LAB_ROOT / "fixtures"

PAIRS = [
    (REPO_ROOT / "data" / "wiseq-bundle-spine.csv", FIXTURES / "wiseq-bundle-spine.csv"),
    (REPO_ROOT / "data" / "wiseq-component-registry.csv", FIXTURES / "wiseq-component-registry.csv"),
]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify only; exit 1 on drift")
    args = ap.parse_args(argv[1:])

    drifted: list[Path] = []

    for src, dst in PAIRS:
        if not src.exists():
            print(f"ERROR  source missing: {src}", file=sys.stderr)
            return 2

        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            if args.check:
                drifted.append(dst)
                print(f"DRIFT  {dst.name} differs from {src.relative_to(REPO_ROOT)}")
                continue
            shutil.copy2(src, dst)
            print(f"synced {dst.name}  <-  {src.relative_to(REPO_ROOT)}")

    if args.check:
        if drifted:
            print(
                "\nVendored spine fixtures are out of date.\n"
                "Run: python lab/scripts/sync_spine_fixtures.py",
                file=sys.stderr,
            )
            return 1
        print("✓ vendored spine fixtures match the repo-root source of truth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
