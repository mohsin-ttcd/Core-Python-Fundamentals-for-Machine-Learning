# Broadcasting is method that is replaces the traditional python loop
# numpy replace loop with built-in array operation called vectorization.

import numpy as np

np_1D_arr = np.arange(1,10)
np_2D_arr = np_1D_arr.reshape(3,-1)
print("*** Original Array ***")
print(np_1D_arr)
print(np_2D_arr)

print("\n*** Broadcasting ***")

cast_1D = np_1D_arr + 5
cast_2D = np_2D_arr + 7
print(cast_1D)
print(cast_2D)