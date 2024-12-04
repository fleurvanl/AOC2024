from day04 import look_left_right, look_down, look_up, look_diagonally, find_x_mas

import pytest

@pytest.fixture
def left_right():
    return 'MMMSXXMASM'

@pytest.fixture
def right_left():
    return 'MSAMXMSMSA'

def test_look_left_right(left_right, right_left):
    assert look_left_right(left_right) == 1
    assert look_left_right(right_left) == 1


@pytest.fixture
def down():
    return ['MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS']


def test_look_down(down):
    assert look_down(0, 'MSAMASMSMX', down) == 1


@pytest.fixture
def up():
    return ['MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM']


def test_look_up(up):
    assert look_up(3, 'XMASAMXAMM', up) == 1


@pytest.fixture
def diagonal_up():
    return ['SMSMSASXSS',
            'SAXAMASAAA',
            'MAMMMXMMMM',
            'MXMXAXMASX']


@pytest.fixture
def diagonal_down():
    return ['MMMSXXMASM',
            'MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS']


def test_look_diagonal(diagonal_up, diagonal_down):
    assert look_diagonally(3, 'MXMXAXMASX', diagonal_up) == 6
    assert look_diagonally(0, 'MMMSXXMASM', diagonal_down) == 1
    assert look_diagonally(3, 'MSAMASMSMX', diagonal_down) == 1


@pytest.fixture
def x_mas():
    return ['MMMSXXMASM',
            'MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS',
            'SAXAMASAAA',
            'MAMMMXMMMM',
            'MXMXAXMASX']


def test_find_x_mas(x_mas):
    num_x_mas = 0
    for i, line in enumerate(x_mas):
        num_x_mas += find_x_mas(i, line, x_mas)
    assert num_x_mas == 9
