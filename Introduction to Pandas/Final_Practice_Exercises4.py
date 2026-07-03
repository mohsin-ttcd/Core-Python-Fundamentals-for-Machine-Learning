# Practice Exercise 4: Putting It All Together
# Using the new AgeGroup column you just created, find the survival rate for 'Child' vs. 'Adult' passengers. Use .groupby().

import pandas as pd

def categorize_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'
    
df = pd.read_csv('titanic.csv')

df_median = df['Age'].median()

df['Age'] = df['Age'].fillna(df_median)

df_cleaned = df.drop('Cabin', axis=1)

df_cleaned = df_cleaned.dropna(subset='Embarked')

df_cleaned = df_cleaned.drop_duplicates()

df_cleaned['AgeGroup'] = df['Age'].apply(categorize_age)

# the survival rate for 'Child' vs. 'Adult' passengers
survival_rate= df_cleaned.groupby('AgeGroup')['Survived'].mean()
survival_rate_data = survival_rate * 100

print('Survival percentages for Child vs. Adult passengers')
print(f"{survival_rate.to_string(float_format="{:.2f}".format)}")
print('\nSurvival rate for Child vs. Adult passengers')
print(f"{survival_rate_data.map("{:.0f}%".format)}")


