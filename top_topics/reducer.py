#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
word = first_line.strip()
count = 1

for line in sys.stdin:
    key = line.strip()
    if word != key:
        heapq.heappushpop(heap, (count, word))
        word = key
        count = 0
    count += 1

heapq.heappushpop(heap, (count, word))

for count, word in heap:
    print(word, count, sep='\t')
