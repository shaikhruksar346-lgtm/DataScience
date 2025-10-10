import numpy as np
import pandas as pd
Client Project: Clean Data and Aggregate

cleaned_data = data.dropna()
print("Cleaned DataFrame:\n", cleaned_data)


column_means = data.mean()
print("Column means:\n", column_means)


df_group = pd.DataFrame({'Group': ['A', 'A', 'B'], 'Score': [10, 20, 30]})
grouped_mean = df_group.groupby('Group').mean()
print("Grouped mean scores:\n", grouped_mean)
