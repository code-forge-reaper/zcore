"""
each function in this file is supposed to be used as a decorator
example:

from helpers import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

"""

import functools
import gc
import time
import resource


def timeit(fn):
    """
    this is a debug decorator, used to measure how long a function takes to run
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Function {fn.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

def cache(fn):
    cache_dict = {}

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = fn(*args, **kwargs)
        return cache_dict[key]

    return wrapper

def nonWorking(reason:str = None):
    def wrap(fn):
        def wrapper(*args, **kwargs):
            # Perform some non-working behavior or logic here
            if reason:
                raise NotImplementedError(f"{fn.__name__} is currently not functional, reason: {reason}.")
            else:
                raise NotImplementedError(f"{fn.__name__} is currently not functional.")
            exit(1)
        return wrapper
    return wrap

def memFree(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        gc.collect()
        return result
    return wrapper

def memUsageGet(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result = fn(*args, **kwargs)
        return result, usage
    return wrapper

if __name__ == "__main__":
    # Test the decorators
    @timeit
    @memFree
    def example_function():
        time.sleep(1)  # Simulate some work
        return "Done"

    @cache
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    @memUsageGet
    def compute_factorial(n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    print("Testing example_function:")
    example_function()
    
    print("\nTesting fib:")
    for n in range(10):
        print(f"fib({n}) = {fib(n)}")

    print("\nTesting memUsageGet:")
    result, memory_usage = compute_factorial(400)
    print(f"Factorial of 400 is {result}")
    print(f"Memory usage: {memory_usage} KB")
