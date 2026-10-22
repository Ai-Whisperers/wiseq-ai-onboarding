#!/usr/bin/env python3
"""scripts/validate_repo.py — repo-integrity validator for wiseq-ai-onboarding.

CI gate (GitHub Actions) + local runnable (`python scripts/validate_repo.py`).
Validates:
  1. Every docs/ file referenced in README.md exists (no broken doc links)
  2. data/oss/*.json parse and carry the required keys (query, items)
  3. data/oss/*.json items have required fields (full_name, url, stars)
  4. data/wiseq-bundle-spine.csv: every bundle's components exist in the
     component registry (referential integrity of the spine)
  5. data/wiseq-component-registry.csv: unique component SKUs
  6. No file contains obvious secrets (token/keyword patterns)

Exit code 0 = pass; non-zero with itemized failures = fail.
Stdlib only — runs on any python3.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures: list[str] = []
checks = 0


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  ✗ {msg}")


def check(cond: bool, good: str, bad: str) -> None:
    global checks
    checks += 1
    ok(good) if cond else fail(bad)


print("== 1. README doc links")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
doc_links = re.findall(r"\]\((docs/[^)#]+)", readme)
check(bool(doc_links), f"{len(doc_links)} doc links found", "no doc links in README")
for link in doc_links:
    p = ROOT / link
    check(p.is_file(), f"exists: {link}", f"MISSING: {link}")

print("== 2. data/oss/*.json schema")
oss_dir = ROOT / "data" / "oss"
oss_files = sorted(oss_dir.glob("*.json"))
check(bool(oss_files), f"{len(oss_files)} oss data files", "no oss data files")
total_items = 0
for jf in oss_files:
    try:
        data = json.loads(jf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{jf.name}: invalid JSON ({e})")
        continue
    if "items" not in data or "query" not in data:
        fail(f"{jf.name}: missing 'items' or 'query' key")
        continue
    bad_items = [i for i in data["items"] if not all(k in i for k in ("full_name", "url", "stars"))]
    if bad_items:
        fail(f"{jf.name}: {len(bad_items)} items missing required fields")
    else:
        total_items += len(data["items"])
ok(f"{total_items} total items across {len(oss_files)} files pass schema")

print("== 3. bundle-spine referential integrity")
spine = ROOT / "data" / "wiseq-bundle-spine.csv"
registry = ROOT / "data" / "wiseq-component-registry.csv"
check(spine.is_file() and registry.is_file(), "spine + registry CSVs present", "spine/registry CSV missing")
if spine.is_file() and registry.is_file():
    reg_rows = list(csv.DictReader(spine.open(encoding="utf-8"))) and list(csv.DictReader(registry.open(encoding="utf-8")))
    reg_skus = {r["component_sku"] for r in reg_rows}
    check(len(reg_skus) == len(reg_rows), f"{len(reg_rows)} unique component SKUs", f"duplicate SKUs in registry ({len(reg_rows) - len(reg_skus)} dupes)")
    bundles = list(csv.DictReader(spine.open(encoding="utf-8")))
    missing_refs = []
    for b in bundles:
        for comp in (b.get("component_1", ""), b.get("component_2", ""), b.get("component_3", "")):
            if comp and comp not in reg_skus:
                missing_refs.append(f"{b['bundle_sku']}->{comp}")
    check(not missing_refs, f"all {len(bundles)} bundles resolve to registry components",
          f"unresolved refs: {missing_refs[:5]}")

print("== 4. secret scan")
SECRET_PAT = re.compile(r"(ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})")
hits = []
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".json", ".csv", ".yml", ".yaml", ".txt", ".py"}:
        try:
            m = SECRET_PAT.search(f.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
        if m:
            hits.append(f"{f.relative_to(ROOT)}: {m.group(0)[:12]}…")
check(not hits, "no secret patterns found", f"secrets detected: {hits[:3]}")

print("== 5. in-page anchor integrity")
# Emoji and punctuation in headings make GitHub's slugger unpredictable, so anchors
# are pinned explicitly with <a id="...">. Every in-page link must resolve to one.
anchors = set()
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    anchors.update(re.findall(r'<a id="([^"]+)">', md.read_text(encoding="utf-8", errors="ignore")))
broken_anchors = []
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8", errors="ignore")
    for target in re.findall(r"\]\(#([a-z0-9][a-z0-9\-]*)\)", text, re.I):
        if target not in anchors:
            broken_anchors.append(f"{md.relative_to(ROOT)}->#{target}")
check(not broken_anchors, f"all in-page anchors resolve ({len(anchors)} pinned)",
      f"broken anchors: {broken_anchors[:5]}")

print(f"\n{checks} checks run, {len(failures)} failures")
if failures:
    print("VALIDATION FAILED")
    sys.exit(1)
print("VALIDATION PASSED ✓")
