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