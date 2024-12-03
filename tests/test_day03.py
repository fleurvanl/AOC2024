import pytest

from day03 import find_mult, find_do_mult


@pytest.fixture
def input():
    return 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'


def test_find_mult(input):
    assert find_mult(input) == 161


@pytest.fixture
def do_input():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_find_do_mult(do_input):
    assert find_do_mult(do_input) == 48