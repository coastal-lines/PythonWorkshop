import matplotlib.pyplot as plt
import mplcursors

class Obj():
    def __init__(self, x, y):
        self.x = x
        self.y = y

prev = None
fig, ax = plt.subplots()
b1 = Obj(0,9)
b2 = Obj(2,8)
b3 = Obj(4,6)

lx = []
lx.append(b1.x)
lx.append(b2.x)
lx.append(b3.x)
ly = []
ly.append(b1.y)
ly.append(b2.y)
ly.append(b3.y)

ax.bar(lx, ly, align="center")

mplcursors.cursor(ax, hover=True).connect("add", lambda sel: sel.annotation.set_text("helllo!"))


"""
    @cursor.connect("add")
    def on_add(sel):
        global prev
        bar_num = sel.target.index + 1
        postfix = "st"
        print(f"You hovered over the {bar_num}{postfix} bar.")
        prev = bar_num
"""

plt.show()

