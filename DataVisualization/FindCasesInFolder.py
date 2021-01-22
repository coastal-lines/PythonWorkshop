import requests
from pyral import Rally, rallyWorkset
import matplotlib.pyplot as plt



testFolderChildrens = None
rally = None

def login(folderID):
    rally = Rally(server=server, user=user, password=password)
    workspaces = rally.getWorkspaces()

    rootWorkspace = None
    for ws in workspaces:
        if(ws.Name == 'BTL Group Ltd.'):
            rootWorkspace = ws
            break

    projects = rally.getProjects(workspace=rootWorkspace.Name)
    rootProject = None
    for pr in projects:
        print(pr.Name)
        if(pr.Name == 'Surpass 12 Regression Test Pack'):
            print(pr);
            rootProject = pr
            break

    rally.setWorkspace(rootWorkspace.Name)
    rally.setProject(rootProject.Name)

    folder_id = "TF22587"

    query_criteria = 'FormattedID = "TF22587"' # + folderID
    #testFolder = rally.get('TestFolder',  query=query_criteria, fetch=True, instance=True)
    #testFolder = rally.get('TestFolder', fetch='True', query=query_criteria, instance=True)
    #folders = rally.get('TestFolder', query='TestFolder.Name = TF22587', instance=True)
    #testFolderChildrens = testFolder.Children
    query = 'FormattedID = %s'
    test_folder_req = rally.get('TestFolder', fetch=True, projectScopeDown=True, query=query % 'TF22587') # folder_id == "TF111"
    test_folder = test_folder_req.next()
    test_cases = test_folder.TestCases
    print('Start working with %s' % folder_id)
    print('Test Folder %s contains %s TestCases' % (folder_id, len(test_cases)))
    list_steps = None
    for test_case in test_cases:
        print(test_case.FormattedID)
        print(test_case.Name)
        list_steps=test_case.Steps
        listInputs = []
        listExpectedResult = []
        for i in list_steps:
            listInputs.append(i.Input)
            print(i.Input)
        for er in list_steps:
            listExpectedResult.append(er.ExpectedResult)
            print(er.ExpectedResult)
    index = ["0","1","2","3","4"]
    values = [5,7,3,4,6]
    plt.bar(index,values)
    plt.show()

login("TF22587")
a = 100