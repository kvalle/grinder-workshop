from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

def say_hello():
    thread = grinder.getThreadNumber()
    print '> worker thread %d: hello world!' % thread

class TestRunner:
    
    def __init__(self):
        self.test = Test(1, "test description").wrap(say_hello)

    def __call__(self):
        self.test()
        
