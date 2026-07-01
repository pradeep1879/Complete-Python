# ==========================================================
# Question 1
# Count how many positive numbers are present in a list.
# ==========================================================

# number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# postive_number_count = 0

# for num in number:
#     print(num)
#     if num > 0:
#         postive_number_count += 1
# print("Final count of positive numbers:", postive_number_count)


# ==========================================================
# Question 2
# Calculate the total count and sum of even numbers
# from 1 to n.
# ==========================================================

n = 10
total_even = 0
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total_even += 1
        sum_even += i

print("Total even numbers:", total_even)
print("Sum of even numbers:", sum_even)


# ==========================================================
# Question 3
# Print the multiplication table of a number.
# Skip the 5th iteration using continue.
# ==========================================================

# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, "x", i, "=", number * i)


# ==========================================================
# Question 4
# Reverse a string without using slicing.
# ==========================================================

# input_str = "python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str

# print(reversed_str)


# ==========================================================
# Question 5
# Find the first non-repeating character in a string.
# ==========================================================

# string = "teeteraidfadf"

# for char in string:
#     print(char)
#     if string.count(char) == 1:
#         print("First unique character:", char)
#         break


# ==========================================================
# Question 6
# Calculate the factorial of a number using while loop.
# ==========================================================

factorial = 1
number = 5

while number > 0:
    print(number)
    factorial = factorial * number
    number = number - 1

print("Factorial:", factorial)


# ==========================================================
# Question 7
# Keep asking the user for input until the value
# is between 1 and 10.
# ==========================================================

# while True:
#     number = int(input("Enter a value between 1 and 10: "))

#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number")


# ==========================================================
# Question 8
# Check whether a number is prime.
# A prime number has exactly two factors:
# 1 and itself.
# ==========================================================

number = 23
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

print(is_prime)


# ==========================================================
# Question 9
# Check whether all elements in a list are unique.
# Stop as soon as a duplicate is found.
# ==========================================================

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:

    if item in unique_item:
        print("Duplicate:", item)
        break

    unique_item.add(item)

print(unique_item)


# ==========================================================
# Question 10
# Exponential Backoff
#
# Retry an operation.
# After every failed attempt, double the waiting time.
#
# 1s → 2s → 4s → 8s → 16s
# ==========================================================

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:

    print("Attempt", attempts + 1, "- Wait Time:", wait_time, "seconds")

    time.sleep(wait_time)

    wait_time *= 2
    attempts += 1