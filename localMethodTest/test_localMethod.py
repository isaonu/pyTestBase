
# Method for local test
def sum_two_num(a, b):
    return a + b


def test_positive_num():
    assert sum_two_num(20, 30) == 50


def test_one_negative_num():
    assert sum_two_num(-20, 30) == 11


def test_two_negative_num():
    assert sum_two_num(-20, -30) == -50


def test_second_one_negative_num():
    assert sum_two_num(20, -30) == -10

