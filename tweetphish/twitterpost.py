import tweepy
from .core import Core


class TwitterPost(Core):

    _TWEET = '''I found a new #phishing site {url}. #phishkit #phishingkit'''

    def post(self, url):
        config = self._get_config()
        auth = tweepy.OAuthHandler(
            config['twitter_consumer_key'],
            config['twitter_consumer_secret']
        )
        auth.set_access_token(
            config['twitter_access_token'],
            config['twitter_access_token_secret']
        )
        self.api = tweepy.API(auth)
        try:
            tweet = self._TWEET.format(
                url=url
            )
            self.api.update_status(tweet)
        except:
            self.__logger.error(f'Error posting tweet: {tweet}')
