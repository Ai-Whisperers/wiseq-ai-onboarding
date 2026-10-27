# Software keep / extend / replace decisions

*Scorecard outcomes after Milestone 1 lab evidence. Critical correctness failures veto high aggregate scores.*

| System / capability | Outcome | Why | Evidence |
| :--- | :--- | :--- | :--- |
| ChannelDock (inventory/bundles/rules) | **Keep** + **Extend** monitors | Native bundles already exist; replacement unjustified | Manual; Exp B |
| Mastersheet as calc engine | **Improve** | Narrative-in-numbers; conflicts | Exp C; doc 26 |
| e-Boekhouden | **Keep** + **Extend** draft automation | Confirmed SoT; API still untested | Manual; Exp A sim |
| Exact Online | **Reject** (for WiseQ) | Wrong package | Claim 39/48 |
| FiveX | **Keep** exports; **Investigate** price rule | Incumbent workflow; +10% unvalidated for automation | Fixtures/pricing |
| bol ×3 accounts | **Keep** + multi-account wrappers | Distinct identities | Manual |
| Hermes Desktop | **Extend** as Rob UI | Chosen Milestone 1 interface | Capability notes |
| QuestPDF | **Investigate further** | PDF rendering complement — not run in M1 | OSS map |
| UVdesk / BillionMail / Umami / n8n | **Investigate further** | Bounded OSS candidates; no M1 bake-off yet | Opportunity map |
| Replace ChannelDock wholesale | **Reject** | No measured gap | Exp B |
| Auto review-deletion agent | **Reject** | Policy / AVG | Doc 29 |

## Margin rule

Migration requires beating incumbent on correctness **and** a predefined operational margin — not feature count or OSS preference.
