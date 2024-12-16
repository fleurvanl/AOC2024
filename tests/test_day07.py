import pytest

from day07 import process_pipe


@pytest.fixture
def operator():
    return ( '*', '+', '|')


@pytest.fixture
def numbers():
    return ['3', '7', '8', '5']


def test_process_pipe(operator, numbers):
    assert process_pipe(operator, numbers) == (['3', '7', '85'], ['*', "+"])
