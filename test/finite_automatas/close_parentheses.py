import unittest
from src.finite_automatas.close_parentheses import close_parentheses


class Close_parentheses(unittest.TestCase):
    def test_success(self):
        self.assertTrue(close_parentheses.execute('&$*#%&')) # Arruma isso

    def test_failure(self):
        self.assertFalse(close_parentheses.execute('')) # Arruma isso
