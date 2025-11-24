def add(x: int, y: int) -> int:
    """Returns the sum of two integers."""
    if type(x) not int or type (y) not int:
        raise TypeError
    return x + y
