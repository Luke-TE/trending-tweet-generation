from collections import namedtuple


def nested_dict_to_obj(d, name="NamedTuple"):
    if isinstance(d, dict):
        d = dict(d)
        for attr_name, attr_value in d.items():
            d[attr_name] = nested_dict_to_obj(attr_value)
            return namedtuple(name, d.keys())(**d)
    elif isinstance(d, list):
        return list(nested_dict_to_obj(item) for item in d)

    return d


def parse_tweet(tweet):
    if ":" in tweet:
        tweet = tweet[tweet.index(':') + 2:]
    return tweet
