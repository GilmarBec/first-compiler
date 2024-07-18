# python3 main.py 0100

import sys

from src.parser import parse
from src.tokenizator import tokenize

if __name__ == '__main__':
    args = sys.argv[1:]

    file = open(args[0], 'r')
    data = file.read()
    file.close()

    clean_data = data.replace(' ', '').replace('\n', '')

    tokens = tokenize(clean_data)

    print('\n'.join([str(x) for x in tokens]))
    print('\n\n')

    try:
        print('Success:', parse(tokens))
    except ValueError:
        print('Faio >:(')
