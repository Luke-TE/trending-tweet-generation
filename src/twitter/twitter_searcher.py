import tweepy


class TwitterSearcher:
    def __init__(self, tweepy_interface: tweepy.API, max_tweets_per_request: int):
        self.tweepy_interface = tweepy_interface
        self.max_tweets_per_request = max_tweets_per_request

    # Get trending queries for a certain area
    def get_trending_topics(self, area_id: int):
        trending_data, = self.tweepy_interface.trends_place(area_id)
        trends = trending_data["trends"]
        # date_of_acquiry = trending_data["created_at"]

        return [trend for trend in trends if trend["name"][0] == '#']

    # Get search results beyond the normal rate limit
    def get_search_results(self, query: str, count: int):
        search_results = []
        current_count = count
        max_id = -1

        while current_count > self.max_tweets_per_request:
            search_results += self._api_search(query, self.max_tweets_per_request, max_id)
            current_count -= self.max_tweets_per_request
            max_id = max([search_result.id for search_result in search_results]) - 1

        search_results += self._api_search(query, current_count, max_id)

        return search_results

    # Get search results, capped by the max results per request
    def _api_search(self, query: str, count: int, max_id: int):
        return list(self.tweepy_interface.search(query,
                                                 lang="en",
                                                 count=count,
                                                 result_type="recent",
                                                 max_id=max_id))



