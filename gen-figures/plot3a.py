import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/nohah/Documents/PAT data/Task3Data.xlsx")

conditions = [
    (data['Number of Assert and Debug Statements'] == 0),
    (data['Number of Assert and Debug Statements'] >= 1) & (data['Number of Assert and Debug Statements'] < 10),
    (data['Number of Assert and Debug Statements'] >= 10) & (data['Number of Assert and Debug Statements'] < 20),
    (data['Number of Assert and Debug Statements'] >= 20) & (data['Number of Assert and Debug Statements'] < 40),
    (data['Number of Assert and Debug Statements'] >= 60) & (data['Number of Assert and Debug Statements'] < 80),
    (data['Number of Assert and Debug Statements'] > 100)
]
values = ['yellow', 'pink', 'orange', 'coral', 'lightblue', 'blue']
data['Colors'] = np.select(conditions, values)

x = list(data['File Name'])
y = list(data['Number of Assert and Debug Statements'])
color = list(data['Colors'])

plt.figure(figsize=(10, 10))
plt.style.use('seaborn')
for i in range(len(x)):
    plt.scatter(x[i], y[i], marker=".", s=100, c=color[i])
plt.title("Distribution of Assert and Debug Statements in Files")
plt.xticks([])
plt.xlabel("Files")
plt.ylabel("Number of Assert and Debug Statements")
plt.savefig('plot3a.png')
