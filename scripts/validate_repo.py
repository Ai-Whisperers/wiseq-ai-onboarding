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

print("== 8. site concept links are live, not repo paths")
# The three demos are published on the Pages site. A link to site-demos/<v>/ inside a
# markdown doc renders as a 404 in a browser, so gate on the live URL and on no raw
# repo-path hrefs surviving.
PAGES = "https://ai-whisperers.github.io/wiseq-ai-onboarding/site-demos/"
CONCEPTS = ["v1-cinematic", "v2-editorial", "v3-webgl"]
d17_low = (ROOT / "docs/17-SITE-CONCEPTS.md").read_text(encoding="utf-8").lower()
rd_low = (ROOT / "README.md").read_text(encoding="utf-8").lower()
for v in CONCEPTS:
    check(f"{PAGES}{v}/index.html" in d17_low,
          f"doc 17 links the live {v} page",
          f"doc 17 must link the published {v} URL, not the repo path")
    check(f"{PAGES}{v}/index.html" in rd_low,
          f"README links the live {v} page",
          f"README 'run it' must point at the published {v} URL")
    check(f'href="site-demos/{v}/"' not in rd_low,
          f"README has no repo-path href for {v}",
          f"README href \"site-demos/{v}/\" 404s in a browser — use the Pages URL")

print("== 6. commercial completeness")
# A proposal that never states its own price cannot be evaluated. Guard the two
# documents a buyer reads first, plus hat-count drift in the specialist review.
price_patterns = ["\u20ac3,500", "\u20ac8,000"]
d04 = (ROOT / "docs/04-AI-STACK-BLUEPRINT.md").read_text(encoding="utf-8")
check(all(x in d04 for x in price_patterns),
      "doc 04 states our actual prices (pilot + Phase 1)",
      "doc 04 must state our own prices, not just market benchmarks")

d04_low = d04.lower()
# NOTE: an earlier version of this check required the phrase "inside two months".
# That phrase was itself wrong: at the top of the investment range the worked
# example takes 2.3 months. The check now requires a payback range AND that the
# over-claiming phrase is absent.
check("what the time saving is worth" in d04_low and "payback" in d04_low,
      "doc 04 carries the payback arithmetic with a worked example",
      "doc 04 needs an ROI/payback section stating a payback period on worked numbers")
# The phrase may appear only inside a caveat that rejects it. Match an assertion:
# "inside two months" NOT preceded by 'not "' / 'not “' on the same line.
_payback_assertions = [i for i, l in enumerate(d04.split("\n"), 1)
                       if "inside two months" in l.lower()
                       and not re.search(r"not[\s\u201c\"']{0,3}\s*[\u201c\"']?inside two months",
                                         l.lower())]
check(not _payback_assertions,
      "doc 04 payback is stated as a range, not the over-claimed 'inside two months'",
      f"doc 04 asserts 'inside two months' at line(s) {_payback_assertions} — the "
      "worked example clears that only at the bottom of the investment range; state "
      "the 2-3 month range and flag the unsourced per-order time premise")

# The four hosting options must agree on price between 04 and 06, or the client
# will find two different numbers for the same choice.
d06 = (ROOT / "docs/06-NEXT-STEPS.md").read_text(encoding="utf-8")
check("\u20ac250" in d06 and "\u20ac175" in d06,
      "doc 06 prices every hosting option (care plan + shared rate)",
      "doc 06 must price hosting options (a) and (c) explicitly")

# README must not contradict the hosting decision it links to.
readme = (ROOT / "README.md").read_text(encoding="utf-8")
check("\u20ac20/mo VPS" not in readme,
      "README carries no stale fixed-cost claim",
      "README still claims a fixed \u20ac20/mo VPS; it must point at the four hosting options")

print("== 7. specialist-review integrity")
d12 = (ROOT / "docs/12-FIFTY-HATS.md").read_text(encoding="utf-8")
hat_titles = re.findall(r"^### \d+\.\s+(.+)$", d12, re.M)
normalised = [re.sub(r"\s*\(revisited\)\s*$", "", t).strip().lower() for t in hat_titles]
duplicates = sorted({t for t in normalised if normalised.count(t) > 1})
check(not duplicates,
      f"all {len(hat_titles)} specialist hats are distinct",
      f"duplicate hats: {duplicates}")

m = re.search(r"^# .*?(\d+) Hats", d12, re.M)
check(m and m.group(1) == str(len(hat_titles)),
      f"hat count in the title matches the body ({len(hat_titles)})",
      f"title says {m.group(1) if m else '?'} hats but body has {len(hat_titles)}")

