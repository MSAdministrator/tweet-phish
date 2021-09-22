import os
import yaml

from .utils.logger import LoggingBase


class Core(metaclass=LoggingBase):

    yaml_config = './data/speedtweet.yml'
    config = None

    def __get_abs_path(self, value):
        """Formats and returns the absolute path for a path value

        Args:
            value (str): A path string in many different accepted formats

        Returns:
            str: The absolute path of the provided string
        """
        return os.path.abspath(os.path.expanduser(os.path.expandvars(value)))

    def _save_config(
        self,
        twitter_consumer_key, 
        twitter_consumer_secret,
        twitter_access_token,
        twitter_access_token_secret
        ):
        if not os.path.exists(self.__get_abs_path(self.yaml_config)):
            os.makedirs(os.path.dirname(self.__get_abs_path(self.yaml_config)))
        config = {
            'twitter_consumer_key': twitter_consumer_key, 
            'twitter_consumer_secret': twitter_consumer_secret,
            'twitter_access_token': twitter_access_token,
            'twitter_access_token_secret': twitter_access_token_secret
        }
        with open(self.__get_abs_path(self.yaml_config), 'w+') as f:
            yaml.dump(config, f)

    def _get_config(self):
        # Check for yaml config first
        if os.path.exists(self.__get_abs_path(self.yaml_config)):
            with open(self.__get_abs_path(self.yaml_config), 'r') as f:
                self.config = yaml.load(f, Loader=yaml.BaseLoader)
        else:
            raise EnvironmentError('Unable to find either the {} yaml config or environmental variables'.format(self.yaml_config))
