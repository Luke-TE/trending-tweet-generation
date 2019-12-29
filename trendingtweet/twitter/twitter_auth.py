import os
import tweepy
import json
import logging

log = logging.getLogger('trending-bot')


class TwitterAuth:
    # Acquire API using json file
    @staticmethod
    def create_auth_from_json_file(filename: str):
        with open(filename) as auth_file:
            auth_dict = json.load(auth_file)

        # Authenticate using JSON file
        auth = tweepy.OAuthHandler(auth_dict["key"], auth_dict["secret_key"])
        auth.set_access_token(auth_dict["token"], auth_dict["token_secret"])

        return TwitterAuth._create_api(auth)

    # Acquire API using environment variables
    @staticmethod
    def create_auth_from_env():
        auth = tweepy.OAuthHandler(os.environ("key"), os.environ("secret_key"))
        auth.set_access_token(os.environ("token"), os.environ("token_secret"))

        return TwitterAuth._create_api(auth)

    # Create and verify API
    @staticmethod
    def _create_api(auth):
        tweepy_api = tweepy.API(auth,
                                wait_on_rate_limit=True,
                                wait_on_rate_limit_notify=True)
        try:
            tweepy_api.verify_credentials()
        except Exception:
            log.error(f"Credentials invalid. Cannot connect to twitter.")
        return tweepy_api
