import tweepy
import time

screen_name = "unlimitedcope"

consumer_key = "2yoD9AScEFJWIVI6lc6Nmg"
consumer_secret = "qf2Pi3qsHvA0RjomsnNRhY5iKDWHIVy9DQWGBzDQIkw"
access_token = "41890375-lzLkRN8mby5403MusMFzK8VeVbuSyd2aVoejewZdd"
access_token_secret = "BqXUHskZRV25p9Wl7iiRl5fURu8DDFq9nIEXQ3It8jxQT"

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
