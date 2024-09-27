import unittest

# Function to be tested
def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    return True

# Test case class
class TestCheckPositive(unittest.TestCase):

    # Test for a positive number
    def test_positive_number(self):
        self.assertTrue(check_positive(5))

    # Test for zero (should raise an error)
    def test_zero(self):
        with self.assertRaises(ValueError):
            check_positive(0)

    # Test for a negative number (should raise an error)
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            check_positive(-5)

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
