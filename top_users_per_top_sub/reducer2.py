#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
key, count = first_line.strip().split('\t', 1)
current_sub, user = key.split(',', 1)
heapq.heappushpop(heap, (int(count), user))

for line in sys.stdin:
    key, count = line.strip().split('\t', 1)
    new_sub, user = key.split(',', 1)
    if new_sub != current_sub:
        topics = ""
        for _, user in heap:
            if user is not None:
                topics += user + ' '
        print(current_sub, topics, sep='\t')
        heap = [(float("-inf"), None) for _ in range(N)]
        current_sub = new_sub
    heapq.heappushpop(heap, (int(count), user))

topics = ""
for _, user in heap:
    if user is not None:
        topics += user + ' '
print(current_sub, topics, sep='\t')
