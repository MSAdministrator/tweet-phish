from .core import Core
from .twitterpost import TwitterPost


class TweetPhish(Core):

    def save_config(self, 
        twitter_consumer_key, 
        twitter_consumer_secret,
        twitter_access_token,
        twitter_access_token_secret
    ):
        self._save_config(
            twitter_consumer_key=twitter_consumer_key,
            twitter_consumer_secret=twitter_consumer_secret,
            twitter_access_token=twitter_access_token,
            twitter_access_token_secret=twitter_access_token_secret
        )

    def tweet(self, url):
        TwitterPost().post(url)
        self.__logger.info('Tweet Posted Successfully!')
