<div align="center">
<img src="../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*Track D · Document 17* · [← Back to the proposal](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)</sub>

---

# Site Concept Showcase — three directions, built not described

*Three scroll-driven design concepts for WiseQ, built during the engagement as working prototypes — not mood boards. Each is a runnable page using WiseQ's real 230-product catalog imagery. Open them in a browser to see the scroll behaviour.*

> **Why these exist.** The proposal in [04 · AI Stack Blueprint](04-AI-STACK-BLUEPRINT.md) is about *operations*. This doc is the visible proof that we ship working software, not slideware. The same team that decoded the bundle spine also wrote the scroll engine.

---

## 🎞️ Concept 01 — Cinematic

**"Geluid is geen speelgoed."** — *Sound is not a toy.*

A full-bleed cinematic hero: a 3D-lit headphone renders over a near-black field with the WISEQ wordmark, an orange accent, and a live volume-limit readout pinned to the bottom. Scroll-driven product choreography follows.

| | |
| :--- | :--- |
| **Direction** | Cinematic · immersive · premium |
| **Tone** | Confident, product-hero, dark |
| **Scroll depth** | ~23,500 px of scroll narrative |
| **Best for** | The homepage — the first impression, and the strongest "we get this brand" signal |
| **Files** | [`site-demos/v1-cinematic/`](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/tree/main/site-demos/v1-cinematic) |

<img src="../assets/demos/v1-cinematic.png" alt="WiseQ cinematic site concept — hero with headphone render on black" width="100%">

---

## 📖 Concept 02 — Editorial

**"Het witboek van veilig geluid."** — *The whitepaper of safe sound.*

An editorial-print aesthetic: a serif masthead in WiseQ orange on warm paper, a chapter rail down the left edge, and long-form typography. Reads like a design annual rather than a store.

| | |
| :--- | :--- |
| **Direction** | Editorial · print-inspired · long-form |
| **Tone** | Considered, authoritative, calm |
| **Scroll depth** | ~26,700 px of scroll narrative |
| **Best for** | The knowledge hub and SEO landing pages — where WiseQ already has a 45-page asset to extend |
| **Files** | [`site-demos/v2-editorial/`](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/tree/main/site-demos/v2-editorial) |

<img src="../assets/demos/v2-editorial.png" alt="WiseQ editorial site concept — serif masthead in orange on warm paper" width="100%">

---

## ✨ Concept 03 — Constellation *(recommended)*

**"Objecten, in plaats van reclame."** — *Objects, instead of advertising.*

A museum-catalogue interface where each product is an **object on a schema**: form, limit, price, purpose. Behind it, a WebGL constellation whose nodes are the actual `threehei` components of MengTo — the Dutch three-in-one cable whose combinatorial explosion is the root of the bundle-recombination problem.

| | |
| :--- | :--- |
| **Direction** | WebGL · data-driven · catalogue |
| **Tone** | Precise, technical, quietly premium |
| **Scroll depth** | ~18,800 px of scroll narrative |
| **Best for** | The differentiator — it makes WiseQ's *weakness* (77 combinatorial bundles) into its *identity* |
| **Files** | [`site-demos/v3-webgl/`](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/tree/main/site-demos/v3-webgl) |

<img src="../assets/demos/v3-webgl.png" alt="WiseQ constellation site concept — product objects as museum catalogue with WebGL component constellation" width="100%">

> **Why this one is the strongest commercially.** WiseQ's catalog audit found **77 combinatorial bundle-products (33% of the catalog)** whose component mapping lived only in human memory. Concept 03 makes that exact structure the visual language of the site — the constellation *is* the bundle graph. It turns an operational liability into a brand asset, and it is the concept that best demonstrates the orchestration layer described in [doc 04](04-AI-STACK-BLUEPRINT.md): the same component registry that drives purchasing would drive the storefront.

---

## 📐 How they were built

| | |
| :--- | :--- |
| **Engine** | Vanilla JS + CSS, no framework, no build step — open the `index.html` and it runs |
| **Catalog** | Real WiseQ imagery — **229 product renders** in [`site-demos/assets/products/`](../site-demos/assets/products/) |
| **Catalog data** | [`site-demos/products.js`](../site-demos/products.js) (55 KB) + [`featured.json`](../site-demos/featured.json) |
| **Typography** | Archivo + Geist, with a fluid type scale |
| **Scroll library** | `scrollcraft.css` / `scrollcraft.js` — one shared scroll-choreography system, vendored per concept so each page runs standalone |

Open any of them locally:

```bash
git clone https://github.com/Ai-Whisperers/wiseq-ai-onboarding.git
cd wiseq-ai-onboarding/site-demos
open index.html            # or: python3 -m http.server 8000
```

---

## 💬 What these are not

- **Not a pitch for a redesign.** WiseQ did not ask for a new visual identity, and this doc does not propose one. These are *demonstrations of craft* — evidence of what the team can ship.
- **Not wireframes.** Every concept is production-quality HTML/CSS/JS against the real catalog.
- **Not committed work.** Nothing here is deployed, and nothing here overrides the live site. If WiseQ likes one, it becomes a Phase-3 conversation with its own scope and price — never a bundled extra.

---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | The stack these concepts plug into |
| **[Automation Backlog](05-AUTOMATION-BACKLOG.md)** | Why the storefront is a backlog item |
| **[Company Profile](01-COMPANY-PROFILE.md)** | The catalog and brand these were built from |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.

---

## 📌 In short

Three complete, scroll-driven storefronts — **production-quality HTML/CSS/JS against WiseQ's real 229-product catalog**, no framework and no build step. They exist as evidence of craft, not as a redesign proposal: **nothing here is deployed and nothing here overrides the live site.** Concept 03 makes the 77-bundle combinatorial problem into the brand's visual language — the constellation *is* the bundle graph.


---

## Continue reading

| Next | Why it matters |
| :--- | :--- |
| **[Ai Stack Blueprint](04-AI-STACK-BLUEPRINT.md)** | The stack these concepts plug into |
| **[Automation Backlog](05-AUTOMATION-BACKLOG.md)** | Why the storefront is a backlog item |
| **[Company Profile](01-COMPANY-PROFILE.md)** | The catalog and brand these were built from |

> **Not sure where to start?** The [README](https://github.com/Ai-Whisperers/wiseq-ai-onboarding#document-map) routes by role — decision-maker, technical, or finance.
