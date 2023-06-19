import pytest

test_control = "dont run"
#####Some existing python marks
@pytest.mark.skip
def test_test_in_progress():
    a = [1,2,3,4]
    assert 6 in a

@pytest.mark.skipif(test_control == "dont run", reason = "Test availabe for iOS only")
def test_not_applicable_to_all_devices():
    assert 20 == 30

@pytest.mark.xfail
def test_cart_no_ready_in_app():
    print("We run this but let pytest know that it will fail and its fine")
    assert 2 == 30

@pytest.mark.xfail(run=False)
def test_cart_no_ready_in_app_dont_run():
    print("We are not even running this one")
    assert 2 == 30

def test_execute():
    assert 20 == 20

