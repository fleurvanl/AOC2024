import pytest

from day09 import visualise_space

@pytest.fixture
def aoc():
    return '12345'


def test_visualise_space(aoc):
    assert visualise_space(aoc) == [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]