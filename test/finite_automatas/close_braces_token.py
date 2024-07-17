import unittest
from src.finite_automatas.close_braces_token import close_braces_token


class Close_braces_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(close_braces_token.execute('}'))

    def test_failure(self):
        try:
            close_braces_token.execute('}}')
        except ValueError:
            self.assertTrue(True)
