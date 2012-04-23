from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from org.json import * # This is for the JSON support
# Parse JSON using: JSONObject(<some text>)
# See more at http://www.json.org/javadoc/org/json/JSONObject.html

class TestRunner:
    
    def __init__(self):
        test1 = Test(1, "GET some JSON")
        self.request1 = test1.wrap(HTTPRequest())

    def __call__(self):
    	# Fetches the initial JSON
        response = self.request1.GET("http://grinder.espenhh.com/json.php")
        print "JSON: " + response.getText()
