from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

url_file_path = grinder.getProperties().getProperty('task2.urls')

def request_factory(url):
    return lambda: HTTPRequest().GET(url)
            
class TestRunner:

    def __init__(self):
        url_file = open(url_file_path)
        self.requests = []
        for num, line in enumerate(url_file):
            url, description = line.split(' ', 1)
            test = Test(num, description.strip())
            request = test.wrap(request_factory(url))
            self.requests.append(request)
        url_file.close()
    
    def __call__(self):
        for request in self.requests:
            request()
