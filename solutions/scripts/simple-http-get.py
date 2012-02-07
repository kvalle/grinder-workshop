from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

class TestRunner:
    
    def __init__(self):
        request = HTTPRequest()
        self.test = Test(1, "GETing some webpage").wrap(request)
    
    def __call__(self):
        self.test.GET("http://example.com")

