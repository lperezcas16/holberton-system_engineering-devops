#!/usr/bin/python3
""" this module contain top_ten function """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ returns the first """
    my_header = {'user-agent': 'i7RANK'}
    par = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit,
        after
    )
    rq = requests.get(
        url,
        headers=my_header,
        allow_redirects=False,
    )
    if rq.status_code == 200:
        hot_list += rq.json().get("data", {}).get("children", [])
        affffter = rq.json().get("data", {}).get("after", None)
        if affffter:
            return recurse(subreddit, hot_list=hot_list, after=affffter)
        else:
            return hot_list
