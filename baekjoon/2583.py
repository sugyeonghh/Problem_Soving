from sys import stdin
from collections import deque

m, n, k = map(int, stdin.readline().split())
graph = [[1 for i in range(n)] for i in range(m)]


for i in range(k):
    y1, x1, y2, x2 = map(int, stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

answer = []
for x in range(m):
    for y in range(n):
        if graph[x][y]:
            answer.append(bfs(x, y))


print(len(answer))
for i in sorted(answer):
    print(i, end=' ')
