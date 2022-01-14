from sys import stdin
from collections import deque

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs(x, y):
	graph[y][x] = 0
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < size and 0 <= ny < size and graph[ny][nx] == 0:
				graph[ny][nx] = graph[y][x] + 1
				queue.append((nx, ny))
				if nx == ax and ny == ay:
					break

for _ in range(int(input())):
	size = int(stdin.readline().strip())
	x, y = map(int, stdin.readline().split())
	ax, ay = map(int, stdin.readline().split())
	graph = [[0] * size for _ in range(size)]
	if x == ax and y == ay:
		print(0)
	else:
		bfs(x, y)
		print(graph[ay][ax])