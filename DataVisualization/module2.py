import matplotlib.pyplot as plt
import mplcursors

class Obj():
    def __init__(self, x, y):
        self.x = x
        self.y = y


#prev = None
fig, ax = plt.subplots()


b1 = Obj(0,9)
b2 = Obj(1,8)
b3 = Obj(2,6)

lx = []
lx.append(b1.x)
lx.append(b2.x)
lx.append(b3.x)
ly = []
ly.append(b1.y)
ly.append(b2.y)
ly.append(b3.y)

labels = ["one", "two", "three"]
ax.set(xticks = range(0, len(lx) + 1), xticklabels = labels, title="Hover over a bar")
ax.bar(lx, ly, align="center")


#work solution for detecting bar index and call method
mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))


plt.show()

