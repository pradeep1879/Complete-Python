# ==========================================================
# Iterators in Python
# ==========================================================

# An iterator is an object that returns one element at a time.
# It remembers its current position, so every call to next()
# gives the next value.

# Most built-in collections like list, tuple, dictionary,
# string, range and file objects are iterable.

# To get an iterator, use iter().

# ==========================================================
# File Object is an Iterator
# ==========================================================

# A file object returns one line at a time.
# __next__() reads the next line from the file.
# When there are no more lines, Python raises StopIteration.

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
...
StopIteration


# ==========================================================
# Iterating using for loop
# ==========================================================

# A for loop automatically calls iter() and next() internally.

>>> for line in open('iteration_tool.py'):
...     print(line)

import time

print("hi there from iteration tool")

username = "pradeep"

print(username)


# ==========================================================
# Reading file using readline()
# ==========================================================

# readline() reads one line at a time.
# We stop when it returns an empty string.

>>> f = open('iteration_tool.py')

>>> while True:
...     line = f.readline()
...     if not line:
...         break
...     print(line, end='')

import time

print("hi there from iteration tool")
username = "pradeep"
print(username)


# ==========================================================
# Iterator on List
# ==========================================================

# iter() converts an iterable into an iterator.
# next() returns one item at a time.

>>> myList = [1, 2, 3, 4, 5]

>>> I = iter(myList)

>>> I

<list_iterator object at 0x1030c3190>

>>> I.__next__()
1

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
...
StopIteration


# ==========================================================
# __iter__() and __next__()
# ==========================================================

# Every iterator has two important methods:
#
# __iter__()  -> returns the iterator itself.
# __next__()  -> returns the next value.

>>> f = open('iteration_tool.py')

>>> iter(f) is f
True

>>> iter(f) is f.__next__()
False

>>> iter(f) is f.__iter__()
True

>>> newList = [1,2,3]

>>> iter(myList) is myList
False

# A list is iterable but NOT an iterator.
# Calling iter(list) creates a new iterator.


# ==========================================================
# Dictionary Iterator
# ==========================================================

# Iterating over a dictionary returns keys by default.

>>> D = {'a':1, 'b':2}

>>> for key in D.keys():
...     print(key)

a
b

>>> I = iter(D)

>>> next(I)
'a'

>>> next(I)
'b'

>>> next(I)

Traceback (most recent call last):
...
StopIteration


# ==========================================================
# Range Iterator
# ==========================================================

# range() returns a range object.
# It is iterable but not an iterator.

>>> range(5)

range(0, 5)

>>> R = range(5)

>>> r

Traceback (most recent call last):
...
NameError

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
...
StopIteration


# ==========================================================
# Quick Notes
# ==========================================================

# -> Iterable: An object that can be looped over.
# -> Iterator: An object that returns one value at a time.
# -> iter() creates an iterator.
# -> next() returns the next value.
# -> When values are exhausted, StopIteration is raised.
# -> for loop automatically uses iter() and next() internally.