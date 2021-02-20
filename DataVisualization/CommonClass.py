import requests
from pyral import Rally, rallyWorkset
import matplotlib.pyplot as plt
from matplotlib import pylab
import seaborn as sns
from pylab import *
from matplotlib.ticker import MaxNLocator
import mplcursors
import pandas as pd
from DataVisualization.Project.RallyCommonObject import RallyCommonObject
from DataVisualization.Project.UserCredential import UserCredential
from DataVisualization.Project.RallyInstance import RallyInstance
from DataVisualization.Project.RallyFolder import RallyFolder
from DataVisualization.Project.RallyWorkspace import RallyWorkspace
from DataVisualization.Visualization.BarClass import BarClass
from DataVisualization.Visualization.TestsAndFoldersActions import TestsAndFoldersActions
from DataVisualization.Visualization.DataFrameActions import DataFrameActions

class UserSpecialBar():
    def __init__(self, name, manual, automated):
        self.name = name
        self.manual = manual
        self.automated = automated

class UserTestFromRequest():
    def __init__(self, rootFolder, tcType, name, id):
        self.rootFolder = rootFolder
        self.tcType = tcType
        self.name = name
        self.id = id

class CommonClass():
    rally = None
    totalTestsCount = 0
    totalManualTestsCount = 0
    totalAutomatedTestsCount = 0
    tabCount = 0
    rootFolder = None
    tidyDataForCustomUserQuery = None

    def login(self, server, login, password):
        self.user = UserCredential(server, login, password)
        self.rally = RallyInstance(self.user).rally

    def startSession(self, workspace, project, folder):
        self.rally.setWorkspace(workspace)
        self.rally.setProject(project)
        self.rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folder + '"').testFolder
        x = 100

    def getRootFolderName(self):
        return self.rootFolder.Name

    def getTidyData(self):
        bars = TestsAndFoldersActions().extractFoldersFromRootFolder(self.rootFolder)
        tidyData = DataFrameActions.PrepareDataFrame(bars)
        return tidyData

    def getUntidyData(self):
        return DataFrameActions.getDataFrame()

    def setRootFolder(self, folderID):
        self.rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folderID + '"').testFolder

    def runCustomRequest(self, query, rootFolderFormattedID):
        #get response with User's query
        testCasesFromUserQuery = self.rally.get('TestCase', fetch = True, projectScopeDown = True, query = query)

        #extract test cases from response
        listTC = []
        for number in range(testCasesFromUserQuery.resultCount):
            listTC.append(testCasesFromUserQuery.next())

        #get root test folders according the main root folder
        rootFolder = RallyFolder(self.rally ,'FormattedID = "' + rootFolderFormattedID + '"').testFolder
        listRootSubfolders = rootFolder.Children

        #prepare cases for bars
        listRootFoldersOfUser = []
        for tc in listTC:
            tcType = None
            tcId = None
            tcRoot = None
            tcName = None

            #name
            tcName = tc.Name

            #id
            tcId = tc.FormattedID

            #type
            if tc.Name.find("AUTOMATED") != -1:
                tcType = "automated"
            else:
                tcType = "manual"

            #root
            for rootFolder in listRootSubfolders:
                if tc.TestFolder.Name == rootFolder.Name:
                    tcRoot = rootFolder.Name
                    break
                elif tc.TestFolder.Parent.Name == rootFolder.Name:
                    tcRoot = tc.TestFolder.Parent.Name
                    break
                else:
                    tf = tc.TestFolder.Parent
                    tcRoot = self.getParentName(tf, rootFolder.Name)
                    #break

            #add to list
            listRootFoldersOfUser.append(UserTestFromRequest(tcRoot, tcType, tcName, tcId))

        self.prepareForMatPlotLib(listRootFoldersOfUser)
        return self.tidyDataForCustomUserQuery

    #find parent name by recursion
    def getParentName(self, testFolder, rootFolderName):
        try:
            if testFolder.Name != None and testFolder.Name == rootFolderName:
                return rootFolderName
            else:
                self.getParentName(testFolder.Parent, rootFolderName)
        except AttributeError:
            print("not this root folder")

    #prepare data for convert into matplotlib's bars
    def prepareForMatPlotLib(self, listRootFoldersOfUser):
        #uniq root folders
        uniqRootFolders = list(set([tc.rootFolder for tc in listRootFoldersOfUser]))

        #for each uniq folder how many manual and auto tests
        listUserBars = []
        for unRoot in uniqRootFolders:
            manual = 0
            automated = 0
            name = unRoot

            for item in listRootFoldersOfUser:
                if unRoot == item.rootFolder:
                    if item.tcType == "manual":
                        manual = manual + 1
                    else:
                        automated = automated + 1

            listUserBars.append(UserSpecialBar(name, manual, automated))

        self.createTidyData(listUserBars)

    #create tidy data
    def createTidyData(self, listUserBars):
        #ids = []
        names = []
        manual = []
        automated = []

        for item in listUserBars:
            #ids.append(item.name)
            names.append(item.name)
            manual.append(item.manual)
            automated.append(item.automated)

        dataFrame = pd.DataFrame({
            'ids': None,
            'names': names,
            'manual': manual,
            'automated': automated
        })

        self.tidyDataForCustomUserQuery = dataFrame.melt(id_vars='names', value_vars=['manual', 'automated'])