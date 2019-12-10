import pytest

from messages import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet('Hello!')
    assert twitter.tweets == ['Hello!']


def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('Long message'*20)
    assert twitter.tweets == []
