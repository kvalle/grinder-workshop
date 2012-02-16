from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

url_file_path = grinder.getProperties().getProperty('task2.urls')

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
    
    def __call__(self):
        for request, url in self.tests:
            request.GET(url)
