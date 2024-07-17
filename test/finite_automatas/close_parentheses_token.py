import unittest
from src.finite_automatas.close_parentheses_token import close_parentheses_token


class Close_parentheses_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(close_parentheses_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(close_parentheses_token.execute('')) # Arruma isso
