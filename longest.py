"""longest."""


def longest(s1, s2):
    """Return the sorted string of unique elements in s1 or s2."""
    return ''.join(sorted(list(set(s1).union(set(s2)))))
