import requests
from pyral import Rally, rallyWorkset



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
    if(pr.Name == 'Surpass 12 Stabilisation & Regression'):
        print(pr);
        rootProject = pr
        break

rally.setWorkspace(rootWorkspace.Name)
rally.setProject(rootProject.Name)

query_criteria = 'FormattedID = TC93789'
response = rally.get('TestCase', fetch='ValidationInput', query=query_criteria)
ref = response.data['Results'][0]['_ref']



#query_criteria = 'FormattedID = TC93789' #% args[0]
#response = rally.get('TestCase', fetch=False, query=query_criteria)
a = 90


"""
options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally(server, user, password, workspace=workspace, project=project)
"""

