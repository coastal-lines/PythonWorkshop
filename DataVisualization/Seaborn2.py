import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd

plt.rcParams.update({'figure.autolayout': True})
#sns.set_style('darkgrid')

x = ['zero', 'one', 'two', 'three', 'four', 'five']
y = [0.5,1,2,3,4,5]
y2 = [6,7,8,9,10,11]

df = pd.DataFrame({
    'Factor': x,
    'Weight': y,
    'Weight2': y2
})

print(df)

tidy = df.melt(id_vars='Factor').rename(columns=str.title)
print(tidy)

ax = sns.barplot(y='Factor', x='Value', hue='Variable', data=tidy)

ax.set_xlim(0, max(y2) + 1)
ax.set_xticks(range(1, max(y2) + 1))

mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))

plt.show()