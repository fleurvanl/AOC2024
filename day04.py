import re

from utils.file_handling import FileHandling


def main():
    file = FileHandling.read_file('input/day04.txt')
    lines = file.split('\n')
    num_xmas = 0
    # find left to right
    for i, line in enumerate(lines):
        left_to_right = len(re.findall(r'XMAS', line))
        num_xmas += left_to_right
        # find right to left
        line = ''.join(list(reversed([i for i in line])))
        right_to_left = len(re.findall(r'XMAS', line))
        num_xmas += right_to_left
        # look down
        # make sure we avoid index errors as we are going to look in 4 lines under the current line
        if i + 3 < len(lines):
            for j, letter in enumerate(line):
                if letter == 'X':
                    if lines[i+1][j] == 'M':
                        if lines[i+2][j] == 'A':
                            if lines[i+3][j] == 'S':
                                num_xmas += 1
        # look up
        # make sure we avoid index errors as we are going to look in 4 lines above the current line
        if i - 3 > 0:
            for j, letter in enumerate(line):
                if letter == 'X':
                    if lines[i-1][j] == 'M':
                        if lines[i-2][j] == 'A':
                            if lines[i-3][j] == 'S':
                                num_xmas += 1
        # look diagonally
        # oh fuck
    print(num_xmas)


if __name__ == '__main__':
    main()
