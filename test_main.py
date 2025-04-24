import unittest
from main import countWellFormedParenthesis

class TestParentheses(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countWellFormedParenthesis(1), 1)
        self.assertEqual(countWellFormedParenthesis(2), 2)
        self.assertEqual(countWellFormedParenthesis(3), 5)
        self.assertEqual(countWellFormedParenthesis(4), 14)
        self.assertEqual(countWellFormedParenthesis(5), 42)
        self.assertEqual(countWellFormedParenthesis(15), 9694845)

if name == '__main__':
    unittest.main()