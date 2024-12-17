from collections import defaultdict

from utils.file_handling import FileHandling


def collect_antennae(lines):
    # {letter: [(row, column), (row, column)]}
    antennae = defaultdict(list)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                antennae[char].append((i, j))
    return antennae


def calculate_antinodes(antennae, lines):
    # dict shape: [(row, column), (row, column]
    antinodes = []
    # we look per letter in the antennae dict and compare each entry with the later entries
    for freq in antennae.keys():
        for a, instance in enumerate(antennae[freq]):
            for b, sec_instance in enumerate(antennae[freq]):
                # make sure we don't check aa; make sure we only check ab and not ba;
                if a < b:
                    row_i, column_i = instance
                    row_j, column_j = sec_instance
                    distance_row = abs(row_i - row_j)
                    distance_col = abs(column_i - column_j)
                    if column_i < column_j:
                        antinode_1 = (row_i - distance_row, column_i - distance_col)
                        antinode_2 = (row_j + distance_row, column_j + distance_col)
                    else:
                        antinode_1 = (row_i - distance_row, column_i + distance_col)
                        antinode_2 = (row_j + distance_row, column_j - distance_col)
                    # check for out of bounds
                    if 0 <= antinode_1[0] < len(lines) and 0 <= antinode_1[1] < len(lines[0]):
                        antinodes.append(antinode_1)
                    if 0 <= antinode_2[0] < len(lines) and 0 <= antinode_2[1] < len(lines[0]):
                        antinodes.append(antinode_2)
    return antinodes


def main():
    file = FileHandling.read_file('input/day08.txt')
    lines = file.split('\n')

    # collect antennae
    antennae = collect_antennae(lines)

    # calculate antinodes
    antinodes = calculate_antinodes(antennae, lines)

    if len(set(antinodes)) > 554: #594: #831:
        print('answer too high')
    #428 is also wrong

    print(len(set(antinodes)))


if __name__ == '__main__':
    main()
