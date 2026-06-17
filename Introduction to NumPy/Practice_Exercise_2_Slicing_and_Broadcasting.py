import numpy as np

# Final Practice Exercises

# Practice Exercise 2: Slicing and Broadcasting
# Using the my_matrix you just created, select and print the entire second row.
# Create a 1D array named modifier with 4 elements: [100, 200, 300, 400].
# Use broadcasting to add the modifier array to every row of my_matrix and print the result.

# Create my_matrix 2D array
my_matrix = np.random.randint(1,50, size=(3,4))
second_row = my_matrix[1:2]
print("The entire second row: ", second_row)

#Created a 1D array
modifier = np.array([100, 200, 300, 400])

# add the modifier array to every row 
broadcasting_matrix = second_row + modifier
print("Matrix after broadcasting addition",broadcasting_matrix)