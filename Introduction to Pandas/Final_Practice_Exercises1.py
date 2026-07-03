# Select all the male passengers who were in 3rd Class (Pclass == 3) and did not survive (Survived == 0). How many are there?

import pandas as pd
import numpy as np

# data ingestion
df = pd.read_csv('titanic.csv')

# remove duplicated row
df = df.drop_duplicates()

df_male = df[(df['Sex'] == 'male') & (df['Pclass'] == 3) & (df['Survived'] == 0)]

print(f"\nMale passengers who did not survived with 3rd class ticket: ")
print(df_male .head())
print(f"\nSum of Male passengers who did not survived with 3rd class ticket:{len(df_male)}")
