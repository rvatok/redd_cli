import pytest
import requests

from reddit import app
from reddit import settings
from reddit.api import *
name = None
limit = 1

@pytest.fixture(scope="module")
def mock_subreddit_list():
    fake_subreddit = search_subreddits(limit=None)
    fake_subreddit.resp = {"Key1":"value1","Key4":"omg","Key2":"value2","Key3":"value3"}
    return fake_subreddit.resp

@pytest.fixture(scope="module")
def search_subreddit():
    resp = {"Key1":"value1","Key4":"omg","Key2":"value2","Key3":"value3"}
    return resp

def test_search_subreddit():
    query = "value1"
    my_fake_list = mock_subreddit_list()
    assert query in my_fake_list, "My query {0} is not found".format(query)

def test_search_subreddit(search_subreddit):
    assert search_subreddit()["Key4"] == "omg"

def test_get_comments():
    pass