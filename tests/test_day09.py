import pytest

from day09 import visualise_space, move_data, calculate_checksum, organise_per_file

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
