import numpy as np

# Part 4: Statistical Functions

data = np.array([5, 10, 15, 20, 25, 30])

print("Statistical Functions for 1D data table")
print(f"Sum of array: {np.sum(data)}")
print(f"Mean (avg) of array: {np.mean(data):.2f}")
print(f"Standard Diviation: {np.std(data):.2f}")
print(f"Max number of array: {np.max(data)}\n")

print("Statistical Functions for 2D data table")
data2D = np.arange(0, 21)
data2 = data2D.reshape(3,-1)
print(data2)
print(f"Sum of 2D array: {np.sum(data2)}")
print(f"Mean (avg) of 2D array: {np.mean(data2):.2f}")
print(f"Standard Diviation: {np.std(data2):.2f}")
print(f"Max number of 2D array: {np.max(data2)}")
print(f"Lenth of 2D array: {data2.size}")


