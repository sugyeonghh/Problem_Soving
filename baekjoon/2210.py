from sys import stdin
from collections import deque

SIZE = 6
graph = [[] for _ in range(SIZE)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# for i in range(SIZE):
# 	graph[i].append(list(map(int, stdin.readline().split())))

graph = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]

res = []
queue = deque()
while queue:
	x, y = queue.popleft()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < SIZE and 0 <= ny < SIZE:
			