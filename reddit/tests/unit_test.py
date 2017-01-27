import pytest
import requests

import sys
sys.path.append("../..")

from reddit import app
from reddit import settings
from reddit.api import *

def mock_api_call(q, params, headers):
    if q == "subreddits/search":
        if params["q"] == "funny":
            return {"data": range(10)}

    return "Some"

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_api_call)

def test_search_subreddit():
    search_subreddits("funny", 10)

def test_search_subreddit(search_subreddit):
    assert search_subreddit()["Key4"] == "omg"

def test_get_comments():
    import pdb; pdb.set_trace()
    pass
