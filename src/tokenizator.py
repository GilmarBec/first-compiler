from src.finite_automata_translator import finite_automatas_translator
from src.finite_automatas.close_braces_token import close_braces_token


class Token:
    def __init__(self, type_: str, value: str or None):
        self.type = type_
        self.value = value

    def __str__(self):
        return f"{self.type}: {self.value}"


def tokenize(_input: str):
    tokens = []

    while len(_input) > 0:
        current_fa = None
        incomplete_fas = [x for x in finite_automatas_translator]
        buffer = ''
        for char in _input:
            buffer += char
            fa_to_remove = []
            for index, fa in enumerate(incomplete_fas):
                try:
                    if fa[0].execute(buffer):
                        current_fa = fa
                        fa_to_remove.append(index)
                except ValueError:
                    fa_to_remove.append(index)

            fa_to_remove.reverse()
            for index in fa_to_remove:
                del incomplete_fas[index]

            if len(incomplete_fas) == 0:
                break

        if current_fa is None:
            print('None FAs could recognize this input', _input)
            raise ValueError('None FAs could recognize this input')

        buffer = ''
        for index, char in enumerate(_input):
            buffer += char
            try:
                current_fa[0].execute(buffer)
            except ValueError:
                _input = _input[index:]
                buffer = buffer[:-1]
                break

        token = Token(current_fa[1], buffer)
        print('_input', _input, str(token))
        tokens.append(token)

        if buffer == _input:
            _input = ''

    return tokens
