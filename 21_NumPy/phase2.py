import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic slicing", arr[1:5]) ## => [2, 3, 4, 5]
print("With step ", arr[1:8:3])  ## => [2, 5, 8]
print("Negative indexing", arr[-3]) ## => 8


arr_2d = np.array([[2, 4, 5, 8],
                   [7, 9, 3, 9],
                   [1, 4, 9, 3]])
print("Specific element", arr_2d[1,2]) ### (row index, column index)
print("Entire row", arr_2d[1])
print("Entire column", arr_2d[:, 1])      #For column 


### Shorting

unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Sorted array", np.sort(unsorted))

arr_2d_unsorted = np.array([[2, 5, 4], 
                            [3, 7, 6],
                            [8, 2, 9]])
print("Sorted 2D array by column\n", np.sort(arr_2d_unsorted, axis=0))
print("Sorted 2D array by row\n", np.sort(arr_2d_unsorted, axis=1))



#### Filtering


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_number = numbers[numbers % 2 == 0]
print("Even numbers \n ", even_number)