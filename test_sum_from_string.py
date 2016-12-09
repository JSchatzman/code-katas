"""Test Sum from string."""

import pytest


answer_table = [
    ["In 2015, I want to know how much does iPhone 6+ cost?", 2021],
    ["1+1=2", 4],
    ["e=mc^2", 2],
    ["aHR0cDovL3d3dy5jb2Rld2Fycy5jb20va2F0YS9uZXcvamF2YXNjcmlwdA==", 53],
    ["a30561ff4fb19170aa598b1431b52edad1fcc3e0", 51820],
    ["x1KT   CmZ__\rYouOY8Uqu-ETtz", 9],
    ["", 0],
    ["Hello World", 0]
]


@pytest.mark.parametrize("string, answer", answer_table)
def test_sum_from_string(string, answer):
    """Test for Sum from string."""
    from sum_from_string import sum_from_string
    assert sum_from_string(string) == answer
