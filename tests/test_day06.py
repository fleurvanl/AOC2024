import pytest

from day06 import find_current_position, move_up_check, move_right_check, move_down_check, move_left_check, change_move


@pytest.fixture
def lines():
    return ['....#.....',
            '......X..#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...',
            '']


def test_find_current_position(lines):
    assert find_current_position(lines) == (6, 4)


def test_move_up_check(lines):
    # returns row, column, obstacle, new_spot
    # runs into obstacle
    assert move_up_check(lines, 1, 4) == (1, 4, True, False)
    # runs off the map
    assert move_up_check(lines, 0, 1) == (9999, 9999, False, False)


def test_move_right_check(lines):
    # returns row, column, obstacle, new_spot
    # runs into obstacle
    assert move_right_check(lines, 1, 8) == (1, 8, True, False)
    # runs into X
    assert move_right_check(lines, 1, 5) == (1, 6, False, False)
    # runs off the map
    assert move_right_check(lines, 0, 10) == (9999, 9999, False, False)


def test_move_down_check(lines):
    # returns row, column, obstacle, new_spot
    # moves to the next row
    assert move_down_check(lines, 1, 8) == (2, 8, False, True)
    # runs off the map
    assert move_down_check(lines, 9, 10) == (9999, 9999, False, False)


def test_move_left_check(lines):
    # returns row, column, obstacle, new_spot
    # moves to the left
    assert move_left_check(lines, 6, 8) == (6, 7, False, True)
    # runs off the map
    assert move_left_check(lines, 0, 0) == (9999, 9999, False, False)


def test_flow(lines):
    visited = 0

    # find current position ^
    row, column = find_current_position(lines)

    # write functions for up, down. left and right
    moves = [move_right_check,
             move_down_check,
             move_left_check,
             move_up_check]
    current_move = move_up_check

    counter = 0

    # while we don't run off the map
    while row != 9999:
        counter += 1
        # move in the desired direction; nno movement is made if we met an obstacle
        row, column, obstacle, new_spot = current_move(lines, row, column)
        # if we find an obstacle, we change the direction we move in; we do not move
        if obstacle:
            current_move = change_move(moves, current_move)
        # as long as we don't meet an obstacle, we're moving
        if new_spot:
            visited += 1
        if counter > 100:
            break
    assert visited == 41