"""
See test_32_unittest_module_1.py for the unit tests.
"""


def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('Can not divide by zero.')
    return x / y