def check_number(x):
    return (x * x - 1) % 3 == 0


def compute_sum(n):
    return reduce(lambda x, y : x + y, filter(check_number, range(n)))


if __name__ == '__main__':
    print compute_sum(int(raw_input('Give n:')))