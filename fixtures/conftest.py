# top conftest file

import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
#Here see how we call innerTopFix fixture, which is not defined here but in the test
def topFixture(order, innermost):
    order.append("topFixture")
    print(order)