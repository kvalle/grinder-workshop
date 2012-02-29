from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

url_file_path = grinder.getProperties().getProperty('task3.urls')

class TestRunner:
    
    def __init__(self):
        url_file = open(url_file_path)
        self.tests = []
        for num, url in enumerate(url_file):
            url = url.strip()
            test = Test(num, url)
            request = test.wrap(HTTPRequest())
            self.tests.append((request, url))
        url_file.close()
        grinder.statistics.delayReports = 1
    
    def __call__(self):
        for request, url in self.tests:
            response = request.GET(url)
        if not self.is_valid(response):
            grinder.statistics.forLastTest.success = 0
        grinder.statistics.report()
            
    def is_valid(self, response):
        if len(response.getData()) < 10: return False
        if response.getStatusCode() != 200: return False
        if "foo bar" not in response.getText(): return False
        if "fatal error" in response.getText(): return False
        else: return True

