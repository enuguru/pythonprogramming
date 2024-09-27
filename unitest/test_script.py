import unittest

# Example function to test
def multiply(a, b):
    return a * b

# Creating a test case
class TestMultiplyFunction(unittest.TestCase):

    # Setup method, runs before each test
    def setUp(self):
        self.a = 10
        self.b = 5

    # A test case
    def test_multiply(self):
        result = multiply(self.a, self.b)
        self.assertEqual(result, 50)

    # Another test case for edge cases
    def test_multiply_with_zero(self):
        self.assertEqual(multiply(self.a, 0), 0)

    # Teardown method, runs after each test
    def tearDown(self):
        pass

# Running the tests
if __name__ == '__main__':
    unittest.main()
