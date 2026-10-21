# Meeting Notes — 2026-10-21 (Working Session with WiseQ)

*From two recorded sessions (transcripts in our private workspace). These notes capture business-relevant intel only.*

## Who we met

WiseQ leadership at their Grootebroek base (the "marketing team left for the dentist" — i.e., small team, founder-led). Presentations included live demos of: the AI Whisperers Hermes agent stack, kanban fleet orchestration, GitHub PR history (350+ PRs, AI branches), token dashboards, and the sister-project backend (bakery/coffee-shop RMS with price tracking, forecasts, WhatsApp ordering, XML invoice parsing).

## What WiseQ told us (business intel)

### Operations
- **Tooling confirmed**: **ChannelDock** (inventory/stock across channels) + **5X** (profitability, segments, advertising, returns-reduction on bol.com). Plus bookkeeping software (offers → invoices → relations), a 24/7 office computer already running.
- **School orders eat 4-hour mornings**: request → offer in bookkeeping (often new relation setup) → confirm → invoice → **manually key everything into ChannelDock** so the warehouse understands. Sometimes 4 hours in a single morning, plus ~4h/week booking time historically.
- **The bundle-recombination workaround** (their words): a USB-Lightning cable sells inside 4 different adapter combinations; when 400 charger+cable combos sell out, they "grab the regular charger and the regular cable" — but **ChannelDock doesn't understand this**, so purchase data gets polluted ("data gets polly"), and re-purchasing runs on "a long human trail of what are we really selling."
- **EAN is the agreed key**: everything is based on EAN/GS1 codes; if actual-product sales drive purchasing, correct amounts follow.
- **Purchase manager pain**: sales data → Excel → 6-month average per EAN, all by hand; error-prone (one costly error/year, despite excellent staff).
- **They have a ~30-page company manual** (software, processes, how-things-work) — agreed to share for MCP/tooling research.
- Team: small but real (marketing function exists; purchase manager; founder-led).

### Positioning & market
- **Two main direct competitors** in kids-headphones-for-schools, both with severely dated websites ("90s", "2000s"); plus generalists. WiseQ sees itself far ahead on web/marketing.
- Interest in **new segments**: parental screen-time controls (as an extra service on kids tablets — the Chinese manufacturer would want it preinstalled), and **elderly hearing** (Bluetooth hearing-assist earbuds; big-corporation competition acknowledged).
- Receptive to: automated school-event-based promos, personalized email campaigns (school anniversaries, competition wins), competitor/price monitoring across Chinese suppliers, AI product images in a consistent house style.
- Already AI-curious: noticed their own blog getting 32 comments; familiar with Gemini/transcription workflows; the founder's environment includes a $20/mo Canada server etc.

### Agreements / next steps from the session
1. WiseQ shares: **company manual (30p), software inventory, access to a sandbox/dummy dataset** for a shadow demo.
2. We build: **a sample automation (school-order pipeline) running on similar test data** — visual, low-risk, "just for you to look at."
3. Research and document: which MCPs, APIs, tooling exist for their exact stack (ChannelDock, 5X, bookkeeping, bol.com, Shopify).

## What we showed them (already done on our side)

- Hermes agent doing live research on WiseQ during the meeting (company/marketplace/marketing lanes)
- Kanban-driven multi-machine agent fleet, session dashboards, token economics (26,000B tokens/mo on one provider)
- Sister-project bakery backend: AI product images from vague recipes, price tracking + forecasts across supermarkets, WhatsApp ordering loop, QR→XML invoice parsing into inventory

## Interpretation (our read, clearly labeled)

WiseQ is an ideal Phase-0 client: process pain is concrete and measurable (4h mornings, manual EAN Excel, bundle re-keying), infrastructure is modern (Shopify+UCP, ChannelDock, 5X, 24/7 machine), the founder personally gets AI (asked the right questions about MCPs, tokens, server costs), and there's an explicit ask ("if you have an AI do stuff in my mailbox, that would be great — save a lot of time").
