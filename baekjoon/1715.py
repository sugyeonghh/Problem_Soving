from heapq import heappush, heappop
from sys import stdin

heap = []

for i in range(int(stdin.readline())):
    heappush(heap, int(stdin.readline()))

if len(heap) == 1:
    print(0)
else:
    answer = 0
    while len(heap) > 1:
        sum = heappop(heap) + heappop(heap)
        answer += sum
        heappush(heap, sum)
    print(answer)