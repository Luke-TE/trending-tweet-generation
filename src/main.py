from tweepy_auth import TweepyAuth
from textgenrnn import textgenrnn
import random
import os
import tweepy
import logging

auth_filename = 'auth.json'
area_id = 23424975
log = logging.getLogger()


def get_trends(api):
    trending_topics = api.trends_place(area_id)
    most_trending_topics = trending_topics[0]

    return [trend for trend in most_trending_topics["trends"] if trend["name"][0] == '#']


def get_search_results(api: tweepy.API, query):
    return api.search(query, lang="en", count=100, result_type="popular")  # 100 is the maximum


def main():
    auth_path = os.path.join('json', auth_filename)
    tweepy_api = TweepyAuth.create_auth_from_json_file(auth_path)

    while True:
        random_trend = random.choice(get_trends(tweepy_api))
        print(f"Trying out {random_trend['query']}")
        search_results = get_search_results(tweepy_api, random_trend["query"])
        search_content = [search_result.text for search_result in search_results]
        print(f"There are {len(search_content)} results.")

        if len(search_content) > 60:
            break

    print(f"Search result chosen is {random_trend['query']}")
    [print(tweet) for tweet in search_content]

    tweet_generator = textgenrnn()
    tweet_generator.train_on_texts(search_content, num_epochs=1)

    print("The output:")
    tweet_generator.generate(temperature=0.5)


if __name__ == '__main__':
    main()
