# Array Indexing and Slicing

import numpy as np

# 1D array

np_array = np.arange(10)
print(f"Original array: {np_array}")

np_array[0] = 100

array_index = np_array[6]
print(array_index)

array_index2 = np_array[2:5]
print(array_index2)

print(np_array)


# 2D array

ar = np.arange(0,12)
array2D = ar.reshape(3,-1)
print(array2D)

element = array2D[2, 3]
print("\ntargeted element: ",element)

# slice start from row: index 0 to end and column: index 2 to end
# index start from 0 as always
slice_2d = array2D[0:,2:]
print("\nSlice rows, and columns:\n", slice_2d)