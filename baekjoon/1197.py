from sys import stdin
from heapq import heappop, heappush, heapify

V, E = map(int, stdin.readline().split())

visited = [0] * (V + 1)
graph = [[] for i in range(V + 1)]

for i in range(E):
    a, b, v = map(int, stdin.readline().split())
    graph[a].append((v, b))
    graph[b].append((v, a))

cnt = 0
answer = 0
q = []
heappush(q, (0, 1))
while q:
    if cnt == V:
        break
    value, vertex = heappop(q)
    if not visited[vertex]:
        visited[vertex] = 1
        cnt += 1
        answer += value
        for i in graph[vertex]:
            heappush(q, i)

print(answer)
