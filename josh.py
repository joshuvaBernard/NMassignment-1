import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('house_price.csv')

price_variable = 'Price'
bedroom_variable = 'number of bedrooms'
variables = ['number of bedrooms', 'number of bathrooms', 'Area of the house(excluding basement)', 'Price']


# print(df[variable].describe())


# To perform uni-variate analysis on price of the houses
sns.histplot(data=df, x=price_variable)
plt.show()
#
# sns.boxplot(data=df, x=price_variable)
# plt.show()
# sns.kdeplot(data=df, x=price_variable)
# plt.show()



# To perform bi-variate analysis on price and number of bedrooms
sns.scatterplot(data=df, x=price_variable, y=bedroom_variable)
plt.show()

# print('Correlation coefficient:', df[price_variable].corr(df[bedroom_variable]))
#
#
# sns.lineplot(data=df, x=price_variable, y=bedroom_variable)
# plt.show()
#
# sns.regplot(data=df, x=price_variable, y=bedroom_variable)
# plt.show()
#
# sns.heatmap(data=df[[price_variable, bedroom_variable]].corr(), annot=True)
# plt.show()


#multivariate
corr_matrix = df[variables].corr()
# print(corr_matrix)
sns.heatmap(data=corr_matrix, annot=True)
plt.show()
# sns.pairplot(data=df[variables])
# plt.show()
#
# sns.set(style='ticks')
# sns.pairplot(df[variables], diag_kind='kde', hue='target_variable')
# plt.show()

# Perform descriptive statistics on the dataset.

# mean = df.mean()
# median = df.median()
# mode = df.mode()
#
# range = np.ptp(df)
# variance = df.var()
# std_dev = df.std()
#
# skewness = df.skew()
# kurtosis = df.kurtosis()
#
# stats_df = pd.DataFrame({'mean': mean, 'median': median, 'mode': mode, 'range': range, 'variance': variance, 'std_dev': std_dev, 'skewness': skewness, 'kurtosis': kurtosis})
#
# print(stats_df)


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
