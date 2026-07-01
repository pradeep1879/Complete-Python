# ==========================================================
# Scope in Python
# ==========================================================

# Scope defines where a variable can be accessed.
# Python mainly has:
# 1. Global Scope
# 2. Local Scope
# 3. Enclosing Scope
# 4. Built-in Scope


# ----------------------------------------------------------
# Global Scope
# ----------------------------------------------------------
# A variable declared outside a function is called a
# global variable. It can be accessed inside functions
# unless a local variable with the same name exists.

username = "pradeepkumar"

def func():
    # username = "kumawat"
    print(username)

print(username)
func()


# ----------------------------------------------------------
# Accessing Global Variables
# ----------------------------------------------------------

x = 22

# def func2(y):
#     z = x + y
#     return z

# result = func2(4)
# print(result)

# The function can access x because it is a global variable.


# ----------------------------------------------------------
# global Keyword
# ----------------------------------------------------------

# global is used when we want to modify a global variable
# inside a function.

# def func3():
#     global x
#     x = 12

# result = func3()
# print(x)


# ----------------------------------------------------------
# Enclosing Scope (Closure)
# ----------------------------------------------------------

# A nested function can access variables from its outer
# function. This is called a closure.

# def f1():
#     x = 88
#
#     def f2():
#         print(x)
#
#     return f2

# result = f1()
# result()


# ----------------------------------------------------------
# Returning Functions
# ----------------------------------------------------------

# Functions are first-class objects in Python.
# This means a function can return another function.

def newFun(num):

    def fun2(x):
        return x ** num

    return fun2


result1 = newFun(3)
sol1 = result1(3)
print(sol1)

result2 = newFun(4)
sol2 = result2(4)
print(sol2)


# ==========================================================
# Quick Notes
# ==========================================================

# -> Global variables are created outside functions.
# -> Local variables exist only inside a function.
# -> global allows modifying a global variable.
# -> Nested functions can access variables from the
#    enclosing function.
# -> A function can return another function.
# -> This concept is called a Closure.