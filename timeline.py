import json
import tweepy
from tweepy import OAuthHandler
from auth import get_api
    
api = get_api()

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)

for status in get_my_timeline(1):
    print(status)