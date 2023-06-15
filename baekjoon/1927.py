from heapq import heappop, heappush
from sys import stdin

heap = []
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        print(heappop(heap) if heap else 0)
    elif n > 0:
        heappush(heap, n)
