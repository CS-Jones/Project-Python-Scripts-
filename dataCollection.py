import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'mOM0xFfIQLBxhk4RGXt1qJxuv'
csecret = 'mrbmLUbCbDBTiIb1zen4lYkaEEoIcjSKzyo41hQZdIpW5NYdef'
atoken = '903992855240335360-Muc0vCduGUWtpAKXCU1llLay8wQiiE2'
asecret = 'o0GdL9xq8fIyMgDm5H8LuB3srDSVivf1AQOJ22jxLVfla'

class listener(StreamListener):

    def on_data(self, data):
        rawTweet = json.dumps(data)
        saveFile = open('twitDBa.json','a')
        saveFile.write(rawTweet)
        saveFile.write('\n')
        saveFile.close()
        
        return True

    def on_error(self, status):
        print (status)
        
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"], languages=["en"])