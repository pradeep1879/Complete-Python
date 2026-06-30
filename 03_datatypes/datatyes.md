# Objects Types / Data Types

- Number: 1234, 3.1415, 3 + 4j, 0b111, Decimal(), Fraction()
- String: 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List: [1, [2, 3], 4.5, [3, 'five']]
- Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary: {'food': 'spam', 'test': 'yum'}, dict
  (hour=10)
- Set: set('abc'), {'a', 'b', 'c'}

- File: open('eggs.txt'), open(r'C:\ham.bin', 'wb')
- Boolean: True, False
- None: none
- Functions, modules, classes 

- Advance: Decorators, Generators, Iterators, MetaProgramming, Comprehesions, Context Managers


# This is for lists 
>>> n1 = [1, 2, 3]
>>> n2 = n1
>>> n1
[1, 2, 3]
>>> n2
[1, 2, 3]
>>> n1[0] = 33
>>> n1
[33, 2, 3]
>>> n2
[33, 2, 3]
>>> n1[0] = 33
>>> n1 = [4, 5, 6]
>>> n2 = [4, 5, 6]
>>> n1[0] = 77
>>> n1
[77, 5, 6]
>>> n2
[4, 5, 6]
>>> n1 = n2
>>> n1
[4, 5, 6]
>>> n2
[4, 5, 6]
>>> n1[0] = 88
>>> n1
[88, 5, 6]
>>> n2
[88, 5, 6]
>>> n1 == n2
True
>>> n1 is n2
True
>>> n2
[88, 5, 6]
>>> n2 = [88, 5, 6]
>>> nq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^
NameError: name 'nq' is not defined. Did you mean: 'n1'?
>>> n1
[88, 5, 6]
>>> n2
[88, 5, 6]
>>> n1 == n2
True
>>> ni is n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^
NameError: name 'ni' is not defined. Did you mean: 'n1'?
>>> n1 is n2
False
>>> 