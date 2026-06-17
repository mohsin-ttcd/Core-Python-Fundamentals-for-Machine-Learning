import numpy as np

# Final Practice Exercises

"""Practice Exercise 1: Array Creation and Statistics

Create a 3x4 NumPy array named my_matrix containing random integers between 1 and 50.
Print the matrix.
Calculate and print the mean of the entire matrix.
Calculate and print the sum of each column."""

my_matrix = np.random.randint(1,50, size = (3,4))
print("The matrix: \n",my_matrix)

# the mean of the entire matrix.
matrix_mean = my_matrix.mean()
print(f"Mean of the entire matrix: {matrix_mean:.2f}")

# the sum of entire matrix
matrix_sum = my_matrix.sum()
print("Sum of entire matrix: ",matrix_sum)

# the sum of each column
column_sum = my_matrix.sum(axis=0)
print("Sum of each column: ",column_sum)

# the sum of each row
row_sum = my_matrix.sum(axis=1)
print("Sum of each row: ",row_sum)