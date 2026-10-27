# ADR 001 — Hermes Desktop first

*Status: Accepted · 2026-10-27*

## Context

WiseQ already leaves an office PC on 24/7. Milestone 1 needs an approval-gated ops seat without premature VPS complexity. Cron/always-on jobs need a companion later.

## Decision

1. **Primary runtime:** Hermes Desktop (`wiseq-lab` profile) on Rob’s machine.  
2. **Always-on companion VPS** (hosting options a–d) is **deferred** until Desktop digests earn daily trust.  
3. YOLO / unsupervised writes stay **off**.

## Consequences

- Docs and demos lead with Desktop; TCO still lists companion options.  
- Lab skills and digests must work offline/synthetic first.  
- Cron health / Langfuse wait for companion profile.
