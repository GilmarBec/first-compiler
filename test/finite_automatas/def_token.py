import unittest
from src.finite_automatas.def_token import def_token


class Def_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(def_token.execute('def'))

    def test_incomplete(self):
        self.assertFalse(def_token.execute('d'))
        self.assertFalse(def_token.execute('de'))

    def test_failure(self):
        try:
            def_token.execute('}')
        except ValueError:
            self.assertTrue(True)

        try:
            def_token.execute('dee')
        except ValueError:
            self.assertTrue(True)

        try:
            def_token.execute('deff')
        except ValueError:
            self.assertTrue(True)
