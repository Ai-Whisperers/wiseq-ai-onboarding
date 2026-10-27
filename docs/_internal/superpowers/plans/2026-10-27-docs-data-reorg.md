# Plan: docs + data full package

> **For agentic workers:** complete tasks in order; run validator at the end.

**Spec:** `docs/superpowers/specs/2026-10-27-docs-data-reorg-design.md`

## Task 1: Folder moves

Create Approach A directories; `git mv` numbered docs into them.

## Task 2: Claim sync

Replace stale GS1 €854 and Trustpilot 25/4.4 in client docs + README; annotate doc 22 as superseded on GS1.

## Task 3: New artifacts

Write `data/README.md`, role pack READMEs, `25-CATALOG-SCORECARD`, `26-UNIT-ECONOMICS`, `27-EVIDENCE-INDEX`, `docs/README.md`.

## Task 4: Link + validator rewrite

Update relative links (`../../assets`, cross-folder doc links), root README paths, `site/index.html`, `index.html`, `scripts/validate_repo.py` (rglob docs, new paths).

## Task 5: Verify

`python scripts/validate_repo.py` → PASS.
