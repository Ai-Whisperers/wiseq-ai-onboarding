# Next Steps

## What we need from WiseQ (the ask-list from our session)

1. **The ~30-page company manual** (software, processes, how things work) — so we can map MCPs, APIs and tooling precisely
2. **Software inventory**: which bookkeeping package (Exact? nl.? other?), ChannelDock plan/API access, 5X export access, mailbox provider
3. **Sandbox/dummy data**: a copy of a few anonymized school orders + the offer→invoice flow, so the shadow demo mirrors reality
4. **API keys / read-only access** (when ready): Shopify (read-only collaborator), ChannelDock (API token), bol Seller (sandbox), mailbox (app-password, read-only first)
5. **30 minutes with the purchase manager** — the EAN/Excel workflow walkthrough, to design the replacement correctly

## What we commit to (Phase 0, ~2 weeks)

- [ ] `data/stack-map.md` — every tool mapped to connector availability (from the manual)
- [ ] EAN registry v1 (seeded from ChannelDock + Shopify exports — no live access needed to start)
- [ ] Shadow school-order demo on dummy data (the "visually, ah, nice" moment promised in the meeting)
- [ ] Read-only dashboard prototype (orders, stock, reviews, channel drift)

## Decision points for Rob

| Question | Options |
|---|---|
| Where does the agent run? | (a) existing 24/7 office machine (b) €20/mo VPS (c) both (VPS primary, office as worker) |
| Bookkeeping connection style? | (a) native API if Exact/nl. supports it (b) browser-automation MCP (works with anything) |
| Review platform priority? | Trustpilot (international) vs Kiyoh (NL standard) vs both |
| First revenue engine? | review invitations (fastest) vs B2B outreach (biggest data advantage) |

## Contact

- This repo: open an issue or comment on any doc — we monitor it
- AI Whisperers operates through Ivan (AI/systems) — direct channel details on request
