from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

url_file_path = grinder.getProperties().getProperty('task2.urls')

def request_factory(url):
    def send_request():
        request = HTTPRequest()
        request.GET(url)
    return send_request
            
class TestRunner:

    def __init__(self):
        url_file = open(url_file_path)
        self.requests = []
        for num, line in enumerate(url_file):
            url, description = line.split(' ', 1)
            test = Test(num, description.strip())
            request_fn = request_factory(url)
            wrapped_request_fn = test.wrap(request_fn)
            self.requests.append(wrapped_request_fn)
        url_file.close()
    
    def __call__(self):
        for request in self.requests:
            request()
