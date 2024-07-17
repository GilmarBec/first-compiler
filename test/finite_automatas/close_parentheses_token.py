import unittest
from src.finite_automatas.close_parentheses_token import close_parentheses_token


class Close_parentheses_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(close_parentheses_token.execute(')'))

    def test_failure(self):
        try:
            close_parentheses_token.execute('))')
        except ValueError:
            self.assertTrue(True)
