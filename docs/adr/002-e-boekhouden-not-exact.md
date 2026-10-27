# ADR 002 — e-Boekhouden (not Exact Online)

*Status: Accepted · 2026-10-27*

## Context

Early proposal text assumed Exact Online. Client operating manual (Oct 27) names **e-Boekhouden** for school offers → invoices → relations.

## Decision

1. Bookkeeping connector target is **e-Boekhouden REST** (read first).  
2. Exact Online MCP / Exact-shaped tools are **out of scope** for WiseQ.  
3. Browser-automation MCP is fallback only if API entitlements fail Gate 1.2.

## Consequences

- Docs, stack-map, and lab accounting fixtures use e-Boekhouden vocabulary.  
- Do not install `exact-mcp` for this client.
