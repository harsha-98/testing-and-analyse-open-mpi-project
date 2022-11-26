import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/nohah/Documents/PAT data/commitcount.xlsx")

conditions = [
    (data['Number of Commits'] == 1),
    (data['Number of Commits'] > 1) & (data['Number of Commits'] < 10),
    (data['Number of Commits'] >= 10) & (data['Number of Commits'] < 20),
    (data['Number of Commits'] >= 20) & (data['Number of Commits'] < 40),
    (data['Number of Commits'] > 120)
]
values = ['pink', 'orange', 'coral', 'lightblue', 'blue']
data['Colors'] = np.select(conditions, values)

x = list(data['File Name'])
y = list(data['Number of Commits'])
color = list(data['Colors'])

plt.figure(figsize=(10, 10))
plt.style.use('seaborn')
for i in range(len(x)):
    plt.scatter(x[i], y[i], marker=".", s=100, c=color[i])
plt.title("Distribution of Commits per File")
plt.xticks([])
plt.xlabel("Files")
plt.ylabel("Number of Commits")
plt.savefig('plot4b.png')
