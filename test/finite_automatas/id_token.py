import unittest
from src.finite_automatas.id_token import id_token


class Id_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(id_token.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(id_token.execute('')) # Arruma isso
