import time
import praw
import OAuth2Util
from credentials import *

r = praw.Reddit('pakalu twitter -> reddit ver 0.1'
		'URL: github.com/brennanb414/pakalubot')
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)

def PostTweet(text,user,tweetID):
	subreddit = r.get_subreddit("oneoneoneoneone")
	title = "pakalu: "+text
	twitterURL = 'https://twitter.com/'+str(user)+'/status/'+str(tweetID)
	
	try:
		subreddit.submit(title,url=twitterURL)
		print("posted "+title+" to "+str(subreddit))
	except praw.errors.APIException:
		print("submission failed")	
