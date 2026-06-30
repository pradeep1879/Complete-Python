# # Give a list of number, count how many are postive
# number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# postive_number_count = 0

# for num in number:
#     print(num)
#     if num > 0:
#         postive_number_count += 1
# print("Final count of postiv number: " , postive_number_count)


#Ques.Calculate the sum of even numbers up to a given number n.

n = 10
total_even = 0
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        total_even += 1
        sum_even += i
print("Total  even number is: ", total_even)
print("Total sum of even number is: ", sum_even)



# #Ques. Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x', i, "=", number * i)



# #Ques. Reverse a string using loop.

# input_str = "python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)

# str = "teeteraidfadf"

# for char in str:
#     print(char)
#     if str.count(char) == 1:
#         print("char is:",char)
#         break




# #Ques.Factorial

factorial = 1
number = 5

while number > 0:
    print(number)
    factorial = factorial * number
    number = number - 1 
print(factorial)


#Ques.Validate the input

# while True:
#     number = int(input("Enter a value b/w 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number")




#Ques.Prime checker

number = 23
is_prime = True

if number > 1:
    for i in  range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)



#Ques. Check all the element in a list are unique.If a duplicate is found, exit the loop, and print the 
#      duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:",item)
        break
    unique_item.add(item)
print(unique_item)


#Ques. Implement an exponential backoff strtegy that doubles the wait time between retries, starting
# from 1 second, but stops after 5 retries.

import time

wait_time = 1 
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts + 1, "-wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *=2
    attempts += 1
