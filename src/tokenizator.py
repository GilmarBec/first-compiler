from src.finite_automata_translator import finite_automatas_translator
from src.finite_automatas.close_braces_token import close_braces_token


class Token:
    def __init__(self, type_: str, value: str or None):
        self.type = type_
        self.value = value

class Tokenizer:
    def tokenize(self, _input: str):

        current_token = None
        buffer = ''
        for char in _input:
            buffer += char
            for fa in finite_automatas_translator:
                if fa[0].execute(buffer):
                    current_token = fa[1]
