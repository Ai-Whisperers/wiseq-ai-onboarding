<div align="center">
<img src="../../../assets/brand/lockup-ink.png" alt="WiseQ × AI Whisperers" height="34">
</div>

<sub>*For Rob* · [← Pack](README.md)</sub>

---

# Read-only access — what we need and how to create it

We already run a full **synthetic lab** without your live systems. The next useful step is **read-only** access so we can load real shapes of data (stock, listings, offers, mail) into monitors and fill the [capability matrix](../../../data/stack-map.md).

**We are not asking for write rights.** No price changes, invoices, shipments, or emails sent by us until you explicitly approve a later gate.

## How to send credentials (agreed channel)

**Send to Ivan on WhatsApp** using the fill-in block:  
→ [whatsapp-cred-template.md](whatsapp-cred-template.md)  
(phone link: https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/start/rob/whatsapp-cred-template.md)

Ivan will vault them immediately and confirm. Prefer Bitwarden Send if you already use it; WhatsApp → Ivan is OK for this Phase 0 handoff.

| Do | Don’t |
| :--- | :--- |
| WhatsApp **Ivan** (or Bitwarden Send to Ivan) | Paste secrets into GitHub issues, group chats, or this public repo |
| Use the [WhatsApp template](whatsapp-cred-template.md) labels so nothing is ambiguous | Send one undifferentiated blob of passwords |
| Name each key `AIW-readonly-YYYY-MM` so you can revoke it later | Reuse an existing FiveX/ChannelDock “full” write integration key |
| Prefer **separate keys per system** | One shared “god” password for everything |
| Tell us the **plan tier** (e.g. ChannelDock Voorraad) when you send the key | Assume we can guess entitlements from the key alone |
| Delete the WhatsApp messages after Ivan says “vaulted” (optional but good) | Leave production write passwords in chat history |

If you prefer, create the keys and stay on a short call while we do a one-time “can we list products?” check — then you keep the secret and we only store what you approve in a vault.

---

## Priority order (start here)

Do **wave 1** first (~30–45 min). Wave 2 when convenient. Wave 3 optional.

### Wave 1 — unblocks most Phase 0 reads

| # | System | What we need | Read-only intent |
| ---: | :--- | :--- | :--- |
| 1 | **ChannelDock** | API key + secret · confirm plan (Gratis / Voorraad / WMS) · PIM yes/no | Products, stock, bundles, shipping rules, unassigned shipments |
| 2 | **bol Seller × active accounts** | Client ID + secret **per account** (NL + Electronics; België only if still used) | Offers, orders, delivery promises, reviews (read) |
| 3 | **e-Boekhouden** | REST API token (not old SOAP) | Relations, offers, invoices — **list/read only** in Phase 0 |
| 4 | **Mailbox provider name** + read access | Which host (Microsoft 365 / Google / other) + app password or shared mailbox | Classify school/CS mail — **no send** |

### Wave 2 — enrich the lab

| # | System | What we need |
| ---: | :--- | :--- |
| 5 | **Shopify** | Collaborator invite **or** custom app with **read** scopes only |
| 6 | **FiveX** | Confirm export path; sample CSV (EAN/stock/sales + reviews) if no API — **no price-write access** |
| 7 | **MyParcel** | API key if school labels are prepared there (read shipments first) |

### Wave 3 — later / human-gated

| # | System | Notes |
| ---: | :--- | :--- |
| 8 | Google Drive CE folder | Share **view** on the cert library folder only |
| 9 | QLS | Ticket/email path is enough initially — no API assumed |

---

## Step-by-step: create each key

### 1. ChannelDock (API key + secret)

