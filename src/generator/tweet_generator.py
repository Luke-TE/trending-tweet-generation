from textgenrnn import textgenrnn
import tweepy


class TweetGenerator:
    def __init__(self, tweepy_interface: tweepy.API):
        self.tweepy_interface = tweepy_interface
        self.generator = None

    def train_model(self, tweet_texts):
        self.generator = textgenrnn()
        self.generator.train_on_texts(tweet_texts,
                                      num_epochs=5)

    def save_model(self):
        self.generator.save("save")

    def generate_tweet(self):
        return self.generator.generate(temperature=0.8,
                                       return_as_list=True)
