import tweepy
import time

lines_num = 500
input_file_name = "followers_ids.txt"

consumer_key = "2yoD9AScEFJWIVI6lc6Nmg"
consumer_secret = "qf2Pi3qsHvA0RjomsnNRhY5iKDWHIVy9DQWGBzDQIkw"
access_token = "41890375-lzLkRN8mby5403MusMFzK8VeVbuSyd2aVoejewZdd"
access_token_secret = "BqXUHskZRV25p9Wl7iiRl5fURu8DDFq9nIEXQ3It8jxQT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

f = open("followers_names.txt", "w")

# TODO: if in timeout
#print('sleeping')
#time.sleep(900)

for line in reversed(open(input_file_name).readlines()[-lines_num:]):
    id = line.rstrip()
    user = api.get_user(id)
    f.write(str(user.screen_name) + ' | ')
    f.write(str(user.created_at) + ' | ')
    f.write(str(user.followers_count) + ' | ')
    f.write("\b\r\n")
    print("writing %s" % id)

f.close()
