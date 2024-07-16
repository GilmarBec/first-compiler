import unittest
from src.finite_automatas.return_token import return_token


class Return_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(return_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(return_token.execute('')) # Arruma isso
