from Visualization.BarClass import BarClass
from pyral import Rally, rallyWorkset

class TestsAndFoldersActions():
    allTestCasesInFolderIncludeSubfolders = []

    #def __init__(self, allTestCasesInFolderIncludeSubfolders, rootFolder):
     #   self.rootFolder = rootFolder

    @staticmethod
    def extractFoldersFromRootFolder(rootFolder):
        listBars = []
        folderNumber = 0
        #first iteration
        #if folder has testcases
        if len(rootFolder.TestCases) > 0:
            folderNumber = folderNumber + 1
            tcDict = TestsAndFoldersActions.extractTestCasesFromFolder(rootFolder)
            listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], rootFolder.Name))

        if len(rootFolder.Children) > 0:
            for folder in rootFolder.Children:
                folderNumber = folderNumber + 1
                TestsAndFoldersActions.extractTestCasesFromFolder(folder)
                tcDict = TestsAndFoldersActions.prepareDict()
                listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], folder.Name))
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.clear()

        return listBars

    @staticmethod
    def extractFolders(folders):
        for folder in folders:
            print(folder.Name)
            print("---")
            TestsAndFoldersActions.extractTestCasesFromFolder(folder)

    @staticmethod
    def extractTestCasesFromFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.append(testCase)
            if len(folder.Children) > 0:
                TestsAndFoldersActions.extractFolders(folder.Children)

    #@staticmethod
    def prepareDict():
        m = 0
        a = 0

        if len(TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders) > 0:
            for testCase in TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders:
                if testCase.Name.find("[AUTOMATED]") == True:
                    a = a + 1
                else:
                    m = m + 1
        testCasesDict = dict(manual = m, automated = a)
        return testCasesDict

"""
        @staticmethod
        def extractSubfolders(folder):
            if len(folder.Children) > 0:
                for folder in folders:
                    folderNumber = folderNumber + 1
                    tcDict = extractTestCasesFromFolder(folder)
                    listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], rootFolder.Name))
"""