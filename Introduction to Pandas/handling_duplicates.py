import pandas as pd

# data ingestion
df = pd.read_csv('titanic.csv')

# data exploration
print(df.info())

# find exact middle value of Age & fill missing Age value
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# remove Cabin column from DataFram
df_cleaned = df.drop(['Cabin'], axis=1)
df_cleaned = df_cleaned.dropna(subset=['Embarked'])
df_cleaned = df_cleaned.reset_index(drop=True)


# Handling Duplicates
print(df_cleaned.duplicated().sum())

print(f"before remove duplicates: {len(df_cleaned)}")
df_cleaned = df_cleaned.drop_duplicates()
print(f"after remove duplicates: {len(df_cleaned)}")
