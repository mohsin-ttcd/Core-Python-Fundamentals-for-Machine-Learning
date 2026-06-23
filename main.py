import pandas as pd

# Part 1: Data Ingestion
df = pd.read_csv('titanic.csv')

# Part 3: Data Cleaning
# find the exact middle value of the Age column
median_age = df['Age'].median()

# fill missing value in Age column
df['Age'] = df['Age'].fillna(median_age)

# remove cabin column entirely
df_clean = df.drop('Cabin', axis=1)


# remove Nan value from the DataFram column Embarked
df_clean = df_clean.dropna(subset=['Embarked'])
df_clean = df_clean.reset_index(drop=True)



# Handling Duplicates
# print(df_clean.duplicated().sum())
df_clean = df_clean.drop_duplicates()
# print(len(df_clean))

# Selecting Columns
ages = df_clean['Age']
# print(ages.head())

name_sex_age = df_clean[['Name', 'Sex', 'Age']]
# print(name_sex_age.head())

# Filtering Rows with Conditions

older_passengers = df_clean[df_clean['Age'] < 50]
# print(f"Older passengers: ")
# print(older_passengers.head())

# Combine conditions: find all females in first class

female_1st = df_clean[(df_clean['Pclass'] == 1) & (df_clean['Sex'] == 'female')]
# print(f"First class feamle: ")
# print(female_1st.head())

male_1st = df_clean[(df_clean['Pclass'] == 1) & (df_clean['Sex'] == 'male')]
# print(f"First class male: ")
# print(male_1st.head())


# Creating New Columns
# print(df_clean.head())
# Create a new column 'FamilySize' by adding SibSp and Parch
# df_clean['Family'] = df_clean['SibSp'] + df_clean['Parch']
# df_clean_sub = df_clean[['SibSp', 'Parch', 'Family']]
# print(df_clean_sub.head())
# print(df_clean.head())

family_data = df_clean['SibSp'] + df_clean['Parch']
col_index = df_clean.columns.get_loc('Parch')

if 'Family' not in df_clean:
    df_clean.insert(loc=col_index + 1, column='Family', value=family_data)

else:
    print('"Family" is alreay in the DataFram')


# print(df_clean.head())


# Grouping Data
# 1. Group the DataFrame by the 'Sex' column
# 2. Select the 'Survived' column
# 3. Calculate the mean of that column for each group
df_clean_group = df_clean.groupby('Sex')['Age'].mean()
print(df_clean_group)

df_clean_group = df_clean.groupby('Sex')['Age'].count()
print(df_clean_group)

df_clean_group = df_clean.groupby('Sex')['Age'].median()
print(df_clean_group)