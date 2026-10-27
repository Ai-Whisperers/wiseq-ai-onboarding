from adapters.vendor import (
    BolRetailerReadStub,
    ChannelDockReadStub,
    EBoekhoudenReadStub,
    MailboxReadStub,
)


def test_vendor_stubs_fail_closed():
    cd = ChannelDockReadStub()
    r = cd.get_stock("119", "wiseq-nl")
    assert r.ok is False
    assert "read-only-access" in (r.error or "")

    assert EBoekhoudenReadStub().draft_offer("SO-1", []).ok is False
    assert BolRetailerReadStub().assortment_online("wiseq-nl").ok is False
    assert MailboxReadStub().list_messages().ok is False
