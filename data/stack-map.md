# Stack map — WiseQ (Phase 0 draft)

*Seeded 2026-10-27 from client operating manual ([extract](client/OPERATING-MANUAL-EXTRACT.md)). Status: **draft** — API availability still to be verified with live tokens.*

| Tool | Confirmed in manual | Connector approach | Creds / access needed | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **ChannelDock** | Yes — SoR inventory, bundles, shipping rules, returns, inbound | REST API (from Voorraad+) | Plan confirm + API token | Bundle UI = native; ask PIM separately |
| **FiveX** | Yes — reports, LVB, price brake, reviews | CSV export first; API TBD | Export access / login | Auto +10% price at ≤10 stock |
| **e-Boekhouden** | Yes — offers, invoices, relations | Research official API / partners | Read-only user | **Not Exact** — correct earlier assumption |
| **bol.com Seller** ×3 | WiseQ NL, Electronics, België (holding exit) | Retailer API wrapper (build) | Per-account tokens / sandbox | Multi-account from day one |
| **QLS** | Carrier + tickets | Email/ticket MCP or portal | Ticket mailbox | Strike escalation path |
| **MyParcel** | B2B DHL labels | API if available | Account | School pipeline |
| **PostNL** | Brievenbus / partijenpost | Existing wrapper eval | — | Invoice dispute is human phone call |
| **Dymo / labels** | EAN stickers | Local print — out of agent scope | — | Warehouse laptop |
| **Excel Mastersheet** | Shipping tariffs, ChannelDock rule templates, SEO keywords, packaging SKUs, price brakes, … | Read export of safe tabs (done) | Controlled share of private tabs | Public extract: [`client/MASTERSHEET-EXTRACT.md`](client/MASTERSHEET-EXTRACT.md) · CSVs in [`client/mastersheet/`](client/mastersheet/) |
| **Google Drive** | CE / DoC library | Drive read MCP | Folder share | Don't regenerate certs |
| **Shopify** | Own shop (manual light) | Admin API | Collaborator | Confirm Phase-0 priority vs bol |
| **Mailbox** | CS + sales | IMAP read-only first | App password | Provider still unnamed |

## Phase-0 deliverable checklist

- [x] Company manual received  
- [ ] Software inventory confirmed with Rob (this table as agenda)  
- [ ] Sandbox / dummy school orders  
- [ ] Read-only tokens  
- [ ] Purchase-manager walkthrough  
- [ ] Annual turnover band  
- [ ] ChannelDock plan + PIM answer  
