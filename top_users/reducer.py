#!/usr/bin/python3

import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
author = first_line.strip()
count = 1

for line in sys.stdin:
    key = line.strip()
    if author != key:
        heapq.heappushpop(heap, (count, author))
        author = key
        count = 0
    count += 1

heapq.heappushpop(heap, (count, author))

for count, author in heap:
    print(author, count, sep='\t')
