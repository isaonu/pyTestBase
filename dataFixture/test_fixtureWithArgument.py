import pytest

@pytest.fixture
def my_fixture(request):
    # Access the argument value passed to the fixture
    arg_value = request.param
    # Perform setup actions using the argument value
    setup_action(arg_value)
    # Return any fixture data or resources
    yield request.param
    # Perform teardown actions (optional)

def setup_action(arg):
    # Perform setup actions based on the argument value
    print(f"Setting up with argument: {arg}")


@pytest.mark.parametrize("my_fixture", [1, 2, 3], indirect=True)
def test_my_function(my_fixture):
    # Test logic that uses the fixture
    assert True

