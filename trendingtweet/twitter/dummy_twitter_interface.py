import logging
from twitter.twitter_interface import TwitterInterface
from utils.string_functions import nested_dict_to_obj

dummy_search_results = [
            {'id': 100, 'text': "Onion Bagel Sunshine"},
            {'id': 200, 'text': "Bagel Sunshine Roots"},
            {'id': 300, 'text': "Sunshine Roots Oysters"}]

dummy_threads = {"trends": [{'name': '#Dummy1', 'query': '#Dummy1'},
                            {'name': '#Dummy2', 'query': '#Dummy2'},
                            {'name': '#Dummy3', 'query': '#Dummy3'}]}


class DummyTwitterInterface(TwitterInterface):
    def __init__(self):
        self.log = logging.getLogger('dummy_interface')

    def tweet(self, message):
        self.log.info(f"DummyTwitterInterface has tweeted the message '{message}'.")

    def get_trend_data(self, area_id):
        self.log.info(f"DummyTwitterInterface tried to acquire trending topics for the area with id '{area_id}'.\n"
                      f"Returning dummy trends.")

        return nested_dict_to_obj(dummy_threads)

    def search(self, query, **kwargs):
        self.log.info(f"DummyTwitterInterface has searched with the query '{query}'.\n"
                      f"Other arguments passed: {kwargs}")

        return nested_dict_to_obj(dummy_search_results)
