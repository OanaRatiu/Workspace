import time

def fibo_deco(func):
    fibo_values = {}
    def wrapper(args):
        if args in fibo_values:
            return fibo_values[args]
        else:
            fibo_values[args] = func(args)
            return fibo_values[args]
    return wrapper



@fibo_deco
def fibbonacci(n):
    if n in (0, 1):
        return n
    return fibbonacci(n-1) + fibbonacci(n-2)

if __name__ == '__main__':
    t = time.clock()
    print fibbonacci(30)
    print time.clock() - t
    print fibbonacci(30)
    print time.clock() - t


# without decorator
#     832040
#     0.28961
#     832040
#     0.578748
