"""Is_Triangle."""


def is_triangle(a, b, c):
    """Test if given numbers can be valid sides of a triangle."""
    if min([a, b, c]) <= 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True
