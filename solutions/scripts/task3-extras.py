from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

url_file_path = grinder.getProperties().getProperty('task3.urls')

class TestRunner:
    def __init__(self):
        url_file = open(url_file_path, 'rb')
        self.tests = []
        for num, line in enumerate(url_file):
            line = [val.strip() for val in line.split('|')]
            url, description, checks = line[0], line[1], line[2:]
            test = Test(num, description)
            request = test.wrap(HTTPRequest())
            self.tests.append((request, url, checks))
        url_file.close()
        grinder.statistics.setDelayReports(True)
    
    def __call__(self):
        for request, url, checks in self.tests:
            response = request.GET(url)
            if not self.is_valid(response, checks):
                self.fail()
            grinder.statistics.report()

    def fail(self):
        grinder.statistics.getForLastTest().setSuccess(False) 
            
    def is_valid(self, response, checks):
        validators = {
            'text': lambda text: text in response.getText(),
            'not-text': lambda text: text not in response.getText(),
            'status': lambda code: int(code) == response.getStatusCode(),
            'min-size': lambda bytes: int(bytes) < len(response.getData())
        }
        for check in checks:
            fn, value = check.split('=')
            validator = validators.get(fn)
            if not validator(value): 
                return False
        return True

