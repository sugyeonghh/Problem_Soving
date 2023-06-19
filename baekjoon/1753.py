from sys import stdin, maxsize
from heapq import heappop, heappush

V, E = map(int, stdin.readline().split())
start = int(stdin.readline())
graph = [[] for _ in range(V + 1)]

INF = maxsize
distance = [INF] * (V + 1)

def dijkstra(s):
    heap = []
    distance[s] = 0
    heappush(heap, (0, s))
    while heap:
        dist, now = heappop(heap)
        if dist > distance[now]:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heappush(heap, (cost, v))

for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dijkstra(start)

for i in distance[1:]:
    print('INF') if i == INF else print(i)