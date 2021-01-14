import requests
from pyral import Rally, rallyWorkset



query_criteria = 'FormattedID = 95208' #% args[0]
response = rally.get('TestCase', fetch=True, query=query_criteria)

"""
options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally(server, user, password, workspace=workspace, project=project)
"""



"""
def auth_rally(user, password):
    url = "https://rally1.rallydev.com/slm/webservice/v2.0/subscription"
    session = requests.Session()
    session.auth = (user, password)
    auth = session.post(url)
    response = session.get(url)
    print(response.text)
    session.close()


"""

