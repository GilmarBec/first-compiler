# python3 main.py 0100

import sys

from src.finite_automatas.end_number import end_number

if __name__ == '__main__':
    args = sys.argv[1:]
    print(end_number.execute(args[0]))
