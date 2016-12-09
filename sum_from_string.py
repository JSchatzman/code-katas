"""Sum from string."""


import re


def sum_from_string(string):
    """Return sum of all numbers in a string."""
    return sum(map(int, re.findall('\d+', string)))
