import time

from net.grinder.script.Grinder import grinder
from net.grinder.script import Test

def some_function(num):
    time.sleep(1)
    print '--- foo #' + str(num)

class TestRunner:
    
    def __init__(self):
        self.test = Test(1, "test description").wrap(some_function)
        self.num = 0
    
    def __call__(self):
        self.num += 1
        self.test(self.num)
        
