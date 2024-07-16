import unittest
from src.finite_automatas.equal_equal_token import equal_equal_token


class Equal_equal_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(equal_equal_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(equal_equal_token.execute('')) # Arruma isso
