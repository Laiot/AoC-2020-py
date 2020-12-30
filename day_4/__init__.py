import os
import pathlib


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    id_list = inp_file.read().split("\n\n")


if __name__ == "__main__":
    main()
