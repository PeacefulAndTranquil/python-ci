def add(x: int, y: int) -> int:
    """Returns the sum of two integers."""
    if type(x) is not int or type(y) is not int:
        raise TypeError
    return x + y
