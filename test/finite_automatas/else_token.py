import unittest
from src.finite_automatas.else_token import else_token


class Else_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(else_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(else_token.execute('')) # Arruma isso
