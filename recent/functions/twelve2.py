import time

def decorator(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            t = time.clock()
            function(*args, **kwargs)
            argument[0] += time.clock() - t
        return wrapper
    return real_decorator


c = [0]

mydecorator = decorator(c)

@mydecorator
def function_to_measure1():
    r = 0
    for i in range(1000):
        r += 2 ** i


@mydecorator
def function_to_measure2(a, b, dict):
    a = a + b


if __name__ == '__main__':
    function_to_measure1()
    function_to_measure2(1,2,{})
    print c[0]