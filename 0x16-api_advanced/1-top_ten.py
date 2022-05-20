#!/usr/bin/python3
""" this module contain top_ten function """

import requests


def top_ten(subreddit):
    """ returns the first """
    my_header = {'user-agent': 'i7RANK'}
    par = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    rq = requests.get(
        url,
        headers=my_header,
        allow_redirects=False,
        params=par
    )

    if rq.status_code == 200:
        children = rq.json().get('data').get('children')
        for i in children:
            print(i.get('data').get('title'))
    else:
        print("None")
