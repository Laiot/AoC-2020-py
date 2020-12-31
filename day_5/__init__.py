import os
import pathlib


def p1(lines):
    res = 0
    for line in lines:
        line = line.rstrip()
        row = list(range(128))
        col = list(range(8))
        for i in line:
            if i == 'F':
                row = row[:len(row) // 2]
            elif i == 'B':
                row = row[len(row) // 2:]
            elif i == 'L':
                col = col[:len(col) // 2]
            elif i == 'R':
                col = col[len(col) // 2:]
        new_res = (row[0] * 8) + col[0]
        res = max(res, new_res)
    return res


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    lines = inp_file.readlines()
    print(p1(lines))


if __name__ == "__main__":
    main()
