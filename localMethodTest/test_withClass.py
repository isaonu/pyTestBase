
def subtract_two_num(a, b):
    return a - b

class TestSubtraction:
    def test_possitive_num(self):
        assert subtract_two_num(31, 26) == 5
