import pytest
import json

json_path = "dataFixture/testData.json"

def json_data_loader(json_file_path, test_data_variable):
    with open(json_file_path) as json_data:
        data = json.load(json_data)
        print(data)
        return data[test_data_variable]


@pytest.fixture(params=json_data_loader(json_path, "sum_validation"))
def data_for_test(request):
    data = request.param
    return data