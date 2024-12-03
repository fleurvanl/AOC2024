import re

from utils.file_handling import FileHandling


def find_mult(file):
    matches = re.findall(r'mul\(\d+,\d+\)', file)
    sum = 0
    for match in matches:
        digits = re.findall(r'\d+', match)
        sum += int(digits[0]) * int(digits[1])
    return sum


def find_do_mult(file):
    dosum = 0
    # split file in do()'s
    dos = file.split('do()')
    # split subfiles in don't()s
    for do in dos:
        dont = do.split("don't()")
        # now the first part of the file should be processed and the second part shouldnt
        dosum += find_mult(dont[0])
    return dosum


def main():
    file = FileHandling.read_file('input/day03.txt')
    sum = find_mult(file)
    print(f'first star: {sum}')
    dosum = find_do_mult(file)
    print(f'second star: {dosum}')


if __name__ == '__main__':
    main()