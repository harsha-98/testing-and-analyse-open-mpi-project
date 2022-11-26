import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/nohah/Documents/PAT data/Task3Data.xlsx")

finalData = data
groupedData = data.groupby(
    ['Location']).sum()

mergedData = pd.merge(finalData, groupedData, on=['Location'])
del mergedData["File Name"]
del mergedData["Number of Assert and Debug Statements_x"]
mergedData = mergedData.drop_duplicates(subset=['Location'])
mergedData.columns = ['Location', 'Number of Assert and Debug Statements']

conditions = [
    (mergedData['Number of Assert and Debug Statements'] == 0),
    (mergedData['Number of Assert and Debug Statements'] >= 1) & (mergedData['Number of Assert and Debug Statements'] < 20),
    (mergedData['Number of Assert and Debug Statements'] >= 20) & (mergedData['Number of Assert and Debug Statements'] < 40),
    (mergedData['Number of Assert and Debug Statements'] >= 60) & (mergedData['Number of Assert and Debug Statements'] < 80),
    (mergedData['Number of Assert and Debug Statements'] >= 80) & (mergedData['Number of Assert and Debug Statements'] < 100),
    (mergedData['Number of Assert and Debug Statements'] > 100)
]
values = ['yellow', 'pink', 'orange', 'coral', 'lightblue', 'blue']
mergedData['Colors'] = np.select(conditions, values)

x = list(mergedData['Location'])
y = list(mergedData['Number of Assert and Debug Statements'])
color = list(mergedData['Colors'])

plt.figure(figsize=(10, 10))
plt.style.use('seaborn')
for i in range(len(x)):
    plt.scatter(x[i], y[i], marker=".", s=100, c=color[i])
plt.title("Distribution of Assert and Debug Statements in File Locations")
plt.xticks([])
plt.xlabel("File Locations")
plt.ylabel("Number of Assert and Debug Statements")
plt.savefig('plot3b.png')
