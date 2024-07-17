from src.finite_automatas.close_braces_token import close_braces_token
from src.finite_automatas.close_parentheses_token import close_parentheses_token
from src.finite_automatas.id_open_parentheses import id_open_parentheses
from src.finite_automatas.id_token import id_token

finite_automatas_translator = [
    (close_braces_token, 'CLOSE_BRACES_TOKEN'),
    (close_parentheses_token, 'CLOSE_PARENTHESES_TOKEN'),
    (id_token, 'ID_TOKEN'),
    (id_open_parentheses, 'ID_OPEN_PARENTHESES_TOKEN'),
]
