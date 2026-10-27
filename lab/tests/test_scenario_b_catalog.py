from scenarios.b_catalog import run_catalog_integrity


def test_bundles_resolve():
    out = run_catalog_integrity()
    assert out["bundle_count"] == 25
    assert out["unresolved_bundles"] == []
    assert out["sample_bundle"]["ok"] is True


def test_missing_eans_flagged():
    out = run_catalog_integrity()
    assert out["missing_ean_count"] > 0


def test_refuse_bad_shipping_templates():
    out = run_catalog_integrity()
    assert out["clone_ok_class"]["ok"] is True
    assert out["clone_needs_confirmation"]["ok"] is False
    assert "NEEDS_CONFIRMATION" in (out["clone_needs_confirmation"]["error"] or "")
    assert out["clone_headphone_case"]["ok"] is False
