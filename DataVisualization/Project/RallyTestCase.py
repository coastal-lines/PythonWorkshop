class RallyTestCase():
    def getTestCaseByFormattedID(formattedID):
        for test_case in test_cases:
            print(test_case.FormattedID)
            print(test_case.Name)
            if(test_case.FormattedID == formattedID):
                return test_case
"""
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
        for expectedResults in list_steps:
            listExpectedResult.append(expectedResults.ExpectedResult)
            print(expectedResults.ExpectedResult)
"""