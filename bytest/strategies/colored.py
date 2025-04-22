from colorama import Fore, Back, Style
from bytest.strategies.base import TestRunnerStrategy


class ColoredRunner(TestRunnerStrategy):
    def run(self, tests: list):
        for test in tests:
            try:
                test()
                print(f" Test {test.__name__} {Fore.GREEN}[PASSED]")
                print(Style.RESET_ALL)
            except AssertionError as e:
                print(f"Test {test.__name__ } {Fore.RED} [FAILED] - {e}")
                print(Style.RESET_ALL)