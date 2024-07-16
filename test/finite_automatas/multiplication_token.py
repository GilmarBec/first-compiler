import unittest
from src.finite_automatas.multiplication_token import multiplication_token


class Multiplication_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(multiplication_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(multiplication_token.execute('')) # Arruma isso
