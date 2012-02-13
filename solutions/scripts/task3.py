from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

class TestRunner:
    
    def __init__(self):
        # sette opp self.tests
        grinder.statistics.delayReports = 1
    
    def __call__(self):
        for test in self.tests:
            response = test()
            if response.getStatusCode() != 200:
                grinder.statistics.forLastTest.success = 0
            grinder.statistics.report()

