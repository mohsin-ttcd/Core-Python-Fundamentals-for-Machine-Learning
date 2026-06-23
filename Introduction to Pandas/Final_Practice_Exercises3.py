# Practice Exercise 3: Creating a Column with a Function
# Define a function called categorize_age that takes an age as input. If the age is less than 18, it should return 'Child'. Otherwise, it should return 'Adult'.
# Use the .apply() method to create a new column in df_cleaned called AgeGroup by applying your function to the Age column.

import pandas as pd

def categorize_age(age):
    #If the age is less than 18
    if age < 18:
        return 'Child'
    else:
        return 'Adult'
    
# load data
df = pd.read_csv('titanic.csv')

# calculate median
df_median = df['Age'].median()

# fill blank age with median
df['Age'] = df['Age'].fillna(df_median)

# remove Cabin column from datafram
df_cleaned = df.drop('Cabin', axis=1)

# remove 2 empty row of Embarked
df_cleaned = df_cleaned.dropna(subset='Embarked')

# remove duplicate
df_cleaned = df_cleaned.drop_duplicates()

df_cleaned['AgeGroup'] = df_cleaned['Age'].apply(categorize_age)

print(df_cleaned.head())
