# <a href="https://twitter.com/DonnyDonny2020">donny2020</a>

I know I'm not supposed to do this, but the orange clown's coronavirus address particularly annoyed me. So this little app is a bot that tweets at him a random choice of the following three gifs when he says something stupid on Twitter (which is always):

<img src="https://github.com/jbachlombardo/donny2020/blob/master/please.gif" height=170> <img src="https://github.com/jbachlombardo/donny2020/blob/master/out_of_element.gif" height=170> <img src="https://github.com/jbachlombardo/donny2020/blob/master/child.gif" height=170>

It's deployed to Heroku and runs off <a href="http://docs.tweepy.org/en/latest/">Tweepy</a>.

Enjoy, for as long as it's allowed to live: <a href="https://twitter.com/DonnyDonny2020">@DonnyDonny2020</a>

*(Note: Navigate to the "Tweets & Replies" tab to see the tweets.)*

#### Update 15-03-20

It is up and running and has produced this hall of fame so far:

<a href="https://twitter.com/DonnyDonny2020/status/1238812133443452933" target = _blank><img src="https://github.com/jbachlombardo/donny2020/blob/master/IMG_0575.PNG" width="285"></a> <a href="https://twitter.com/DonnyDonny2020/status/1238827222716289024" target = _blank><img src="https://github.com/jbachlombardo/donny2020/blob/master/IMG_0576.PNG" width="285"></a>

I'll post the best tweet for each gif for posterity...

### donny2020.py

Script for bot. Order of operations:
- Only run rest of script based on random T / F draw
- Authorize and access Twitter API (Tweepy)
- Gather most recent tweets by Trump
- Ensure there is a non-RT in the most recent tweets to respond to
- Check tweet occurred in last hour (within range of hourly clock worker)
- Post randomly selected gif in reply to any tweet that passes above checks

*Note: Credentials tokens not uploaded.*

### clock.py

Hourly clock to run script.

### Procfile

Heroku environment clock worker.

### requirements.txt

Dependencies for Heroku environment
