import functools
import praw
import os

from dotenv import load_dotenv
from functools import lru_cache

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

    def user_overview(self, redditor):

        redditor = self.praw.redditor(redditor)

        overview = {
            'name': redditor.name,
            'comment_karma': redditor.comment_karma,
            'link_karma': redditor.link_karma,
            'total_karma': redditor.comment_karma + redditor.link_karma,
            'new_comments': redditor.comments.new(limit=10),
            'new_submissions': redditor.submissions.new(limit=10),
            'top_comments': redditor.comments.top(limit=10),
            'top_submissions': redditor.submissions.top(limit=10),
            'created_utc': redditor.created_utc,
            'icon_img': redditor.icon_img,
            'gilded': redditor.gilded,
        }
        return overview