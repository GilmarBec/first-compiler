# python3 main.py 0100

import sys

from src.finite_automatas.digits import digits

if __name__ == '__main__':
    args = sys.argv[1:]
    print(digits.execute(args[0]))
