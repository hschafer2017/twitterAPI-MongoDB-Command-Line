from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth
from pymongo import MongoClient
import json
import os

MONGODB_URI = os.environ.get('MONGODB_URI')
MONGODB_NAME = os.environ.get('MONGODB_NAME')


topic = input("What topic do you want to search for? ")
how_many = int(input("How many tweets do you want? "))

keyword_list=[topic]
limit = how_many


class MyStreamListener(StreamListener):
    # Class that Tweepy has built, has collects all functionality of tweets

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with MongoClient(MONGODB_URI) as conn:
                    db = conn[MONGODB_NAME]
                    coll = db[topic]
                    coll.insert(json.loads(data))
                    return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
                return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True

auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)