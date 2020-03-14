import numpy as np
import donny2020_credentials
import tweepy
import pandas as pd
import datetime
import sys
from glob import glob

# ----- Randomize whether run program -----

rundonny = np.random.choice([True, False], p = [0.7, 0.3])
if rundonny :
    pass
else :
    sys.exit()

# ----- Access API -----

key = donny2020_credentials.key
secret_key = donny2020_credentials.secret_key
token = donny2020_credentials.token
token_secret = donny2020_credentials.token_secret

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

# ----- Gather media -----

fpaths = glob('*.gif')

# ----- Gather recent tweets -----

n_tweets = 15

recent_tweets = api.user_timeline(id = 'realDonaldTrump', count = n_tweets)

# ----- Check for retweets -----

recent_tweet = None

for t in recent_tweets :
    if t._json['text'].startswith('RT') :
        continue
    else :
        recent_tweet = t
        break

if recent_tweet == None :
    sys.exit()

# ----- Check for recency -----

tweet_time = pd.to_datetime(recent_tweet._json['created_at'])
now = datetime.datetime.now(tz = tweet_time.tz)
diff = now - tweet_time

if diff > datetime.timedelta(hours = 1) :
    sys.exit()
else : # Tweet content if all tests passed
    api.update_with_media(filename = np.random.choice(gifs), status = '@{}'.format(recent_tweet._json['user']['screen_name']), in_reply_to_status_id = recent_tweet._json['id'])
