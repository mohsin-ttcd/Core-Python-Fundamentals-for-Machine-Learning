# Final Exercise: Multi-Step Analysis

# Task: Write a single chain of commands or multiple commands to achieve the following:

# First, calculate the average Color_Intensity for the entire dataset.
# Next, select all wines that belong to Class 3.
# From that selection of Class 3 wines, further filter it to find only those with a Color_Intensity greater than the average you calculated in step 1.
# Finally, from the resulting data, display only the Alcohol, Color_Intensity, and Proline columns.

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

# the average Color_Intensity for the entire dataset.
Color_Intensity_average = wine_df['Color_Intensity'].mean()
# print(f"\nThe average Color_Intensity for the entire dataset: {Color_Intensity_average:.2f}\n")

#select all wines that belong to Class 3.
class_3_wine = wine_df[wine_df['Class'] == 3]
# print("Select all wines that belong to Class 3")
# print(f"{class_3_wine}\n")

# From that selection of Class 3 wines, further filter it to find only those with a Color_Intensity greater than the average you calculated in step 1.
greater_avg_class_3 = class_3_wine[class_3_wine['Color_Intensity'] > Color_Intensity_average]
# print("Filter out wine that have greater Color_Intensity than the average Color_Intensity")
# print(f"{greater_avg_class_3}\n")

# Finally, from the resulting data, display only the Alcohol, Color_Intensity, and Proline columns.
final_df = greater_avg_class_3[["Alcohol", "Color_Intensity", "Proline"]]
print("\nDisplay only the Alcohol, Color_Intensity, and Proline columns\n")
print(final_df)