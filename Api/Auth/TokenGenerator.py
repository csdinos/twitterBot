import requests
import base64
import json

class TokenGenerator:
    'Retrieve a token for accessing twitter\'s API'

    URL = 'https://api.twitter.com/oauth2/token'
    key = ''
    secret = ''

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def generate(self):
        headers = {'Authorization' : self.getAuthorizationToken()}
        requestData = {'grant_type': 'client_credentials'}

        jsonResponse = requests.post(self.URL, requestData, headers=headers)
        token = json.loads(jsonResponse.text)['access_token']

        #TODO maybe somehow use static functionality so as not to generate it
        # over and over again but just once and then return the same.
        return token

    def getAuthorizationToken(self):
        return 'Basic ' + base64.b64encode(self.key + ':' + self.secret)
