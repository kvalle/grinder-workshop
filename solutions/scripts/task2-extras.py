from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

def request_factory(url):
    return lambda: HTTPRequest().GET(url)

class TestRunner:
    
    def __init__(self):
        file_path = grinder.getProperties().getProperty('task2.urls')
        url_file = open(file_path)
        urls = [url.strip() for url in url_file]
        url_file.close()
        self.tests = []
        for num, url in enumerate(urls):
            test = Test(num, url).wrap(request_factory(url))
            self.tests.append(test)
    
    def __call__(self):
        for test in self.tests:
            test()
