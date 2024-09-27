import unittest
from my_module import add, subtract, multiply

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

if __name__ == '__main__':
    unittest.main()
