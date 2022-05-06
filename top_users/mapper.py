#!/usr/bin/python3
import sys
import json

for line in sys.stdin:
    comment = json.loads(line)
    author = comment['author']
    if "[deleted]" not in author:
        print(author)
