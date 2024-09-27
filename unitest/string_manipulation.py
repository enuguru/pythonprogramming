import unittest

# Function to be tested
def capitalize_words(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])

# Test case class
class TestCapitalizeWords(unittest.TestCase):

    # Test for a normal sentence
    def test_normal_sentence(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    # Test for an empty string
    def test_empty_string(self):
        self.assertEqual(capitalize_words(""), "")

    # Test for a sentence with multiple spaces
    def test_sentence_with_spaces(self):
        self.assertEqual(capitalize_words("hello   world"), "Hello   World")

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
