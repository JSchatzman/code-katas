"""Test validate_pin.py."""

import pytest


answer_table = [
    ["1", False],
    ["12", False],
    ["123", False],
    ["12345", False],
    ["1234567", False],
    ["1.234", False],
    ["00000000", False],
    ["a234", False],
    [".234", False],
    ["1234", True],
    ["0000", True],
    ["1111", True],
    ["123456", True],
    ["090909", True]
]


@pytest.mark.parametrize("pin, answer", answer_table)
def test_validate_pin(pin, answer):
    """Test for multiply function."""
    from validate_pin import validate_pin
    assert validate_pin(pin) == answer
