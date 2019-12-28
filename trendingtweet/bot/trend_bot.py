from generator.tweet_generator import TweetGenerator
from twitter.twitter_interface import TwitterInterface
from twitter.twitter_searcher import TwitterSearcher
import random
import logging

from utils.string_functions import parse_tweet

UK_AREA_CODE = 23424975
TWEET_COUNT = 2000
log = logging.getLogger('trending-bot')


class TrendBot:
    def __init__(self, twitter_interface: TwitterInterface, max_tweets_per_request: int):
        self.twitter_interface = twitter_interface
        self.max_tweets_per_request = max_tweets_per_request

    def tweet_test(self):
        message = "Hello World!"
        self.twitter_interface.tweet(message)
        log.info(f"Tweeted with message: {message}")

    def tweet_trending_topic(self):
        searcher = TwitterSearcher(self.twitter_interface, self.max_tweets_per_request)

        trending_topics = searcher.get_trending_topics(UK_AREA_CODE)
        selected_trend = random.choice(trending_topics)

        search_results = searcher.get_search_results(selected_trend.query, TWEET_COUNT)
        search_content = [search_result.text for search_result in search_results]
        search_content = [parse_tweet(tweet) for tweet in search_content]

        generator = TweetGenerator(self.twitter_interface)
        generator.train_model(search_content)

        message = generator.generate_tweet()
        self.twitter_interface.tweet(message)
        log.info(f"Tweeted with message: {message}")
