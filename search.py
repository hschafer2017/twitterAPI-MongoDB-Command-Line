import tweepy
from auth import get_api

api = get_api()


def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]
    
tweets = search("Bill Gates", 10)
first_tweet = tweets[3]
hashtags = [h.text for h in first_tweet.entities['hashtags']]

print("Username: @" + tweets[3].user.screen_name)
print("Text: " + tweets[3].text)
print("Hashtags: #" + str(hashtags))
print("Favorites: " + str(tweets[3].favorite_count))
print("Retweets: " + str(tweets[3].retweet_count))
print("Followers: " + str(tweets[3].user.followers_count))
print("Following: " + str(tweets[3].user.friends_count))
print("Number of Tweets: " + str(tweets[3].user.statuses_count))
