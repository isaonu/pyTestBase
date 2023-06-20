#Run this test with -s to see the prints and be more explinatory
import pytest

@pytest.fixture
def localFixture():
    print("Fixture from local file")
    return "Fixture from local file"

@pytest.fixture
def localFixture2(request):
    greetings = "Hello"
    print("Fixture2 from local file")
    yield greetings
    print("Clean up in the fixture2")

@pytest.fixture
def innermost(order):
    order.append("innerFixture-top")
    print(order)

def test_localFixture(localFixture):
    assert localFixture == "Fixture from local file"

def test_localFixture2(localFixture2):
    assert localFixture2 == "Hello"

def test_fixtureTop(order, topFixture):
    assert order == ["innerFixture-top", "topFixture"]