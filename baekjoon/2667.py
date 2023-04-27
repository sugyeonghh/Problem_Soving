from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
	graph[x][y] = 0
	queue = deque()
	queue.append((x, y))
	count = 1
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
				graph[nx][ny] = 0
				queue.append((nx, ny))
				count += 1
	return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = []

for i in range(n):
	for j in range(n):
		if graph[i][j]:
			answer.append(bfs(i, j))

print(len(answer))
for i in sorted(answer):
	print(i)