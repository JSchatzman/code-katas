"""Test multiply.py."""

import pytest


answer_table = [
    [1, 1, 1],
    [2, 1, 2],
    [2, 2, 4],
    [4, -1, -4],
    [1, 0, 0],
    [100, 100, 10000],
    [0, 0, 0]
]


@pytest.mark.parametrize("a, b, answer", answer_table)
def test_fibonacci(a, b, answer):
    """Test for multiply function."""
    from multiply import multiply
    assert multiply(a, b) == answer
