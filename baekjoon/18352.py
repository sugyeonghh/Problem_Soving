import sys
import heapq

def dijkstra(v):
	q = []
	heapq.heappush(q, (0, v))
	distance[v] = 0
	while q:
		dist, v = heapq.heappop(q)
		for i in graph[v]:
			if dist + edge < distance[i]:
				distance[i] = dist + edge
				heapq.heappush(q, (distance[i], i))
			
n, m, k, x = map(int, sys.stdin.readline().split())
distance = [sys.maxsize] * (n + 1)
distance[0] = 0
graph = [[] for _ in range(n + 1)]
edge = 1
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)

dijkstra(x)

if k in distance:
	for i in range(1, n + 1):
		if distance[i] == k:
			print(i)
else:
	print(-1)