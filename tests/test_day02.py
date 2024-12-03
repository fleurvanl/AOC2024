import pytest

from day02 import check_report, check_report_dampner


@pytest.fixture
def safe():
    return '7 6 4 2 1'.split(' ')


@pytest.fixture
def unsafe():
    return '1 2 7 8 9'.split(' ')


@pytest.fixture
def safe_with_dampner():
    return '8 6 4 4 1'.split(' ')


@pytest.fixture
def unsafe_increase_decrease():
    return '3 5 7 4 1'.split(' ')


def test_check_report(safe, unsafe, safe_with_dampner):
    assert check_report(safe)
    assert not check_report(unsafe)
    assert not check_report(safe_with_dampner)


def test_check_report_dampner(safe, unsafe, safe_with_dampner, unsafe_increase_decrease):
    assert check_report_dampner(safe, level=0)
    assert not check_report_dampner(unsafe, level=0)
    assert check_report_dampner(safe_with_dampner, level=0)
    assert not check_report_dampner(unsafe_increase_decrease, level=1)
