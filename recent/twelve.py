import time


def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            t = time.clock()
            print decorator_to_enhance.__name__, time.clock() - t
            return decorator_to_enhance(func)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def measure_1_decorator(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        measured_func = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return measured_func
    return wrapper


@measure_1_decorator()
def function_to_measure1():
    for i in range(100):
        pass

#function_to_measure1 = measure_1_decorator()(function_to_measure1)

@measure_1_decorator()
def function_to_measure2(a, b, dict):
    a = a + b


if __name__ == '__main__':
    function_to_measure1()
    function_to_measure2(1,2,{})


