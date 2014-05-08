import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        measured_func = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return measured_func
    return wrapper

@my_decorator
def function_to_measure1():
    for i in range(100):
        pass

@my_decorator
def function_to_measure2(a, b, dict):
    a = a + b


if __name__ == '__main__':
    function_to_measure1()
    function_to_measure2(1,2,{})