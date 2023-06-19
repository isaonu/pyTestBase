import pytest

@pytest.fixture
def subDirectoryFix(order):
    order.append("subDirectoryFix")
    print(order)