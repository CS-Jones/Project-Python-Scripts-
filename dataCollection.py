import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = ''
csecret = ''
atoken = ''
asecret = ''

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