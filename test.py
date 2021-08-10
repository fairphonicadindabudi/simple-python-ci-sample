import unittest

from math_addition import addition


class TestAddition(unittest.TestCase):
    def test_addition(self):
        """
        Test that it can addition two integer
        """
        self.assertEqual(addition(1,1), 2)
        self.assertEqual(addition(-1,1), 0)
        self.assertEqual(addition(76,59), 135)


if __name__ == '__main__':
    unittest.main()