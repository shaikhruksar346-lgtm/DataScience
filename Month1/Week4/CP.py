import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

Client Project: Dashboard Visualizations (Seaborn)

df_heatmap = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))
sns.heatmap(df_heatmap)
plt.title("Heatmap")
plt.show()


df_pairplot = pd.DataFrame(np.random.rand(50, 3), columns=['Feature1', 'Feature2', 'Feature3'])
sns.pairplot(df_pairplot)
plt.suptitle("Pairplot")
plt.show()
