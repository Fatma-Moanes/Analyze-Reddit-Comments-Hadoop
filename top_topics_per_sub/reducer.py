#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
current_sub, current_word = first_line.strip().split(',', 1)
count = 1

for line in sys.stdin:
    new_sub, new_word = line.strip().split(',', 1)
    if new_sub != current_sub:
        for count, word in heap:
            if word is not None:
                print(current_sub, word, count, sep='\t')
        count = 0
        heap = [(float("-inf"), None) for _ in range(N)]
        current_sub = new_sub
        current_word = new_word
    elif new_word != current_word:
        heapq.heappushpop(heap, (count, current_word))
        current_word = new_word
        count = 0
    count += 1

for count, word in heap:
    if word is not None:
        print(current_sub, word, count, sep='\t')
