def increment_number(a = [-1]):
    """
    >>> increment_number()
    0

    >>> increment_number()
    1

    >>> increment_number([2])
    3

    >>> increment_number([2])
    3
    """
    a[0] = a[0] + 1
    return a[0]


if __name__ == '__main__':
    print increment_number()
    print increment_number()
    print increment_number()