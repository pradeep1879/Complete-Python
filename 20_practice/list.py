#Ques. Find tha largest and smallest number in the list.
nums = [3, 7, 2, 9, 4]
print(max(nums), min(nums))

#Ques. Reverse a list without using reverse() or slicing.
#range(start, stop, step)
list0 = [2, 4, 5, 8, 9, 1]
rev = []

for i in range(len(list0)-1, -1, -1):
    rev.append(list[i])
print(rev)


for i in range(len(list0)-3, -1, -1):
    rev.append(list[i])
print(rev)

#Ques.Count how many times each element appears in list.

list1 = [3, 2, 3, 5, 2, 4, 3, 8, 9, 8]
fre = {}
for i in list1:
    fre[i] = fre.get(i, 0) + 1
print(fre) 

#Ques.Remove duplicates but keep the original order.

list2 = [3, 4, 8, 3,  8, 7, 5, 4]
result = []
seen = set()

for i in list2:
    if i  not in seen:
        result.append(i)
        seen.add(i)
print(result)



#Ques. Find second largest number in the list.
list3 = [10, 20, 4, 45, 99]
unique = list(set(list3))
unique.remove(max(unique))
print(max(unique))


#Ques. Combine two list index-wise.
a = [3, 1, 5]
b = [8, 9, 3]
result = [a[i] + b[i] for i in range(len(a))]
print(result)

#Qes. Factorial question.
factorial = 1
number = 5

while number > 0:
    factorial = factorial * number
    number = number - 1
print(factorial)

