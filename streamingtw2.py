from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "221143834-0DRKB4IQZZDCH5daCMwSwk6ho0btJfWfEt0qLEZX"
access_token_secret = "p994lr2ToMWICMPBBc4DY3VNy9eHAOSuOQ1ivkGCCKRGG"
consumer_key = "EYwq6RuhjSts2Ib9pe79V8tg1"
consumer_secret = "16tJrXQcL4aVNHhULKCuNxzqLx5ycb6Kl3XsBEKzthGt9yNewU"

f = open('streamingtweets2.json','a', newline='')
#analyser = SentimentIntensityAnalyzer()

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        json_load = json.loads(data)
        texts = json_load['text']
        coded = texts.encode('utf-8')
        s = str(coded)
        f.write(s[2:-1])		
        return True
		
		
    def on_error(self, status):
        print(status)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, StdOutListener())

# This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['euro', 'dollar', 'loonie', ], languages=['en'])