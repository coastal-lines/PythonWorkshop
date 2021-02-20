from tkinter import *
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

#window - экземпляр класса tkinter
window = Tk()
window.geometry("1700x900")
window.configure(bg="black")

#ttk.Notebook - это контейнер для таб
tabControl = ttk.Notebook(window)

#Frame - виджет помогающий разместить несколько областей для элементов
tabFrame = Frame(master = window, width = 1600, height = 800, bg="white")
tabFrame.place(x = 0, y = 0)

dpi = 96
plt.rcParams['figure.figsize']=(1400 / dpi, 700 / dpi)
fig, ax = plt.subplots()
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips)

#мы это используем для отрисовки, когда все готово???????
canvas = FigureCanvasTkAgg(fig, master = tabFrame)
canvas.draw()
canvas.get_tk_widget().grid()

#фрейм для авто/ручное
tabFrame2 = Frame(master = window, width = 200, height = 200, bg="red")
tabFrame2.place(x = 1500, y = 0)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
ax2.axis('equal')
fig2.set_size_inches(2,2)
canvas2 = FigureCanvasTkAgg(fig2, master = tabFrame2)
canvas2.draw()
canvas2.get_tk_widget().grid()

#фрейм для флеш
tabFrame3 = Frame(master = window, width = 200, height = 200, bg="red")
tabFrame3.place(x = 1500, y = 300)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig3, ax3 = plt.subplots()
ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
ax3.axis('equal')
fig3.set_size_inches(2,2)
canvas3 = FigureCanvasTkAgg(fig3, master = tabFrame3)
canvas3.draw()
canvas3.get_tk_widget().grid()

#фрейм для секюр клиент
tabFrame4 = Frame(master = window, width = 200, height = 200, bg="red")
tabFrame4.place(x = 1500, y = 600)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig4, ax4 = plt.subplots()
ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
ax4.axis('equal')
fig4.set_size_inches(2,2)
canvas4 = FigureCanvasTkAgg(fig4, master = tabFrame4)
canvas4.draw()
canvas4.get_tk_widget().grid()


window.mainloop() 