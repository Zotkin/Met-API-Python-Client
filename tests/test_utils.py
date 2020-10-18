from met_api.utils import logical_xnor


def test_logical_xnor():
    assert logical_xnor(False, False)
    assert logical_xnor(True, True)
    assert not logical_xnor(True, None)
    assert not logical_xnor(None, True)