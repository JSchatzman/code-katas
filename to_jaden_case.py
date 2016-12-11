"""Convert String to Jaden Case."""


def to_jaden_case(string):
    """Return every word in the input string in captialized form."""
    return ' '.join(list(map(lambda x: x.capitalize(), string.split(' '))))
