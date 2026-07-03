import pandas as pd


column_names = [
    'Class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity_of_Ash',
    'Magnesium', 'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols',
    'Proanthocyanins', 'Color_Intensity', 'Hue', 'OD280_OD315_of_Diluted_Wines',
    'Proline'
]


df = pd.read_csv('wine.data', names=column_names)
# print(df.head())
# print(df.info())
# print(df.describe())
class_value = df['Class'].value_counts()
# print(class_value)

Alcohol_Column = df[['Alcohol', 'Malic_Acid', 'Ash']].head()
# print(Alcohol_Column)

# print(df.loc[2:5])


alco_14 = (df['Alcohol'] > 14)
high_alco_wine = df[df['Alcohol'] > 14]
print(alco_14.head())
print(high_alco_wine.head())