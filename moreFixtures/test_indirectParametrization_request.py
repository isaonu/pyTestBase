import pytest


@pytest.fixture()
def setup_browser(request):
    #Check how we use the value from the indirect paramatrization of this feature
    return "Running browser: " + request.param

@pytest.mark.parametrize("setup_browser", [("chrome"), ("firefox")])
def test_login(setup_browser):
    #Check how we use the return value from a fixture
    print(setup_browser)
    print("Inside the test")