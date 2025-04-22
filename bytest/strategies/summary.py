from bytest.strategies.base import TestRunnerStrategy

class SummaryRunner(TestRunnerStrategy):
    def run(self,tests):
        failed = 0
        passed = 0
        for test in tests:
            try:
                test()
                passed += 1
            except AssertionError as e:
                failed += 1
        print(f"{passed} passed, {failed} failed")
        failed = 0
        passed = 0