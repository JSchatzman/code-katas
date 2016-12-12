"""Test sum_terms.py."""

import pytest


answer_table = [
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"],
    [4, "1.49"],
    [5, "1.57"],
    [6, "1.63"],
    [7, "1.68"],
    [8, "1.73"],
    [9, "1.77"],
    [15, "1.94"],
    [39, "2.26"],
    [58, "2.40"],
    [0, "0.00"],

]


@pytest.mark.parametrize("n, answer", answer_table)
def test_sum_terms(n, answer):
    """Test for sum_terms function."""
    from sum_terms import sum_terms
    assert sum_terms(n) == answer
