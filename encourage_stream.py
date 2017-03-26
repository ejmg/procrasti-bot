# -*- coding: utf-8 -*-
"""
    The streaming portion of the Procrasti-Bot. 

    Created by Gabby 'the irony in me creating this is amazing' Ortman
"""
import tweepy as ty
import json
import random
from procrastibotSecrets import *

#override tweepy.StreamListener class
class ProcrastinateStreamListener(ty.StreamListener):

    def __init__(self, api):
        self.api = api
        super(ty.StreamListener, self).__init__()

    def on_data(self, data):
        data = json.loads(data)
        self.respond(data)

    def on_error(self, status):
        print(status)

    def respond(self, data): 
        """
            pick a way to respond, you fuck
        """
        #print(data['user']['screen_name'] + ": "+ data['text'])
        user = data['user']['screen_name']

         # avoid getting into an infinite loop with the bot at all costs
        if user == 'procrasti_bot':
            return
        tweet_id = data['id']

        if user == 'frescopaintings': 
            reply = "stop procrastinating " + str(random.randint(0, 1000)) #YES
            reply_tweet = "@{} " + reply
            reply_tweet = reply_tweet.format(user)
            print(reply_tweet)
            api.update_status(status=reply_tweet, in_reply_to_status_id=tweet_id)

def set_twitter_auth():
    """
    authorize with the Twitter API
    thanks, elias
    """
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

if __name__ == "__main__": 
    api = set_twitter_auth()
    procrastinateStreamListener = ProcrastinateStreamListener(api)
    procrastinateStream = ty.Stream(auth = api.auth, listener=procrastinateStreamListener)
    procrastinateStream.filter(track=['procrastinate, procrastination, procrastinating'])