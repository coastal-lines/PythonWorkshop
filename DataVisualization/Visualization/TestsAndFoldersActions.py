from Visualization.BarClass import BarClass

class TestsAndFoldersActions():
    listBars = []
    foldersCount = 0
    folderNumber = 0
    allTestCasesInFolderIncludeSubfolders = []
    thisIsRootFolder = True

    @staticmethod
    def extractFoldersFromRootFolder(rootFolder):
        #first iteration
        #if folder has testcases
        if len(rootFolder.TestCases) > 0:
            folderNumber = folderNumber + 1
            tcDict = extractTestCasesFromFolder(rootFolder)
            listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], rootFolder.Name))

        if len(rootFolder.Children) > 0:
            for folder in rootFolder.Children:
                folderNumber = folderNumber + 1
                extractTestCasesFromFolder(folder)
                tcDict = extractTestCasesFromFolder(allTestCasesInFolderIncludeSubfolders)
                listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], folder.Name))

    @staticmethod
    def extractFolders(folders):
        for folder in folders:
            print(folder.Name)
            print("---")
            extractTestCasesFromFolder(folder)

    @staticmethod
    def extractTestCasesFromFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                allTestCasesInFolderIncludeSubfolders.append(testCase)
            if len(folder.Children) > 0:
                extractFolders(folder.Children)

    @staticmethod
    def extractTestCasesFromFolder(allTestCasesInFolderIncludeSubfolders):
        m = 0
        a = 0

        listTestCases = []

        if len(allTestCasesInFolderIncludeSubfolders) > 0:
            for testCase in allTestCasesInFolderIncludeSubfolders:
                if testCase.Name.find("[AUTOMATED]"):
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