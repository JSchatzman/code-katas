"""Test spin_words.py."""

import pytest


answer_table = [
    ["Hey fellow warriors", "Hey wollef sroirraw"],
    ["This is a test", "This is a test"],
    ["This is another test", "This is rehtona test"]

]


@pytest.mark.parametrize("sentence, output", answer_table)
def test_spin_words(sentence, output):
    """Test for spin_words function."""
    from spin_words import spin_words
    assert spin_words(sentence) == output
