import praw

class Think(object):
    def __init__(self,config):
        self.connection = praw.Reddit(client_id=config['praw_id'],
                                      client_secret=config['praw_secret'],
                                      user_agent=config['praw_user_agent'],)
        self.subreddit = config['subreddit']


    def get_random(self):
        subreddit = self.connection.subreddit(self.subreddit)

        # Retrieve a random submission from specified subreddit
        post = subreddit.random()
        return post.url
