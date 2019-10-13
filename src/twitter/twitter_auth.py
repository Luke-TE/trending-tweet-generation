import os
import tweepy
import json


class TweepyAuth:
    @staticmethod
    def create_auth_from_json_file(filename: str):
        # JSON file to JSON data
        with open(filename) as auth_file:
            auth_dict = json.load(auth_file)

        # Authenticate using JSON file
        auth = tweepy.OAuthHandler(auth_dict["key"], auth_dict["secret_key"])
        auth.set_access_token(auth_dict["token"], auth_dict["token_secret"])

        return TweepyAuth._create_api(auth)

    @staticmethod
    def create_auth_from_env():
        # Authenticate using environment variables
        auth = tweepy.OAuthHandler(os.environ("key"), os.environ("secret_key"))
        auth.set_access_token(os.environ("token"), os.environ("token_secret"))

        return TweepyAuth._create_api(auth)

    @staticmethod
    def _create_api(auth):
        # Create and verify API
        tweepy_api = tweepy.API(auth,
                                wait_on_rate_limit=True,
                                wait_on_rate_limit_notify=True)
        tweepy_api.verify_credentials()
        return tweepy_api
