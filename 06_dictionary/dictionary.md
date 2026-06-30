# Dictionary in Python
>>> chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types['Green'] = "Fresh"
>>> chai_tyes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^^^
NameError: name 'chai_tyes' is not defined. Did you mean: 'chai_types'?
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> 


>>> chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> if 'Masala' in chai_types:
...     print("i have masala")
... 
i have masala
>>> chai_types["Earl Gray"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Gray': 'Citrus'}
>>> chai_types.pop("Earl Gray")
'Citrus'
>>> chai_types.pop("Earl Gray")
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> 





>>> chai_types.popitem()
('Green', 'Mild')
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> del chai_types["Masala"]
>>> chai_types
{'Ginger': 'Zesty'}
>>> chai_types = chai_types.copy()
>>> 





>>> squared_num = {X:X**2 for X in range(10)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> squared_num.clear()
>>> squared_num
{}


>>> keys = ["masala", "ginger", "lemon"]
>>> keys
['masala', 'ginger', 'lemon']
>>> default_values = "Delicious"
>>> new_dict = dict.
dict.clear(      dict.fromkeys(   dict.items(      dict.mro()       dict.popitem(    dict.update(    
dict.copy(       dict.get(        dict.keys(       dict.pop(        dict.setdefault( dict.values(    
>>> new_dict = dict.fromkeys(key, default_values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    
NameError: name 'key' is not defined. Did you mean: 'keys'?
>>> new_dict = dict.fromkeys(keys, default_values)
>>> new_dict
{'masala': 'Delicious', 'ginger': 'Delicious', 'lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'], 'lemon': ['masala', 'ginger', 'lemon']}
