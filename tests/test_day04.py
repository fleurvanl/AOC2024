from day04 import look_left_right, look_down, look_diagonally

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

