import json
from bytest.strategies.base import TestRunnerStrategy


class JSONRunner(TestRunnerStrategy):
    def __init__(self,filename="result.json"):
        self.filename = filename
        
    def run(self, tests: list):
        result = []
        for test in tests:
            try:
                test()
                result.append({"test":test.__name__,"status":"PASSED"})
            except AssertionError as e:
                result.append({"test":test.__name__,"status":"FAILED","error":str(e)})
            with open(self.filename,"w") as f:
                json.dump(result,f,indent=2)