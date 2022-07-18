### Description

Get trending NFT accounts from twitter.

### Start

workon tw_api

To get list of all followers

1. change screen_name in get_all_followers_ids.py
2. python get_all_followers_ids.py
3. lines_num - first n followers, default 100
4. python get_follower_names.py
5. cp followers_names.txt lists/desired_name.txt

To get recent followings from influential:

1. Update influential.txt
2. follow_count - number of last followings per influenter
3. python get_recent_following.py
4. cp new_following_list lists/desired_name.txt
