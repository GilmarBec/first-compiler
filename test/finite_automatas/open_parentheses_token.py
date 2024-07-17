import unittest
from src.finite_automatas.open_parentheses_token import open_parentheses_token


class Open_parentheses_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(open_parentheses_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(open_parentheses_token.execute('')) # Arruma isso
