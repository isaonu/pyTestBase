import pytest

@pytest.fixture
def innermost(order, subDirectoryFix):
    order.append("innerFix-mid")
    print(order)

def test_fixtureMid(order, topFixture):
    assert order == ["subDirectoryFix", "innerFix-mid", "topFixture"]