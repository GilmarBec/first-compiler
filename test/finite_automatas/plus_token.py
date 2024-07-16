import unittest
from src.finite_automatas.plus_token import plus_token


class Plus_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(plus_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(plus_token.execute('')) # Arruma isso
