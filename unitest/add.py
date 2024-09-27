import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test case class
class TestAddFunction(unittest.TestCase):

    # Test case for positive numbers
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    # Test case for negative numbers
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    # Test case for adding zero
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
