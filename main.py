from bytest.runner import TestRunner
from bytest.factory import TestStrategyFactory
from bytest.decorations import registered_tests 
import sys
import my_test

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verbose"
    strategy = TestStrategyFactory(mode=mode)
    test_runner = TestRunner(strategy)
    test_runner.run_tests(registered_tests)
    # print(registered_tests)