import os
import pathlib


def p1(lines, right, down):
    res = 0
    index_r = 0
    index_d = 0
    limit = len(lines[0]) - (right + 1)

    for line in lines:
        if index_d % down == 0:
            if line[index_r] == '#':
                res += 1

            if index_r >= limit:
                index_r -= limit
            else:
                index_r += right

        index_d += 1

    return res


def p2(lines):
    return p1(lines, 1, 1) * p1(lines, 3, 1) * p1(lines, 5, 1) * p1(lines, 7, 1) * p1(lines, 1, 2)


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    lines = inp_file.readlines()
    print(p1(lines, 3, 1))
    print(p2(lines))


if __name__ == "__main__":
    main()
