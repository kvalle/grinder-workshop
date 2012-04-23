from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

# Getting the path to the file holding the URLs from our test configuration
url_file_path = grinder.getProperties().getProperty('task2.urls')

class TestRunner:
    
    def __init__(self):
        pass
        # TODO: 
        # 1. Read the file (tip: the `open()` function might come in handy).
        # 2. Then, create test objects for each URL (tip: you can iterate over the 
        # file object as if it was a list of lines).
    
    def __call__(self):
        pass 
        # 3. Make GET requests for each of the URLs
