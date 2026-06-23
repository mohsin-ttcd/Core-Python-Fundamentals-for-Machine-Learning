#### Practice Exercise 2: Grouping and Aggregation

# **Calculate the average `Fare` paid by passengers for each passenger class (`Pclass`).** Which class paid the most on average?

import pandas as pd
import numpy as np

# data ingestion
df = pd.read_csv('titanic.csv')

# remove duplicates
df = df.drop_duplicates()

# group data by class
df_fare_avg = df.groupby('Pclass')['Fare'].mean()
print(f"The average 'Fare' paid by the each passengers class: ")
print(f"{df_fare_avg}")

print(f"Class {df_fare_avg.idxmax()} paid the most on average!")

