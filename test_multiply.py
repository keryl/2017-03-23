import unittest
import multiply

class MultiplyTestCase(unittest.TestCase):

    def test_multiplies_numbers(self):
        result = multiply.multiply(4, 5)
        self.assertEqual(20, result)

if __name__ == "__main__":
    unittest.main()