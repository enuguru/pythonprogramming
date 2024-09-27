import unittest

# Class to be tested
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Test case class
class TestPersonClass(unittest.TestCase):

    # Test for the greet function
    def test_greet(self):
        person = Person("John", 30)
        self.assertEqual(person.greet(), "Hello, my name is John and I am 30 years old.")

    # Test for initializing the name and age
    def test_person_initialization(self):
        person = Person("Jane", 25)
        self.assertEqual(person.name, "Jane")
        self.assertEqual(person.age, 25)

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
