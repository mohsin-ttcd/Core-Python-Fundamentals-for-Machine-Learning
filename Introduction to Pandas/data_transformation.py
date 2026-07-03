import pandas as pd

# data ingestion
df = pd.read_csv('titanic.csv')

# data exploration
# print(df.info())

# find exact middle value of Age & fill missing Age value
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# remove Cabin column from DataFram
df_cleaned = df.drop(['Cabin'], axis=1)
df_cleaned = df_cleaned.dropna(subset=['Embarked'])
df_cleaned = df_cleaned.reset_index(drop=True)


# Handling Duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Data Transformation
# Creating New Columns

# Creating New Columns automatically at end position
# df_cleaned['Family'] = df_cleaned['SibSp'] + df_cleaned['Parch']
# print(df_cleaned.head())
# print(df_cleaned[['SibSp', 'Parch', 'Family']].head())

# Creating New Columns at specific position
temp_family = df_cleaned['SibSp'] + df_cleaned['Parch']
col_index = df_cleaned.columns.get_loc('Parch')

if 'Family' not in df_cleaned.columns:
    df_cleaned.insert(loc=col_index + 1, column='Family', value=temp_family)
    print('New column inserted')
    print(df_cleaned.head())

else:
    print("Family columns already in the DataFrame")


# Grouping Data 
df_class = df_cleaned.groupby('Pclass')['Pclass'].count()
print("Sum of passengers class by there gender:")
print(df_class.head())

df_survived = df_cleaned.groupby('Sex')['Survived'].sum()
print(df_survived)