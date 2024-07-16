import unittest
from src.finite_automatas.close_braces_token import close_braces_token


class Close_braces_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(close_braces_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(close_braces_token.execute('')) # Arruma isso
