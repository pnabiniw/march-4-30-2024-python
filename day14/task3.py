# Create a decorator function which calculates the execution time of a function
import time


def execution_time(func):
    def inner_fxn(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time is ",round(end-start, 2), " seconds")
        return result
    return inner_fxn


@execution_time
def my_fxn():
    for i in range(100000000):
        pass

my_fxn()
