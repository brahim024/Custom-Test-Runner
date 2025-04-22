from abc import ABC, abstractmethod


class TestRunnerStrategy(ABC):
    @abstractmethod
    def run(self, tests: list):
        pass