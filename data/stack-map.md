# Stack map — WiseQ (Phase 0 draft)

*Seeded 2026-10-27 from client operating manual ([extract](client/OPERATING-MANUAL-EXTRACT.md)). Status: **draft**.*

**Read this carefully:** “Confirmed in manual” = client workflow intent. It is **not** account entitlement, API permission, or production-write approval. Vendor marketing (“REST from Voorraad+”) is also not WiseQ’s plan until Rob confirms. Exit criteria = filled **capability matrix** below, not a longer connector wish-list. See [doc 29](../docs/60-governance/03-critical-audit-2026-10-27.md).

| Tool | Confirmed in manual | Vendor-feature knowledge | WiseQ account / tech status | Creds needed | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ChannelDock** | Inventory, bundles, shipping rules, returns, inbound | REST + webhooks marketed from Voorraad+ | Plan + token + permissions **untested** | Plan confirm + API token | Bundle UI ≠ API proof |
| **FiveX** | Reports, LVB, price brake, reviews | Unknown public write API | Export path described; automation semantics **untested** | Export access / login | No auto price writes |
| **e-Boekhouden** | Offers, invoices, relations | Research official API / partners | Endpoints + sandbox **untested** | Read-only user | **Not Exact** |
| **bol.com Seller** ×3 | WiseQ NL, Electronics, België (holding exit) | Retailer API | Per-account scopes **untested** | Per-account tokens / sandbox | België = migration |
| **QLS** | Carrier + tickets | Portal / email | Interface **untested** | Ticket mailbox | Strike escalation |
| **MyParcel** | B2B DHL labels | API if available | Label/cancel/billing **untested** | Account | School pipeline |
| **PostNL** | Brievenbus / partijenpost | Existing wrapper eval | — | — | Invoice dispute = human |
| **Dymo / labels** | EAN stickers | Local print | Out of agent scope | — | Warehouse laptop |
| **Excel Mastersheet** | Tariffs, CD templates, SEO, packaging | — | Safe tabs exported; private tabs stay private | Controlled share | [`client/MASTERSHEET-EXTRACT.md`](client/MASTERSHEET-EXTRACT.md) |
| **Google Drive** | CE / DoC library | Drive read MCP | — | Folder share | Don’t regenerate certs |
| **Shopify** | Own shop (manual light) | Admin API | Phase-0 priority **TBD** | Collaborator | Confirm vs bol |
| **Mailbox** | CS + sales | IMAP read-only first | Provider **unnamed** | App password | Approved-send policy required |

## Capability matrix (fill in Phase 0)

For each integration, record before any production write:

| Integration | Vendor docs URL | Account entitlement | Required permission | Operation tested (R/W) | Error / idempotency notes | Prod writes allowed? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ChannelDock | | | | | | No |
| FiveX | | | | | | No |
| e-Boekhouden | | | | | | No |
| bol NL | | | | | | No |
| bol Electronics | | | | | | No |
| bol België | | | | | | No |
| MyParcel / DHL | | | | | | No |
| QLS | | | | | | No |
| Mailbox | | | | | | No |
| Shopify | | | | | | No |

## Phase-0 deliverable checklist

- [x] Company manual received  
- [ ] Software inventory confirmed with Rob (this table as agenda)  
- [ ] Capability matrix rows filled with evidence  
- [ ] Sandbox / dummy school orders  
- [ ] Read-only tokens  
- [ ] Purchase-manager walkthrough  
- [ ] Annual turnover band  
- [ ] ChannelDock plan + PIM answer  
- [ ] Raw-manual publication approval ([`client/README.md`](client/README.md))  
