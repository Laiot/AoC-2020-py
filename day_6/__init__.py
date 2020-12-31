import os
import pathlib


def p1(groups):
    res = 0
    for group in groups:
        group = ''.join([line.strip() for line in group.rstrip()])
        res += len(set(group))
    return res


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    groups = inp_file.read().split("\n\n")
    print(p1(groups))


if __name__ == "__main__":
    main()
