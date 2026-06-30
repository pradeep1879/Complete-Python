#Ques. Write a decorator that measures the time a function  takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

#Ques. Create a decorator to print the function name and the values of argument every 
#      time the function called.


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def greeting(name , greet="Hello"):
    print("f{greet}, {name}")

greeting("Pradeep", greet="Hi thre")

#Ques.Implement a decorator that caches the return values of a function, so that when it's called 
#    with the same arguments, the cached value is returned instead of re-executing the function.

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def sum(a, b):
    time.sleep(4)
    return a + b

print(sum(3, 3))
print(sum(3, 3))