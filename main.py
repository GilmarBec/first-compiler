# python3 main.py 0100

import sys

from src.parser import parse
from src.tokenizator import tokenize


def find_lexical_error_coordinates(position, data):
    line = 1
    column = 1
    clean_index = 0
    print('position', position)

    for char in data:
        if char == '\n':
            line += 1
            column = 0
            continue

        if char == ' ':
            column += 1
            continue

        if char == '\t':
            column += 4
            continue

        if position <= clean_index:
            break

        column += 1
        clean_index += 1
    print(f'Lexical Error on Line {line}, column {column}')
    sys.exit(1)


def execute(args):
    file = open(args[0], 'r')
    data = file.read()
    file.close()

    clean_data = data.replace(' ', '').replace('\n', '').replace('\t', '')

    success, res = tokenize(clean_data)

    if not success:
        find_lexical_error_coordinates(res, data)

    tokens = res

    print('\n'.join([str(x) for x in tokens]), '\n\n')

    try:
        print('\n\nSuccess:', parse(tokens))
    except ValueError:
        print('\n\nFail >:(')


if __name__ == '__main__':
    execute(sys.argv[1:])
