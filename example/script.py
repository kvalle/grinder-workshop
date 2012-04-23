from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

# defining a simple "hello world" function, in order to have something to test 
def hello_world():
    thread = grinder.getThreadNumber()
    print '> worker thread %d: hello world!' % thread

class TestRunner:
    
    def __init__(self):
        # creating a Grinder test object
        test = Test(1, "test description") 
        # creating a proxy, by wrapping the hello world function
        self.wrapped_function = test.wrap(hello_world) 

    def __call__(self):
        # calling "hello world" through the wrapped function
        self.wrapped_function() 

