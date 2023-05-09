#!/usr/bin/python3

"""A Script that queries the REDDIT API and prints 1st 10 hot post"""
import requests


def top_ten(subreddit):
    """retrieve top 10 hot post per subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
