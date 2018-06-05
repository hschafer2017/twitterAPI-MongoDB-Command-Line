import json
import tweepy
from tweepy import OAuthHandler
from auth import get_api
    
api = get_api()

def get_friends_of(username):
    user = api.get_user(username)
    return user.friends()
# If an error shows on your editor, it's not an actual error. It should still run. 

for friend in get_friends_of("USERNAME"):
    print(friend)