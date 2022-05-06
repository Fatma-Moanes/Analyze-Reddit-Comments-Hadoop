#!/usr/bin/python3
import sys
import heapq

N = int(sys.argv[1])
heap = [(float("-inf"), None) for _ in range(N)]
first_line = sys.stdin.readline()
current_sub, current_user = first_line.strip().split(',', 1)
count = 1

for line in sys.stdin:
    new_sub, new_user = line.strip().split(',', 1)
    if new_sub != current_sub:
        for count, user in heap:
            if user is not None:
                print(current_sub, user, count, sep='\t')
        count = 0
        heap = [(float("-inf"), None) for _ in range(N)]
        current_sub = new_sub
        current_user = new_user
    elif new_user != current_user:
        heapq.heappushpop(heap, (count, current_user))
        current_user = new_user
        count = 0
    count += 1

for count, user in heap:
    if user is not None:
        print(current_sub, user, count, sep='\t')
