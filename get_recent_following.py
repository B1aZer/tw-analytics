import tweepy
import time
from shutil import copyfile
from datetime import datetime
import os
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(dotenv)

follow_count = 20

# TODO: if you already in timeout
# print('sleeping')
# time.sleep(900)

auth = tweepy.OAuthHandler(os.getenv('consumer_key'),
                           os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'),
                      os.getenv('access_token_secret'))
api = tweepy.API(auth)

# TODO: require https://developer.twitter.com/en/docs/twitter-ads-api/apply
auth2 = tweepy.OAuthHandler(os.getenv('api_key'), os.getenv('api_secret'))
auth2.set_access_token(os.getenv('api_access_token'),
                       os.getenv('api_token_secret'))
api2 = tweepy.API(auth2)


# read influential list
influental_list = None
with open('influential.txt') as f:
    influental_list = f.readlines()

# write following ids, by 20
with open('following.txt', 'w') as f:
    for influencer in influental_list:
        name = influencer.split(' ')[0]
        # find recent following
        # import pdb; pdb.set_trace()
        # TODO: 15 req x 15 min limit
        following_ids = tweepy.Cursor(
            api.friends_ids, screen_name=name).items(follow_count)
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

# TODO: 900 req x 15 min
new_following = []
for fol_id in following_ids_new:
    if fol_id not in following_ids_old:
        user = api.get_user(fol_id)
        new_following.append(user)

# order by date created
with open('new_following_list.txt', 'w') as f:
    for user in sorted(new_following, key=(lambda x: x.created_at), reverse=True):
        f.write(user.screen_name + " | ")
        f.write(str(user.created_at) + " | ")
        f.write(str(user.followers_count) + " | ")
        f.write("\r\n")

# copy to lists
copyfile("new_following_list.txt", "lists/following-lists/%s.txt" %
         (datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')))

# copy following to prev
copyfile("following.txt", "following_prev.txt")
