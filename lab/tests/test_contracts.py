"""Contract smoke: fixture adapters return SimulatedResult shape."""

from adapters.fixture import (
    FixtureAccounting,
    FixtureInventory,
    FixtureMailbox,
    FixtureMarketplace,
    FixtureShipping,
)


def test_all_fixture_calls_are_simulated():
    inv = FixtureInventory()
    r = inv.get_stock("101", "wiseq_nl")
    assert r.simulated is True
    assert r.source == "fixture"

    m = FixtureMarketplace().assortment_online("wiseq_nl")
    assert m.simulated is True
    assert m.data["all_online"] is False  # 999-gap offline

    bel = FixtureMarketplace().assortment_online("wiseq_belgie")
    assert bel.data["migration_state"] == "phasing_out"

    mail = FixtureMailbox().list_messages()
    assert mail.ok and len(mail.data["messages"]) >= 2

    ship = FixtureShipping().quote(
        country="NL", product_class="school_parcel", qty=1, method="QLS_EUROPLUS"
    )
    assert ship.ok and ship.data["unit_eur"] == 10.54

    acct = FixtureAccounting()
    offer = acct.draft_offer("SO-X", [{"qty": 1}])
    assert offer.needs_approval is True
