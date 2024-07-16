import unittest
from src.finite_automatas.if_token import if_token


class If_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(if_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(if_token.execute('')) # Arruma isso
