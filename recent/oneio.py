def read_from_file(f):
    """
    >>> read_from_file([])
    0

    >>> read_from_file([1])
    1.0

    >>> read_from_file([1, 2, 3])
    6.0

    >>> read_from_file([1.5, 2.5, 4.2])
    8.2

    >>> read_from_file([10000000000, 10000000000])
    20000000000.0
    """
    # sum = 0
    # for line in f:
    #     sum += float(line)
    # return sum
    if f == []:
        return 0
    return reduce(lambda x, y: float(x) + float(y), f, 0.0) 

if __name__ == "__main__":
    with open("nbs.txt", "r") as f:
        print read_from_file(f)