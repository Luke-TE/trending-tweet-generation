from textgenrnn import textgenrnn
from twitter.twitter_interface import TwitterInterface


class TweetGenerator:
    def __init__(self, twitter_interface: TwitterInterface, generator: Generator):
        self.tweepy_interface = twitter_interface
        self.generator = generator

    def train_model(self, tweet_texts):
        self.generator = textgenrnn()
        self.generator.train_on_texts(tweet_texts,
                                      num_epochs=1)

    def save_model(self):
        self.generator.save("save")

    def generate_tweet(self):
        return self.generator.generate(temperature=0.8,
                                       return_as_list=True)
