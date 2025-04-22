registered_tests = []

def testcase(func):
    registered_tests.append(func)
    return func
