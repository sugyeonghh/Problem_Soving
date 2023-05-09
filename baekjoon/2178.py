from collections import deque
from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline()[:-1])) for _ in range(N)]

bfs()

print(graph[N - 1][M - 1])