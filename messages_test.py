import pytest

from messages import Twitter


@pytest.fixture(name='twitter')
def fixture_twitter():
    twitter = Twitter()
    yield twitter
    twitter.delete()


def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Hello!')
    assert twitter.tweets == ['Hello!']


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('Long message'*20)
    assert twitter.tweets == []


@pytest.mark.parametrize("message, expected", (
        ("Message #with a hashtag", ["with"]),
        ("#with a hashtag", ["with"]),
        ("#WITH a hashtag", ["with"]),
        ("Message with a #hashtag", ["hashtag"]),
        ("Message #with 2 #hashtags", ["with", "hashtags"])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
