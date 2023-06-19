import pytest

@pytest.mark.p1
def test_sample0():
    a = [1,2,3,4]
    assert 2 in a

@pytest.mark.smoke
def test_sample1():
    print("Smoke test1")
    a = [1,2,3,4]
    assert 4 in a

@pytest.mark.smoke
def test_sample2():
    print("Smoke test2")
    a = [1,2,3,4]
    assert 6 in a