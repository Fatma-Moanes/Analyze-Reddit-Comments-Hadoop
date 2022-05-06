#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
word, ups = first_line.strip().split('\t', 1)
total_ups = int(ups)

for line in sys.stdin:
    key, ups = line.strip().split('\t', 1)
    if word != key:
        heapq.heappushpop(heap, (total_ups, word))
        word = key
        total_ups = 0
    total_ups += int(ups)

heapq.heappushpop(heap, (total_ups, word))

for total_ups, word in heap:
    print(word, total_ups, sep='\t')
