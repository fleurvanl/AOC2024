import pytest

from day06 import (find_current_position,
                   move_up_check,
                   move_right_check,
                   move_down_check,
                   move_left_check,
                   change_move,
                   walk)


@pytest.fixture
def lines():
    return ['....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...',
            '']


@pytest.fixture
def find_x():
    return ['.....X.....']


@pytest.fixture
def infinite():
    return ['....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#.#^.....',
            '........#.',
            '#.........',
            '......#...',
            '']


@pytest.fixture
def run_off_map_right():
    return ['....#.....',
            '..........',
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
    assert move_up_check(lines, 1, 4) == (1, 4, True)
    # runs off the map
    assert move_up_check(lines, 0, 1) == (9999, 9999, False)


def test_move_right_check(lines, find_x, run_off_map_right):
    # returns row, column, obstacle, new_spot
    # runs into obstacle
    assert move_right_check(lines, 1, 8) == (1, 8, True)
    # runs into X
    assert move_right_check(find_x, 0, 4) == (0, 5, False)
    # runs off the map
    assert move_right_check(lines, 0, 9) == (9999, 9999, False)
    # runs off the map on the right side
    assert move_right_check(run_off_map_right, 1, 9) == (9999, 9999, False)


def test_move_down_check(lines):
    # returns row, column, obstacle, new_spot
    # moves to the next row
    assert move_down_check(lines, 1, 8) == (2, 8, False)
    # runs off the map
    assert move_down_check(lines, 9, 10) == (9999, 9999, False)


def test_move_left_check(lines):
    # returns row, column, obstacle, new_spot
    # moves to the left
    assert move_left_check(lines, 6, 8) == (6, 7, False)
    # runs off the map
    assert move_left_check(lines, 0, 0) == (9999, 9999, False)


def test_walk(lines):
    visited = 0

    # find current position ^
    row, column = find_current_position(lines)
    # replace '^' with 'X'
    lines[row] = lines[row][:column] + 'X' + lines[row][column + 1:]

    # write functions for up, down. left and right
    moves = [move_right_check,
             move_down_check,
             move_left_check,
             move_up_check]
    current_move = move_up_check

    counter = 0

    s1_lines, _ = walk(lines, row, column, moves, current_move)

    # count Xs
    for line in s1_lines:
        visited += line.count('X')

    assert visited == 41


def test_s2(infinite):
    # write functions for up, down. left and right
    moves = [move_right_check,
             move_down_check,
             move_left_check,
             move_up_check]
    current_move = move_up_check

    # find current position ^
    row, column = find_current_position(infinite)
    infinite[row] = infinite[row][:column] + 'X' + infinite[row][column + 1:]

    _, infinite = walk(infinite, row, column, moves, current_move)

    assert infinite
