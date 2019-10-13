import tweepy


class TweepySearcher:
    def __init__(self, tweepy_interface: tweepy.API, max_tweets_per_request: int):
        self.tweepy_interface = tweepy_interface
        self.max_tweets_per_request = max_tweets_per_request

    def get_trending_topics(self, area_id: int):
        trending_topics = self.tweepy_interface.trends_place(area_id)
        most_trending_topics = trending_topics[0]

        return [trend for trend in most_trending_topics["trends"] if trend["name"][0] == '#']

    def get_trending_tweets(self):
        pass

    def get_search_results(self, query: str, count: int):
        search_results = []
        current_count = 0
        max_id = 0 # wrongeo

        while count > self.max_tweets_per_request:
            search_results += self._get_search_results_limited(query, self.max_tweets_per_request)
            current_count -= self.max_tweets_per_request

        search_results += self._get_search_results_limited(query, current_count)

        return search_results

    def _api_search(self, query: str, count: int):
        return list(self.tweepy_interface.search(query,
                                                 lang="en",
                                                 count=count,
                                                 result_type="recent"))

    def _api_search_with_max_id(self, query: str, count: int, max_id: int):
        return list(self.tweepy_interface.search(query,
                                                 lang="en",
                                                 count=count,
                                                 result_type="recent",
                                                 max_id=max_id))



