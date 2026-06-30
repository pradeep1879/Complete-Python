import math


def square(number):
    return(number ** 2)

result = square(4)
print(result)
print(square(4))


def sumToNum(num1, num2):
    return num1 + num2

addition = sumToNum(25, 23)
print(addition)


def multiply(p1,p2):
    return p1*p2

multiplication = multiply(23, 23)
multiplication = multiply("a", 23)
print(multiplication)


def circle_stats(radius):
    area =  math.pi * (radius ** 2)
    circuference = 2 * math.pi * radius
    return area, circuference

a, c = circle_stats(4)
print("Area: ", a, "Circuference: ", c)


def greet(name = "kumar"):
    return "Hello, " + name + " !"
print(greet("pradeep")) 
print(greet()) 


def add(a, b):
    return a + b

result = add(23, 34)
print(result)

cube = lambda x: x ** 3
print(cube(3))


def sum_all(*args):
    print(args)
    return sum(args)
print(sum_all(1,3,5,5))



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



def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)

































