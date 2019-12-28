from abc import ABC, abstractmethod


class TwitterInterface(ABC):
    @abstractmethod
    def tweet(self, message):
        pass

    @abstractmethod
    def get_trend_data(self, area_id):
        pass

    @abstractmethod
    def search(self, query, **kwargs):
        pass
