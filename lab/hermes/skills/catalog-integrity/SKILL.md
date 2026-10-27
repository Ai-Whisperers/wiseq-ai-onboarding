---
name: catalog-integrity
description: Bundle spine and shipping-template validation in the lab.
---

# catalog-integrity

1. Use `scenarios.b_catalog.run_catalog_integrity`.
2. Report unresolved bundles (expect none) and missing EAN count.
3. Attempt template clone for OK vs NEEDS_CONFIRMATION classes.
4. Refuse automation for non-OK templates.
