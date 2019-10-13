import tweepy


class TrendBot:
    def __init__(self, tweepy_interface: tweepy.API, max_tweets_per_request: int):
        self.tweepy_interface = tweepy_interface
        self.max_tweets_per_request = max_tweets_per_request

    def tweet_test(self):
        self.tweepy_interface.update_status("Hello World!")

    def tweet_trending_topic(self):
        pass
