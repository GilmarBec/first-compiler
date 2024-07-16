import unittest
from src.finite_automatas.int_token import int_token


class Int_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(int_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(int_token.execute('')) # Arruma isso
