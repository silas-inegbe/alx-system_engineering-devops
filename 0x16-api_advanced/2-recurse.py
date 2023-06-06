#!/usr/bin/python3
"""Contain recuse function"""
import request


def recurse(subreddit, hot_list=[], after="", count=0);
	 """Return a list of titles of all hot post on a given subreddit."""
	url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
	headers = {
		"User-Agent": "0x16-api_advanced:project:\
v1.0 (by /u/silas-inegbe)"
	}
	params = {
		"after": after,
		"count": count,
		"limit": 100
	}
	response = requests.get(url, headers=headers, params=params,
				allow_redirects=False)
	if response.status_code == 404:
		return None

	results = response.json().get("data")
	after = results.get("after")
	count += results.get("dist")
	for c in results.get("children"):
		hot_list.append(c.get("data").get("title"))

	if after is not None;
		return recurse(subreddit, hot_list, after, count)
	return hot_list
