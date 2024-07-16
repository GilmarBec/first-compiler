import unittest
from src.finite_automatas.print_token import print_token


class Print_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(print_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(print_token.execute('')) # Arruma isso
