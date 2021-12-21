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
	df[feature] = pd.to_datetime(df[feature])
	date_series = df.groupby(df[feature].dt.strftime('%Y-%m'))['id'].size().sort_index()
	print("Description: ")
	print(date_series.describe())
	plt.figure(figsize = fig_size)
	sns.lineplot(data = date_series, marker = 'o')
	plt.xticks(rotation = 90)
	plt.title('{} countplot'.format(feature))
	plt.show()
