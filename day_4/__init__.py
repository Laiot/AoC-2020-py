import os
import pathlib
import re


def check_field_existence(idd):
    if 'byr' in idd and 'iyr' in idd and 'eyr' in idd and 'hgt' in idd and 'hcl' in idd and 'ecl' in idd and \
            'pid' in idd:
        return True


def p1(id_list):
    res = 0
    for idd in id_list:
        if check_field_existence(idd):
            res += 1
    return res


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    filename = os.path.join(directory, 'inp.txt')

    inp_file = open(filename, 'r')
    id_list = inp_file.read().split("\n\n")

    print(p1(id_list))

    res = 0
    for idd in id_list:
        check = 0
        if check_field_existence(idd):
            fields = re.split(' |\n', idd)
            for field in fields:
                key, value = field.split(":")
                if key == "byr" and 1920 <= int(value) <= 2002:
                    check += 1
                elif key == "iyr" and 2010 <= int(value) <= 2020:
                    check += 1
                elif key == "eyr" and 2020 <= int(value) <= 2030:
                    check += 1
                elif key == "hgt":
                    num = value[:-2]
                    if "cm" in value and 150 <= int(num) <= 193:
                        check += 1
                    elif "in" in value and 59 <= int(num) <= 76:
                        check += 1
                elif key == "hcl":
                    if re.match('#[0-9a-f]*', value) and len(value) == 7:
                        check += 1
                elif key == "ecl":
                    if 'amb' in value or 'blu' in value or 'brn' in value or 'gry' in value or 'grn' in value or 'hzl' in value or 'oth' in value:
                        check += 1
                elif key == "pid" and len(value) == 9 and value.isdigit():
                    check += 1
        if check >= 7:
            res += 1

    print(res)


if __name__ == "__main__":
    main()
