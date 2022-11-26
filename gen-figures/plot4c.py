import pandas as pd
import matplotlib.pyplot as plt

z = []

data = pd.read_excel("C:/Users/nohah/Documents/PAT data/dateCreated.xlsx")

data = data.dropna()

x = list(data['File Name'])
y = list(data['Date Created'])

for i in y:
    z.append(i.year)

newData = {'File Name': x, 'Date Created': z}
newDF = pd.DataFrame(newData)

newDF = newDF[newDF['Date Created'] >= 2012]

finalData = newDF
newDF = finalData.groupby(['Date Created']).size().reset_index(name='Number of Files')

Dates = newDF['Date Created'].head(12)
Names = newDF['Number of Files'].head(12)

fig, ax = plt.subplots(figsize=(16, 9))
ax.barh(Dates, Names)

for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

ax.grid(b=True, color='grey',
        linestyle='-.', linewidth=0.5,
        alpha=0.2)

ax.invert_yaxis()

for i in ax.patches:
    plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
             str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold',
             color='grey')

ax.set_title('Files Created Over the Years',
             loc='left', )

plt.savefig('plot4c.png')
