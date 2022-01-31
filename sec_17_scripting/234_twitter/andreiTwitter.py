#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine, not in this Repl. 
import tweepy
import time

auth = tweepy.OAuthHandler('ScI99mxlHqIMo1a9R0Ol2PGpM', 'bodxDleWeJer1qBXZdCEPOkqOjtnysZZ7q370ckyh0B1iQ6jiN')
auth.set_access_token('211666326-RkJw4GhXV4ZVJ19TcB4OljhoE7EKV34KliBYlG9x', 'T9sVms7WuiFGf45Cm5UEYTCkofWk6j2jOp1WirB9fDg6g')
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "porn"
numberOfTweets = 10

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

'''
#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()
'''

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        # tweet.favorite()
        print(f'tweet hallado: {tweet.text}')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break