import unittest
from src.finite_automatas.open_parentheses import open_parentheses


class Open_parentheses(unittest.TestCase):
    def test_success(self):
        self.assertTrue(open_parentheses.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(open_parentheses.execute('')) # Arruma isso
