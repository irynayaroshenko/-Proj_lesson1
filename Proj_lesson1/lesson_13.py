"""
Decorators
"""
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def my_function():
    print("Hello, world!")


import datetime


def timer(func):
    def wrapper(y):
        start = datetime.datetime.now()
        x = func(y)
        print(f"Total time = {datetime.datetime.now() - start}")
        return x
    return wrapper


@timer
def counter(y):
    x = 100
    for x in range(y):
        x = x**10
    return x

print(counter(1234567))

# 2 decorators for one func
import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        x = func(*args, **kwargs)
        print(f"Total time = {datetime.datetime.now() - start}")
        return x
    return wrapper


def decor(func):
    def wrapper(*args, **kwargs):
        print("=" * 100)
        x = func(*args, **kwargs)
        print("=" * 100)
        return x
    return wrapper


@decor
@timer
def counter(y):
    x = 100
    for x in range(y):
        x = x ** 10
    return x


print(counter(12345000))