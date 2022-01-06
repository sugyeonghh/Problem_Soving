from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
	graph[y][x] = 0
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < m and 0 <= ny < n and graph[ny][nx]:
				graph[ny][nx] = 0
				queue.append((nx, ny))

for t in range(int(stdin.readline())):
	m, n, k = map(int, stdin.readline().split())
	graph = [[0] * m for i in range(n)]
	cnt = 0
	for i in range(k):
		x, y = map(int, stdin.readline().split())
		graph[y][x] = 1
	for y in range(n):
		for x in range(m):
			if graph[y][x]:
				cnt += 1
				bfs(x, y)
	print(cnt)