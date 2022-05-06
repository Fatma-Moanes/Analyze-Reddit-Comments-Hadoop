#!/usr/bin/python3
import sys
import json

top_subs = {}
with open(sys.argv[1], "r") as file:
    for line in file:
        top_subs[line.split('\t')[0]] = 1

for line in sys.stdin:
    comment = json.loads(line)
    subreddit = comment['subreddit']
    if subreddit not in top_subs:
        continue

    author = comment['author']
    if "[deleted]" not in author:
        print(subreddit + ',' + author)
