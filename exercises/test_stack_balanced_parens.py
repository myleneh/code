#!/usr/local/bin/python3
"""
Unittest for stack_balanced_parens.py
"""
import stack_balanced_parens
import unittest

class TestStackParens(unittest.TestCase):
    def test_balanced(self):
        expression = "{[()]}"
        self.assertTrue(stack_balanced_parens.isBalanced(expression))

    def test_unbalanced(self):
        expression = "{[()]}("
        self.assertFalse(stack_balanced_parens.isBalanced(expression))

    def test_numbers_unbalanced(self):
        expression = "(4+5)*(2+(4-7)"
        self.assertFalse(stack_balanced_parens.isBalanced(expression))

    def test_numbers_balanced(self):
        expression = "(7+8)*{3-[5+6]*4}"
        self.assertTrue(stack_balanced_parens.isBalanced(expression))

if __name__ == "__main__":
    unittest.main()
