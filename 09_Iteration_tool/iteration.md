>>> f.readline()
>>> f = open('iteration_tool.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("hi there from iteration tool")\n'
>>> f.__next__()
'username = "pradeep"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^^^^^^
StopIteration
>>> 

>>> for line in open('iteration_tool.py'):
...     print(line)
... 
import time



print("hi there from iteration tool")

username = "pradeep"

print(username)
>>> 

>>> f = open('iteration_tool.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
...
import time

print("hi there from iteration tool")
username = "pradeep"
print(username)>>> 



>>> myList = [1, 2, 3, 4, 5]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x1030c3190>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x1030c3190>
>>> I
<list_iterator object at 0x1030c3190>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
5
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^^^^^^
StopIteration
>>> 

>> f = open('iteration_tool.py')
>>> iter(f) is f
True
>>> iter(f) is f.__next__()
False
>>> iter(f) is f.__iter__()
True
>>> newList = [1,2,3]
>>> iter(myList) is myList
False
>>> 






>>> D = {'a':1, 'b':2}
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x1030d6d90>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^
StopIteration
>>> 



>> range(5)
range(0, 5)
>>> R = range(5)
>>> r
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^
NameError: name 'r' is not defined. Did you mean: 'R'?
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^
StopIteration
>>> 












