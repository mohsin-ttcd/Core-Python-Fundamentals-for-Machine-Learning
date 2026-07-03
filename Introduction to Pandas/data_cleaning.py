import pandas as pd

# data ingestion
df = pd.read_csv('titanic.csv')

# data exploration
print(df.info())

# find exact middle value of Age
median_age = df['Age'].median()

# fill missing Age value
df['Age'] = df['Age'].fillna(median_age)

# remove Cabin column from DataFram
df_cleaned = df.drop(['Cabin'], axis=1)

df_cleaned = df_cleaned.dropna(subset=['Embarked'])
print(df_cleaned.info())

df_cleaned = df_cleaned.reset_index(drop=True)
print(df_cleaned)

