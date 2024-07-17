import unittest
from src.finite_automatas.id_open_parentheses_token import id_open_parentheses_token


class Id_open_parentheses_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(id_open_parentheses_token.execute('asd('))
        self.assertTrue(id_open_parentheses_token.execute('a12e3sd('))
        self.assertTrue(id_open_parentheses_token.execute('_a12A3sd('))
        self.assertTrue(id_open_parentheses_token.execute('_('))
        self.assertTrue(id_open_parentheses_token.execute('RA3asd('))

    def test_incomplete(self):
        self.assertFalse(id_open_parentheses_token.execute('asd'))
        self.assertFalse(id_open_parentheses_token.execute('dsauq_wkAjb9AS38sdaf4y'))

    def test_failure(self):
        try:
            id_open_parentheses_token.execute('asd)')
        except ValueError:
            self.assertTrue(True)

        try:
            id_open_parentheses_token.execute('1asd')
        except ValueError:
            self.assertTrue(True)

        try:
            id_open_parentheses_token.execute('%')
        except ValueError:
            self.assertTrue(True)

        try:
            id_open_parentheses_token.execute('(')
        except ValueError:
            self.assertTrue(True)
