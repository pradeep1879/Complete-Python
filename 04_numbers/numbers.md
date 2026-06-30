# Numbers in Python

>>> repr('pradeep')
"'pradeep'"
>>> str('pradeep')
'pradeep'
>>> print('pradeep')
pradeep
>>> 5 == 5.0
True
>>> 4.0 != 5.0
True
>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2
>>> (2 + 3j) * 3
(6+9j)
>>> 0o18
  File "<stdin>", line 1
    0o18
       ^
SyntaxError: invalid digit '8' in octal literal
>>> 0o20
16


>>> import random
>>> random.random()
0.4456719714128691
>>> 
>>> random.random()
0.346772629801648
>>> random.random()
0.40141295546610134
>>> random.randint(1, 20)
11
>>> random.randint(1, 20)
4
>>> random.randint(1, 20)

>>> l1 = ['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(l1)
'lemon'

>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> 

>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') 
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>> 



>>> setone = {1, 2, 3, 4}
>>> setone & {2, 5}
{2}
>>> setone | {2,5}
{1, 2, 3, 4, 5}
>>> setone - {1, 2, 3, 4}
set()
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>-45:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 5
6
>>>            



















