import unittest
from src.finite_automatas.semicolon_token import semicolon_token


class Semicolon_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(semicolon_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(semicolon_token.execute('')) # Arruma isso
