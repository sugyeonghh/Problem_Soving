from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
answer = 0
max_high = 0

for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    max_high = max(max_high, max(graph[i]))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, high):
    q = deque([(x, y)])
    graph[x][y] = high
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and high < graph[nx][ny]:
                graph[nx][ny] = high
                q.append((nx, ny))

for high in reversed(range(max_high)):
    count = 0
    for i in range(n):
        for j in range(n):
            if high < graph[i][j]:
                bfs(i, j, high)
                count += 1
    answer = max(answer, count)
print(answer)