import tweepy

from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

tweet = 'This is a test tweet generated from my test-bot :)'

api.update_status(tweet)
