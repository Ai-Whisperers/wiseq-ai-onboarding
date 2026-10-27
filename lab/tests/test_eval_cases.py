import json
from pathlib import Path

from eval.audit import append_audit, read_audit
from scenarios.a_school import run_school_order

CASES = json.loads(
    (Path(__file__).resolve().parents[1] / "fixtures" / "mailbox" / "eval_cases.json").read_text(
        encoding="utf-8"
    )
)


def test_mailbox_eval_cases():
    for case in CASES:
        approve = case.get("approve", True)
        out = run_school_order(case["message_id"], approve=approve)
        assert out["status"] == case["expect_status"], case["id"]
        for key in case["must_have_keys"]:
            assert key in out, f"{case['id']} missing {key}"
        append_audit(
            "school_eval",
            simulated=True,
            approved=approve if case["expect_status"] != "escalated" else None,
            case_id=case["id"],
            status=out["status"],
        )


def test_audit_log_appends():
    before = len(read_audit(1000))
    append_audit("unit_test_ping", simulated=True)
    after = read_audit(1000)
    assert len(after) >= before + 1
    assert after[-1]["action"] == "unit_test_ping"
