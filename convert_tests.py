import convert
import unittest


class TestCases(unittest.TestCase):
    # Task 1
    def test_str_to_float_1(self):
        words = '3.2'
        assert convert.str_to_float(words) == 3.2

    def test_str_to_float_2(self):
        words = '3 s2t8'
        assert convert.str_to_float(words) == None

    def test_str_to_float_3(self):
        words = 'Hello'
        assert convert.str_to_float(words) == None

    def test_str_to_float_4(self):
        words = '-8'
        assert convert.str_to_float(words) == -8

    # Task 2
    


if __name__ == '__main__':
    unittest.main()
