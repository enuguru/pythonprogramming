import unittest

# Function to be tested
def get_value(dictionary, key):
    return dictionary.get(key, None)

# Test case class
class TestGetValue(unittest.TestCase):

    # Test for key present in the dictionary
    def test_key_present(self):
        self.assertEqual(get_value({'a': 1, 'b': 2}, 'a'), 1)

    # Test for key not present in the dictionary
    def test_key_not_present(self):
        self.assertIsNone(get_value({'a': 1, 'b': 2}, 'c'))

    # Test for an empty dictionary
    def test_empty_dictionary(self):
        self.assertIsNone(get_value({}, 'a'))

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
