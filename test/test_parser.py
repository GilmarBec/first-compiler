import unittest

from src.parser import parse
from src.tokenizator import Token


class ParserTest(unittest.TestCase):
    def test_success_def(self):
        self.assertTrue(parse(build_def([
            Token('RETURN_TOKEN', 'return'),
            Token('SEMICOLON_TOKEN', ';'),
        ], [
            Token('INT_TOKEN', 'int'),
            Token('ID_TOKEN', 'is_valid'),
            Token('COMMA_TOKEN', ','),
            Token('INT_TOKEN', 'int'),
            Token('ID_TOKEN', 'magic_number'),
            Token('COMMA_TOKEN', ','),
        ]) + build_def([
            Token('RETURN_TOKEN', 'return'),
            Token('SEMICOLON_TOKEN', ';'),
        ])))

        self.assertTrue(parse(build_def([
            Token('RETURN_TOKEN', 'return'),
            Token('SEMICOLON_TOKEN', ';'),
        ], [
            Token('INT_TOKEN', 'int'),
            Token('ID_TOKEN', 'is_valid'),
        ])))

    # test ['if', 'else', '*', '+', 'def', '<', 'number', '=', 'id', ';', '(', ')', '{', '}']
    def test_success_if_else(self):
        self.assertTrue(parse(build_def(build_if(
            [
                Token('NUMBER_TOKEN', '3'),
                Token('LESS_TOKEN', '<'),
                Token('NUMBER_TOKEN', '42.5'),
            ],
            build_if([Token('ID_TOKEN', 'is_valid')], [
                Token('ID_TOKEN', 'magic_number'),
                Token('EQUAL_TOKEN', '='),
                Token('NUMBER_TOKEN', '45'),
                Token('SEMICOLON_TOKEN', ';'),
            ], [
                Token('ID_TOKEN', 'magic_number'),
                Token('EQUAL_TOKEN', '='),
                Token('NUMBER_TOKEN', '45'),
                Token('PLUS_TOKEN', '+'),
                Token('NUMBER_TOKEN', '22'),
                Token('MULTIPLICATION_TOKEN', '*'),
                Token('NUMBER_TOKEN', '5'),
                Token('SEMICOLON_TOKEN', ';'),
            ])
        ))))

    def test_success_empty(self):
        self.assertTrue(parse([]))

    def test_success_outside_def(self):
        self.assertTrue(parse([
            Token('ID_TOKEN', 'magic_number'),
            Token('EQUAL_TOKEN', '='),
            Token('OPEN_PARENTHESES_TOKEN', '('),
            Token('NUMBER_TOKEN', '2'),
            Token('PLUS_TOKEN', '+'),
            Token('NUMBER_TOKEN', '2'),
            Token('CLOSE_PARENTHESES_TOKEN', ')'),
            Token('MULTIPLICATION_TOKEN', '*'),
            Token('NUMBER_TOKEN', '3'),
            Token('GREATER_TOKEN', '>'),
            Token('NUMBER_TOKEN', '14'),
            Token('SEMICOLON_TOKEN', ';'),
        ]))
        self.assertTrue(parse([
            Token('ID_TOKEN', 'magic_number2'),
            Token('EQUAL_TOKEN', '='),
            Token('NUMBER_TOKEN', '2'),
            Token('GREATER_TOKEN', '=='),
            Token('NUMBER_TOKEN', '14'),
            Token('SEMICOLON_TOKEN', ';'),
        ]))

        self.assertTrue(parse([
            Token('PRINT_TOKEN', 'print'),
            Token('OPEN_PARENTHESES_TOKEN', '('),
            Token('NUMBER_TOKEN', '2'),
            Token('CLOSE_PARENTHESES_TOKEN', ')'),
            Token('SEMICOLON_TOKEN', ';'),
        ]))


def build_def(stmtlist, parlist=None):
    if parlist is None:
        parlist = []

    return [
        Token('DEF_TOKEN', 'def'),
        Token('ID_OPEN_PARENTHESES_TOKEN', 'test('),
    ] + parlist + [
        Token('CLOSE_PARENTHESES_TOKEN', ')'),
        Token('OPEN_BRACES_TOKEN', '{'),
    ] + stmtlist + [
        Token('CLOSE_BRACES_TOKEN', '}'),
    ]


def build_if(expr, stmt1, stmt2=None):
    res = [
        Token('IF_TOKEN', 'if'),
        Token('OPEN_PARENTHESES_TOKEN', '('),
    ] + expr + [
        Token('CLOSE_PARENTHESES_TOKEN', ')'),
    ] + stmt1

    if stmt2 is None:
        return res

    return res + [
        Token('ELSE_TOKEN', 'else'),
    ] + stmt2
