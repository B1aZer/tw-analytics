cd /home/hipi/Sites/GooDee/twitter_followers
source venv/bin/activate
python get_recent_following.py | ts '[%Y-%m-%d %H:%M:%.S]' >> /home/hipi/Sites/GooDee/_airflow/recent_followers.log
status=$?
## repeat after 15m ## 
if [ $status -ne 0 ]; then
    sleep 15m
    python get_recent_following.py | ts '[%Y-%m-%d %H:%M:%.S]' >> /home/hipi/Sites/GooDee/_airflow/recent_followers.log
fi
status=$?
## repeat after 15m ## 
if [ $status -ne 0 ]; then
    sleep 15m
    python get_recent_following.py | ts '[%Y-%m-%d %H:%M:%.S]' >> /home/hipi/Sites/GooDee/_airflow/recent_followers.log
fi
status=$?
## repeat after 15m ## 
if [ $status -ne 0 ]; then
    sleep 15m
    python get_recent_following.py | ts '[%Y-%m-%d %H:%M:%.S]' >> /home/hipi/Sites/GooDee/_airflow/recent_followers.log
fi