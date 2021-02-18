from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd
from pyral import Rally, rallyWorkset
from DataVisualization.CommonClass import CommonClass
from DataVisualization.Visualization.UserTabData import UserTabData

class UserInterface():
    tabCount = 0
    tabControl = None
    queryText = None
    commonClass = CommonClass()
    tidy = None
    unTidy = None
    rootFolderName = None
    listUserTabData = []

    def createWindow(self):
        window = Tk()

        #title
        window.title("Rally Data Visualization and Prediction")
        window.geometry("1650x900")

        #tabs holder
        self.tabControl = ttk.Notebook(window)

        #elements frame
        frameElements = Frame(master = window, width = 1600, height = 20)
        frameElements.place(x = 0, y = 850)

        lbl = Label(master = frameElements, text="Query input:")
        lbl.place(x = 0, y = 0, width=100)
        self.queryText = Entry(master = frameElements)
        self.queryText.place(x = 100, y = 0, width=900)
        btn = Button(master = frameElements, text = "Find test cases", command = self.createTab)
        btn.place(x = 1000, y = 0, width=92)

        self.createMainTab()

        #endles loop for wait any user interactions - will works during window is opened
        window.mainloop()


    def createMainTab(self):
        tab = ttk.Frame()

        self.tabControl.add(tab, text ='Settings')
        #the main screen?!
        self.tabControl.place(x = 0, y = 0, width = 1650, height = 850)

        lbl1 = Label(master = tab, text="Server:")
        lbl1.place(x = 0, y = 0, width=100)
        self.serverText = Entry(master = tab)
        self.serverText.place(x = 100, y = 0, width=200)
        lbl2 = Label(master = tab, text="User:")
        lbl2.place(x = 0, y = 20, width=100)
        self.userText = Entry(master = tab)
        self.userText.place(x = 100, y = 20, width=200)
        lbl3 = Label(master = tab, text="Password:")
        lbl3.place(x = 0, y = 40, width=100)
        self.passwordText = Entry(master = tab)
        self.passwordText.place(x = 100, y = 40, width=200)

        lbl4 = Label(master = tab, text="Workspace:")
        lbl4.place(x = 0, y = 60, width=100)
        self.workspaceText = Entry(master = tab)
        self.workspaceText.place(x = 100, y = 60, width=200)
        lbl5 = Label(master = tab, text="Project:")
        lbl5.place(x = 0, y = 80, width=100)
        self.projectText = Entry(master = tab)
        self.projectText.place(x = 100, y = 80, width=200)
        lbl6 = Label(master = tab, text="Root folder:")
        lbl6.place(x = 0, y = 100, width=100)
        self.rootFolderText = Entry(master = tab)
        self.rootFolderText.place(x = 100, y = 100, width=200)

        btn = Button(master = tab, text = "Start session", command = self.startSession)
        btn.place(x = 100, y = 120, width=200)
    
    def createTab(self):
        if self.queryText.get() == "":
            self.createDefaultTab()
        else:
            self.creatCustomTab()

    def creatCustomTab(self):
        query = self.queryText.get()
        tidy = self.commonClass.runCustomRequest(query, self.rootFolderText.get())

        self.tabCount = self.tabCount + 1

        #matplotlib frame 
        tab = ttk.Frame()

        self.tabControl.add(tab, text = "User query")
        self.tabControl.place(x = 0, y = 0)

        canvas = Canvas(master = tab, width = 1600, height = 800)
        canvas.place(x = 0, y = 0)

        dpi = 96
        plt.rcParams['figure.figsize']=(1550 / dpi, 750 / dpi)
        plt.rcParams.update({'figure.autolayout': True})

        fig, ax = plt.subplots()

        #set folder name for Figure
        fig.suptitle("User query: " + query)

        self.listUserTabData.append(UserTabData(self.tabCount, None, None, None))

        ax = sns.barplot(y='names', x='value', hue='variable', data = tidy)

        ax.set_xlim(0, max(tidy.value) + 1)
        ax.set_xticks(range(1, max(tidy.value) + 1))

        canvas = FigureCanvasTkAgg(fig, master = tab)
        canvas.draw()
        canvas.get_tk_widget().grid()

        toolbar = NavigationToolbar2Tk(canvas, tab, pack_toolbar = False)
        toolbar.place(x = 0, y = 780)

    def createDefaultTab(self):
        self.tabCount = self.tabCount + 1

        #matplotlib frame 
        tab = ttk.Frame()

        #get root folder name
        self.rootFolderName = self.commonClass.getRootFolderName()

        #self.tabControl.add(tab, text ='Tab ' + str(self.tabCount))
        self.tabControl.add(tab, text = self.rootFolderName)
        self.tabControl.place(x = 0, y = 0)

        canvas = Canvas(master = tab, width = 1600, height = 800)
        canvas.place(x = 0, y = 0)

        dpi = 96
        plt.rcParams['figure.figsize']=(1550 / dpi, 750 / dpi)
        plt.rcParams.update({'figure.autolayout': True})

        fig, ax = plt.subplots()

        #set folder name for Figure
        fig.suptitle(self.rootFolderName)

        #get tidy data
        self.tidy = self.commonClass.getTidyData()
        self.unTidy = self.commonClass.getUntidyData()

        self.listUserTabData.append(UserTabData(self.tabCount, self.tidy, self.unTidy, self.rootFolderName))

        ax = sns.barplot(y='names', x='value', hue='variable', data = self.tidy)

        ax.set_xlim(0, max(self.tidy.value) + 1)
        ax.set_xticks(range(1, max(self.tidy.value) + 1))

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().grid()

        toolbar = NavigationToolbar2Tk(canvas, tab, pack_toolbar=False)
        toolbar.place(x = 0, y = 780)

        mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(self.openNextTabByUserSelecting(sel.target.index)))

    def startSession(self):
        self.commonClass.startSession(self.serverText.get(), self.userText.get(), self.passwordText.get(), self.workspaceText.get(), self.projectText.get(), self.rootFolderText.get())

    def openNextTabByUserSelecting(self, index):
        print("bar is: " + str(index))

        #need to use current tab's data - at this monent there are data just from the last tab
        #if current = actual => don't override
        allTabs = self.tabControl.tabs()
        cTab = self.tabControl.select()
        currentTab = self.tabControl.nametowidget(cTab)
        cName = currentTab._name
        currentTabIndex = allTabs.index("." + cName)
        self.rootFolderName = self.listUserTabData[currentTabIndex - 1].rootFolderName
        self.tidy = self.listUserTabData[currentTabIndex - 1].tidyData
        self.unTidy = self.listUserTabData[currentTabIndex - 1].untidyData

        #override rootFolder
        #don't open new tab if folder has only test cases
        if int((len(self.tidy.names) / 2)) > 1:
            newFolderId = self.unTidy.ids[index]
            self.commonClass.setRootFolder(newFolderId)
            self.createTab()