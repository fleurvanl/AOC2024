from utils.file_handling import FileHandling

import pytest
import os

@pytest.fixture
def file_path():
    return os.path.join(os.getcwd(), 'test_input.txt')

def test_read_file(file_path):
    file_content = FileHandling.read_file(file_path)
    assert isinstance(file_content, str)
    lines = file_content.split('\n')
    assert len(lines) == 4
    assert lines[0] == 'abc'
