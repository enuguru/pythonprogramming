import unittest

# Function to be tested
def sort_numbers(numbers):
    return sorted(numbers)

# Test case class
class TestSortNumbers(unittest.TestCase):

    # Test for a list with positive numbers
    def test_sort_positive(self):
        self.assertEqual(sort_numbers([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])

    # Test for a list with negative numbers
    def test_sort_negative(self):
        self.assertEqual(sort_numbers([-1, -3, -2]), [-3, -2, -1])

    # Test for an already sorted list
    def test_already_sorted(self):
        self.assertEqual(sort_numbers([1, 2, 3]), [1, 2, 3])

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
