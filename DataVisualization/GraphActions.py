import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.ticker as ticker
import mplcursors

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

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

def on_click(event):
    #print("Y1 is: " + str(event.artist._y1) + " X0 is: " + str(event.artist._x0) + " X1 is: " + str(event.artist._x1) + " Width is:" + str(event.artist._width))
    print("-")

fig.canvas.mpl_connect('pick_event', on_click)

cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def on_add(sel):
    global prev
    bar_num = sel.target.index + 1
    postfix = "st"
    print(f"You hovered over the {bar_num}{postfix} bar.")
    prev = bar_num

plt.grid()
plt.show()