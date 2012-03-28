from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from org.json import *

class TestRunner:
    
    def __init__(self):
        test1 = Test(1, "GET some JSON")
        self.request1 = test1.wrap(HTTPRequest())

        test2 = Test(2, "GET profilepicture")
        self.request2 = test2.wrap(HTTPRequest())
    
    def __call__(self):
    	# Fetches the initial JSON
        response = self.request1.GET("http://grinder.espenhh.com/json.php")
        print "JSON: " + response.text

        # Parses the JSON (Using a Java library). Then prints the field "fetched"
        jsonObject = JSONObject(response.text)
        fetched = jsonObject.getString("fetched")
        print "FETCHED: " + fetched

        # Gets the single tweets, and loops through them
        tweetsJsonObject = jsonObject.getJSONArray("tweets")
        for i in range(0,tweetsJsonObject.length()):
            singleTweet = tweetsJsonObject.getJSONObject(i)

            # Print out a single tweet
            userName = singleTweet.getString("user")
            tweet = singleTweet.getString("tweet")
            print "TWEET: " + userName + ": " + tweet

            # Fetch the URL to the profile picture, and GET it.
            profilePictureUri = singleTweet.getString("profile_image")
            print "GET against profile picture uri: " + profilePictureUri
            self.request2.GET(profilePictureUri)