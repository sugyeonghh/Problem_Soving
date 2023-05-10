from sys import stdin
from collections import deque

def bfs():
	queue = deque([s])
	visited[s] = 1
	while queue:
		vertex = queue.popleft()
		if vertex == g:
			return graph[g]
		for pos in [vertex + u, vertex - d]:
			if 0 < pos <= f and not visited[pos]:
				visited[pos] = 1
				graph[pos] = graph[vertex] + 1
				queue.append(pos)
	return -1

f, s, g, u, d = map(int, stdin.readline().split())
graph = [0] * (f + 1)
visited = [0] * (f + 1)

answer = bfs()
print(answer if answer != -1 else 'use the stairs')
