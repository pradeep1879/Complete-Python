import numpy as np

## Filter

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_number = numbers[numbers % 2 == 0]
print("Even numbers", even_number)

## Filter with mask
mask = numbers > 5
print("Numbers greater than 5: ", numbers[mask])

## Fancy indexing vs np.where()

indices = [0, 2, 4]
print(numbers[indices])

where_result = np.where(numbers > 5)
print(where_result)
print("NP where", numbers[where_result])

condition_array = np.where(numbers > 5, numbers*2, numbers)
print(condition_array)


## Adding and removing data

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

combined = np.concatenate((arr1, arr2))
print(combined)


### Array compatiblity

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



## Advanced operation with Business examples.

#Data structure: [restaurant_id, 2021 , 2022, 2023, 2024]
import matplotlib.pyplot as plt

sales_data = np.array([
        [1, 150000, 180000, 220000, 250000],  ## Paradise Biryani
        [2, 120000, 140000, 160000, 190000],  ## Beijing Bites
        [3, 200000, 230000, 260000, 300000],  ## Pizza Hub
        [4, 180000, 210000, 240000, 270000],  ## Burger Point
        [5, 160000, 185000, 205000, 230000]   ## Chai Point
])


print("==== Zomata sales analysis ====")
print("Sales data shape: \n", sales_data.shape)
print("Sample data for 1st restaurant: \n", sales_data[0:3])

# total sales per year
print(np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print("Yearly total: ",yearly_total)

## minimum sales per restaurant 
min_sales = np.min(sales_data[:, 1:], axis=1)
print("minimum sales per restaurant: ",min_sales)

## maximum sales per year

max_sales = np.max(sales_data[:, 1:], axis=0)
print("maximum sales per year: ",max_sales)

## Average per restaurant
avg_sales = np.mean(sales_data[:, 1:], axis=1)
print("Average per restaurant: ",avg_sales)

## Cumulative sum
cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print("Cumulative sum: ",cumsum)


# plt.figure(figsize=(10, 6))
# plt.plot(np.mean(cumsum, axis=0))
# plt.title("Average cumulative sales across all restaurant")
# plt.xlabel("years")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()



vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])
print("Sum of two vectors \n", vector1 + vector2)
print("Product of two vectors \n", vector1 * vector2)
print("Dot product of two vectors \n", np.dot(vector1, vector2))

angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)


restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe'])
vectorized_upper = np.vectorize(str.upper)

print("Vectorized Upper: \n ", vectorized_upper(restaurant_types))



monthly_avg = sales_data[:, 1:] / 12
print("Monthly average: ",monthly_avg)


################################################################################################

array1 =  np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
array2 = np.random.rand(3, 3)
array3 = np.zeros((3, 3))

np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)

loaded_array1 = np.load('array1.npy')
print(loaded_array1)