readme_hat = re.search(r"Specialist Review — (\d+) Hats", readme)
check(readme_hat and readme_hat.group(1) == str(len(hat_titles)),
      "README hat count matches doc 12",
      "README hat count disagrees with doc 12")

# == 8. retracted-claim guards ================================================
# Each of these was a published claim that turned out to be false or arithmetically
# impossible. Every one of them was silently reintroduced by a later editing session
# at least once, so each gets a machine check. See analysis/RETRACTION-*.md (internal).
print("== 8. retracted-claim guards")

CLIENT_MD = [p for p in (ROOT / "docs").glob("*.md")] + [ROOT / "README.md"]
client_text = {p: p.read_text(encoding="utf-8") for p in CLIENT_MD}

def occurrences(pattern, exclude_docs=()):
    """Files+lines matching pattern, ignoring the correction notes themselves."""
    hits = []
    rx = re.compile(pattern, re.I)
    for p, text in client_text.items():
        if p.name in exclude_docs:
            continue
        for i, line in enumerate(text.split("\n"), 1):
            if rx.search(line):
                hits.append(f"{p.relative_to(ROOT)}:{i}")
    return hits

# (1) "250+ reviews" — impossible: reviews depend on buyers replying, not on us.
review_hits = occurrences(r"250\+ reviews|25 → 250", exclude_docs=("05-AUTOMATION-BACKLOG.md", "19-CRITICAL-REVIEW.md", "23-ACCEPTANCE-CRITERIA.md", "22-AUDIT-RESPONSE.md"))
check(not review_hits,
      "the impossible '250+ reviews' target is not stated as a promise anywhere",
      f"reintroduced at {review_hits} — reviews are not ours to produce; "
      "promise invitation coverage instead (see doc 05)")

# (2) Trustpilot invitations are NOT free and unlimited — they count towards the
#     monthly invitation allowance. This exact error was introduced by a fix.
inv_hits = occurrences(r"free and unlimited")
check(not inv_hits,
      "no claim that Trustpilot invitations are free and unlimited",
      f"reintroduced at {inv_hits} — API invitations count towards the monthly "
      "invitation allowance (developers.trustpilot.com/api-module-overview)")

# (3) GS1 10-pack arithmetic: 139 codes needs 14 packs, not 12 (12 covers 120).
# doc 08/11/19 quote the old figure inside their correction tables.
gs1_hits = [h for h in occurrences(r"€733")
            if not any(x in h for x in ("OSS-INTEGRATIONS", "COMPLIANCE-REGULATORY",
                                        "CRITICAL-REVIEW", "AUDIT-RESPONSE"))]
check(not gs1_hits,
      "GS1 is quoted at the corrected 14-pack figure, not the short-by-19 one",
      f"€733 reintroduced at {gs1_hits} — 139 codes = 14 packs of 10 = €854/yr; "
      "12 packs covers only 120 codes")

# (4) ChannelDock/5X DO have APIs. "No public API found" was a search failure
#     that was escalated into a critical risk and nearly killed the deal.
# doc 08 and doc 19 legitimately quote the phrase inside their retraction notes.
api_hits = occurrences(r"no public API docs found in searches",
                       exclude_docs=("08-OSS-INTEGRATIONS.md", "19-CRITICAL-REVIEW.md"))
check(not api_hits,
      "the inherited 'no public API' negative finding is not restated as fact",
      f"reintroduced at {api_hits} — ChannelDock ships a REST API (from Voorraad, "
      "€45/mo) and 5X has a documented bol.com API link; see doc 08")

# (5) The bundle counts: 77 is title-keyword hits, 25 are actually decomposed.
spine_rows = len(list(csv.DictReader(
    (ROOT / "data/wiseq-bundle-spine.csv").open(encoding="utf-8"))))
check(spine_rows == 25,
      f"bundle spine CSV holds {spine_rows} decomposed bundles",
      f"bundle spine has {spine_rows} rows; docs must not claim 77 are decomposed")

# (6) Internal-only analysis must never be publishable from this client repo.
gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
check("analysis/" in gitignore,
      "internal analysis/ is gitignored",
      "analysis/ is not gitignored — it holds our margins, unbilled labour and "
      "unverified costs, and must never reach the public client repo")


print(f"\n{checks} checks run, {len(failures)} failures")
if failures:
    print("VALIDATION FAILED")
    sys.exit(1)
print("VALIDATION PASSED ✓")
