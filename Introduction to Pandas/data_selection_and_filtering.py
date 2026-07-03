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

# Data Selection and Filtering
# Select a single column that retun series
print("Select the Age column: ")
ages = df_cleaned['Age']
print(ages.head())

# Select a multiple column that retun datafram
print("Select multiple column")
all_int = df_cleaned[['PassengerId', 'Survived', 'Pclass', 'SibSp', 'Parch']]
print(all_int.head())

# Filtering Rows with Conditions
print("Print passengers details more than 50years old")
df_passengers = df_cleaned[df_cleaned['Age'] > 50]
print(df_cleaned.head())

print("Passengers with siblings 1, 1st class and male")
df_passengers = df_cleaned[(df_cleaned['Pclass'] == 1) & (df_cleaned['SibSp'] == 1) & (df_cleaned['Sex'] == 'male')]
print(df_passengers.head())
print(df_passengers.shape)
