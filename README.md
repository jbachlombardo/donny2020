# <a href="https://twitter.com/DonnyDonny2020">donny2020</a>

I know I'm not supposed to do this, but the orange clown's coronavirus address particularly annoyed me. So this little app is a bot that tweets at him one of the following three gifs when he says something stupid on Twitter (which is always):

![](please.gif) ![](child.gif) ![](out_of_element.gif)

It's deployed to Heroku and runs off <a href="http://docs.tweepy.org/en/latest/">Tweepy</a>.

Enjoy, for as long as it's allowed to live: <a href="https://twitter.com/DonnyDonny2020">@DonnyDonny2020</a>

(Note: Navigate to the "Tweets & Replies" tab to see the tweets.)

### donny2020.py

Script for bot. Order of operations:
- Only runs rest of script based on random
- Authorizes and accesses API
- Gathers most recent tweets by Trump
- Ensures there is a non-RT in the most recent tweets to respond to
- Checks tweet occurred in last hour (within range of hourly clock -- see below)
- Tweets media in reply to tweet that passed checks

Note: Credentials tokens not uploaded.

### clock.py

Hourly clock to run script.

### Procfile

Heroku environment clock worker.

### requirements.txt

Dependencies for Heroku environment
