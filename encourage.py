"""
	A bot that sends out reminders to stop procrastinating and Helpful Study Tips 

	A work of art by Gabby 'Habitual Procrastinator' Ortman
"""
import tweepy as ty
from procrastibotSecrets import *
from procrasti_bot_messages import automated_messages
import random

def setTwitterAuth():
    """
    obtains authorization from Twitter API
    Thank u Elias, may I never have to actually write this for as long as I create Twitter Bots
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def sendTweet(api):
    """
    selects a psuedo-random tweet from the tweets list, checks for duplicates,
    and tweets the message.

    thank u Elias, pt 2
    """
    tweet = automated_messages[random.randint(0, len(automated_messages) - 1)]
    deleteOldTweets(api, tweet)
    api.update_status(tweet)

def deleteOldTweets(api, tweet):
    """
    delete any any tweet that is a duplicate of the tweet in the last
    96 tweets. 
    """
    oldTweets = api.user_timeline("@procrasti_bot2", count=96)
    for old in oldTweets:
        if old.text == tweet:
            api.destroy_status(old.id)

if __name__ == '__main__':
	api = setTwitterAuth() 
	sendTweet(api)