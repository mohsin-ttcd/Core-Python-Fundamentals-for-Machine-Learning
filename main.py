import numpy as np


num_1d = np.arange(9)
print(num_1d)

num_1d_shape = num_1d.shape
print(num_1d_shape)

num_2d = num_1d.reshape(3,3)
print(num_2d)

num_2d_shape = num_2d.shape
print(num_2d_shape)

