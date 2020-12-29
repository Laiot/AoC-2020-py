import os
import pathlib


def p1(lines):
    for a in lines:
        for b in lines:
            a_n = int(a)
            b_n = int(b)
            if a_n != b_n and a_n + b_n == 2020:
                return a_n * b_n


def p2(lines):
    for a in lines:
        for b in lines:
            for c in lines:
                a_n = int(a)
                b_n = int(b)
                c_n = int(c)
                if a_n != b_n and a_n != c_n and b_n != c_n and a_n + b_n + c_n == 2020:
                    return a_n * b_n * c_n


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    lines = inp_file.readlines()
    print(p1(lines))
    print(p2(lines))


if __name__ == "__main__":
    main()
