"""Create series_sum function."""


def sum_terms(n):
    """Return the nth value in the series."""
    if n == 0:
        return '0.00'
    elif n == 1:
        return '1.00'
    else:
        value = 1
        for i in range(1, n):
            value += float(1) / (1 + (3 * i))
        return str(format(value, '.2f'))
