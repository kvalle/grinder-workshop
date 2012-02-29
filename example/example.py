import time

from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

def some_function():
    run = grinder.getRunNumber()
    thread = grinder.getThreadNumber()
    print '> output #%d from worker thread %d' % (run, thread)

class TestRunner:
    
    def __init__(self):
        self.test = Test(1, "test description").wrap(some_function)
    
    def __call__(self):
        self.test()
        
