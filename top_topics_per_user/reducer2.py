#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
key, count = first_line.strip().split('\t', 1)
current_sub, topic = key.split(',', 1)
heapq.heappushpop(heap, (int(count), topic))

for line in sys.stdin:
    key, count = line.strip().split('\t', 1)
    new_sub, topic = key.split(',', 1)
    if new_sub != current_sub:
        topics = ""
        for _, topic in heap:
            if topic is not None:
                topics += topic + ' '
        print(current_sub, topics, sep='\t')
        heap = [(float("-inf"), None) for _ in range(N)]
        current_sub = new_sub
    heapq.heappushpop(heap, (int(count), topic))

topics = ""
for _, topic in heap:
    if topic is not None:
        topics += topic + ' '
print(current_sub, topics, sep='\t')