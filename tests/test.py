from main.main import addition, subtraction, multiplication, division
import unittest

class TestSum(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5) 

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 2), 1)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2.0)


if __name__ == '__main__':
    unittest.main()