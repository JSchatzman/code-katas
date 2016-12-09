"""Calculate Years."""


def calculate_years(principal, interest, tax, desired):
    """Return how many years needed to achieve desired money given input."""
    current = principal
    years = 0
    while current < desired:
        previous = current
        current = current * (1 + interest)
        current = current - (current - previous) * (tax)
        years += 1
    return years
