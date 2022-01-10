from sys import stdin

def dijkstra(r):
	


n, m, k, x = map(int, stdin.readline().split())
graph = [[0] * n for i in range(n)]
for i in range(m):
	a, b = map(int, stdin.readline().split())
	graph[a - 1][b - 1] = 1
