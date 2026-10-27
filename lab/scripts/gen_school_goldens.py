"""Generate school_inbox.json (~32) and eval_cases.json (~40)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_INBOX = ROOT / "fixtures" / "mailbox" / "school_inbox.json"
OUT_CASES = ROOT / "fixtures" / "mailbox" / "eval_cases.json"


def main() -> None:
    msgs: list[dict] = []
    msgs.append(
        {
            "id": "mail_school_001",
            "folder": "inbox",
            "from": "inkoop@demo-basisschool.nl",
            "subject": "Offerteaanvraag WiseQ Unbreakable headphones (klas 5)",
            "body": (
                "Goedemorgen,\n\nWij ontvangen graag een offerte voor 30x Unbreakable "
                "koptelefoons inclusief 2 jaar garantie en verzending naar Grootebroek.\n\n"
                "Met vriendelijke groet,\nInkoop Demo Basisschool"
            ),
            "school_order_id": "SO-2026-001",
            "parsed": {
                "school": "Demo Basisschool",
                "sku_hint": "unbreakable",
                "qty": 30,
                "needs_catalog": False,
                "needs_sample": False,
                "reseller": None,
            },
        }
    )
    msgs.append(
        {
            "id": "mail_school_002",
            "folder": "inbox",
            "from": "dir@demo-stichting.nl",
            "subject": "Catalogus + proefexemplaar",
            "body": "Kunnen jullie een catalogus en een proefexemplaar sturen?",
            "school_order_id": "SO-2026-002",
            "parsed": {
                "school": "Demo Stichting",
                "sku_hint": None,
                "qty": None,
                "needs_catalog": True,
                "needs_sample": True,
                "reseller": None,
            },
        }
    )

    schools = [
        ("De Regenboog", "junior", 12, None),
        ("OBS De Brug", "kids-anc", 25, None),
        ("Stichting Leerrijk", "unbreakable", 40, "EDG"),
        ("College Noord", "tablet-cart", 2, None),
        ("Basisschool Zon", "hearing-protect", 60, None),
        ("IKC Haven", "unbreakable", 15, "ITS"),
        ("Montessori Delft", "junior", 8, None),
        ("VO Campus", "kids-anc", 50, "Onderwijsmagazijn"),
    ]
    n = 3
    for school, sku, qty, reseller in schools:
        slug = school.lower().replace(" ", "-")
        msgs.append(
            {
                "id": f"mail_school_{n:03d}",
                "folder": "inbox",
                "from": f"inkoop@{slug}.demo.nl",
                "subject": f"Offerte {qty}x {sku}",
                "body": f"Offerte svp voor {qty} stuks ({sku}). School: {school}.",
                "school_order_id": f"SO-2026-{n:03d}",
                "parsed": {
                    "school": school,
                    "sku_hint": sku,
                    "qty": qty,
                    "needs_catalog": False,
                    "needs_sample": False,
                    "reseller": reseller,
                },
            }
        )
        n += 1

    for school, kind in [
        ("Proefschool West", "sample"),
        ("Catalogusgroep Oost", "catalog"),
        ("Beide Aanvraag", "both"),
    ]:
        msgs.append(
            {
                "id": f"mail_school_{n:03d}",
                "folder": "inbox",
                "from": f"info@{kind}.demo.nl",
                "subject": f"Aanvraag {kind}",
                "body": f"Graag {kind} informatie.",
                "school_order_id": f"SO-2026-{n:03d}",
                "parsed": {
                    "school": school,
                    "sku_hint": None,
                    "qty": None,
                    "needs_catalog": kind in ("catalog", "both"),
                    "needs_sample": kind in ("sample", "both"),
                    "reseller": None,
                },
            }
        )
        n += 1

    for qty in [1, 5, 10, 20, 35, 45, 55, 100]:
        msgs.append(
            {
                "id": f"mail_school_{n:03d}",
                "folder": "inbox",
                "from": f"bulk{qty}@demo-school.nl",
                "subject": f"{qty}x Unbreakable",
                "body": f"{qty} stuks Unbreakable svp.",
                "school_order_id": f"SO-2026-{n:03d}",
                "parsed": {
                    "school": f"Demo Bulk {qty}",
                    "sku_hint": "unbreakable",
                    "qty": qty,
                    "needs_catalog": False,
                    "needs_sample": False,
                    "reseller": None,
                },
            }
        )
        n += 1

    msgs.append(
        {
            "id": f"mail_school_{n:03d}",
            "folder": "inbox",
            "from": "twijfel@demo.nl",
            "subject": "Misschien Unbreakable?",
            "body": "We overwegen Unbreakable maar weten het aantal nog niet.",
            "school_order_id": f"SO-2026-{n:03d}",
            "parsed": {
                "school": "Twijfel School",
                "sku_hint": "unbreakable",
                "qty": None,
                "needs_catalog": False,
                "needs_sample": False,
                "reseller": None,
                "ambiguous": True,
            },
        }
    )
    n += 1
    msgs.append(
        {
            "id": f"mail_school_{n:03d}",
            "folder": "inbox",
            "from": "bestuur@stichting-demo.nl",
            "subject": "Vervolg bestelling na sample",
            "body": "Sample was goed — offerte voor 24x Kids ANC.",
            "school_order_id": f"SO-2026-{n:03d}",
            "parsed": {
                "school": "Stichting Demo",
                "sku_hint": "kids-anc",
                "qty": 24,
                "needs_catalog": False,
                "needs_sample": False,
                "reseller": None,
                "follow_up": True,
            },
        }
    )

    while len(msgs) < 32:
        i = len(msgs) + 1
        msgs.append(
            {
                "id": f"mail_school_{i:03d}",
                "folder": "inbox",
                "from": f"school{i}@demo.nl",
                "subject": f"Offerte junior set {i}",
                "body": f"10x junior voor school {i}",
                "school_order_id": f"SO-2026-{i:03d}",
                "parsed": {
                    "school": f"Demo {i}",
                    "sku_hint": "junior",
                    "qty": 10,
                    "needs_catalog": False,
                    "needs_sample": False,
                    "reseller": None,
                },
            }
        )

    cases: list[dict] = [
        {
            "id": "happy-offer-request",
            "message_id": "mail_school_001",
            "expect_status": "ok",
            "must_have_keys": ["offer", "invoice", "shipment"],
            "notes": "Full pipeline with approval",
        },
        {
            "id": "catalog-sample-escalation",
            "message_id": "mail_school_002",
            "expect_status": "escalated",
            "must_have_keys": ["reason"],
            "notes": "Do not invent product lines",
        },
        {
            "id": "awaiting-approval",
            "message_id": "mail_school_001",
            "approve": False,
            "expect_status": "awaiting_approval",
            "must_have_keys": ["invoice"],
            "notes": "Commit blocked without APPROVE",
        },
    ]
    for m in msgs:
        if m["id"] == "mail_school_001":
            continue
        parsed = m["parsed"]
        if parsed.get("needs_catalog") or parsed.get("needs_sample"):
            cases.append(
                {
                    "id": f"esc-{m['id']}",
                    "message_id": m["id"],
                    "expect_status": "escalated",
                    "must_have_keys": ["reason"],
                    "notes": "catalog/sample",
                }
            )
        else:
            cases.append(
                {
                    "id": f"ok-{m['id']}",
                    "message_id": m["id"],
                    "expect_status": "ok",
                    "must_have_keys": ["offer", "invoice", "shipment"],
                    "notes": "happy path",
                }
            )
        if len(cases) >= 40:
            break

    OUT_INBOX.write_text(json.dumps(msgs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_CASES.write_text(json.dumps(cases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(msgs)} messages, {len(cases)} eval cases")


if __name__ == "__main__":
    main()
