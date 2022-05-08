import tweepy
import time
from shutil import copyfile
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
follow_count = 20

# TODO: if you already in timeout
#print('sleeping')
#time.sleep(900)

# copy following to prev
copyfile("following.txt", "following_prev.txt")

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# read influential list
influental_list = None
with open('influential.txt') as f:
    influental_list = f.readlines()

with open('following.txt', 'w') as f:
    for influencer in influental_list:
        name = influencer.split(' ')[0]
        # find recent following
        following_ids = tweepy.Cursor(api.friends_ids, screen_name=name).items(follow_count)
        # write to file
        for f_id in following_ids:
            f.write(str(f_id) + '\r\n')
        print("sleeping on %s" % name)
        time.sleep(60)

# create new file with new entries between new and prev
with open('following.txt') as f:
    following_ids_new = f.readlines()
with open('following_prev.txt') as f:
    following_ids_old = f.readlines()

new_following = []
for fol_id in following_ids_new:
    if fol_id not in following_ids_old:
        user = api.get_user(fol_id)
        new_following.append(user)

with open('new_following_list.txt', 'w') as f:
    # order by date created
    for user in sorted(new_following, key=(lambda x: x.created_at), reverse=True):
        f.write(user.screen_name + " | ")
        f.write(str(user.created_at) + " | ")
        f.write(str(user.followers_count) + " | ")
        f.write("\r\n")

copyfile("new_following_list.txt", "lists/new_following_list_%s_%s_%s.txt" % (datetime.now().strftime('%m'), datetime.now().strftime('%d'), datetime.now().strftime('%y')))
