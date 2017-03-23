import unittest
import average

class AverageTestCase(unittest.TestCase):

    def test_calculates_average_of_numbers_in_list(self):
        result = average.average(15, 5)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main()
