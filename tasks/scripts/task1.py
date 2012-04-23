from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

class TestRunner:

    def __init__(self):
        pass
        # TODO: create a Test object, then use it to wrap a HTTPRequest object
        # The wrapped HTTPRequest must then be assigned to an instance variable
        # (using the `self` keyword) in order to accessable in the __call__
        # method.
    
    def __call__(self):
        pass 
        # TODO: Use the GET method of the wrapped HTTPRequest to retrieve an URL
        # of your choosing. 
        # Can't decide on one? Try GETing http://grinder.espenhh.com/reliable.php
