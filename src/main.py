''' This file takes a word from the user and performs sentimental analysis using 
matplotlib and vader_lexicon'''

import pandas as pd
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

'''My twitter api keys'''
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''


#setting the authorisation for the rest api 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

'''getting the tweets data'''
#Taking the string and the count
keyword=input('Enter the string upon which you want to run this script \n ')
counter= int(input('Enter the number of tweets you want to search \n'))


#Formation of dataframe

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
tweets = api.search(keyword,lang='en',count=counter) # only english tweets taken in
data = pd.DataFrame([tweet.text for tweet in tweets],columns=['tweets'])



