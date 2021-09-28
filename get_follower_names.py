import tweepy
import time

lines_num = 500
input_file_name = "followers_ids.txt"

consumer_key = "x"
consumer_secret = "x"
access_token = "x"
access_token_secret = "x"

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