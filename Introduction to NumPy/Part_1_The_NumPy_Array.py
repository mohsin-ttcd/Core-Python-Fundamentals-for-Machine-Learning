# [ ] Lab: Introduction to NumPy for Data Science

# Objectives
# After completing this lab, you will be able to:

# Understand the difference between a Python list and a NumPy array.

# Create 1D and 2D NumPy arrays.

# Perform indexing and slicing to access array data.

# Apply mathematical and statistical operations to arrays.

# Understand how Broadcasting simplifies operations on arrays of different sizes.


import numpy as np

# create numpy array
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

my_np_array = np.array(my_list)
print(my_np_array)
print(type(my_np_array))

# create 2-dimentional array

my_2d_list = [[1, 2, 3], [4, 5, 6]]
print(my_2d_list)
print(type(my_2d_list))

my_2d_array = np.array(my_2d_list)
print(my_2d_array)
print(type(my_2d_array))


# An array of all zeros with shape (2 rows, 3 cols)
num = (5,10)
print(num)
print(type(num))

zeros_array = np.zeros(num)
print(zeros_array)
print(type(zeros_array))

num = (5,10)
zeros_array = np.zeros(num, dtype=int)
print(zeros_array)
print(type(zeros_array))

# Create a Matrix of Ones
num = (5,10)
one_array = np.ones(num)
print(one_array)
one_array = np.ones(num, dtype=int)
print(one_array)


num = ((5,10), (2,4))
array = np.array(num)
print(array)
print(type(array))

# Like Python's range(), but creates an array (start, stop, step)
range_array = np.arange(0, 10, 2) 
print("\nArray from a range:", range_array)

num = (1,5,3)
# range_array = np.arange(1,5,3)
range_array = np.arange(*num)
print(range_array)
print(*num)

num_1d = np.arange(9)
print(num_1d)

num_2d = num_1d.reshape(3,3)
print(num_2d)