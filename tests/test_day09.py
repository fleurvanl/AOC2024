import pytest

from day09 import visualise_space, move_data, calculate_checksum, organise_per_file, move_data_per_file

@pytest.fixture
def aoc():
    return '12345'


def test_visualise_space(aoc):
    assert visualise_space(aoc) == [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]


def test_move_data(aoc):
    assert move_data(visualise_space(aoc)) == [0, 2, 2, 1, 1, 1, 2, 2, 2, None, None, None, None, None, None]


def test_calculate_checksum(aoc):
    assert (calculate_checksum(move_data(visualise_space(aoc))) == 60)


def test_organise_per_file(aoc):
    assert organise_per_file(visualise_space(aoc)) == [[0], [None, None], [1, 1, 1], [None, None, None, None], [2, 2, 2, 2, 2]]


@pytest.fixture
def aoc2():
    return [[0, 0], [None, None, None], [1, 1, 1], [None, None, None], [2], [None, None, None], [3, 3, 3], [None],
            [4, 4], [None], [5, 5, 5, 5], [None], [6, 6, 6, 6], [None], [7, 7, 7], [None], [8, 8, 8, 8], [9, 9]]

def test_move_data_per_file(aoc2):
    assert move_data_per_file(aoc2) == [[0, 0], [9, 9], [2], [1, 1, 1], [7, 7, 7], [None], [4, 4], [None], [3, 3, 3],
                                        [None, None, None, None], [5, 5, 5, 5], [6, 6, 6, 6],
                                        [None, None, None, None, None], [8, 8, 8, 8], [None, None, None]]
