<div align="center">
<img src="../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track C · Document 10* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# WiseQ OSS Catalog — 31 topics · 100 curated repos

*GitHub Search API, 2026-10-22, ≥5★, non-archived, junk-filtered, deduped across topics (raw: `data/oss/`, 31 files). Assigned to the stack layers of the AI blueprint (doc 04). Adoption rules: same as doc 08 §1 — official API first, OSS second, custom thin build third.*

## ⭐ The adopted additions (beyond doc 08)

| Layer | Repo | ★ | Why |
|---|---|---|---|
| Helpdesk / school-order inbox | [uvdesk/community-skeleton](https://github.com/uvdesk/community-skeleton) | 19.6k | Self-hosted support desk — the school-email inbox becomes a ticket queue the agent works |
| Privacy-safe analytics | [umami-software/umami](https://github.com/umami-software/umami) | 39.5k | Cookieless analytics — GDPR-clean shop metrics without GA cookies |
| PDF invoices/labels | [QuestPDF/QuestPDF](https://github.com/QuestPDF/QuestPDF) | 14.2k | Programmatic PDF (packing slips, invoices, labels) — pairs with the e-boekhouden flow |
| Self-hosted ESP | [Billionmail/BillionMail](https://github.com/Billionmail/BillionMail) | 15.9k | Newsletter + review-ask flows without Klaviyo cost (fixes no-ESP finding) |
| PIM | [unopim/unopim](https://github.com/unopim/unopim) | 11k | If catalog grows past Shopify-native — 230 SKUs today; watch, not adopt |
| SEO | [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) | 6.4k | SEO as MCP skills — agent runs audits natively |
| Bookkeeping reference | [mayswind/ezbookkeeping](https://github.com/mayswind/ezbookkeeping) | 5.8k | Self-hosted bookkeeping patterns; e-Boekhouden API stays primary |
| Translations | [ever-co/ever-traduora](https://github.com/ever-co/ever-traduora) | 2.1k | EN/NL product-content management when Amazon.de/.fr expansion lands |
| Barcode/labels | [lukevp/ESC-POS-.NET](https://github.com/lukevp/ESC-POS-.NET) | 671 | Label printing for EAN-13 barcode labels (pairs with zint) |

## Agentic layer

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) | 2,990 | TypeScript | agentic-commerce | Open Source AI trading agent that operates autonomously across 1000+ markets - P |
| [jettbrains/-L-](https://github.com/jettbrains/-L-) | 166 | - | agentic-commerce, translations | W3C Strategic Highlights  September 2019  This report was prepared for the Septe |
| [agentic-commerce-protocol/agentic-commerce-protocol](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol) | 1,585 | JavaScript | agentic-commerce | The Agentic Commerce Protocol (ACP) is an interaction model and open standard fo |
| [0xNyk/awesome-agent-cortex](https://github.com/0xNyk/awesome-agent-cortex) | 226 | JavaScript | agentic-commerce | Curated map of AI agent frameworks, protocols, runtimes, skills, memory, identit |
| [visa/trusted-agent-protocol](https://github.com/visa/trusted-agent-protocol) | 213 | Python | agentic-commerce | Establishing a universal standard of trust between AI agents and merchants for t |
| [daydreamsai/lucid-agents](https://github.com/daydreamsai/lucid-agents) | 199 | TypeScript | agentic-commerce | Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, |
| [edwinkys/phantasm](https://github.com/edwinkys/phantasm) | 197 | Svelte | workflow | Toolkits to create a human-in-the-loop approval layer to monitor and guide AI ag |

## Catalog data

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [zint/zint](https://github.com/zint/zint) | 821 | C | ean-gs1 | A barcode encoding library supporting over 50 symbologies including Code 128, Da |
| [lukevp/ESC-POS-.NET](https://github.com/lukevp/ESC-POS-.NET) | 671 | C# | barcodes-labels | Efficient, Easy to Use Thermal Printing & POS (Windows/Linux/OSX, WiFi/BT/USB/Et |
| [jshor/symbology](https://github.com/jshor/symbology) | 230 | TypeScript | ean-gs1 | 🔖 Generates 1D, 2D, or composite barcodes in png, svg, or eps formats. Supports  |

## Customer ops

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [uvdesk/community-skeleton](https://github.com/uvdesk/community-skeleton) | 19,640 | CSS | helpdesk | UVdesk Open Source Community Helpdesk is a comprehensive ticketing support syste |
| [neuronetio/gantt-schedule-timeline-calendar](https://github.com/neuronetio/gantt-schedule-timeline-calendar) | 3,636 | TypeScript | calendar-scheduling | Gantt Gantt Gantt Timeline Schedule Calendar [ javascript gantt, js gantt, proje |
| [helpyio/helpy](https://github.com/helpyio/helpy) | 2,469 | Ruby | helpdesk | Helpy is a modern, open source helpdesk customer support application. Features i |
| [Django-CRM/Django-CRM](https://github.com/Django-CRM/Django-CRM) | 2,456 | Python | helpdesk | BottleCRM: free, open-source (MIT) CRM with sales, support tickets and invoicing |
| [ever-co/ever-traduora](https://github.com/ever-co/ever-traduora) | 2,138 | JavaScript | translations | Ever® Traduora™ - Open Translation Management Platform - https://traduora.co |
| [opral/inlang](https://github.com/opral/inlang) | 2,007 | TypeScript | translations | Open format TMS (translation management system) |
| [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) | 1,692 | Python | helpdesk | A Django application to manage tickets for an internal helpdesk. Formerly known  |
| [polonel/trudesk](https://github.com/polonel/trudesk) | 1,499 | JavaScript | helpdesk | :coffee: :seedling: Trudesk is an open-source help desk/ticketing solution. |
| [opensupports/opensupports](https://github.com/opensupports/opensupports) | 1,038 | JavaScript | helpdesk | OpenSupports is a simple and beautiful open source ticket system |
| [znuny/Znuny](https://github.com/znuny/Znuny) | 605 | Perl | helpdesk | Znuny is a free, open-source, and versatile web-based ticketing system for Custo |
| [HashenUdara/edoc-doctor-appointment-system](https://github.com/HashenUdara/edoc-doctor-appointment-system) | 582 | PHP | calendar-scheduling | This PHP-based open source project is a web application for booking medical appo |
| [Bytedesk/bytedesk](https://github.com/Bytedesk/bytedesk) | 511 | JavaScript | helpdesk | Open Souce IM with AI powered live-chat, email, ticket support, omni-channel cus |
| [coderflexx/laravel-ticket](https://github.com/coderflexx/laravel-ticket) | 445 | PHP | helpdesk | A full-featured support ticket system for Laravel with Eloquent models and a cle |
| [nateherkai/snagtime](https://github.com/nateherkai/snagtime) | 392 | TypeScript | calendar-scheduling | Free, self-hostable scheduling app with booking links, Google Calendar sync, SMT |
| [shashirajraja/Train-Ticket-Reservation-System](https://github.com/shashirajraja/Train-Ticket-Reservation-System) | 317 | Java | calendar-scheduling | This is the website build for searching the Train Schedule , Seat Availability,  |
| [go2ismail/DotnetDesk](https://github.com/go2ismail/DotnetDesk) | 213 | C# | helpdesk | Asp.Net Example web application showing the capabilities of ASP.NET Core 2 MVC,  |
| [txty-io/texterify](https://github.com/txty-io/texterify) | 203 | TypeScript | translations | The translation and localization management system. |
| [OpenLucasKaka/i18n-workflow-helper](https://github.com/OpenLucasKaka/i18n-workflow-helper) | 194 | TypeScript | translations | A VS Code i18n workflow plugin for React, Vue, JavaScript, and TypeScript projec |

## Intelligence

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [2scraper/amazon-scraper](https://github.com/2scraper/amazon-scraper) | 11 | Python | marketplace-api, scraper-commerce | Amazon scraper: search results, best sellers, product pages and reviews across 2 |

## Marketing & trust

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [umami-software/umami](https://github.com/umami-software/umami) | 39,515 | TypeScript | analytics-privacy | Umami is a privacy-first analytics platform. Traffic, campaigns, behavior, conve |
| [plausible/analytics](https://github.com/plausible/analytics) | 29,593 | Elixir | analytics-privacy | Open source, privacy-first web analytics. Lightweight, cookie-free Google Analyt |
| [Billionmail/BillionMail](https://github.com/Billionmail/BillionMail) | 15,941 | Go | email-automation | BillionMail gives you open-source MailServer, NewsLetter,  Email Marketing — ful |
| [Openpanel-dev/openpanel](https://github.com/Openpanel-dev/openpanel) | 7,180 | TypeScript | analytics-privacy | OpenPanel is an open-source web and product analytics platform, an open-source a |
| [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) | 6,378 | Shell | seo-audit | Free SEO MCP server + open-source SEO and GEO skills for Claude: keyword researc |
| [electerious/Ackee](https://github.com/electerious/Ackee) | 4,718 | JavaScript | analytics-privacy | Self-hosted, Node.js based analytics tool for those who care about privacy. |
| [milesmcc/shynet](https://github.com/milesmcc/shynet) | 3,156 | Python | analytics-privacy | Modern, privacy-friendly, and detailed web analytics that works without cookies  |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | 2,780 | Python | seo-audit | AI Marketing Suite for Claude Code. 15 marketing skills with parallel subagents  |
| [Notifuse/notifuse](https://github.com/Notifuse/notifuse) | 2,255 | Go | email-automation | Open-source, self-hosted newsletter, email marketing and transactional email pla |
| [mettle/sendportal](https://github.com/mettle/sendportal) | 2,179 | PHP | email-automation | Open-source self-hosted email marketing. Manage your own newsletters at a fracti |
| [obsei/obsei](https://github.com/obsei/obsei) | 1,440 | Python | analytics-privacy | Open source, privacy-first Voice of Customer analytics. A self-hosted alternativ |
| [JustinBeckwith/linkinator](https://github.com/JustinBeckwith/linkinator) | 1,276 | TypeScript | seo-audit | Broken link checker that crawls websites and validates links. Find broken links, |
| [Swetrix/swetrix](https://github.com/Swetrix/swetrix) | 1,212 | TypeScript | analytics-privacy | 📈 Open source, privacy-first web analytics — a cookie-less Google Analytics alte |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | 1,145 | Python | seo-audit | Open-source Answer Engine Optimization (AEO) & Generative Engine Optimization (G |
| [rampstackco/claude-skills](https://github.com/rampstackco/claude-skills) | 985 | JavaScript | seo-audit | Stack-agnostic Claude Skills covering the full website lifecycle: brand, design, |
| [offen/offen](https://github.com/offen/offen) | 982 | JavaScript | analytics-privacy | Offen Fair Web Analytics |
| [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | 970 | Rust | seo-audit | SiteOne Crawler is a cross-platform website crawler and analyzer for SEO, securi |
| [leopard627/fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) | 874 | Python | seo-audit | Fire your SEO·GEO agency 🔥 A Claude Code skill that audits and optimizes SEO·AEO |
| [StJudeWasHere/seonaut](https://github.com/StJudeWasHere/seonaut) | 823 | Go | seo-audit | Open source SEO audit tool. |
| [StanGirard/seo-audits-toolkit](https://github.com/StanGirard/seo-audits-toolkit) | 822 | Python | seo-audit | SEO & Security Audit for Websites. Lighthouse & Security Headers crawler, Sitema |
| [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) | 769 | Python | seo-audit | SEO agent skill for OpenClaw,Claude Code, and AI agents. Generate beginner SEO a |
| [AgriciDaniel/jev-seo](https://github.com/AgriciDaniel/jev-seo) | 696 | Python | seo-audit | Live SEO audit for any website from one homepage URL, judged by Jev. PDF, XLSX a |
| [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) | 641 | TypeScript | seo-audit | A comprehensive SEO audit command-line tool with 332 audit rules across 20 categ |
| [OpenLabs-so/openanalytics](https://github.com/OpenLabs-so/openanalytics) | 636 | TypeScript | analytics-privacy | Open-source, privacy-first and cookieless web analytics with revenue attribution |
| [unifapi-agent/agents](https://github.com/unifapi-agent/agents) | 597 | JavaScript | seo-audit | Open-source marketing agents for Claude, ChatGPT, Codex, OpenClaw & Hermes. One  |
| [umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) | 564 | JavaScript | seo-audit | 🔍 Google SEO's full docs as an AI prompt machine — drop it into your AI assistan |
| [Yuzzyuk/marketing-os](https://github.com/Yuzzyuk/marketing-os) | 560 | - | seo-audit | An entire marketing department as one Claude skill. 14 modules: audits scored 0- |
| [foo-software/lighthouse-check-action](https://github.com/foo-software/lighthouse-check-action) | 513 | TypeScript | seo-audit | GitHub Action for running @GoogleChromeLabs Lighthouse audits with all the bells |
| [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube) | 506 | Python | seo-audit | Claude Code skill for YouTube creators — channel audits, video SEO, retention sc |
| [elmohq/elmo](https://github.com/elmohq/elmo) | 479 | TypeScript | seo-audit | Open-source Answer Engine Optimization (AEO) and Generative Engine Optimization  |
| [joeseesun/qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) | 458 | Python | seo-audit | Audit, diagnose, research, plan, implement, experiment on, and verify website SE |
| [inhouseseo/superseo-skills](https://github.com/inhouseseo/superseo-skills) | 363 | - | seo-audit | 11 Claude skills for SEO: page audits, linkbuilding, article writing, E-E-A-T au |
| [sheshbabu/freshlytics](https://github.com/sheshbabu/freshlytics) | 362 | TypeScript | analytics-privacy | Open source privacy-friendly analytics |
| [kennyzir/7deer_skills](https://github.com/kennyzir/7deer_skills) | 328 | Python | seo-audit | Composable, auditable Agent Skills for building Roblox game sites—from opportuni |
| [viasite/site-audit-seo](https://github.com/viasite/site-audit-seo) | 304 | JavaScript | seo-audit | Web service and CLI tool for SEO site audit: crawl site, lighthouse all pages, v |
| [squirrelscan/squirrelscan](https://github.com/squirrelscan/squirrelscan) | 289 | TypeScript | seo-audit | The website QA tool for your coding agent. 300+ audit rules across SEO, performa |
| [abhinaba-ghosh/playwright-lighthouse](https://github.com/abhinaba-ghosh/playwright-lighthouse) | 284 | JavaScript | seo-audit | :performing_arts:: Playwright Lighthouse Audit |
| [th0th/poeticmetric](https://github.com/th0th/poeticmetric) | 268 | TypeScript | analytics-privacy | PoeticMetric is a free as in freedom, open source, privacy-first, regulation-com |
| [OmniRise/LinkBreeze](https://github.com/OmniRise/LinkBreeze) | 256 | TypeScript | analytics-privacy | The self-hosted Linktree alternative. Import from any competitor in 30 seconds.  |
| [SNLabat/SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) | 256 | - | seo-audit | SEO/GEO/AEO Audit Skill for Claude |
| [patrickgwsmith/Lantern](https://github.com/patrickgwsmith/Lantern) | 250 | Swift | seo-audit | Mac app for website auditing and crawling |
| [Asqatasun/Asqatasun](https://github.com/Asqatasun/Asqatasun) | 241 | Java | seo-audit | Mirror of Asqatasun ---> we've moved to GITLAB https://gitlab.com/asqatasun/Asqa |
| [zupcode-com/awesome-free-services-for-your-next-startup-or-saas](https://github.com/zupcode-com/awesome-free-services-for-your-next-startup-or-saas) | 228 | - | seo-audit | Build your next startup for FREE with services ranging from website design, app  |
| [shafy/fugu](https://github.com/shafy/fugu) | 214 | Ruby | analytics-privacy | Free, privacy-friendly, simple, open-source and self-hostable product analytics. |
| [seranking/seo-skills](https://github.com/seranking/seo-skills) | 181 | Python | seo-audit | Claude SEO Skills — production Claude Agent Skills for the SE Ranking MCP server |

## Marketplace

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [NhaPhatHanh/github](https://github.com/NhaPhatHanh/github) | 65 | - | google-shopping-feed, marketplace-sync | <!DOCTYPE html> <html lang="en" data-color-mode="auto" data-light-theme="light"  |
| [jennywelson123/8-Best-Online-Payment-Solutions-For-Your-E-Commerce-Website](https://github.com/jennywelson123/8-Best-Online-Payment-Solutions-For-Your-E-Commerce-Website) | 11 | - | marketplace-api, marketplace-sync | E-commerce company owners of today have the challenge of picking the best online |
| [BartWaardenburg/bol-mcp](https://github.com/BartWaardenburg/bol-mcp) | 5 | TypeScript | bol-com, marketplace-api | MCP server for bol.com Retailer API automation: orders, offers, shipments, retur |
| [apiguru-app/amazon-scraper-v2](https://github.com/apiguru-app/amazon-scraper-v2) | 221 | Python | marketplace-api | Agent-ready Amazon Scraper API: real-time product details (batch ASIN), offers & |

## Orders & finance

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [QuestPDF/QuestPDF](https://github.com/QuestPDF/QuestPDF) | 14,209 | C# | pdf-generation | QuestPDF is a modern library for PDF document generation. Its fluent C# API lets |
| [mayswind/ezbookkeeping](https://github.com/mayswind/ezbookkeeping) | 5,796 | Go | accounting | ezBookkeeping is an open source, powerful, self-hosted personal finance app that |
| [TNT-Likely/BeeCount](https://github.com/TNT-Likely/BeeCount) | 2,609 | Dart | accounting | Local-first bookkeeping for iOS/Android/Web · Self-hosted cloud + iCloud/WebDAV/ |
| [VonHoltenCodes/SlowBooks-Pro-2026](https://github.com/VonHoltenCodes/SlowBooks-Pro-2026) | 804 | Python | accounting | Free, source-available accounting: double-entry bookkeeping, invoicing, US payro |
| [erp-mafia/accounted](https://github.com/erp-mafia/accounted) | 426 | TypeScript | accounting | The Open Source ERP Built for Agents |
| [ComPDFKit/compdf-generation](https://github.com/ComPDFKit/compdf-generation) | 362 | TypeScript | pdf-generation | Generate PDFs effortlessly with the open-source ComPDF Generation SDK. Design HT |
| [stemword/php-inventory-management-system](https://github.com/stemword/php-inventory-management-system) | 292 | PHP | pdf-generation | Open source inventory management system with php and mysql Invoice generation an |
| [kaloraat/react-node-ecommerce](https://github.com/kaloraat/react-node-ecommerce) | 285 | JavaScript | order-to-cash | React Node Ecommerce with Paypal and Credit Card payments with Admin Order Manag |
| [kirilkirkov/Electronic-Invoicing-And-Warehouse-Management-System](https://github.com/kirilkirkov/Electronic-Invoicing-And-Warehouse-Management-System) | 207 | PHP | pdf-generation | A self-hosted open-source application built with CodeIgniter and Bootstrap. Feat |
| [TNT-Likely/BeeCount-Cloud](https://github.com/TNT-Likely/BeeCount-Cloud) | 180 | TypeScript | accounting | Self-hosted cloud for BeeCount — one Docker image runs the sync server + web app |

## Store & catalog

| Repo | ★ | Lang | Topics | Description |
|---|---|---|---|---|
| [unopim/unopim](https://github.com/unopim/unopim) | 11,042 | PHP | pim-open | Open source Product Information Management (PIM) and Digital Asset Management (D |
| [AhmadHassan-BTed/ShopifyAutoAuth](https://github.com/AhmadHassan-BTed/ShopifyAutoAuth) | 2,133 | Python | shopify-tooling | Enterprise-grade Shopify Admin API authentication adapter — OAuth 2.0 Client Cre |
| [magefan/magento-google-shopping-feed](https://github.com/magefan/magento-google-shopping-feed) | 10 | - | google-shopping-feed, product-feed | Magento Google Shopping Feed is an extension that allows you to auto-generate pr |
| [wearepixel/laravel-google-shopping-feed](https://github.com/wearepixel/laravel-google-shopping-feed) | 6 | PHP | google-shopping-feed, product-feed | An XML Product feed implementation for Google Merchant Shopping |
| [akeneo/pim-community-dev](https://github.com/akeneo/pim-community-dev) | 1,046 | PHP | pim-open | [Community Development Repository] The open source Product Information Managemen |
| [uicrooks/shopify-theme-lab](https://github.com/uicrooks/shopify-theme-lab) | 821 | JavaScript | shopify-cli | Shopify theme development environment using Liquid, Vue and Tailwind CSS. Built  |
| [Shopify/cli](https://github.com/Shopify/cli) | 762 | TypeScript | shopify-cli | Build apps, themes, and hydrogen storefronts for Shopify |
| [Shopify/shopify_django_app](https://github.com/Shopify/shopify_django_app) | 504 | Python | shopify-tooling | Get a Shopify app up and running with Django and Python Shopify API |
| [akeneo/pim-community-standard](https://github.com/akeneo/pim-community-standard) | 436 | - | pim-open | [Community Standard Edition] The open source Product Information Management (PIM |
| [atrocore/atrocore](https://github.com/atrocore/atrocore) | 240 | JavaScript | pim-open | AtroCore is an enterprise-ready, highly configurable Business Application Platfo |
| [atrocore/atropim](https://github.com/atrocore/atropim) | 210 | PHP | pim-open | AtroPIM is a flexible, highly configurable, modular, open-source product informa |
| [jasewarner/gulp-shopify](https://github.com/jasewarner/gulp-shopify) | 184 | Liquid | shopify-cli | Blank slate Shopify theme for Developers, packaged with Gulp.js for processing S |

*Total shown: 100 curated repos of 416 candidates across 31 topics.*

---

## 📌 In short

**~416–420 repositories found; ~100 listed in this menu** across 31 topics and 9 stack layers — assigned to the layer of the blueprint in [doc 04](../a-proposal/04-AI-STACK-BLUEPRINT.md) that would adopt them. **Six topic JSON files are still stubs** (content-generation, review-automation, product-matching, inventory-sync, invoice-parse, edtech) — see [`data/README.md`](../../data/README.md). Four entries are already named for Phase 1 (UVdesk, Umami, BillionMail, QuestPDF). Adoption rule: **official API first, proven OSS second, custom thin build only as a last resort** — a menu, not a shopping list.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Oss Integrations](08-OSS-INTEGRATIONS.md)** | Why orchestration is the moat |
| **[Hermes Jev Aiw Reuse](../d-delivery/14-HERMES-JEV-AIW-REUSE.md)** | What we already run in-house |
| **[Devops Masterplan](../d-delivery/15-DEVOPS-MASTERPLAN.md)** | Which catalog entries enter the stack |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
