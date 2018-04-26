import tweepy
import tkinter

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#	print(tweet.text)

user = api.me()
print(user.name)
'''
timeline = api.home_timeline()
print(timeline)
'''
#Follow everyone following you
#Favorite and Retweet a Tweet based on keywords
#Reply to a user based on a keyword

for follower in tweepy.Cursor(api.followers).items():
	follower.follow()
	print("Followed everyone that is following " + user.name)

	root = Tk()
label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)
label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)
label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)
label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)
label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)
label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)
label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)

label1.pack()
E1.pack()
root.mainloop()

def getE1():
    return E1.get()

def mainFunction():

	
	#retweet based on a keyword
	search = "design"
	#number of tweets to interact with
	numberOfTweets = "1"

	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
		try:
			#to favorite replace tweet.retweet() with tweet.favorite()
			tweet.retweet()
			print("Retweeted tweet")
		
		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break
		getE1()
		search = getE1()

		getE2()
		numberOfTweets = getE2()
		numberOfTweets = int(numberOfTweets)

		if reply == "yes":
	    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
	            try:
	                tweetId = tweet.user.id
	                username = tweet.user.screen_name
	                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
	                print ("Replied with " + phrase)
	            
	           except tweepy.TweepError as e:
	                print(e.reason)
				except StopIteration:
	                break
'''
tweetId = tweet.user.id
username = tweet.user.screen_name

phrase = "Interesting"
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
            
           except tweepy.TweepError as e:
                print(e.reason)

           except StopIteration:
                break
'''