cd /home/hipi/Sites/GooDee/twitter_followers
source venv/bin/activate
python get_recent_following.py | ts '[%Y-%m-%d %H:%M:%.S]' >> /home/hipi/Sites/GooDee/_airflow/recent_followers.log
