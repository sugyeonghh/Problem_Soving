# 서울의 지하철
# 그래프 탐색 / bfs / dijkstra

from sys import stdin
from collections import deque

def bfs(v):
	queue = deque()
	visited[v] = 0
	queue.append(v)
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if graph[i] and not visited[i]:
				visited[v] = 1
				queue.append(v)


n = int(stdin.readline().strip())
graph = []
visited = []
num = 0
for _ in range(n):
	line = list(map(int, stdin.readline().split()))[1:]
	visited.append([0] * len(line))
	for i in line:
		graph.append((num, i))
	num += 1
start = 0
arrival = int(stdin.readline().strip())