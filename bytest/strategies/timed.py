import time
from bytest.strategies.base import TestRunnerStrategy

class TimeRunner(TestRunnerStrategy):
    def run(self, tests: list):
        for test in tests:
            try:
                start_time = time.time()
                test()
                print(f"Test {test.__name__} [PASSED] took %s seconds " % (time.time() - start_time))
            except AssertionError as e:
                print(f"Test {test.__name__} [FAILED] took %s seconds " % (time.time() - start_time))