import tweepy
import time

'''
API Key: OD514u2jUtJCiaoVuv33vqEUl
API Key Secret: Li6WHJVH9uwGfd5rQuqpYhly62EX0wbsV8R8T7HQKAtmTbXajd
Bearer token: AAAAAAAAAAAAAAAAAAAAACOGYQEAAAAAevbK6engjUnupMR9VsoIHCaVNtw%3DqMmNwXQOLduMJIoTYQcLqNksgFjlIzGNmAYdhY9tkBic5BKMWo
Acces token: 211666326-lLnuKWjJaddcXY1IQNOaekKzcWaawGceKJZF5na6
Acces token secret: mBdTp3LJ47BzXG4E2Ol4KUcyiABMQ2slV7ZYImYLY9Ub3
'''
auth = tweepy.OAuthHandler('ScI99mxlHqIMo1a9R0Ol2PGpM', 'bodxDleWeJer1qBXZdCEPOkqOjtnysZZ7q370ckyh0B1iQ6jiN')
auth.set_access_token('211666326-RkJw4GhXV4ZVJ19TcB4OljhoE7EKV34KliBYlG9x', 'T9sVms7WuiFGf45Cm5UEYTCkofWk6j2jOp1WirB9fDg6g')
api = tweepy.API(auth)

user = api.me()

# testing some functions
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limitHandler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(200)

def myUnfollow(friend):
    api.destroy_friendship(screen_name=friend.screen_name, user_id=friend.id)
    print(f"se dejo de seguir a @{friend.screen_name}")

def main():
    # funciton example. print all followers
    try:
        for friend in limitHandler(tweepy.Cursor(api.friends).items()):
            if friend.screen_name == 'algun nombre': myUnfollow(friend)
            elif friend.screen_name == 'otroNombre': myUnfollow(friend)
            else:
                print(f'{friend.screen_name} continua amistad')
            
    except RuntimeError:
        pass  # para q no muestre el error

if __name__ == '__main__':
    main()