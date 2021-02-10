from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

#actions
def getText():
    print(txt.get())

#tkinter
window = Tk()

#title
window.title("Rally Data Visualization and Prediction")

window.geometry("1024x768")

#canvas = Canvas(window, width = 600, height = 200, bg="gray")
#canvas.grid(column = 0, row = 0)


fig = plt.figure()
index = ["0","1","2","3","4"]
values = [5,7,3,4,6]
plt.bar(index,values)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master = window)
toolbar = NavigationToolbar2Tk(canvas, window) 


lbl = Label(window, text="Query input:")
lbl.grid(column = 0, row = 1)

txt = Entry(window, width = 100)
txt.grid(column = 1, row = 1)

btn = Button(window, text = "Find test cases", command = getText)
btn.grid(column = 2, row = 1)

lbl2 = Label(window, text="Query input2:")
lbl2.grid(column = 0, row = 2)


#endles loop for wait any user interactions - will works during window is opened
window.mainloop()