import sys
sys.setrecursionlimit(10**9)

def dfs(v):
	for i in graph[v]:
		if not visited[i]:
			visited[i] = v
			dfs(i)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

dfs(1)
for i in range(2, n + 1):
	print(visited[i])