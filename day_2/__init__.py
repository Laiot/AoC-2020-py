import os
import pathlib


def p1(lines):
    res = 0

    for line in lines:
        line_ar = line.split(" ")
        f_arg, s_arg = line_ar[0].split("-")
        to_check = line_ar[1][:-1]
        psw = line_ar[2]
        count = 0

        for c in psw:
            if c == to_check:
                count += 1

        if int(f_arg) <= count <= int(s_arg):
            res += 1

    return res


def p2(lines):
    res = 0

    for line in lines:
        line_ar = line.split(" ")
        f_arg, s_arg = line_ar[0].split("-")
        to_check = line_ar[1][:-1]
        psw = line_ar[2]

        f_check = psw[int(f_arg) - 1] == to_check and psw[int(s_arg) - 1] != to_check
        s_check = psw[int(s_arg) - 1] == to_check and psw[int(f_arg) - 1] != to_check

        if f_check or s_check:
            res += 1

    return res


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    lines = inp_file.readlines()
    print(p1(lines))
    print(p2(lines))


if __name__ == "__main__":
    main()
