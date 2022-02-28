from sys import stdin
from collections import deque

graph = []
queue = deque()
m, n = map(int, stdin.readline().split())
for _ in range(n):
	graph.append(list(map(int, stdin.readline().split())))

for y in range(n):
	for x in range(m):
		if graph[y][x] == 1:
			queue.append((x, y))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
days = -1
while queue:
	x, y = queue.popleft()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
			graph[ny][nx] = graph[y][x] + 1
			queue.append((nx, ny))

for i in graph:
	if 0 in i:
		days = -1
		break
	n = max(i) - 1
	days = n if days < n else days
print(days)