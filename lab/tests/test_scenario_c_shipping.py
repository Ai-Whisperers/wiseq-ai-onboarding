from scenarios.c_shipping import run_shipping_quotes


def test_typed_tariffs_match_golden():
    out = run_shipping_quotes()
    assert out["all_match"] is True
    assert out["uplift_blocked"] is True
    for q in out["quotes"]:
        assert q["match"], q
