import numpy as np

# Final Practice Exercises

# Practice Exercise 3: Practical Application
# You have a NumPy array representing five different product prices: prices = np.array([19.99, 25.50, 9.95, 32.00, 65.75]).

# Write a single line of code to calculate the final price of each product after adding a 20% tax. Print the resulting array.

prices = np.array([19.99, 25.50, 9.95, 32.00, 65.75])

# more time complex
after_tax_prices = prices + (prices * .20)
print(f"The final price of each product after adding a 20% tax: {after_tax_prices}")

# less time complex
final_prices = prices * 1.20
print("Final prices with tax:", final_prices)