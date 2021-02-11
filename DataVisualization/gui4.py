from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd

def plot2():
    dpi = 96
    plt.rcParams['figure.figsize']=(1050 / dpi, 750 / dpi)
    plt.rcParams.update({'figure.autolayout': True})

    fig, ax = plt.subplots()

    x = ['zero', 'one', 'two', 'three', 'four', 'five']
    y = [0.5,1,2,3,4,5]
    y2 = [6,7,8,9,10,11]

    df = pd.DataFrame({
        'Factor': x,
        'manual': y,
        'automated': y2
    })

    print(df)

    tidy = df.melt(id_vars='Factor').rename(columns=str.title)
    print(tidy)

    ax = sns.barplot(y='Factor', x='Value', hue='Variable', data=tidy)

    ax.set_xlim(0, max(y2) + 1)
    ax.set_xticks(range(1, max(y2) + 1))

    mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))

    canvas = FigureCanvasTkAgg(fig, master=frameCanvas)
    canvas.draw()
    canvas.get_tk_widget().grid()

#plot
def plot(): 
    fig = Figure(figsize=(5, 4), dpi=200)
    index = ["0","1","2","3","4"]
    values = [5,7,3,4,6]
    plt.bar(index,values)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = frameCanvas)
    canvas.draw()
    canvas.get_tk_widget().grid()
    frame = Frame(master = frameCanvas, width = 1200, height = 800)
    #frame.grid(row=0, column=1)
    toobar = NavigationToolbar2Tk(canvas, frame)
    #canvas.get_tk_widget().grid(row=1, column=0)

#actions
def getText():
    print(txt.get())

#tkinter
window = Tk()
#title
window.title("Rally Data Visualization and Prediction")
window.geometry("1400x900")

frameCanvas = Frame(window, width = 1100, height = 800, bg="white")
frameCanvas.place(x = 0, y = 0)
canvas = Canvas(master = frameCanvas, width = 1100, height = 800)
canvas.place(x = 0, y = 0)

frameElements = Frame(window, width = 1100, height = 20)
frameElements.place(x = 0, y = 780)

lbl = Label(master = frameElements, text="Query input:")
lbl.place(x = 0, y = 0, width=100)
txt = Entry(master = frameElements)
txt.place(x = 100, y = 0, width=900)
btn = Button(master = frameElements, text = "Find test cases", command = plot2)
btn.place(x = 1000, y = 0, width=92)

#endles loop for wait any user interactions - will works during window is opened
window.mainloop()