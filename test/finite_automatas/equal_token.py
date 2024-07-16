import unittest
from src.finite_automatas.equal_token import equal_token


class Equal_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(equal_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(equal_token.execute('')) # Arruma isso
