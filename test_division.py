import unittest
import division

class DivisionTestCase(unittest.TestCase):

    def test_divides_numbers(self):
        result = division.divide(20, 5)
        self.assertEqual(4, result)

    def test_returns_string_infinity_if_divisor_is_zero(self):
        result = division.divide(20, 0)
        self.assertEqual("Infinity", result)

if __name__ == "__main__":
    unittest.main()