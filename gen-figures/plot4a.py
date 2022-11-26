import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/nohah/Documents/PAT data/author.xlsx")
data.head()
df = pd.DataFrame(data)

Author = df['Author'].head(12)
Contribution = df['Contribution'].head(12)

fig, ax = plt.subplots(figsize=(16, 9))
ax.barh(Author, Contribution)

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

ax.set_title('Authors and Their Contributions',
             loc='left', )

plt.savefig('plot4a.png')
