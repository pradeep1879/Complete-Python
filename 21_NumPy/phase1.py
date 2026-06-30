import numpy as np

arr_1d = np.array([1, 3, 5, 7, 9])
print("1D Array: ", arr_1d)


arr_2d = np.array([[1, 3, 5, 7, 9], [3, 5, 7, 9, 9]])
print("2D Array: ", arr_2d)


### List vs Numpy

list = [3, 4, 6, 8]
print("multiplication of list: ", list * 2)  ## =>[3, 4, 6, 8, 3, 4, 6, 8]

np_arry = np.array([3, 8, 9, 2])
print("multiplication of np array: ", np_arry * 2) ## => [6, 16, 18, 4]

import time 
start = time.time()

py_list = [i*2 for i in range(1000000)]
print("\n List operation time: ", time.time() - start)


start = time.time()
np_array = np.arange(100000)
print("\n Numpy operation time: ", time.time() - start)


## Creating array from scratch

zeros = np.zeros((3, 4))
print("Zeros array: \n", zeros)

ones = np.ones((3, 4))
print("Ones array: \n", ones)

full = np.full((2, 2), 9)
print("Full array: \n", full)

random = np.random.random((2, 3))
print("Random array: \n", random)

sequence = np.arange(0, 10, 2)
print("Sequence array: \n", sequence)



### Array, Vectors, Tensors


vector = np.array([2, 3, 4])
print("Vector : \n", vector)

matrix = np.array([[23, 33, 29],[32, 43, 34]])
print("Matrix : \n", matrix)


tensor = np.array([[[1, 2], [4, 6]], 
                   [[8, 9], [1, 3]]])
print("Tensor : \n", tensor)
                    

#### Array properties

arr = np.array([[23, 33, 29],
                [32, 43, 34]])

print("Shape : \n", arr.shape)
print("Dimension : \n", arr.ndim)
print("Size : \n", arr.size)
print("DType: \n", arr.dtype)

### Array Reshaping


arr = np.arange(12)
print("Original array \n", arr)

reshaped = arr.reshape((3, 4))
print("Reshaped array \n", reshaped)

flattend = reshaped.flatten()
print("Flattend array \n", flattend)

# ravel (returns view, instead of copy)
raveled = reshaped.ravel()
print(" Reveled array \n", raveled)


# Transpose
transpose = reshaped.T
print(" Transposed array \n", transpose)



