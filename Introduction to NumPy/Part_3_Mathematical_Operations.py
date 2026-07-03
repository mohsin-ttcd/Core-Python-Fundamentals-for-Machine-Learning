# Part 3: Mathematical Operations

import numpy as np

# np_array = np.arange(10,20)
# print("original array",np_array)

# np_addition =  np_array + 10
# print("Numpy addition: ",np_addition)

# np_subtraction = np_array - 3
# print("Numpy subtraction: ", np_subtraction)

# np_multiplication = np_array * 2
# print("Numpy multiplication", np_multiplication)

# np_division = np_array / 2
# print("Numpy division: ",np_division)

# np_square = np_array ** 2
# print("Numpy square: ", np_square)


# Element-by-Element Operations

np_1arr = np.arange(1,6)
np_2arr = np.arange(6,11)

print("** Original array **")
print(np_1arr)
print(np_2arr)

print("\n** Element-by-Element Operations **")
sum_of_2_array = np_1arr + np_2arr
print(sum_of_2_array)