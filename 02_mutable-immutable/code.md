"""
===========================================================
                MUTABLE vs IMMUTABLE OBJECTS
===========================================================

What is Mutability?
-------------------
Mutability means whether an object can be changed after it
is created.

There are two types of objects in Python:

1. Immutable Objects
   - Cannot be modified after creation.
   - Any change creates a new object.

   Examples:
   • int
   • float
   • bool
   • str
   • tuple

2. Mutable Objects
   - Can be modified after creation.
   - Changes happen in the same object.

   Examples:
   • list
   • dictionary
   • set
   • bytearray

-----------------------------------------------------------
Example 1: Immutable Objects (Integers)
-----------------------------------------------------------
"""

x = 10
y = x

print("x =", x)
print("y =", y)

# Changing y does NOT affect x because integers are immutable.
y = 15

print("\nAfter changing y:")
print("x =", x)
print("y =", y)

"""
Explanation:
-------------
Initially,

x ----> 10
y ----> 10

After writing:

y = 15

Python creates a new integer object (15) and makes y point
to it.

Now,

x ----> 10
y ----> 15

The original value of x remains unchanged.
"""

print("\nAssign x = y")
x = y

print("x =", x)
print("y =", y)

"""
Now both variables point to the same value (15).

x ----> 15
y ----> 15
"""

print("\n" + "=" * 55)

"""
-----------------------------------------------------------
Example 2: Immutable Objects (Strings)
-----------------------------------------------------------
"""

username = "pradeep"
x = "kumar"

print("username =", username)
print("x =", x)

# Assigning x to username changes only the reference.
username = x

print("\nAfter username = x")
print("username =", username)
print("x =", x)

"""
Explanation:
-------------
Strings are immutable.

Initially,

username ----> "pradeep"
x -----------→ "kumar"

After:

username = x

Both variables refer to the same string object.

username ----> "kumar"
x -----------→ "kumar"

The string "pradeep" is not modified.
Instead, username simply starts referring to another string.
"""

print("\n" + "=" * 55)

"""
Key Points
----------

✔ Variables store references to objects, not the actual data.

✔ Assignment (=) copies the reference, not the object.

✔ Immutable objects cannot be changed.
  Any modification creates a new object.

✔ Reassigning one variable never changes another variable
  that was pointing to the old object.

Examples of Immutable Types:
int, float, bool, str, tuple

Examples of Mutable Types:
list, dict, set, bytearray
"""