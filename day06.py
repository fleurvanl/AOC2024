from utils.file_handling import FileHandling


def find_current_position(lines):
    for i, line in enumerate(lines):
        if '^' in line:
            row = i
            column = line.index('^')
    return row, column


def change_move(moves, current_move):
    current_index = moves.index(current_move)
    if current_index != len(moves) - 1:
        return moves[current_index + 1]
    else:
        return moves[0]


def move_up_check(lines, row, column):
    # returns row, column, obstacle
    # runs off the map
    if row == 0:
        return 9999, 9999, False
    # above is free
    elif lines[row - 1][column] == '.':
        return row - 1, column, False
    # above is free but we have been there before
    elif lines[row - 1][column] == 'X':
        return row - 1, column, False
    # above is obstacle
    else:
        return row, column, True


def move_right_check(lines, row, column):
    # returns row, column, obstacle
    # runs off the map
    if column == len(lines[row]) - 1:
        return 9999, 9999, False
    # right is free
    elif lines[row][column + 1] == '.':
        return row, column + 1, False
    # right is free but we have been there before
    elif lines[row][column + 1] == 'X':
        return row, column + 1, False
    # right is obstacle
    else:
        return row, column, True


def move_down_check(lines, row, column):
    # returns row, column, obstacle
    # account for new line at the end of the file
    # runs off the map
    if row == len(lines) - 2:
        return 9999, 9999, False
    # below is free
    elif lines[row + 1][column] == '.':
        return row + 1, column, False
    # below is free but we have been there before
    elif lines[row + 1][column] == 'X':
        return row + 1, column, False
    # below is obstacle
    else:
        return row, column, True


def move_left_check(lines, row, column):
    # returns row, column, obstacle
    # runs off the map
    if column == 0:
        return 9999, 9999, False
    # left is free
    elif lines[row][column - 1] == '.':
        return row, column - 1, False
    # left is free but we have been there before
    elif lines[row][column - 1] == 'X':
        return row, column - 1, False
    # left is obstacle
    else:
        return row, column, True


def walk(lines, row, column, moves, current_move):
    print('NEW WALK')
    count = 0
    # while we don't run off the map
    while row != 9999:
        count += 1
        # move in the desired direction; nno movement is made if we met an obstacle
        row, column, obstacle = current_move(lines, row, column)
        # mark current spot with X to note where we've been; check in place in case we just ran off the map
        if row != 9999:
            lines[row] = lines[row][:column] + 'X' + lines[row][column + 1:]
        # if we find an obstacle, we change the direction we move in; we do not move
        if obstacle:
            current_move = change_move(moves, current_move)
        # if infinite looping, return True to indicate that we are infinite looping (second star solution)
        if count > 10000:
            print('count over 10.000')
            return lines, True
    print(count)
    # return lines, False, to indicate that we walked off the map and there's no infinite looping (second star solution)
    return lines, False



def main():
    file = FileHandling.read_file('input/day06.txt')
    lines = file.split('\n')

    visited = 0

    # find current position ^
    initial_row, initial_column = find_current_position(lines)
    # replace '^' with 'X'
    s1_lines = lines.copy()
    s1_lines[initial_row] = s1_lines[initial_row][:initial_column] + 'X' + s1_lines[initial_row][initial_column + 1:]

    # write functions for up, down. left and right
    moves = [move_right_check,
             move_down_check,
             move_left_check,
             move_up_check]
    current_move = move_up_check

    s1_lines, _ = walk(s1_lines, initial_row, initial_column, moves, current_move)

    # count Xs
    for line in s1_lines:
        visited += line.count('X')

    print(f'first star: {visited}')

    num_obstructions = 0
    for i, line in enumerate(s1_lines):
        for j in range(len(line)):
            # speed up the process by only placing obstacles in places where the guard would have walked according to
            # the first part of the exercise
            if line[j] == 'X':
                adjusted_lines = lines.copy()
                # insert obstacle in object
                adjusted_lines[i] = adjusted_lines[i][:j] + '#' + adjusted_lines[i][j + 1:]
                _ , infinite = walk(adjusted_lines, initial_row, initial_column, moves, current_move)
                if infinite:
                    num_obstructions += 1

    print(f'second star: {num_obstructions}') # 1435 too low
    # obstacle cannot be put in guards starting location --> but that should make our solution lower if anything
    #


if __name__ == '__main__':
    main()
