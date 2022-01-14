from sys import stdin
from collections import deque

def bfs(v):
	queue = deque()
	queue.append(v)
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				visited[i] = visited[v] + 1
				queue.append(i)

n = int(stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
start, end = map(int, stdin.readline().split())
for _ in range(int(stdin.readline().strip())):
	x, y = map(int, stdin.readline().split())
	graph[x].append(y)
	graph[y].append(x)

bfs(start)
print(visited[end] if visited[end] else -1)