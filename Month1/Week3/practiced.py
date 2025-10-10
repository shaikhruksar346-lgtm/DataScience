import numpy as np
import pandas as pd

Practice: NumPy and Pandas Basics

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Squares:", arr ** 2)


data = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print("Original DataFrame:\n", data)
