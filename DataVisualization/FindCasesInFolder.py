import requests
from pyral import Rally, rallyWorkset



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

    query_criteria = 'FormattedID = "TF22587"' # + folderID
    #testFolder = rally.get('TestFolder',  query=query_criteria, fetch=True, instance=True)
    testFolder = rally.get('TestFolder', fetch='ValidationInput', query=query_criteria, instance=True)
    testFolderChildrens = testFolder.Children
    a = 100

login("TF22587")
a = 100
