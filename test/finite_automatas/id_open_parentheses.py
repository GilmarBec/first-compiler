import unittest
from src.finite_automatas.id_open_parentheses import id_open_parentheses


class Id_open_parentheses(unittest.TestCase):
    def test_success(self):
        self.assertTrue(id_open_parentheses.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(id_open_parentheses.execute('')) # Arruma isso
