import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')

def categorical_eda(df, feature, fig_size):
	print('Unique values:', df[feature].unique())
	print('No. of unique values:', df[feature].nunique())
	print('Missing values count:', df[feature].isna().sum(), '/ {}'.format(len(df[feature])))
	print('Missing values %:', df[feature].isna().mean())
	print('Value counts: ')
	print(df[feature].value_counts(normalize = True) * 100)
	plt.figure(figsize = fig_size)
	sns.countplot(data = df, x = feature, palette = 'ch:.25_r')
	plt.xticks(rotation = 90)
	plt.title('{} countplot'.format(feature))
	plt.show()

def timeseries_eda(df, feature, fig_size):
	print('Unique values:', df[feature].unique())
	print('No. of unique values:', df[feature].nunique())
	print('Missing values count:', df[feature].isna().sum(), '/ {}'.format(len(df[feature])))
	print('Missing values %:', df[feature].isna().mean())
	print('Value counts: ')
	print(df[feature].value_counts(normalize = True) * 100)
	#df[feature] = pd.to_datetime(df[feature])
	date_series = df.groupby(pd.to_datetime(df[feature]).dt.strftime('%Y-%m'))['id'].size().sort_index()
	print("Description: ")
	print(date_series.describe())
	plt.figure(figsize = fig_size)
	sns.lineplot(data = date_series, marker = 'o')
	plt.xticks(rotation = 90)
	plt.title('{} countplot'.format(feature))
	plt.show()

def continous_eda(df, feature, fig_size):
	print('Missing values count:', df[feature].isna().sum(), '/ {}'.format(len(df[feature])))
	print('Missing values %:', df[feature].isna().mean())
	print('Descriptive stats: ')
	print(df[feature].describe())
	plt.figure(figsize = fig_size)
	sns.histplot(x = df[feature], kde = False, bins = 20)
	plt.title('{} histplot'.format(feature))
	plt.show()
	plt.figure(figsize = fig_size)
	sns.scatterplot(x = df.index, y = df[feature])
	plt.title('{} scatterplot'.format(feature))
	plt.show()
	plt.figure(figsize = fig_size)
	sns.boxplot(x = df[feature])
	plt.title('{} boxplot'.format(feature))
	plt.show()
