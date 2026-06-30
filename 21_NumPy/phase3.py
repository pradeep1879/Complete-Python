
"""
===========================================================
                NUMPY BASICS & OPERATIONS
===========================================================

Topics Covered
--------------
• Boolean Filtering & Masks
• Fancy Indexing & np.where()
• Array Concatenation & Stacking
• Array Shape Compatibility
• Aggregation Functions
• Vector Operations
• Vectorization
• Saving & Loading Arrays

This file demonstrates commonly used NumPy operations with
simple examples and a restaurant sales dataset.
"""

import numpy as np

# ==========================================================
# FILTERING
# ----------------------------------------------------------
# Boolean indexing selects elements satisfying a condition.
# ==========================================================

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

even_number = numbers[numbers % 2 == 0]
print("Even numbers", even_number)

# A mask is a Boolean array that can be reused.
mask = numbers > 5
print("Numbers greater than 5: ", numbers[mask])

# ==========================================================
# FANCY INDEXING & np.where()
# ----------------------------------------------------------
# Fancy indexing selects elements using indices.
# np.where() returns indices or performs conditional logic.
# ==========================================================

indices = [0, 2, 4]
print(numbers[indices])

where_result = np.where(numbers > 5)
print(where_result)
print("NP where", numbers[where_result])

condition_array = np.where(numbers > 5, numbers * 2, numbers)
print(condition_array)

# ==========================================================
# ADDING & REMOVING DATA
# ----------------------------------------------------------
# concatenate() joins arrays.
# vstack() adds rows.
# hstack() adds columns.
# delete() removes elements.
# ==========================================================

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

combined = np.concatenate((arr1, arr2))
print(combined)

# ==========================================================
# ARRAY COMPATIBILITY
# ----------------------------------------------------------
# Arrays should have compatible shapes before many
# mathematical operations.
# ==========================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 10])
c = np.array([7, 8, 9])

print("Compatiblity shapes", a.shape == b.shape)
print("Compatiblity shapes", a.shape == c.shape)

original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original, new_row))
print(original)
print("With new row \n", with_new_row)

new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("With new col \n", with_new_col)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
deleted = np.delete(arr, 4)
print("Array after deletion \n", deleted)

# ==========================================================
# BUSINESS EXAMPLE - RESTAURANT SALES ANALYSIS
# ----------------------------------------------------------
# Dataset Format:
# [Restaurant_ID, 2021, 2022, 2023, 2024]
# ==========================================================

import matplotlib.pyplot as plt

sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== Zomato Sales Analysis ====")
print("Sales data shape:\n", sales_data.shape)
print("Sample data:\n", sales_data[0:3])

# ==========================================================
# AGGREGATION FUNCTIONS
# ----------------------------------------------------------
# sum()    -> Total
# min()    -> Minimum
# max()    -> Maximum
# mean()   -> Average
# cumsum() -> Running Total
# ==========================================================

print(np.sum(sales_data, axis=0))

yearly_total = np.sum(sales_data[:, 1:], axis=0)
print("Yearly total:", yearly_total)

min_sales = np.min(sales_data[:, 1:], axis=1)
print("Minimum sales per restaurant:", min_sales)

max_sales = np.max(sales_data[:, 1:], axis=0)
print("Maximum sales per year:", max_sales)

avg_sales = np.mean(sales_data[:, 1:], axis=1)
print("Average sales per restaurant:", avg_sales)

cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print("Cumulative sum:\n", cumsum)

# Uncomment to visualize cumulative sales.
# plt.figure(figsize=(10, 6))
# plt.plot(np.mean(cumsum, axis=0))
# plt.title("Average cumulative sales")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()

# ==========================================================
# VECTOR OPERATIONS
# ----------------------------------------------------------
# Demonstrates addition, multiplication,
# dot product and angle between vectors.
# ==========================================================

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Sum of two vectors\n", vector1 + vector2)
print("Product of two vectors\n", vector1 * vector2)
print("Dot product\n", np.dot(vector1, vector2))

angle = np.arccos(
    np.dot(vector1, vector2) /
    (np.linalg.norm(vector1) * np.linalg.norm(vector2))
)
print(angle)

# ==========================================================
# VECTORIZATION
# ----------------------------------------------------------
# Applies an operation to every element without loops.
# ==========================================================

restaurant_types = np.array(
    ['biryani', 'chinese', 'pizza', 'burger', 'cafe']
)

vectorized_upper = np.vectorize(str.upper)
print("Vectorized Upper:\n", vectorized_upper(restaurant_types))

# Convert yearly sales into monthly averages.
monthly_avg = sales_data[:, 1:] / 12
print("Monthly average:", monthly_avg)

# ==========================================================
# SAVING & LOADING ARRAYS
# ----------------------------------------------------------
# np.save() stores arrays in .npy format.
# np.load() loads them back.
# ==========================================================

array1 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

array2 = np.random.rand(3, 3)
array3 = np.zeros((3, 3))

np.save("array1.npy", array1)
np.save("array2.npy", array2)
np.save("array3.npy", array3)

loaded_array1 = np.load("array1.npy")
print(loaded_array1)
