import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '25UmFC2N1YcvXw1CW10dWROQ2'
CONSUMER_SECRET = 'AMsdjxNMPU7HjCFVzEP30VLivtYgDe2Jb5rMP4apcVaLgN35fO'
OAUTH_TOKEN = '792959700-JvuvSw66IiCXzyqH7ffmcRu3zEsmgDdv56wW8QmS'
OAUTH_TOKEN_SECRET = '1rZAkrkM8ecBskwUbIyOegBfbslFcPkATqpM0loupkKfJ'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

DUB_WOE_ID = 560743
UK_WOE_ID = 23424975

dub_trends = api.trends_place(DUB_WOE_ID)
uk_trends = api.trends_place(UK_WOE_ID)

# trends = dub_trends[0]['trends']
# trends_uk = uk_trends[0]['trends']

trend_names = set([t['name'] for t in dub_trends[0]['trends']])
trend_names_uk = set([i['name'] for i in uk_trends[0]['trends']])

both = set.intersection(trend_names, trend_names_uk)

#print(trend_names)
#print(trend_names_uk)
print(both)


# trends = api.trends_place(DUB_WOE_ID)

# print (json.dumps(trends, indent=1))