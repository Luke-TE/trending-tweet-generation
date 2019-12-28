import tweepy

from twitter.twitter_interface import TwitterInterface
from utils.string_functions import nested_dict_to_obj


class TweepyInterface(TwitterInterface):
    def __init__(self, api: tweepy.API):
        self.api = api

    def tweet(self, message):
        self.api.update_status(message)

    def get_trend_data(self, area_id):
        return nested_dict_to_obj(self.api.trends_place(area_id)[0], name='TrendingTopics')

    def search(self, query, **kwargs):
        return list(self.api.search(query, **kwargs))
