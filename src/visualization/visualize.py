import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')

def categorical_eda(df, feature, fig_size):
	print('Unique values:', df['feature'].unique())
	print('No. of unique values:', df['feature'].nunique())
	plt.figure(figsize = fig_size))
	sns.countplot(data = df, x = feature, palette = 'ch:.25_r')
    plt.xticks(rotation = 90)
    plt.show()
	plt.figure(figsize = figsize)