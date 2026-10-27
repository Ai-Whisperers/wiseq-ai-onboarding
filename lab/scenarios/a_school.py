"""Experiment A — school order pipeline (simulated)."""

from __future__ import annotations

from adapters.fixture import FixtureAccounting, FixtureMailbox, FixtureShipping


def run_school_order(message_id: str = "mail_school_001", approve: bool = True) -> dict:
    mail = FixtureMailbox()
    acct = FixtureAccounting()
    ship = FixtureShipping()

    msg = mail.get_message(message_id)
    assert msg.ok
    parsed = msg.data["parsed"]
    school_order_id = msg.data["school_order_id"]

    if parsed.get("needs_catalog") or parsed.get("needs_sample"):
        return {
            "status": "escalated",
            "reason": "catalog/sample path — human sends materials first",
            "message_id": message_id,
            "simulated": True,
        }

    lines = [
        {
            "sku_hint": parsed.get("sku_hint"),
            "qty": parsed.get("qty"),
            "warranty_years": 2,
        }
    ]
    offer = acct.draft_offer(school_order_id, lines)
    # idempotent replay
    offer2 = acct.draft_offer(school_order_id, lines)
    inv_draft = acct.draft_invoice(offer.data["offer_id"])
    inv = acct.commit_invoice(inv_draft.data["invoice_id"], approved=approve)
    shipment = ship.prepare_shipment(inv.data.get("invoice_id", ""), approved=approve)

    return {
        "status": "ok" if approve and inv.data.get("status") == "committed" else "awaiting_approval",
        "message_id": message_id,
        "school_order_id": school_order_id,
        "offer": offer.data,
        "offer_replay_idempotent": offer2.data.get("idempotent_replay") is True,
        "invoice": inv.data,
        "shipment": shipment.data,
        "simulated": True,
    }


def run_duplicate_submit(message_id: str = "mail_school_001") -> dict:
    """Submitting twice must not create two committed invoices."""
    first = run_school_order(message_id, approve=True)
    second = run_school_order(message_id, approve=True)
    # Note: FixtureAccounting is new each call — share instance for true idempotency demo
    mail = FixtureMailbox()
    acct = FixtureAccounting()
    msg = mail.get_message(message_id)
    sid = msg.data["school_order_id"]
    lines = [{"sku_hint": "unbreakable", "qty": 30, "warranty_years": 2}]
    o1 = acct.draft_offer(sid, lines)
    o2 = acct.draft_offer(sid, lines)
    i1 = acct.draft_invoice(o1.data["offer_id"])
    c1 = acct.commit_invoice(i1.data["invoice_id"], approved=True)
    i2 = acct.draft_invoice(o1.data["offer_id"])
    c2 = acct.commit_invoice(i2.data["invoice_id"], approved=True)
    return {
        "single_offer_id": o1.data["offer_id"] == o2.data["offer_id"],
        "second_offer_replay": o2.data.get("idempotent_replay") is True,
        "single_invoice_id": c1.data["invoice_id"] == c2.data["invoice_id"],
        "second_invoice_replay": c2.data.get("idempotent_replay") is True,
        "first_pipeline_ok": first["status"] == "ok",
        "second_pipeline_ok": second["status"] == "ok",
        "simulated": True,
    }
