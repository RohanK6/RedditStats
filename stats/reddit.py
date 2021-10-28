import functools
import praw
import os
import logging

from dotenv import load_dotenv
from functools import lru_cache
from prawcore.exceptions import NotFound
import datetime

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

class Reddit:
    def __init__(self):
        self.praw = praw.Reddit(
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET,
            user_agent = USER_AGENT
        )

    @lru_cache(maxsize=None)
    def user_overview(self, redditor):

        try:
            self.validate_redditor(redditor)
        except NotFound:
            return None

        redditor = self.praw.redditor(redditor)

        overview = {
            'name': redditor.name,
            'comment_karma': redditor.comment_karma,
            'link_karma': redditor.link_karma,
            'total_karma': redditor.comment_karma + redditor.link_karma,
            'new_comments': list(redditor.comments.new(limit=10)),
            'new_submissions': list(redditor.submissions.new(limit=10)),
            'top_comments': list(redditor.comments.top(limit=10)),
            'top_submissions': list(redditor.submissions.top(limit=10)),
            'created_time': redditor.created_utc,
            'icon_img': redditor.icon_img,
            'gilded': redditor.gilded,
        }

        converted_time = datetime.datetime.fromtimestamp(overview['created_time'])
        formatted_time = converted_time.strftime('%B %d, %Y')
        overview['created_time'] = formatted_time

        return overview
    
    def validate_redditor(self, redditor):
        return self.praw.redditor(redditor).id
    
    def subreddit_overview(self, subreddit):

        try:
            self.validate_subreddit(subreddit)
        except Exception:
            return None


        subreddit = self.praw.subreddit(subreddit)

        overview = {
            'name': subreddit.display_name,
            'description': subreddit.public_description,
            'subscribers': subreddit.subscribers,
            'over18': subreddit.over18,
            'created_time': subreddit.created_utc,
            'hot': list(subreddit.hot(limit=10)),
            'new': list(subreddit.new(limit=10)),
            'top': list(subreddit.top(limit=10)),
            'icon': subreddit.icon_img,
            'banner': subreddit.banner_img,
            'header': subreddit.header_img,
        }

        converted_time = datetime.datetime.fromtimestamp(overview['created_time'])
        formatted_time = converted_time.strftime('%B %d, %Y')
        overview['created_time'] = formatted_time

        return overview
    
    def validate_subreddit(self, subreddit):
        return self.praw.subreddit(subreddit).id