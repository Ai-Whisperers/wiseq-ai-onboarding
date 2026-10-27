---
name: school-pipeline
description: Simulated school order path — mailbox to offer/invoice/shipment drafts.
---

# school-pipeline

Run the synthetic school-order workflow.

## Steps

1. Read `fixtures/mailbox/school_inbox.json` or call `scenarios.a_school.run_school_order`.
2. Catalog/sample requests → escalate (do not invent products).
3. Draft offer → draft invoice → shipment prep; mark `simulated=true`.
4. Without approval, stop at `awaiting_approval`.
5. On `APPROVE`, show committed simulated invoice/shipment ids.
6. Prove idempotency via `run_duplicate_submit`.

## Forbidden

Real e-Boekhouden or MyParcel calls. Duplicate invoices on retry.
