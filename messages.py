class Twitter:
    version = "2.0"

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        self.tweets.append(message)


t = Twitter()
print(t.tweets)
t.tweet('First message')
print(t.tweets)
