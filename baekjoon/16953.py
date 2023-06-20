from sys import stdin
from heapq import heappop, heappush

a, b = map(int, stdin.readline().split())

heap = [(a, 1)]
while heap:
    num, count = heappop(heap)
    if num >= b:
        print(count) if num == b else print(-1)
        break
    heappush(heap, (num * 2, count + 1))
    heappush(heap, (num * 10 + 1, count + 1))
