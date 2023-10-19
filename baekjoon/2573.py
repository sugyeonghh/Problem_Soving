from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for i in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]

def melt_graph():
    melted = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = i+dx
                    ny = j+dy
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        melted[i][j] += 1
    for i in range(n):
        for j in range(m):
            graph[i][j] -= melted[i][j]
            if graph[i][j] < 0: 
                graph[i][j] = 0

def bfs(x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1


def count_graph():
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > 0:
                bfs(i,j)
                count += 1
    return count

result = 0
while True:
    melt_graph()
    result += 1
    visited = [[0 for i in range(m)] for j in range(n)]
    count = count_graph()
    if count >= 2:
        print(result)
        break
    elif count == 0:
        print(0)
        break
