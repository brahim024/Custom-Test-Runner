class TestRunner:
    def __init__(self,strategy):
        self.strategy = strategy
        
    def run_tests(self,tests):
        return self.strategy.run(tests)