# Exercise 2: Filtering with Multiple Conditions

# Task: Filter the wine_df to find all wines that belong to Class 1 AND have a Magnesium level greater than 120.

import pandas as pd
import numpy as np

column_header = [
    'Class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity_of_Ash',
    'Magnesium', 'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols',
    'Proanthocyanins', 'Color_Intensity', 'Hue', 'OD280_OD315_of_Diluted_Wines',
    'Proline'
]

wine_df = pd.read_csv('wine.data', names=column_header)

# print(wine_df.head())
# print(wine_df.info())
# print(wine_df.describe())

high_magnesium = wine_df[(wine_df['Class'] == 1) & (wine_df['Magnesium'] > 120)]
print("\nAll wines that belong to Class 1 AND have a Magnesium level greater than 120\n")
print(high_magnesium)