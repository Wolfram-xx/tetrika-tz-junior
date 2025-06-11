import unittest
from solution1 import *

class TestStrictDecorator(unittest.TestCase):

    def test_sum_two_correct_types(self):
        self.assertEqual(sum_two(2, 3), 5)
        self.assertEqual(sum_two(-1, 1), 0)

    def test_sum_two_wrong_type_first_argument(self):
        with self.assertRaises(TypeError) as cm:
            sum_two("1", 2)
        self.assertIn("У переменной a зафиксирован тип", str(cm.exception))

    def test_sum_two_wrong_type_second_argument(self):
        with self.assertRaises(TypeError) as cm:
            sum_two(1, 2.5)
        self.assertIn("У переменной b зафиксирован тип", str(cm.exception))

    def test_sum_two_both_arguments_wrong_type(self):
        with self.assertRaises(TypeError) as cm:
            sum_two("1", [2])
        self.assertIn("У переменной a зафиксирован тип", str(cm.exception))

    def test_sum_two_missing_argument(self):
        with self.assertRaises(TypeError):
            sum_two(1)

    def test_sum_two_extra_argument(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)

    def test_sum_two_keyword_arguments(self):
        self.assertEqual(sum_two(a=4, b=5), 9)

    def test_sum_two_mixed_arguments(self):
        self.assertEqual(sum_two(4, b=6), 10)

if __name__ == "__main__":
    unittest.main()