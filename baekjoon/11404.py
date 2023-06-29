from sys import stdin
from sys import maxsize
from collections import deque

INF = maxsize
N = int(stdin.readline())
M = int(stdin.readline())
graph = [[INF for i in range(N)] for j in range(N)]

for i in range(N):
    graph[i][i] = 0

for i in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in i:
        print(0, end=' ') if j == INF else print(j, end=' ')
    print()