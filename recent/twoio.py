def is_prime(a):
    """
    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(7)
    True

    >>> is_prime(10)
    False
    """
    if a == 0 or a == 1:
        return False
    return all(a % i for i in xrange(2, a/2 + 1))


def compute_prime(limit):
    """
    >>> sorted(compute_prime(10))
    [2, 3, 5, 7]

    >>> sorted(compute_prime(0))
    []

    >>> sorted(compute_prime(1))
    []
    """
    for number in range(limit + 1):
        if is_prime(number):
            yield number
    

if __name__ == "__main__":
    with open("2io.txt", "w+") as f:
        gen = compute_prime(int(raw_input('Give n:')))
        for number in gen:
            f.write(str(number) + "\n")