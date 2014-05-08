import math

def compute_prime(limit):
    """
    >>> sorted(compute_prime(10))
    [2, 3, 5, 7]

    >>> sorted(compute_prime(0))
    []

    >>> sorted(compute_prime(1))
    []
    """
    isComposite = [0 for i in range(limit + 1)]
    for number in range(2, int(math.sqrt(limit)) + 1):
        if not isComposite[number]:
             for i in range(number*number, limit + 1, number):
                isComposite[i] = 1

    return [i for i in range(2, len(isComposite)) if isComposite[i] == 0]


if __name__ == "__main__":
    with open("2io.txt", "w+") as f:
        gen = compute_prime(int(raw_input('Give n:')))
        for number in gen:
            f.write(str(number) + "\n")