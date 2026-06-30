# Python Strings
>>> tea_varities = ["Black", "Geen", "Oolong", "Milk"]
>>> print(tea_varities)
['Black', 'Geen', 'Oolong', 'Milk']

>>> print(tea_varities[1:3])
['Geen', 'Oolong']

>>> print(tea_varities[0:3])
['Black', 'Geen', 'Oolong']

>>> >>> print(tea_varities[2:])
['Oolong', 'Milk']

>>> tea_varities[2] = "Clove"
>>> tea_varities[2] = "Clove"
>>> print(tea_varities)
['Black', 'Geen', 'Clove', 'Milk']

>>> tea_varities[1:3] = "Lemon"
>>> tea_varities
['Black', 'L', 'e', 'm', 'o', 'n', 'Milk']

>>> tea_varities[1:3] = ["Lemon"]
>>> tea_varities[1:3] = ["Lemon"]
>>> tea_varities[1:3] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'm', 'o', 'n', 'Milk']

>>> tea_varities[1:3] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'm', 'o', 'n', 'Milk']
>>> 


>>> tea_varities[1:1] = ["test1", "test2"]
>>> tea_varities
['Black', 'test1', 'test2', 'Lemon', 'm', 'o', 'n', 'Milk']

>>> tea_varities[1:3]
['test1', 'test2']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'Lemon', 'm', 'o', 'n', 'Milk']
>>> 


>>> for tea in tea_varities:
...     print(tea, end="-")
... 
Black-Lemon-m-o-n-Milk->>> 


>>> tea_varities
['Black', 'Lemon', 'm', 'o', 'n', 'Milk']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> if "Lemon" in tea_varities:
...     print("I have Lemon")
... 
I have Lemon


>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'Lemon', 'm', 'o', 'n', 'Milk', 'Oolong']


>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 



# Dictionary in Python


























