username = "pradeepkumar"

def func():
    # username = "kumawat"
    print(username)

print(username)
func()

x = 22

# def func2(y):
#     z = x + y
#     return z
# result = func2(4)
# print(result)


# def func3():
#     global x
#     x = 12
# result = func3()
# print(x)



# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# result = f1()
# result()


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


