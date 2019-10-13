from generator.tweet_generator import TweetGenerator
from twitter.twitter_searcher import TwitterSearcher
import tweepy
import random
import logging

UK_AREA_CODE = 23424975
TWEET_COUNT = 2000
log = logging.getLogger('trending-bot')


class TrendBot:
    def __init__(self, tweepy_interface: tweepy.API, max_tweets_per_request: int):
        self.tweepy_interface = tweepy_interface
        self.max_tweets_per_request = max_tweets_per_request

    def tweet_test(self):
        message = "Hello World!"
        self.tweepy_interface.update_status(message)
        log.debug(f"Tweeted with message: {message}")

    def tweet_trending_topic(self):
        searcher = TwitterSearcher(self.tweepy_interface,
                                   self.max_tweets_per_request)

        trending_topics = searcher.get_trending_topics(UK_AREA_CODE)
        selected_trend = random.choice(trending_topics)

        search_results = searcher.get_search_results(selected_trend['query'], TWEET_COUNT)
        search_content = [search_result.text for search_result in search_results]
        search_content = [self._parse_tweet(tweet) for tweet in search_content]

        generator = TweetGenerator(self.tweepy_interface)
        generator.train_model(search_content)

        message = generator.generate_tweet()
        self.tweepy_interface.update_status(message)
        log.debug(f"Tweeted with message: {message}")

    def _parse_tweet(self, tweet):
        if ":" in tweet:
            tweet = tweet[tweet.index(':') + 2:]
        return tweet
