import pytest
#variables from .env
from dotenv import load_dotenv
import os
load_dotenv()

def sum_two_num(a, b):
    return a + b

# Data with fixture
def test_sum_two_num_fixture(data_for_test):
    result = sum_two_num(data_for_test["a"], data_for_test["b"])
    assert result == data_for_test["result"]

# Data with .env variable
def test_sum_two_num_env_var():
    print(type(os.environ["a0"]))
    result = sum_two_num(int(os.environ["a0"]), int(os.environ["b0"]))
    assert result == 50

# Data with .env variable
def test_env_var():
    print(type(os.environ["word1"]))
    assert (os.environ["word1"] + " " + os.environ["word2"]) == "Hello Bye"