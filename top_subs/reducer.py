#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
subreddit = first_line.strip()
count = 1

for line in sys.stdin:
    key = line.strip()
    if subreddit != key:
        heapq.heappushpop(heap, (count, subreddit))
        subreddit = key
        count = 0
    count += 1

heapq.heappushpop(heap, (count, subreddit))

for count, subreddit in heap:
    print(subreddit, count, sep='\t')
