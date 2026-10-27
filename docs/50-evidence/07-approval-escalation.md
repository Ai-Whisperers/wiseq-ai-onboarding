# Approval and escalation (Hermes Desktop)

*Closes the gap between “agent drafts” and “Rob commits.”*

## Principle

Consequential actions are **proposals** until Rob approves in Hermes Desktop (or an equivalent recorded channel). Milestone 1 uses lab simulation: approval flips a fixture state; nothing external happens.

## Action classes

| Class | Examples | Default |
| :--- | :--- | :--- |
| **Free** | Read fixtures, answer questions, classify mail, compute tariffs | Auto |
| **Draft** | Offer text, invoice draft, CS reply, price recommendation | Auto-create draft; show in Desktop |
| **Approve-to-commit** | “Create invoice”, “book shipment”, “clone shipping rule”, “apply price” | Explicit Rob approval in chat (`APPROVE <id>`) |
| **Forbidden** | Review remove-request automation, CE sticker peel, YOLO host damage, prod writes without Gate | Block + explain |

## Desktop UX (Milestone 1)

1. Skill produces artifact under `lab/eval/out/` with `status: awaiting_approval`.
2. Message to Rob includes: summary, evidence paths, `simulated=true`, risk notes.
3. Rob replies `APPROVE <artifact_id>` or `REJECT <artifact_id> reason`.
4. System records decision in audit log; only then runs commit step on **fixture** adapters.

YOLO mode must remain **off** for profile `wiseq-lab`.

## Escalation triggers

| Trigger | Action |
| :--- | :--- |
| Ambiguous school email (missing school / products) | Escalate; do not invent lines |
| Shipping template `NEEDS_CONFIRMATION` | Refuse clone; ask Rob |
| Stock/price conflict across accounts | Escalate with both values |
| Policy-sensitive review content | Draft CS resolution only; never ask to delete rating |
| Missing CE document | Escalate to Drive search + human |
| Parser confidence below threshold | Human takeover |

## Later channels (not Milestone 1)

Email digest with approve links, Telegram buttons, or remote gateway Webapp — only after Desktop approval path is proven and security reviewed ([capability notes](06-hermes-desktop.md)).
