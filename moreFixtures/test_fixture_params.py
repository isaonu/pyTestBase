import pytest



@pytest.fixture(params=["serviceA", "serviceB"])
def start_services(request):
    return request.param

def test_fixtures_params(start_services):
    print(start_services)

