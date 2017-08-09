from Auth import TokenGenerator
import requests
import json

class TweetRetriever:
    'Retrieve tweets of a list'

    URL = 'https://api.twitter.com/1.1/lists/statuses.json'
    key = ''
    secret = ''

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def getTweets(self, list_id, lastTweetId):
        headers = {'Authorization' : self.getToken()}
        requestData = {
            'list_id': list_id,
            'include_rts': False,
            'count': 20,
            'since_id': lastTweetId
        }

        jsonResponse = requests.get(self.URL, params=requestData, headers=headers)
        tweets = json.loads(jsonResponse.text)

        return tweets

    def getToken(self):
        tokenGenerator = TokenGenerator(self.key, self.secret)
        return 'Bearer ' + tokenGenerator.generate()
