from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

# Getting the path to the file holding the URLs from our test configuration
url_file_path = grinder.getProperties().getProperty('task2.urls')

class TestRunner:
    
    def __init__(self):
        pass # Read the file, and create tests for each URL
    
    def __call__(self):
        pass # Make a GET request for each URL/test
