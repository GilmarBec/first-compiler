import unittest
from src.finite_automatas.less_token import less_token


class Less_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(less_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(less_token.execute('')) # Arruma isso
