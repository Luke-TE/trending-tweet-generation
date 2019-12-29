import logging
from twitter.twitter_interface import TwitterInterface
log = logging.getLogger('trending-bot')


class TwitterSearcher:
    def __init__(self, twitter_interface: TwitterInterface, max_tweets_per_request: int):
        self.twitter_interface = twitter_interface
        self.max_tweets_per_request = max_tweets_per_request

    # Get trending queries for a certain area
    def get_trending_topics(self, area_id: int):
        log.debug("Searcher sending a request for trends.")
        trending_data = self.twitter_interface.get_trend_data(area_id)

        # date_of_creation = trending_data.created_at
        return [trend for trend in trending_data.trends if trend.name[0] == '#']

    # Get search results beyond the normal rate limit
    def get_search_results(self, query: str, count: int):
        search_results = []
        current_count = count
        max_id = -1

        log.debug(f"Searcher searching for tweets with the query '{query}'.")
        while current_count > self.max_tweets_per_request:
            search_results += self._wrapped_search(query, self.max_tweets_per_request, max_id)
            current_count -= self.max_tweets_per_request
            max_id = max(search_result.id for search_result in search_results) - 1

        search_results += self._wrapped_search(query, current_count, max_id)

        return search_results

    # Get search results, capped by the max results per request
    def _wrapped_search(self, query: str, count: int, max_id: int):
        search_kwargs = {'lang': "en", 'count': count, 'result_type': "recent", 'max_id': max_id}
        return self.twitter_interface.search(query, **search_kwargs)




