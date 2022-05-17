import tweepy
import time
import os
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(dotenv)

lines_num = 500
input_file_name = "followers_ids.txt"

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

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
    f.write(str(user.screen_name) + ' ' + os.getenv('LOG_FILES_SEPARATOR') + ' ')
    f.write(str(user.created_at) + ' ' + os.getenv('LOG_FILES_SEPARATOR') + ' ')
    f.write(str(user.followers_count) + ' ' + os.getenv('LOG_FILES_SEPARATOR') + ' ')
    f.write("\b\r\n")
    print("writing %s" % id)

f.close()
