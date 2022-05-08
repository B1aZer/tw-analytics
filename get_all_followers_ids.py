import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

screen_name = "anonymicenft"

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

f = open("followers_ids.txt", "w")

# if you already in timeout
#print('sleeping')
#time.sleep(900)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
    ids.extend(page)
    print('sleeping in cycle')
    time.sleep(60)

print len(ids)
for id in ids:
    f.write(str(id)+"\r\n")

f.close()
