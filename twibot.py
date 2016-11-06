#Original author: github.com/Brennanb414
#requires:
#	-tweepy 3.3.0
#	-praw
#	-OAuth2Util
#
import logging
import traceback
from credentials import *
from tweepy import StreamListener
from tweepy import Stream
import tweepy,time
from redditbot import *


#twitter setup

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class MyStreamListener(StreamListener):
	
    def on_status(self, status):
        # called when user tweets, this makes it so only pakalu's tweets get posted, and not all the RTs
	if(status.author.screen_name == "pakalupapito"):
		try:		
			print("\n------Tweet info-------"
			"\nAuthor: "+str(status.author.screen_name)+
			"\nID: "+str(status.id)+
			"\nText: "+str(status.text))
			PostTweet(status.text,status.author.screen_name,status.id)
		except Exception as e:
			print("Tweet error: "+str(traceback.format_exc)+ "\n E: "+str(e))			
			
    def on_error(self, status):
	if status == 420:
		print ("Error was 420, waiting 15 mins")
		time.sleep(60*15)
		print("\nwait over")
	else:
		print("Error was: "+str(status))

if __name__ == '__main__':
	listener = MyStreamListener()
	twitterStream = Stream(auth, listener)

	#must be the user's ID. get it from here: https://tweeterid.com/
	twitterStream.filter(follow=['1582341876'])
