# -*- coding: utf-8 -*-
"""
    The streaming portion of the Procrasti-Bot. 

    Created by Gabby 'the irony in me creating this is amazing' Ortman
"""
import tweepy as ty
import json
import random
import time
from procrastibotSecrets import *
from procrasti_bot_messages import rando_messages, warning_messages

#override tweepy.StreamListener class
class ProcrastinateStreamListener(ty.StreamListener):

    def __init__(self, api):
        self.api = api
        super(ty.StreamListener, self).__init__()
        #add gabbs, spook, elias, and i for now
        self.users = {'1000747464' : 0, '479991180' : 0, '3035238043' : 0, '775783928720351234' : 0}

    def on_data(self, data):
        data = json.loads(data)
        self.respond(data)

    def on_error(self, status):
        # if status_code == 420:
        #     #JUST...............SLEEP
        #     time.sleep(900)
        print(status)

    def respond(self, data): 
        """
            *snaps* let's tell people not to procrastinate!!!
        """
        #print(data['user']['screen_name'] + ": "+ data['text'])
        # print(data)
        user = data['user']['screen_name']
        user_id = str(data['user']['id'])
        text = data['text']

        # avoid getting into an infinite loop with the bot at all costs
        if user == 'procrasti_bot':
            return
        tweet_id = data['id']

        if user_id in self.users: 
            self.users[user_id] += 1
            if(self.users[user_id] == 3): 
                self.shame(user_id, tweet_id)
        else: 
            # reply = rando_messages[random.randint(0, len(rando_messages) - 1)]
            # reply_tweet = "@{} " + reply
            # reply_tweet = reply_tweet.format(user)
            # api.update_status(status=reply_tweet, in_reply_to_status_id=tweet_id)
            pass

    def shame(self, user_id, tweet_id): 
        # reset counter 
        self.users[user_id] = 0
        user = api.get_user(id = user_id).screen_name
        message = warning_messages[random.randint(0, len(warning_messages) - 1)]
        tweet = "@{} " + message
        tweet = tweet.format(user)
        api.update_status(status=tweet, in_reply_to_status_id=tweet_id)

    def add_user(self, user_id): 
        pass

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
    procrastinateStream.filter(track=['procrastinate, procrastination, procrastinating'], follow=procrastinateStreamListener.users, async = True)