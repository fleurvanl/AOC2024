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
    # returns row, column, obstacle, new_spot
    # runs off the map
    if row == 0:
        return 9999, 9999, False, False
    # above is free
    elif lines[row - 1][column] == '.':
        return row - 1, column, False, True
    # above is free but we have been there before
    elif lines[row - 1][column] == 'X':
        return row - 1, column, False, False
    # above is obstacle
    else:
        return row, column, True, False


def move_right_check(lines, row, column):
    # returns row, column, obstacle, new_spot
    # runs off the map
    if column == len(lines[0]):
        return 9999, 9999, False, False
    # right is free
    elif lines[row][column + 1] == '.':
        return row, column + 1, False, True
    # right is free but we have been there before
    elif lines[row][column + 1] == 'X':
        return row, column + 1, False, False
    # right is obstacle
    else:
        return row, column, True, False


def move_down_check(lines, row, column):
    # returns row, column, obstacle, new_spot
    # account for new line at the end of the file
    # runs off the map
    if row == len(lines) - 2:
        return 9999, 9999, False, False
    # below is free
    elif lines[row + 1][column] == '.':
        return row + 1, column, False, True
    # below is free but we have been there before
    elif lines[row + 1][column] == 'X':
        return row + 1, column, False, False
    # below is obstacle
    else:
        return row, column, True, False


def move_left_check(lines, row, column):
    # returns row, column, obstacle, new_spot
    # runs off the map
    if column == 0:
        return 9999, 9999, False, False
    # left is free
    elif lines[row][column - 1] == '.':
        return row, column - 1, False, True
    # left is free but we have been there before
    elif lines[row][column - 1] == 'X':
        return row, column - 1, False, False
    # left is obstacle
    else:
        return row, column, True, False


def main():
    file = FileHandling.read_file('input/day06.txt')
    lines = file.split('\n')

    visited = 0

    # find current position ^
    row, column = find_current_position(lines)

    # write functions for up, down. left and right
    moves = [move_right_check,
             move_down_check,
             move_left_check,
             move_up_check]
    current_move = move_up_check

    # while we don't run off the map
    while row != 9999:
        # move in the desired direction; nno movement is made if we met an obstacle
        row, column, obstacle, new_spot = current_move(lines, row, column)
        # if we find an obstacle, we change the direction we move in; we do not move
        if obstacle:
            current_move = change_move(moves, current_move)
        # as long as we don't meet an obstacle, we're moving
        if new_spot:
            visited += 1

    print(f'first star: {visited}')


if __name__ == '__main__':
    main()
