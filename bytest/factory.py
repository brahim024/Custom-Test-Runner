from bytest.strategies.silent import SilentRunner
from bytest.strategies.verbose import VerboseRunner
from bytest.strategies.summary import SummaryRunner
from bytest.strategies.json import JSONRunner
from bytest.strategies.colored import ColoredRunner
from bytest.strategies.timed import TimeRunner


class TestStrategyFactory:
    def __new__(self,mode=None):
        return {
            "verbose": VerboseRunner(),
            "silent": SilentRunner(),
            "json": JSONRunner(),
            "summary": SummaryRunner(),
            "colored":ColoredRunner()
        }.get(mode, VerboseRunner())
        