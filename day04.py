import re

from utils.file_handling import FileHandling


def look_left_right(line):
    num_xmas = 0
    # find left to right
    left_to_right = len(re.findall(r'XMAS', line))
    num_xmas += left_to_right
    # find right to left
    line = ''.join(list(reversed([i for i in line])))
    right_to_left = len(re.findall(r'XMAS', line))
    num_xmas += right_to_left
    return num_xmas


def look_down(i, line, lines):
    num_xmas = 0
    # make sure we avoid index errors as we are going to look in 4 lines under the current line
    if i + 3 < len(lines):
        for j, letter in enumerate(line):
            if letter == 'X':
                if lines[i + 1][j] == 'M':
                    if lines[i + 2][j] == 'A':
                        if lines[i + 3][j] == 'S':
                            num_xmas += 1
    return num_xmas


def look_up(i, line, lines):
    num_xmas = 0
    # make sure we avoid index errors as we are going to look in 4 lines above the current line
    if i - 3 >= 0:
        for j, letter in enumerate(line):
            if letter == 'X':
                if lines[i-1][j] == 'M':
                    if lines[i-2][j] == 'A':
                        if lines[i-3][j] == 'S':
                            num_xmas += 1
    return num_xmas


def look_diagonally(i, line, lines):
    num_xmas = 0
    # look down to the right
    if i + 3 < len(lines):
        for j, letter in enumerate(line):
            if j + 3 < len(line):
                if letter == 'X':
                    if lines[i + 1][j + 1] == 'M':
                        if lines[i + 2][j + 2] == 'A':
                            if lines[i + 3][j + 3] == 'S':
                                num_xmas += 1
    # look down to the left
    if i + 3 < len(lines):
        for j, letter in enumerate(line):
            if j - 3 >= 0:
                if letter == 'X':
                    if lines[i + 1][j - 1] == 'M':
                        if lines[i + 2][j - 2] == 'A':
                            if lines[i + 3][j - 3] == 'S':
                                num_xmas += 1
    # look up to the right
    if i - 3 >= 0:
        for j, letter in enumerate(line):
            if j + 3 < len(line):
                if letter == 'X':
                    if lines[i - 1][j + 1] == 'M':
                        if lines[i - 2][j + 2] == 'A':
                            if lines[i - 3][j + 3] == 'S':
                                num_xmas += 1
    # look up to the left
    if i - 3 >= 0:
        for j, letter in enumerate(line):
            if j - 3 >= 0:
                if letter == 'X':
                    if lines[i - 1][j - 1] == 'M':
                        if lines[i - 2][j - 2] == 'A':
                            if lines[i - 3][j - 3] == 'S':
                                num_xmas += 1
    return num_xmas


def find_x_mas(i, line, lines):
    num_x_mas = 0
    if i + 2 < len(lines):
        for j, letter in enumerate(line):
            if j + 2 < len(line):
                # find MAS
                if letter == 'M':
                    # find M . M
                    #      . A .
                    #      S . S
                    if line[j+2] == 'M':
                        if lines[i + 1][j + 1] == 'A' and lines[i + 2][j] == 'S' and lines[i + 2][j + 2] == 'S':
                            num_x_mas += 1
                    # find M . S
                    #      . A .
                    #      M . S
                    if line[j+2] == 'S':
                        if lines[i + 1][j + 1] == 'A' and lines[i + 2][j] == 'M' and lines[i + 2][j + 2] == 'S':
                            num_x_mas += 1

                # find SAM
                elif letter == 'S':
                    # find S . M
                    #      . A .
                    #      S . M
                    if line[j + 2] == 'M':
                        if lines[i + 1][j + 1] == 'A' and lines[i + 2][j] == 'S' and lines[i + 2][j + 2] == 'M':
                            num_x_mas += 1
                    # find S . S
                    #      . A .
                    #      M . M
                    if line[j + 2] == 'S':
                        if lines[i + 1][j + 1] == 'A' and lines[i + 2][j] == 'M' and lines[i + 2][j + 2] == 'M':
                            num_x_mas += 1
    return num_x_mas


def main():
    file = FileHandling.read_file('input/day04.txt')
    lines = file.split('\n')
    num_xmas = 0
    num_x_mas = 0
    for i, line in enumerate(lines):
        # look left to right and right to left
        num_xmas += look_left_right(line)
        # look down
        num_xmas += look_down(i, line, lines)
        # look up
        num_xmas += look_up(i, line, lines)
        # look diagonally
        num_xmas += look_diagonally(i, line, lines)
        # find x-mas
        num_x_mas += find_x_mas(i, line, lines)
    print(f'first star: {num_xmas}')
    print(f'second star: {num_x_mas}')


if __name__ == '__main__':
    main()
