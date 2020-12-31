import os
import pathlib
import itertools
from functools import reduce
import operator


def calc_id(seat_code):
    row = list(range(128))
    col = list(range(8))
    for i in seat_code:
        if i == 'F':
            row = row[:len(row) // 2]
        elif i == 'B':
            row = row[len(row) // 2:]
        elif i == 'L':
            col = col[:len(col) // 2]
        elif i == 'R':
            col = col[len(col) // 2:]
    return (row[0] * 8) + col[0]


def p1(lines):
    res = 0
    for line in lines:
        line = line.rstrip()
        res = max(res, calc_id(line))
    return res


def p2(lines):
    ids = []
    for line in lines:
        line = line.rstrip()
        ids.append(calc_id(line))

    for numbers in itertools.combinations(ids, 2):
        if reduce(operator.sub, numbers) == 2 and numbers[1] + 1 not in ids:
            return numbers[1] + 1


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    lines = inp_file.readlines()
    print(p1(lines))
    print(p2(lines))


if __name__ == "__main__":
    main()
