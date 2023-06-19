import pytest

def sum_two_num(a, b):
    return a + b

@pytest.mark.parametrize("valueA, valueB, expected",
                         [(20, 30, 50), (1.2, 3.6, 4.8), (-10, 20, 10), (-50, -100, -150)])
def test_sum_two_num(valueA, valueB, expected):
    assert sum_two_num(valueA, valueB) == expected