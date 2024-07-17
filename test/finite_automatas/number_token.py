import unittest
from src.finite_automatas.number_token import number_token


class Number_token(unittest.TestCase):
    def test_success(self):
        self.assertTrue(number_token.execute('0123546789'))
        self.assertTrue(number_token.execute('+0123546789'))
        self.assertTrue(number_token.execute('-0123546789'))
        self.assertTrue(number_token.execute('0123546789.0123456'))
        self.assertTrue(number_token.execute('+0123546789.0123456'))
        self.assertTrue(number_token.execute('-0123546789.0123456'))

    def test_incomplete(self):
        self.assertFalse(number_token.execute('+'))
        self.assertFalse(number_token.execute('-'))
        self.assertFalse(number_token.execute('0123546789.'))
        self.assertFalse(number_token.execute('+0123546789.'))
        self.assertFalse(number_token.execute('-0123546789.'))

    def test_failure(self):
        try:
            number_token.execute('queijo')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('*123154')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('.')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('+.')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('-.')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('216354-')
        except ValueError:
            self.assertTrue(True)

        try:
            number_token.execute('216354.-')
        except ValueError:
            self.assertTrue(True)
