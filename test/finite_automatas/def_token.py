import unittest
from src.finite_automatas.def_token import def_token


class Def_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(def_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(def_token.execute('')) # Arruma isso
