#!/usr/bin/python3
"""
Consists of the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
	"""returns the mumber of subscribers in a subereddit"""
	if subreddit is none or type(subreddit) is not str:
		return 0
	r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
		headers={'User-Agent': '0x16-api_advanced:project:\
v1.0 (by /u/silas-inegbe)'}).json()
	subs = r.get("data", {}).get("subscribers", 0)
	return subs
