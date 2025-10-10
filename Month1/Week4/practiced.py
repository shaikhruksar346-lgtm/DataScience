import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

Practice: Basic plots (Matplotlib)
x = [1, 2, 3, 4]
y = [10, 8, 6, 12]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


data = [1, 2, 2, 3, 3, 3, 4, 5]
plt.hist(data, bins=4)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

