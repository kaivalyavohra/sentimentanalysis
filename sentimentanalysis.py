import tweepy
from textblob import TextBlob


numoftweets=0
#twitter account authentication
auth = tweepy.OAuthHandler("SEE TWITTER API","SEE TWITTER API")
auth.set_access_token("SEE TWITTER API", "SEE TWITTER API")
api = tweepy.API(auth)

#initialize subjectivity and positivty rating
score,score2=0,0

searchstring=input("Enter a subject to search: ")

#search for latest 1500 tweets
public_tweets=api.search(q=searchstring,count=1500)
for tweet in public_tweets:
	i=TextBlob(tweet.text)
	#if a subjective tweet
	if i.sentiment.subjectivity>0.5:
		score+=i.sentiment.polarity
		score2+=i.sentiment.subjectivity
		numoftweets+=1
		# print(i.sentiment)
		# print(tweet.text)

print(round(((score/numoftweets)+1)*50),"percent approval")


print(round((score2/numoftweets)*100),"percent subjective")