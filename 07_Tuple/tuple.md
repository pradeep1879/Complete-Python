>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[1]
'Green'
>>> tea_types[-1]
'Oolong'
>>> tea_types[0]
'Black'
>>> tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^^^^^^
TypeError: 'tuple' object does not support item assignment
>>> 


>>> len(tea_types)
3
>>> another_tea =  ("Herbal", "Earl Gray")
>>> all_tea = tea_tyeps + another_tea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
              ^^^^^
NameError: name 'tea_tyeps' is not defined. Did you mean: 'tea_types'?
>>> all_tea = tea_types + another_tea
>>> all_tea
('Black', 'Green', 'Oolong', 'Herbal', 'Earl Gray')
>>> another_tea = ("Herbal", "Earl Gray", "Herbal")
>>> another_tea.count("Herbal")
2
>>>  

>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, oolong) = tea_types
>>> Black
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^
NameError: name 'Black' is not defined. Did you mean: 'black'?
>>> black
'Black'
>>> 













