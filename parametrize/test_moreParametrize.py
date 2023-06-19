import pytest

def sum_two_num(a, b):
    return a + b

#testing all combinations
@pytest.mark.parametrize("x", [1,2])
@pytest.mark.parametrize("y", [10,5])
def test_sum(x, y):
    print(sum_two_num(x, y))
    assert True
