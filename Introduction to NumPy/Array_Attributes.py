import numpy as np


num_1d = np.arange(9)
print(num_1d)

num_1d_shape = num_1d.shape
print(num_1d_shape)

num_2d = num_1d.reshape(9,-1)
print(num_2d)

num_2d_shape = num_2d.shape
print(num_2d_shape)

num_1d = np.arange(6)
print(num_1d)
print(num_1d.ndim)
print(num_1d.dtype)

num_2d = num_1d.reshape(3,-1)
print(num_2d)
print(num_2d.ndim)
print(num_2d.dtype)