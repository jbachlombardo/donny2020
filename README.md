# <a href="https://twitter.com/DonnyDonny2020">DonnyDonny2020</a>

I know I'm not supposed to do this, but the orange clown's coronavirus address particularly annoyed me. So this little bot  tweets at him a random choice of the following three gifs when he says something stupid on Twitter (which is always):

<img src="https://github.com/jbachlombardo/donny2020/blob/master/gifs/please.gif" height=170> <img src="https://github.com/jbachlombardo/donny2020/blob/master/gifs/out_of_element.gif" height=170> <img src="https://github.com/jbachlombardo/donny2020/blob/master/gifs/child.gif" height=170>

It's deployed to Heroku and runs off <a href="http://docs.tweepy.org/en/latest/">Tweepy</a>.

Enjoy, for as long as it's allowed to live: <a href="https://twitter.com/DonnyDonny2020/with_replies">@DonnyDonny2020</a>

#### Update 26-03-20

It is up and running and has produced this hall of fame so far:

<a href="https://twitter.com/DonnyDonny2020/status/1238812133443452933"><img src="https://github.com/jbachlombardo/donny2020/blob/master/Results/IMG_0598.PNG" width="285" alt="result1_140320"></a> <a href="https://twitter.com/DonnyDonny2020/status/1238827222716289024"><img src="https://github.com/jbachlombardo/donny2020/blob/master/Results/IMG_0597.PNG" width="285" alt="result2_140320"></a> <a href="https://twitter.com/DonnyDonny2020/status/1242919187112222721"><img src="https://github.com/jbachlombardo/donny2020/blob/master/Results/IMG_0646.PNG" width="285" alt="result3_180320"></a>

I'll post the best tweet for each gif for posterity...

### donny2020.py

Script for bot. Order of operations:
1. Only run rest of script based on random T / F draw
1. Authorize and access Twitter API (Tweepy)
1. Gather most recent tweets by Trump
1. Ensure there is a non-RT in the most recent tweets to respond to
1. Check tweet occurred in last hour (within range of hourly clock worker)
1. Post randomly selected gif in reply to any tweet that passes above checks

*Note: Credentials tokens not uploaded.*

### clock.py

Hourly clock to run script.

### Procfile

Heroku environment clock worker.

### requirements.txt

Dependencies for Heroku environment
