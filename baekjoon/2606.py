

num = int(input())
conneted = int(input())
graph = []

for n in range(conneted):
	i, j = map(int, input().split())
	graph.append(i)
	graph[i].append([])
	graph[i].append(j)

print(graph)