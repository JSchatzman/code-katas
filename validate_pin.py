"""Validate a Pin Number."""


def validate_pin(pin):
    """Validate an input pin number."""
    if not pin.isdigit():
        return False
    elif '.' in str(pin):
        return False
    elif len(pin) != 6 and len(pin) != 4:
        return False
    elif float(pin) < 0:
        return False
    else:
        return True
