import unittest
from src.finite_automatas.number import number


class Number(unittest.TestCase):
    def test_success(self):
        self.assertTrue(number.execute('0123456789'))
        self.assertTrue(number.execute('-0123456789'))
        self.assertTrue(number.execute('+0123456789'))
        self.assertTrue(number.execute('012345.6789'))
        self.assertTrue(number.execute('-012345.6789'))
        self.assertTrue(number.execute('+012345.6789'))

    def test_failure(self):
        self.assertTrue(number.execute('012345.6789'))
        self.assertTrue(number.execute('012345.6789'))
        self.assertTrue(number.execute('-012345.6789'))
        self.assertTrue(number.execute('+012345.6789'))

    def test_out_of_language_failure(self):
        self.assertFalse(number.execute(''))
        self.assertFalse(number.execute('a'))
        self.assertFalse(number.execute('*'))
        self.assertFalse(number.execute('('))
