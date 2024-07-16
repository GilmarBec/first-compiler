import unittest
from src.finite_automatas.greater_token import greater_token


class Greater_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(greater_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(greater_token.execute('')) # Arruma isso
