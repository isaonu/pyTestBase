
def sum_two_num(a, b):
    return a + b;

def hello_world():
    return "Hello world"

def returning_even_list():
    return [20,40,60,80,100]

def are_all_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
    else:
        return True

#####Operands assertions
#== assertion
def test_equal():
    assert sum_two_num(2, 3) == 5

def test_equal_two():
    assert hello_world() == "Hello world"

#!=assertion
def test_different_than():
    assert sum_two_num(2, 10) != 30

#> assertion
def test_grater_than():
    assert 20 > 10;

#####Msg
#default msg
def test_default_msg():
    assert hello_world() == "Hello class"

#custom msg
def test_custom_msg():
    assert hello_world() == "Hello class", "print msg is not correct"

##### Using methods
#Other existing operations from python
def test_python_methods_to_assert():
    mySet = {1,2,3,4,5}
    assert 3 in mySet

def test_length_method_to_assert():
    myList = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    assert len(myList) == 5

# True assertion using defined methods that already checks some condition
def test_my_assertion():
   assert are_all_even(returning_even_list());