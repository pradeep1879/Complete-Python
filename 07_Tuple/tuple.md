# ==========================================================
# Tuple
# ==========================================================

# A tuple is an ordered collection of items.
# Unlike lists, tuples are immutable, which means we
# cannot modify their elements after creation.

>>> tea_types = ("Black", "Green", "Oolong")

>>> tea_types

('Black', 'Green', 'Oolong')

# ----------------------------------------------------------
# Accessing Elements
# ----------------------------------------------------------
# Tuples support both positive and negative indexing.

>>> tea_types[1]

'Green'

>>> tea_types[-1]

'Oolong'

>>> tea_types[0]

'Black'


# ----------------------------------------------------------
# Tuples are Immutable
# ----------------------------------------------------------
# Trying to change an element raises a TypeError because
# tuples do not support item assignment.

>>> tea_types[0] = "Lemon"

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

    import platform

    ^^^^^^^^^^^^

TypeError: 'tuple' object does not support item assignment


# ----------------------------------------------------------
# len()
# ----------------------------------------------------------
# Returns the total number of elements in the tuple.

>>> len(tea_types)

3


# ----------------------------------------------------------
# Concatenating Tuples
# ----------------------------------------------------------
# '+' joins two tuples and creates a new tuple.

>>> another_tea = ("Herbal", "Earl Gray")

>>> all_tea = tea_tyeps + another_tea

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

    import platform

              ^^^^^

NameError: name 'tea_tyeps' is not defined. Did you mean: 'tea_types'?

# The error above is because of a typo (tea_tyeps).

>>> all_tea = tea_types + another_tea

>>> all_tea

('Black', 'Green', 'Oolong', 'Herbal', 'Earl Gray')


# ----------------------------------------------------------
# count()
# ----------------------------------------------------------
# Returns how many times a value appears.

>>> another_tea = ("Herbal", "Earl Gray", "Herbal")

>>> another_tea.count("Herbal")

2


# ----------------------------------------------------------
# Tuple Unpacking
# ----------------------------------------------------------
# Each tuple element can be assigned directly to a variable.

>>> tea_types

('Black', 'Green', 'Oolong')

>>> (black, green, oolong) = tea_types

>>> Black

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

    import platform

    ^^^^^

NameError: name 'Black' is not defined. Did you mean: 'black'?

# Python variable names are case-sensitive.

>>> black

'Black'


# ==========================================================
# Quick Notes
# ==========================================================

# -> Ordered collection
# -> Immutable
# -> Supports indexing & slicing
# -> Allows duplicate values
# -> Faster than lists
# -> Common methods: count(), index()