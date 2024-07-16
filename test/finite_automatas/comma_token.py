import unittest
from src.finite_automatas.comma_token import comma_token


class Comma_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(comma_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(comma_token.execute('')) # Arruma isso
