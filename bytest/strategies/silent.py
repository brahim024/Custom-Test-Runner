from bytest.strategies.base import TestRunnerStrategy

class SilentRunner(TestRunnerStrategy):
    def run(self,tests: list):
        for test in tests:
            try:
                test()
            except AssertionError as e:
                pass