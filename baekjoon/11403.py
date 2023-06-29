from sys import stdin
from sys import maxsize
from collections import deque

INF = maxsize
N = int(stdin.readline())
graph = []

for i in range(N):
    input = list(map(int, stdin.readline().replace('0', str(INF)).split()))
    graph.append(input)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in i:
        print(0, end=' ') if j == INF else print(1, end=' ')
    print()