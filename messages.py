import os
import re


class Twitter:
    version = "2.0"

    def __init__(self, backend=None):
        self.backend = backend
        self.tweets = []
        if self.backend and not os.path.exists(self.backend):
            with open(self.backend, 'w'):
                pass

    def delete(self):
        print('It\'s the end')

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('Too long message')
        self.tweets.append(message)

    def find_hashtags(self, message):
        return [hashtag.lower() for hashtag in re.findall(r'#(\w+)', message)]
