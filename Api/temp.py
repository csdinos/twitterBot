# temp file, just to test things out
# until we get the formating and storing functionality
import sys
sys.path.insert(0, '/home/dinos/twitterBot/')
from secrets import *
from ListRetriever import *
from TweetRetriever import *

listRetriever = ListRetriever(C_KEY, C_SECRET);
tweetRetriever = TweetRetriever(C_KEY, C_SECRET);

testList = listRetriever.getListByName('Test')

if testList:
    print 'getting tweets for list id=' + str(testList['id'])
    hardcodedLastTweetId = 89533004989371124
    tweets = tweetRetriever.getTweets(testList['id'], hardcodedLastTweetId)
    print 'got ' + str(len(tweets)) + ' tweets'
else:
    print 'list not found'
