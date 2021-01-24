import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig = plt.figure()

ax = plt.axes()
axes = fig.add_axes(ax)
plt.axis([0, 10, 0, 10])

bars = []
b1 = axes.bar([2], [10], picker=True)
b1.set_label("999999999999")
b2 = axes.bar([2.5], [8], picker=True)
axes.bar([4], [1], picker=True)
axes.bar([4.5], [3], picker=True)
bars.append(b1)
bars.append(b2)

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

plt.xticks([2.2], ["folder name"])

def on_click(event):
    print(event)

fig.canvas.mpl_connect('pick_event', on_click)

plt.grid()
plt.show()