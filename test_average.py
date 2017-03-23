import unittest
import average

class AverageTestCase(unittest.TestCase):


    def test_calculates_average_of_numbers_in_list(self):
        result = average.average([10,2,3,4,5])
        self.assertEqual(4.8, result)
if __name__ == "__main__":
    unittest.main()
