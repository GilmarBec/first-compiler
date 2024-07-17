from src.finite_automatas.close_braces_token import close_braces_token
from src.finite_automatas.close_parentheses_token import close_parentheses_token
from src.finite_automatas.comma_token import comma_token
from src.finite_automatas.def_token import def_token
from src.finite_automatas.equal_equal_token import equal_equal_token
from src.finite_automatas.equal_token import equal_token
from src.finite_automatas.greater_token import greater_token
from src.finite_automatas.id_open_parentheses_token import id_open_parentheses_token
from src.finite_automatas.id_token import id_token
from src.finite_automatas.if_token import if_token
from src.finite_automatas.int_token import int_token
from src.finite_automatas.less_token import less_token
from src.finite_automatas.minus_token import minus_token
from src.finite_automatas.multiplication_token import multiplication_token
from src.finite_automatas.number_token import number_token
from src.finite_automatas.open_braces_token import open_braces_token
from src.finite_automatas.open_parentheses_token import open_parentheses_token
from src.finite_automatas.plus_token import plus_token
from src.finite_automatas.print_token import print_token
from src.finite_automatas.return_token import return_token
from src.finite_automatas.semicolon_token import semicolon_token

finite_automatas_translator = [
    (close_braces_token, 'CLOSE_BRACES_TOKEN'),
    (close_parentheses_token, 'CLOSE_PARENTHESES_TOKEN'),
    (comma_token, 'COMMA_TOKEN'),
    (def_token, 'DEF_TOKEN'),
    (equal_equal_token, 'EQUAL_EQUAL_TOKEN'),
    (equal_token, 'EQUAL_TOKEN'),
    (greater_token, 'GREATER_TOKEN'),
    (id_open_parentheses_token, 'ID_OPEN_PARENTHESES_TOKEN'),
    (id_token, 'ID_TOKEN'),
    (if_token, 'IF_TOKEN'),
    (int_token, 'INT_TOKEN'),
    (less_token, 'LESS_TOKEN'),
    (minus_token, 'MINUS_TOKEN'),
    (multiplication_token, 'MULTIPLICATION_TOKEN'),
    (number_token, 'NUMBER_TOKEN'),
    (open_braces_token, 'OPEN_BRACES_TOKEN'),
    (open_parentheses_token, 'OPEN_PARENTHESES_TOKEN'),
    (plus_token, 'PLUS_TOKEN'),
    (print_token, 'PRINT_TOKEN'),
    (return_token, 'RETURN_TOKEN'),
    (semicolon_token, 'SEMICOLON_TOKEN'),
]
