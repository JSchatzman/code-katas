"""Test valid parentheses.py."""

import pytest


answer_table = [
    ['', 0],
    ['(', 1],
    [')', -1],
    ['(((((((((())))', 1],
    ['()()()()((()))', 0],
    ['()()(((ignorethis)))', 0],
    ['()()(((ignorethis))))', -1],
    ['()()(((ignorethis))', 1],
    [')))(((', -1]

]


@pytest.mark.parametrize("string, answer", answer_table)
def test_valid_parentheses(string, answer):
    """Test for valiid parenthetics function."""
    from parenthetics import valid_parentheses
    assert valid_parentheses(string) == answer
