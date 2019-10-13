from bot.trend_bot import TrendBot
from twitter.twitter_auth import TwitterAuth
import os

MAX_TWEETS_PER_REQUEST = 100
auth_filename = 'auth.json'


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Execute the trend bot.")
    parser.add_argument("--test", action='store_true')
    parser.add_argument("--json", action='store_true')
    args = parser.parse_args()

    auth_path = os.path.join('config', auth_filename)
    if args.json:
        tweepy_api = TwitterAuth.create_auth_from_json_file(auth_path)
    else:
        tweepy_api = TwitterAuth.create_auth_from_env()

    trend_bot = TrendBot(tweepy_api, MAX_TWEETS_PER_REQUEST)

    if args.test:
        trend_bot.tweet_test()
    else:
        trend_bot.tweet_trending_topic()


if __name__ == '__main__':
    main()
