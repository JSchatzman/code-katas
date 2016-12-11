"""Test Is_Triangle."""

import pytest


answer_table = [
    [1, 2, 2, True],
    [7, 2, 2, False],
    [1, 2, 3, False],
    [1, 3, 2, False],
    [3, 1, 2, False],
    [5, 1, 2, False],
    [1, 2, 5, False],
    [2, 5, 1, False],
    [4, 2, 3, True],
    [5, 1, 5, True],
    [2, 2, 2, True],
    [-1, 2, 3, False],
    [1, -2, 3, False],
    [1, 2, -3, False],
    [0, 2, 3, False]

]


@pytest.mark.parametrize("a, b, c, answer", answer_table)
def test_is_triangle(a, b, c, answer):
    """Test for calculate_years function."""
    from is_triangle import is_triangle
    assert is_triangle(a, b, c) == answer