**Docs:** [REST API help (NL)](https://www.channeldock.com/help/nl/integrations-api/api/channeldock-rest-api-documentation/) · [API reference](https://docs.channeldock.com/) · [Settings overview](https://channeldock.com/nl/settings-api-webhooks/)

1. Log in to ChannelDock.  
2. Go to **Instellingen → API & Webhooks**.  
3. Under API keys, click **Genereer nieuwe API-sleutels**.  
4. Description: `AIW-readonly-2026-10`.  
5. If the UI lets you **limit endpoints**, prefer read of products/stock/orders/shipments — avoid shipment-create if separable.  
6. Copy **API key** and **API secret** once; store in your password manager.  
7. Reply with: plan name (Gratis / Voorraad / Volledig WMS) and whether **PIM** is on.

**Also tell us:** do you already use ChannelDock **Bundels** (manual says yes) — then we will not rebuild bundle UI.

---

### 2. bol.com Retailer API (per seller account)

**Docs:** [Client credentials aanmaken (NL)](https://partnerplatform.bol.com/nl/idp/toegang-krijgen-tot-de-api) · [Retailer API credentials](https://api.bol.com/retailer/public/Retailer-API/credentials_for_retailer_api.html) · [Authentication](https://api.bol.com/retailer/public/Retailer-API/authentication.html)

Repeat for **WiseQ NL** and **WiseQ Electronics** (and België only if still operational):

1. Log in to that seller account → **Instellingen → Diensten → API Instellingen**.  
2. Fill **technisch contact** (can be you + Ivan as CC note) → Opslaan.  
3. Under **Client credentials voor de Retailer API** → **Aanmaken**.  
4. Name: `AIW-readonly-WiseQ-NL` (or Electronics / Belgie).  
5. Copy **Client ID** and **Toon secret → Client secret**.  
6. Send us which account the pair belongs to.

We will only call **read** endpoints (offers, orders, shipments, returns as needed). We will **not** change prices or stock until a later written approval.

---

### 3. e-Boekhouden (REST API token)

**Docs:** [API-koppeling](https://www.e-boekhouden.nl/koppelingen/api) · [REST reference](https://api.e-boekhouden.nl/scalar/)

1. Log in as **beheerder** of the administratie.  
2. **Beheer → Inrichting → Koppelingen**.  
3. Choose **e-Boekhouden API** (not **API/SOAP (oud)**) → Verder.  
4. **Toevoegen** → name `AIW-readonly-2026-10`.  
5. Optional: set an **expiry date** (e.g. +90 days) and calendar reminder.  
6. Copy the token **immediately** (shown once) into your password manager.  
7. Send the token via secure share.

Phase 0: we only **list** relations / offers / invoices to match the school-order shadow demo. No create/send until you approve.

---

### 4. Mailbox (read-only)

We need to know the provider first:

| If you use… | What to create |
| :--- | :--- |
| **Microsoft 365** | App password or shared mailbox with **read** for a dedicated `aiw-readonly@…` (or Graph app with Mail.Read only) |
| **Google Workspace / Gmail** | [App password](https://support.google.com/accounts/answer/185833) on an account that can read the CS/sales inbox (2FA required) |
| **Other** | Tell us the host + whether IMAP exists |

**Policy:** drafts only; **you** send. No automatic “please change your bol rating” messages.

---

### 5. Shopify (optional wave 2)

**Docs:** [Collaborator accounts](https://help.shopify.com/en/manual/your-account/users/security/collaborator-accounts) · [Access scopes](https://shopify.dev/docs/api/usage/access-scopes)

**Preferred for Phase 0:** invite AI Whisperers as a **collaborator** with the minimum roles needed to **view products / orders / inventory** (no manage themes, no manage settings unless required).

**Alternative:** create a custom app / Dev Dashboard app and grant only:

- `read_products`  
- `read_inventory`  
- `read_orders` (last 60 days is enough to start)  

Do **not** grant `write_*` scopes yet.

---

### 6. FiveX (exports first)

We do **not** need price-automation rights.

1. Export a recent **product/stock/sales** report and a **review** extract (anonymise customer names if easy).  
2. Share via secure file link (not the public repo).  
3. If FiveX has an API for your plan, send docs + a read token; otherwise CSV is enough for Phase 0.

---

### 7. MyParcel (optional)

If school DHL labels go through MyParcel: create an API key in the MyParcel account settings (label in UI as `AIW-readonly`) and share securely. We start with **shipment/status read** only.

---

## Checklist you can paste back

**Preferred:** use the full [WhatsApp template](whatsapp-cred-template.md).

Short form:

```text
[ ] ChannelDock plan: ________  PIM: yes/no
[ ] ChannelDock API key+secret (AIW-readonly-…) — WhatsApp to Ivan
[ ] bol NL client id+secret — WhatsApp to Ivan
[ ] bol Electronics client id+secret — WhatsApp to Ivan
[ ] bol België: still needed? yes/no
[ ] e-Boekhouden REST token — WhatsApp to Ivan
[ ] Mailbox provider: ________  read method: ________
[ ] Shopify: collaborator / custom app / skip for now
[ ] FiveX: sample CSVs later / API later
[ ] Raw Handleiding may stay public in GitHub? yes/no
```

---

## What we do after you send wave 1

1. Ivan vaults secrets (never this public repo) — see AIW receive checklist.  
2. Run **read-only** smoke tests; fill [`data/stack-map.md`](../../../data/stack-map.md) capability matrix.  
3. Show you a digest: assortment gaps, ungefrankeerd queue sample, school-offer shape — still **no writes**.  
4. Only then discuss any draft/write permission.

Related: [WhatsApp template](whatsapp-cred-template.md) · [Open asks](open-asks.md) · [Next Steps](../../20-offer/03-next-steps.md) · [Lab](../../../lab/README.md)
