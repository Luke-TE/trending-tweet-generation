import logging
import os
from bot.trend_bot import TrendBot
from twitter.dummy_twitter_interface import DummyTwitterInterface
from twitter.tweepy_interface import TweepyInterface
from twitter.twitter_auth import TwitterAuth


MAX_TWEETS_PER_REQUEST = 100
auth_filename = 'auth.json'
logging.basicConfig(level=logging.INFO)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Execute the trend bot.")
    parser.add_argument("--test", action='store_true', help="")
    parser.add_argument("--json", action='store_true', help="")
    args = parser.parse_args()

    auth_path = os.path.join('resources', auth_filename)
    tweepy_api = TwitterAuth.create_auth_from_json_file(auth_path) if args.json else TwitterAuth.create_auth_from_env()
    twitter_interface = TweepyInterface(tweepy_api) if not args.test else DummyTwitterInterface()

    trend_bot = TrendBot(twitter_interface, MAX_TWEETS_PER_REQUEST)
    trend_bot.tweet_trending_topic()


if __name__ == '__main__':
    main()
