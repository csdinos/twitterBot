from Auth import TokenGenerator
import requests
import json

class ListRetriever:
    'Retrieve a list of our follower buddies'

    URL = 'https://api.twitter.com/1.1/lists/list.json'
    USER_ID = '894195594360737792'
    key = ''
    secret = ''

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def getLists(self):
        headers = {'Authorization' : self.getToken()}
        requestData = {'user_id': self.USER_ID}

        jsonResponse = requests.get(self.URL, params=requestData, headers=headers)
        lists = json.loads(jsonResponse.text)

        return lists

    def getListByName(self, name):
        lists = self.getLists()
        for listElem in lists:
            if name == listElem['name']:
                return listElem

        return False

    def getToken(self):
        tokenGenerator = TokenGenerator(self.key, self.secret)
        return 'Bearer ' + tokenGenerator.generate()
