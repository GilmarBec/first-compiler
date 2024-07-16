import unittest
from src.finite_automatas.open_braces_token import open_braces_token


class Open_braces_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(open_braces_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(open_braces_token.execute('')) # Arruma isso
