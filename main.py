import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('house_price.csv')

price_variable = 'Price'
bedroom_variable = 'number of bedrooms'
variables = ['number of bedrooms', 'number of bathrooms', 'Area of the house(excluding basement)', 'Price']

# To perform uni-variate analysis on price of the houses
sns.histplot(data=df, x=price_variable)
plt.show()

# To perform bi-variate analysis on price and number of bedrooms
sns.scatterplot(data=df, x=price_variable, y=bedroom_variable)
plt.show()

#multivariate
corr_matrix = df[variables].corr()
# print(corr_matrix)
sns.heatmap(data=corr_matrix, annot=True)
plt.show()

# print(df.describe())
corr = df.corr()
print(corr)
sns.heatmap(corr, cmap='coolwarm')
plt.show()
print('Skewness:')
print(df.skew())
print('\nKurtosis:')
print(df.kurt())
print('Mode:')
print(df.mode())

#handle missing
print(df.isnull().sum())
df.dropna(inplace=True)
df.dropna(axis=1, inplace=True)
df.fillna(df.mean(), inplace=True)
df.fillna(df.median(), inplace=True)
df.fillna(df.mode(), inplace=True)
df.fillna(method='ffill', inplace=True)
df.fillna(method='bfill', inplace=True)
df.interpolate(inplace=True)
df.fillna(-999, inplace=True)
