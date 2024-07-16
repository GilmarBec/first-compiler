import unittest
from src.finite_automatas.minus_token import minus_token


class Minus_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(minus_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(minus_token.execute('')) # Arruma isso
