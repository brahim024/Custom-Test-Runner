from bytest.strategies.base import TestRunnerStrategy

class VerboseRunner(TestRunnerStrategy):
    def run(self,tests):
        for test in tests:
            try:
                test()
                print(f"{test.__name__} [PASSED]")
            except AssertionError as e:
                print(f"{test.__name__} [FAILED] - {e}")
        return 