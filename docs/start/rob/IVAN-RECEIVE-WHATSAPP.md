<div align="center">
<img src="../../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*AIW only · Ivan* · [← Pack](README.md)</sub>

---

# Ivan — receive Rob’s WhatsApp credentials

Rob will send Wave 1 read-only keys **via WhatsApp to Ivan**. This page is the receive checklist so nothing is lost, leaked, or left only in chat history.

## Before he sends

| ☐ | Prep |
| :--- | :--- |
| ☐ | Send him [send-message-keys](send-message-keys.md) + link to [whatsapp-cred-template](whatsapp-cred-template.md) |
| ☐ | Confirm he uses labels `AIW-readonly-…` so he can revoke |
| ☐ | Bitwarden (or 1Password) vault collection ready: `WiseQ / Phase-0 read-only` |
| ☐ | Private note template ready (fields below) — **never** in this public repo |

## When WhatsApp arrives

| ☐ | Action | Detail |
| :--- | :--- | :--- |
| ☐ | **Acknowledge** in WhatsApp: “Received — vaulting now, won’t put in GitHub” |
| ☐ | **Copy into vault immediately** (within minutes) — one item per system |
| ☐ | Tag each vault item: system · account (NL/Electronics/BE) · `AIW-readonly-2026-10` · received date |
| ☐ | Fill private intake note (local/vault only) using fields below |
| ☐ | **Do not** forward the chat to Slack/email/GitHub/Cursor chat with secrets pasted |
| ☐ | **Do not** commit `.env` or dump files to `wiseq-ai-onboarding` |
| ☐ | After vault OK: reply “Vaulted. I’ll smoke-test ChannelDock first and ping you.” |
| ☐ | Optionally ask Rob to **delete** the WhatsApp messages once vaulted |

## Vault item naming (suggested)

```text
WiseQ · ChannelDock · AIW-readonly-2026-10
WiseQ · bol NL · AIW-readonly-2026-10
WiseQ · bol Electronics · AIW-readonly-2026-10
WiseQ · bol België · AIW-readonly-2026-10   (if live)
WiseQ · e-Boekhouden REST · AIW-readonly-2026-10
WiseQ · Mailbox read · <provider> · AIW-readonly-2026-10
```

## Private intake fields (vault secure note — not git)

```text
Received_at:
Via: WhatsApp → Ivan
ChannelDock_plan:
ChannelDock_PIM:
bol_accounts_received: NL / Electronics / BE
Mailbox_provider:
Mailbox_method:
Handleiding_public_OK: yes/no/unknown
Missing:
Smoke_ChannelDock: pending/pass/fail
Smoke_bol: pending/pass/fail
Smoke_eboekhouden: pending/pass/fail
Smoke_mailbox: pending/pass/fail
```

## After vault

1. Read-smoke in order: ChannelDock → bol (per account) → e-Boekhouden → mailbox.  
2. Update [`data/stack-map.md`](../../../data/stack-map.md) capability cells (**R** only) — no secrets in the cells.  
3. Tell Rob what worked / what’s missing (use [open-asks](open-asks.md)).  
4. Schedule Desktop demo if not done ([DEMO-SCRIPT](../../../lab/hermes/DEMO-SCRIPT.md)).

## If a secret was pasted into the wrong place

| Place | Do |
| :--- | :--- |
| This git repo / PR / issue | Rotate key with Rob **immediately**; purge history if committed |
| Cursor / agent chat | Rotate if the transcript may sync to cloud logs; vault the replacement |
| Group WhatsApp | Ask Rob to rotate; treat as exposed |

## Related

- Rob how-to: [read-only-access](read-only-access.md)  
- Rob WhatsApp fill-in: [whatsapp-cred-template](whatsapp-cred-template.md)  
- Rob outreach: [send-message-keys](send-message-keys.md)
