from scenarios.a_school import run_duplicate_submit, run_school_order


def test_school_order_happy_path():
    out = run_school_order("mail_school_001", approve=True)
    assert out["simulated"] is True
    assert out["status"] == "ok"
    assert out["offer_replay_idempotent"] is True
    assert out["invoice"]["status"] == "committed"
    assert out["shipment"]["status"] == "label_prepared_simulated"


def test_school_order_requires_approval():
    out = run_school_order("mail_school_001", approve=False)
    assert out["status"] == "awaiting_approval"
    assert out["invoice"]["status"] == "awaiting_approval"


def test_catalog_sample_escalates():
    out = run_school_order("mail_school_002", approve=True)
    assert out["status"] == "escalated"


def test_no_duplicate_invoices_on_retry():
    out = run_duplicate_submit()
    assert out["single_offer_id"] is True
    assert out["second_offer_replay"] is True
    assert out["single_invoice_id"] is True
    assert out["second_invoice_replay"] is True
