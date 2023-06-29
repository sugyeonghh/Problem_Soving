from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())

graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = True
    print(v, end=' ')
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = True
                q.append(i)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)