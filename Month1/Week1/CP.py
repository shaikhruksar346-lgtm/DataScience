import pandas as pd
import matplotlib.pyplot as plt

#data of a person social media account
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Followers': [1200, 1500, 1800, 2100, 2500, 3000],
    'Likes': [300, 400, 450, 500, 600, 750],
    'Shares': [50, 70, 65, 80, 100, 120]
}


df = pd.DataFrame(data)


print("First few rows of the dataset:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())


df['EngagementRate'] = ((df['Likes'] + df['Shares']) / df['Followers']) * 100
print("\nData with Engagement Rate column:")
print(df)


plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Followers'], marker='o', label='Followers')
plt.plot(df['Month'], df['EngagementRate'], marker='s', label='Engagement Rate (%)')
plt.title('Social Media Growth & Engagement Over 6 Months')
plt.xlabel('Month')
plt.ylabel('Count / Percentage')
plt.legend()
plt.grid(True)
plt.show()
