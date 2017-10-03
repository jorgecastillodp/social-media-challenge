import json
import tweepy

class Listener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        print(tweet)
        return True

if __name__ == '__main__':
 
    listener = Listener()
    auth = tweepy.OAuthHandler("cznZ7zL8OI0qePJwia4yfMeTf", "cBkzdvwAWIHSqflvhavIJMAvRqzORlJEYQaXMZfQ2AU4bRcViF")
    auth.set_access_token("369285142-shtjE1S4LxfCqXHsQCbIZ2crDqoaaHu3Vjrjx7Tx", "BaDUPePhZ7O5YPPGrCjJOX16plWWUNRDK8khRX9jwbn1z")
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Trump'])

