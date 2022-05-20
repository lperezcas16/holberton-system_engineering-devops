#!/usr/bin/python3
""" this module contain number_of_subscribers function """

import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    my_header = {'user-agent': 'i7RANK'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    rq = requests.get(url, headers=my_header, allow_redirects=False)

    if rq.status_code == 200:
        return rq.json().get('data').get('subscribers')
    else:
        return 0
