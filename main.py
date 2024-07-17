# python3 main.py 0100

import sys

from src.tokenizator import tokenize

if __name__ == '__main__':
    args = sys.argv[1:]

    file = open(args[0], 'r')
    data = file.read()
    file.close()

    clean_data = data.replace(' ', '').replace('\n', '')

    print([str(x) for x in tokenize(clean_data)])
