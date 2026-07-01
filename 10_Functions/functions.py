import math

# ==========================================================
# Functions
# ==========================================================

# A function is a block of reusable code that performs a
# specific task. It helps avoid writing the same code again
# and makes the program easier to read and maintain.


# ----------------------------------------------------------
# Function with a single parameter
# ----------------------------------------------------------

def square(number):
    return(number ** 2)

result = square(4)
print(result)
print(square(4))


# ----------------------------------------------------------
# Function with multiple parameters
# ----------------------------------------------------------

# Functions can take multiple arguments.

def sumToNum(num1, num2):
    return num1 + num2

addition = sumToNum(25, 23)
print(addition)


# ----------------------------------------------------------
# Python supports dynamic typing
# ----------------------------------------------------------

# The same function works with numbers and strings depending
# on the data type passed.

def multiply(p1, p2):
    return p1 * p2

multiplication = multiply(23, 23)
multiplication = multiply("a", 23)
print(multiplication)


# ----------------------------------------------------------
# Returning Multiple Values
# ----------------------------------------------------------

# A function can return more than one value.
# Python automatically returns them as a tuple.

def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circuference = 2 * math.pi * radius
    return area, circuference

a, c = circle_stats(4)
print("Area:", a, "Circuference:", c)


# ----------------------------------------------------------
# Default Arguments
# ----------------------------------------------------------

# If no argument is passed, the default value is used.

def greet(name="kumar"):
    return "Hello, " + name + " !"

print(greet("pradeep"))
print(greet())


# ----------------------------------------------------------
# Basic Function Example
# ----------------------------------------------------------

def add(a, b):
    return a + b

result = add(23, 34)
print(result)


# ----------------------------------------------------------
# Lambda Function
# ----------------------------------------------------------

# Lambda is a small anonymous function used for short
# operations.

cube = lambda x: x ** 3

print(cube(3))


# ----------------------------------------------------------
# *args
# ----------------------------------------------------------

# *args allows a function to accept any number of
# positional arguments.

def sum_all(*args):
    print(args)
    return sum(args)

print(sum_all(1, 3, 5, 5))


# ----------------------------------------------------------
# **kwargs
# ----------------------------------------------------------

# **kwargs accepts any number of keyword arguments.
# It stores them as a dictionary.

# def print_kwargs(name, power):
#     print("Name:", name, "Power:", power)

# print_kwargs(name="rahul", power="kumar")
# print_kwargs(name="rahul")
# print_kwargs(name="rahul", power="kumar")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="kumar", power="kumawat")
print_kwargs(name="rahul")
print_kwargs(name="pradeep", power="kumawat")


# ----------------------------------------------------------
# Generator Function
# ----------------------------------------------------------

# A generator uses 'yield' instead of 'return'.
# It generates values one at a time instead of storing
# them all in memory.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)


# ==========================================================
# Quick Notes
# ==========================================================

# -> def is used to create a function.
# -> return sends a value back to the caller.
# -> A function can have multiple parameters.
# -> Functions can return multiple values.
# -> Default arguments are used when no value is passed.
# -> Lambda functions are useful for short expressions.
# -> *args accepts multiple positional arguments.
# -> **kwargs accepts multiple keyword arguments.
# -> yield creates a generator and returns one value at a time.