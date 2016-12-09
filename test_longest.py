"""Test Is_Triangle."""

import pytest


answer_table = [
    ["aretheyhere", "yestheyarehere", "aehrsty"],
    ["loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu"],
    ["inmanylanguages", "theresapairoffunctions", "acefghilmnoprstuy"],
    ["lordsofthefallen", "gamekult", "adefghklmnorstu"],
    ["codewars", "codewars", "acdeorsw"],
    ["agenerationmustconfrontthelooming", "codewarrs", "acdefghilmnorstuw"]
]


@pytest.mark.parametrize("s1, s2, answer", answer_table)
def test_longest(s1, s2, answer):
    """Test for longest function."""
    from longest import longest
    assert longest(s1, s2) == answer
